#!/usr/bin/env python
# -*- coding: utf-8 -*-

NAME = 'FixIndents'
DESC = 'A simple yet flexible utility to convert indentation.'
VERSION = '0.2'
AUTHOR = 'Mathieu D. (MatToufoutu)'

import os
import sys
from argparse import ArgumentParser


def convert_indents(in_filename, out_filename, in_tabs, in_size, out_tabs, out_size, debug):
    in_indent_char = '\t' if in_tabs else ' '
    out_indent = '\t' if out_tabs else (' ' * out_size)
    out_file = None if debug else open(out_filename, 'w')
    if not debug:
        print "[*] Converting %s" % in_filename
    with open(in_filename) as in_file:
        for line in in_file:
            char_count = 0
            for char in line:
                if char == in_indent_char:
                    char_count += 1
                else:
                    break
            indent_count = char_count if in_tabs else (char_count / in_size)
            line = (out_indent * indent_count) + line[char_count:]
            if debug:
                print line.rstrip()
            else:
                out_file.write(line)
    if not debug:
        out_file.close()


def overwrite_file(path):
    print "[!] File already exists: %s" % path
    print "    Overwrite? [y/N] ",
    resp = raw_input().lower()
    if resp == 'y':
        return True
    elif resp in ('', 'n'):
        return False
    else:
        print '[!] Invalid answer, aborting'
        sys.exit(0)


def main():
    no_touch_dirs = ('.git', '.hg', '.svn')

    parser = ArgumentParser(description=DESC)
    parser.add_argument('--version', action='version', version=VERSION)

    # Source file indentation specs
    source_specs = parser.add_mutually_exclusive_group(required=True)
    source_specs.add_argument('-st', '--source-tabs',
                              help='Source file uses tabs for indentation.',
                              action='store_true', )
    source_specs.add_argument('-sz', '--source-size',
                              help='Indents size in source file(s).',
                              type=int,
                              metavar='SIZE')

    # Destination file indentation specs
    target_specs = parser.add_mutually_exclusive_group(required=True)
    target_specs.add_argument('-dt', '--dest-tabs',
                              help='Use tabs for indentation in destination file.',
                              action='store_true')
    target_specs.add_argument('-ds', '--dest-size',
                              help='Indents size in destination file.',
                              type=int,
                              default=4,
                              metavar='SIZE')
    # Source and target paths
    parser.add_argument('-s', '--source',
                        help='File of folder from which code should be read.',
                        required=True)
    output_group = parser.add_mutually_exclusive_group(required=True)
    output_group.add_argument('-d', '--dest',
                              help='File or folder to which code should be written.')
    output_group.add_argument('-dbug', '--debug',
                              help="Output converted data to console, don't write anything.",
                              action='store_true',
                              default=False)
    parser.add_argument('-e', '--exclude',
                        help=(
                            'Comma-separated list of directory names to ignore. '
                            'Only useful when SOURCE is a directory.'
                        ),
                        metavar='FOLDERS')
    parser.add_argument('-ext', '--extensions',
                        help=(
                            'Comma-separated list of specific file extensions to convert. '
                            'Only useful when SOURCE is a directory.'
                        ))
    args = parser.parse_args()

    # Arguments checks
    if not os.path.exists(args.source):
        parser.error('file or directory not found: %s' % args.source)
    if (not args.source_tabs) and (args.source_size == 0):
        parser.error("--source-size value can't be 0")
    if (not args.dest_tabs) and (args.dest_size == 0):
        parser.error("--dest-size value can't be 0")

    # File input
    if os.path.isfile(args.source):
        if (not args.debug) and os.path.exists(args.dest):
            if overwrite_file(args.dest):
                convert_indents(
                    args.source, args.dest,
                    args.source_tabs, args.source_size,
                    args.dest_tabs, args.dest_size,
                    args.debug
                )
        else:
            convert_indents(
                args.source, args.dest,
                args.source_tabs, args.source_size,
                args.dest_tabs, args.dest_size,
                args.debug
            )

    # Directory input
    else:
        if args.source == args.dest:
            parser.error("--source and --dest values can't be the same.")
        no_touch_dirs += () if args.exclude is None else tuple(args.exclude.split(','))
        if args.debug:
            args.dest = '.'  # Prevents errors
        else:
            if not args.dest.endswith(os.path.sep):
                args.dest += os.path.sep
        for dirpath, dirnames, filenames in os.walk(args.source, followlinks=True):
            for d in no_touch_dirs:
                if d in dirnames:
                    dirnames.remove(d)
            if args.extensions is not None:
                handled_files = set()
                for ext in args.extensions.split(','):
                    for f in filenames:
                        if f[-(len(ext)):] == ext:
                            handled_files.add(f)
            else:
                handled_files = filenames
            for filename in handled_files:
                in_path = os.path.abspath(os.path.join(dirpath, filename))
                out_path = os.path.abspath(os.path.join(args.dest, dirpath, filename))
                out_dir = os.path.dirname(out_path)
                if (not args.debug) and (not os.path.exists(out_dir)):
                    os.makedirs(out_dir)
                if (not args.debug) and os.path.exists(out_path):
                    if overwrite_file(out_path):
                        convert_indents(
                            in_path, out_path,
                            args.source_tabs, args.source_size,
                            args.dest_tabs, args.dest_size,
                            args.debug
                        )
                else:
                    convert_indents(
                        in_path, out_path,
                        args.source_tabs, args.source_size,
                        args.dest_tabs, args.dest_size,
                        args.debug
                    )


if __name__ == '__main__':
    main()
