import os
import sys
import shutil

class html(object):
    def __init__(self, path = None, dest = None):
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
        
    def move(self, path = None, dest = None):
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
                list_cpath.append(os.path.join(os.path.abspath(path), os.path.basename(i)))
            for j in list_cpath:
                if str(j).endswith("htm") or str(j).endswith("html"):
                    if os.path.exists(j):
                        shutil.copy2(j, dest)
                    if os.path.exists(os.path.splitext(j)[0] + "_files"):
                        if os.path.exists(os.path.join(dest, os.path.basename(os.path.splitext(j)[0] + "_files"))):
                            self.Remove(os.path.join(dest, os.path.basename(os.path.splitext(j)[0] + "_files")))
                        if not os.path.exists(os.path.join(dest, os.path.basename(os.path.splitext(j)[0] + "_files"))):
                            shutil.copytree(os.path.splitext(j)[0] + "_files", os.path.join(dest, os.path.basename(os.path.splitext(j)[0] + "_files")))
            return True
        elif os.path.isfile(path):
            if str(path).endswith("htm") or str(path).endswith("html"):
                if os.path.exists(path):
                    shutil.copy2(path, dest)
                if os.path.exists(os.path.splitext(path)[0] + "_files"):
                    if os.path.exists(os.path.join(dest, os.path.basename(os.path.splitext(path)[0] + "_files"))):
                        self.Remove(os.path.join(dest, os.path.basename(os.path.splitext(path)[0] + "_files")))
                    if not os.path.exists(os.path.join(dest, os.path.basename(os.path.splitext(path)[0] + "_files"))):
                        shutil.copytree(os.path.splitext(path)[0] + "_files", os.path.join(dest, os.path.basename(os.path.splitext(path)[0] + "_files")))
            return True
        else:
            return False
                
    def moveones(self, path = None, dest = None):
        if path != None and isinstance(path, list):
            for i in path:
                if self.move(i, dest):
                    pass
            return True
        elif path != None and not isinstance(path, list):
            if self.move(path, dest):
                pass
            return True
        else:
            return False
        
    def run(self):
        if len(sys.argv) == 2:
            self.moveones(os.getcwd(), sys.argv[1])
        elif len(sys.argv) > 1:
            self.moveones(sys.argv[1:-1], sys.argv[-1])
        else:
            print "\n"
            print "       Usage: %s [%s] %s" % (os.path.basename(__file__), "SRC", "DST")
            print "\n"
            print "       if SRC if None default SRC will current directory"
            
            
if __name__ == "__main__":
    c = html()
    c.run()