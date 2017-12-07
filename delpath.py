import os
import sys

class delpath(object):
    def __init__(self, path = None):
        super(delpath, self)
        self.path = path
        
    def delPath(self, path = None):
        if path == None:
            if self.path != None:
                path = self.path
            else:
                return False
            
        MPATH = os.getenv('PATH')
        #print "MPATH  =", MPATH
        if MPATH[-1] == ';':
            MPATH = MPATH[:-1]
        MPATH = str(MPATH).split(";")
        #print "MPATH 2 =", MPATH
        MPATH2 = []
        for i in MPATH:
            MPATH2.append(str(i).lower())
        #print "MPATH2 =", MPATH2
        #print "-" * 170
        #if str(path).replace('\\', '\\\\') in MPATH2:
        if str(path).lower() in MPATH2:
            del(MPATH2[MPATH2.index(str(path).lower())])
            #print "MPATH2 1 =", MPATH2
            MPATH3 = ";".join(MPATH2)
            #print "-" * 170
            #os.system("SET PATH=" + MPATH3)
            os.system('c:\pyx\mpath.bat ' + MPATH3)
            os.system('SET PATH=' + MPATH3)
            os.environ.update({'TEMP': MPATH3})
            f = open(r'c:\pyx\xpath.bat', 'w')            
            f.write('@echo off\n')
            f.write('SET PATH=' + MPATH3)
            f.close()
            #os.environ.update({'PATH': MPATH3,})
            #print "PATH  =", path
            #print "PATH1 =", str(path).replace('\\', '\\\\')
            #print "TRUE"
        else:
            pass
            #print "PATH =", path
            #print "PATH1 =", str(path).replace('\\', '\\\\')
            #print "FALSE"
        
if __name__ == "__main__":
    c = delpath()
    c.delPath(sys.argv[1])