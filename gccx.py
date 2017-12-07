import os
import sys
import argparse

GCC_PATH = r"c:\PROGRA~1\CodeBlocks\MinGW\bin\mingw32-g++.exe"
THIS_PATH = os.getcwd()

class gcc(object):
    def __init__(self, gcc_path = None):
        super(gcc, self)
        self.gcc_path = gcc_path
        
    def Gcc(self, filename, gcc_path = None, execute = None):
        if gcc_path == None:
            if self.gcc_path != None:
                gcc_path = self.gcc_path
            else:
                return False
        gcc_path_dir = os.path.dirname(gcc_path)
        os.chdir(gcc_path_dir)
        if os.path.splitext(filename)[1] == '':
            os.system(self.gcc_path + " -Wall -fexceptions -g -c " + os.path.join(THIS_PATH, filename) + " -o" + os.path.join(THIS_PATH, filename + ".o"))
            os.system(self.gcc_path + " -o " + os.path.join(THIS_PATH, filename + ".exe") + " " + os.path.join(THIS_PATH, filename + ".o"))
            if execute:
                os.system(os.path.join(THIS_PATH, filename + ".exe"))
        else:
            os.system(self.gcc_path + " -Wall -fexceptions -g -c " + os.path.join(THIS_PATH, filename) + " -o" + os.path.join(THIS_PATH, os.path.splitext(filename)[0] + ".o"))
            os.system(self.gcc_path + " -o " + os.path.join(THIS_PATH, os.path.splitext(filename)[0] + ".exe") + " " + os.path.join(THIS_PATH, os.path.splitext(filename)[0] + ".o"))
            if execute:
                os.system(os.path.join(THIS_PATH, os.path.splitext(filename)[0] + ".exe"))
            
    def usage(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('FILE', help = 'File source code (*.c|*.cpp)', action = 'store')
        parser.add_argument('-x', '--execute', help = 'Execute file after compile success full', action = 'store_true')
        parser.add_argument('-c', '--compiler', help = 'GCC|CPP Compiler Path (OPTION)', action = 'store')
        if len(sys.argv) > 1:
            args = parser.parse_args()
            self.Gcc(args.FILE, args.compiler, args.execute)
        else:
            parser.print_help()
        
if __name__ == '__main__':
    #if len(sys.argv) > 1:
    c = gcc(GCC_PATH)
        #c.Gcc(sys.argv[1])
    c.usage()
    #else:
        #print "USAGE:", os.path.basename(__file__) + " file[.c|cpp]"