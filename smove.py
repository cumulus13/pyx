import os
import shutil
import sys

class skipmove(object):
    def __init__(self):
        super(skipmove, self)
        
    def move(self, dst, src = None):
        if src == None:
            src = os.getcwd()
        if os.path.isdir(src):    
            list_src = os.listdir(src)
            data_src = []
            for i in list_src:
                data_src.append(os.path.join(os.path.abspath(src), i))
            for a in data_src:
                if os.path.exists(os.path.join(os.path.abspath(dst), i)):
                    pass
                else:
                    shutil.copy2(i, dst)
        elif os.path.isfile(src):
            if os.path.exists(os.path.join(os.path.abspath(dst), src)):
                pass
            else:
                shutil.copy2(src, dst)
        
    def start(self, src, dst):
        if isinstance(src, list):
            for i in src:
                self.move(i, dst)
        else:
            self.move(src, dst)
            
if __name__ == '__main__':
    c = skipmove()
    if len(sys.argv) == 2:
        c.move(os.getcwd(), sys.argv[1])
    elif len(sys.argv) == 3:
        c.move(sys.argv[1], sys.argv[2])
    elif len(sys.argv) > 3:
        src = " ".join(sys.argv[1:-1])
        c.move(src, dst)