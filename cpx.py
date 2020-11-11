import shutil
import os
import sys
from make_colors import make_colors
import argparse
import re

class CPX(object):
    def __init__(self):
        super(CPX, self)

    def copy(self, src, dst, overwrite=False, colors=True):
        if not overwrite:
            status_overwrite = ''
        else:
            status_overwrite = "[OVERWRITE]"
        if overwrite:
            if os.path.isfile(os.path.join(dst, src)):
                os.remove(os.path.join(dst, src))
            shutil.copy2(src, dst)
        else:
            if os.path.isfile(os.path.join(dst, src)):
                pass
            else:
                shutil.copy2(src, dst)

        if colors:
            print make_colors(" COPY FILE: ", 'lightgreen', color_type= 'colorama') + make_colors("\"", 'cyan') + make_colors(str(src), 'lightyellow', color_type= 'colorama') + make_colors('"', 'cyan') + make_colors(" --> ", 'white', attrs= ['bold']) + make_colors("\"", 'cyan') + make_colors(os.path.abspath(dst), 'lightgreen', color_type= 'colorama') + make_colors("\"", 'cyan') + make_colors(status_overwrite, 'white', 'red', color_type= 'colorama', attrs=['bold'])
        else:
            print ' COPY FILE: "{0}" -> "{1}" {2}'.format(src, os.path.abspath(dst), status_overwrite)

    def copy_start(self, pattern, dst, overwrite=False, recursive=False, colors=True):
        if recursive:
            list_files = os.popen('dir /b /s %s'%(pattern))
        else:
            list_files = os.popen('dir /b %s'%(pattern))
        # print "LIST FILES:"
        # print list_files.readlines()
        src_dir = os.path.dirname(pattern)

        if not src_dir:
            src_dir = os.getcwd()
        for i in list_files.readlines():
            src = os.path.join(src_dir, str(i).split("\n")[0])
            self.copy(src, dst, overwrite, colors)

    def usage(self):
        parser = argparse.ArgumentParser(formatter_class= argparse.RawTextHelpFormatter)
        parser.add_argument('SRC', action='store', help='Source File, Pattern')
        parser.add_argument('DST', action='store', help='Destination Directory')
        parser.add_argument('-o', '--overwrite', action='store_true', help='Overwrite action')
        parser.add_argument('-r', '--recursive', action='store_true', help='copy with pattern recursive/with sub Directory')
        parser.add_argument('-c', '--colors', action='store_true', help='show log int color')
        if len(sys.argv) == 1:
            parser.print_help()
        else:
            args = parser.parse_args()
            if "*" in args.SRC:
                self.copy_start(args.SRC, args.DST, args.overwrite, args.recursive, args.colors)
            else:
                self.copy_start(args.SRC, args.DST, args.overwrite, args.colors)


if __name__ == '__main__':
    c = CPX()
    c.usage()