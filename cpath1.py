import os
import sys
import argparse

PATH_APP = r'c:\exe\cpathx.exe'

def addpath(path, add = None):
    #print "PATH =", path
    if add != None:
        os.system(PATH_APP + " " + path + '\\' + add)
    else:
        os.system(PATH_APP + " " + path)
    
def usage():
    path01 = ''
    if '+' in sys.argv[1:]:
        i = sys.argv[1:].index('+')
        if i > 0:
            #print "AAA"
            print sys.argv[1:]
            #print "sys.argv[1:-i]) =", sys.argv[1:-i-1]
            #print "sys.argv[1:-i]) =", sys.argv[i+2:]
            path01 = os.path.join('\\'.join(sys.argv[1:-i-1]), '\\'.join(sys.argv[i+2:]))
            #print "os.path.splitdrive(path01)[0] =",  os.path.splitdrive(path01)
            if os.path.splitdrive(path01)[0] == '' or os.path.splitdrive(path01)[0] == None:
                #print "XXX"
                root = os.path.splitdrive(os.getcwd())[0]
                #print "root =", root
                path01 = os.path.join(root, "\\", path01)
        else:
            #print "I =", i
            #print "BBB"
            path01 = os.path.join(os.getcwd(), '\\'.join(sys.argv[2:]))
    else:
        #print "CCC"
        path01 = '\\'.join(sys.argv[1:])
        path01 = os.path.join(os.getcwd(), path01)
    #print "path01 =", path01
    addpath(path01)
    
if __name__ == '__main__':
    usage()