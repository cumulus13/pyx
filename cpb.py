import datetime
import os
import sys
import optparse
import shutil


class copy(object):

    def __init__(self, src=None, dst=None):
        super(copy, self)
        self.src = src
        self.dst = dst

    def timenow(self):
        now = datetime.datetime.now()
        return datetime.datetime.strftime(now, '%y%m%d%H%M%S%f')

    def cpb(self, src=None, overwrite=None, dest=None):
        if src is None:
            if not self.src is None:
                src = self.src
            else:
                return WindowsError('Can\'t find source file !')
        # if dst == None:
        # 	if self.dst != None:
        # 		dst = self.dst
        # 	else:
        # 		return WindowsError('Error destination file !')

        abspath = os.path.abspath(src)
        dirname = os.path.dirname(abspath)
        filename = os.path.basename(abspath)
        fileext = os.path.splitext(filename)[1]
        nullfilename = os.path.splitext(filename)[0]

        if dest:
            if os.path.isdir(dest):
                destfile = os.path.join(
                    dest, nullfilename + "_" + self.timenow() + fileext)
            else:
                destfile = os.path.join(
                    dirname, nullfilename + "_" + self.timenow() + fileext)
        else:
            destfile = os.path.join(
                dirname, nullfilename + "_" + self.timenow() + fileext)
        if os.path.exists(destfile):
            if overwrite:
                os.remove(destfile)
                shutil.copyfile(abspath, destfile)
            else:
                q = raw_input("File exists, overwrite ? (y/n): ")
                if str(q).lower() == 'y':
                    os.remove(destfile)
                    shutil.copyfile(abspath, destfile)
        else:
            shutil.copyfile(abspath, destfile)

    def usage(self):
        usage = " file1 file2 file3 ... [options]"
        parser = optparse.OptionParser(usage=usage)
        # parser.add_option('FILE', help='File copy to', action='store')
        parser.add_option(
            '-p', '--path', help='Option destination copy file', action='store')
        parser.add_option('-o', '--overwrite',
                          help='Overwrite', action='store_true')
        if len(sys.argv) == 1:
            parser.print_help()
        else:
            options, args = parser.parse_args()
            if len(args) > 0:
                for i in args:
                    self.cpb(i, options.overwrite, options.path)
            else:
                print "No File copy to !"
if __name__ == '__main__':
    c = copy()
    c.usage()
