import os
import optparse
import sys


class rnx(object):

    def __init__(self):
        super(rnx, self)

    def rename(self, path, dest=None, upper=None, lower=None, title=None, ext=None, allchange = None):
        path = os.path.abspath(path)
        if ext != None:
            if "." not in ext[0]:
                ext = "." + ext
        if dest == None:
            dest = path
        else:
            dest_ext = os.path.splitext(dest)[1]
            dest_dir = os.path.dirname(dest)
            dest_name = os.path.basename(dest)
        
        path_ext = os.path.splitext(path)[1]
        path_dir = os.path.dirname(path)
        path_name = os.path.basename(path)
        
        if dest_dir == '':
            dest_dir = path_dir
        if dest_ext == '':
            dest_ext = path_ext
        else:
            dest_name = os.path.splitext(dest)[0]
        if ext:
            dest_ext = ext
        if upper:
            dest_name = str(dest_name).upper()
            if allchange:
                dest_ext = str(dest_ext).upper()
        if lower:
            dest_name = str(dest_name).lower()
            if allchange:
                dest_ext = str(dest_ext).lower()
        if title:
            dest_name = str(dest_name).title()
            if allchange:
                dest_ext = str(dest_ext).title()

        file_dest = os.path.join(dest_dir, dest_name + dest_ext)
        
        os.rename(path, file_dest)
        print "\n"
        print "rename : \"" + path + "\" ---> " + file_dest

    def usage(self):
        parser = optparse.OptionParser()
        parser.add_option(
            '-u', '--upper', help='Rename to upper case too', action='store_true')
        parser.add_option(
            '-l', '--lower', help='Rename to lower case too', action='store_true')
        parser.add_option(
            '-t', '--title', help='Rename to title case too', action='store_true')
        parser.add_option(
            '-e', '--ext', help='Destination Extention to', action='store')
        parser.add_option(
            '-a', '--all', help='Rename all (name + ext) to case to', action='store_true')
        
        options, args = parser.parse_args()

        if len(sys.argv) == 1:
            parser.print_help()
        else:
            if len(args) == 2:
                self.rename(args[0], args[1], options.upper, options.lower, options.title, options.ext, options.all)
            elif len(args) == 1:
                self.rename(args[0], None, options.upper, options.lower, options.title, options.ext, options.all)

if __name__ == '__main__':
    c = rnx()
    c.usage()
