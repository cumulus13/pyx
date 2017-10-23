import os
import sys
import shutil


class html(object):

    def __init__(self, path=None, dest=None):
        super(html, self)
        self.path = path
        self.dest = dest

    def on_rm_error(self, func, path, exc_info):
        os.chmod(path, stat.S_IWRITE)
        os.unlink(path)

    def Remove(self, rmdir):
        try:
            shutil.rmtree(rmdir)
        except:
            shutil.rmtree(rmdir,onerror = self.on_rm_error)

    def move(self, path=None, dest=None, overwrite=None):
        if self.path != None:
            path = self.path
        else:
            if path == None:
                return False
        if self.dest != None:
            dest = self.dest
        else:
            if dest == None:
                return False
        if os.path.isdir(path):
            list_path = os.listdir(path)
            list_cpath = []
            for i in list_path:
                list_cpath.append(os.path.join(
                    os.path.abspath(path), os.path.basename(i)))
            for j in list_cpath:
                if str(j).endswith("htm") or str(j).endswith("html"):
                    if overwrite:
                        if os.path.isfile(os.path.join(dest, j)):
                            os.remove(os.path.join(dest, j))
                        if os.path.isdir(os.path.join(dest, os.path.splitext(j)[0] + "_files")):
                            self.Remove(os.path.join(dest, os.path.splitext(j)[0] + "_files"))
                    if os.path.exists(j):
                        shutil.move(j, dest)
                    if os.path.exists(os.path.splitext(j)[0] + "_files"):
                        shutil.move(os.path.splitext(j)[0] + "_files", dest)
            return True
        elif os.path.isfile(path):
            if overwrite:
                if os.path.isfile(os.path.join(dest, path)):
                    os.remove(os.path.join(dest, path))
                if os.path.isdir(os.path.join(dest, os.path.splitext(path)[0] + "_files")):
                    self.Remove(os.path.join(dest, os.path.splitext(path)[0] + "_files"))
            if str(path).endswith("htm") or str(path).endswith("html"):
                if os.path.exists(path):
                    shutil.move(path, dest)
                if os.path.exists(os.path.splitext(path)[0] + "_files"):
                    shutil.move(os.path.splitext(path)[0] + "_files", dest)
            return True
        else:
            return False

    def moveones(self, path=None, dest=None, overwrite=None):
        if path != None and isinstance(path, list):
            for i in path:
                if self.move(i, dest, overwrite):
                    pass
            return True
        elif path != None and not isinstance(path, list):
            if self.move(path, dest, overwrite):
                pass
            return True
        else:
            return False

    def run(self):
        overwrite = False
        if '-o' in sys.argv:
            overwrite = True
            for i in sys.argv:
                if i == '-o':
                    del(sys.argv[sys.argv.index(i)])
            # print "overwrite =", overwrite
            # print "sys.argv  =", sys.argv
        if len(sys.argv) == 2:
            if not os.path.isdir(os.path.join(os.getcwd(), 'HTML')) or not os.path.isdir(os.path.join(os.getcwd(), 'html')):
                os.mkdir(os.path.join(os.getcwd(), 'HTML'))
            self.moveones(sys.argv[1], os.path.join(os.getcwd(), 'HTML'), overwrite)
        elif len(sys.argv) > 1:
            if os.path.isdir(sys.argv[-1]):
                self.moveones(sys.argv[1:-1], sys.argv[-1], overwrite)
            else:
                print "Please defintion Directory move to !"
                return
        else:
            print "\n"
            print "       Usage: %s [%s] %s" % (os.path.basename(__file__), "SRC", "DST [-o overwrite]" )
            print "\n"
            print "       if SRC if None default SRC will current directory"

    def auto_number(self, dest):
        dest, ext = os.path.splitext(os.path.abspath(dest))
        dest1 = dest
        i = 1
        while True:
            if os.path.exists(dest + "_" + str(i) + ext):
                i = i + 1
            else:
                dest = dest + "_" + str(i) + ext
                break
        if dest == dest1:
            return dest + "_" + "10000" + ext
        else:
            return dest

    # def usage(self):
    #     import argparse
    #     parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter)
    #     parser.add('SOURCE', help='Source Files *.htm[l]', action='store')
    #     parser.add('-d', '--destination', help='Destination Folder, default "HTML" forlder in current directory', action='store')
    #     parser.add('-o', '--overwrite', help='Overwrite if exists', action='store')
    #     if len(sys.argv) == 1:
    #         parser.print_help()
    #     else:
    #         if len(sys.argv) == 2:
    #             self.moveones(os.getcwd(), sys.argv[1])
    #             args = parser.parse_args()


if __name__ == "__main__":
    c = html()
    c.run()
