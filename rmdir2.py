import os
import sys
import shutil
import argparse

def on_rm_error(self, func, path, exc_info):
    os.chmod(path, stat.S_IWRITE)
    os.unlink(path)

def rmdir(path = None, exception = None):
    if path:
        if os.path.isdir(path):
            listdir = os.listdir(path)
        else:
            return "Invalid Path Please specific it !"
    listdir = os.listdir(os.getcwd())
    if exception:
        if isinstance(exception, list):
            for a in listdir:
                for e in exception:
                    if str(e).lower() == str(a).lower():
                        del(listdir[listdir.index(a)])
        else:
            for a in listdir:
                if str(a).lower() == str(exception).lower():
                    del(listdir[listdir.index(a)])            
    for i in listdir:
        if os.path.isdir(os.path.join(os.getcwd(), i)):
            shutil.rmtree(i, True, onerror = on_rm_error)
    return True
            
def usage():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', help = 'Root path to delete, default is current directory', action = 'store')
    parser.add_argument('-e', '--exception', help = 'Exception will not to delete', action = 'store', nargs = '*')
    parser.add_argument('-q', '--quite', help = 'No Question', action = 'store_true')
    if len(sys.argv) > 1:
        args = parser.parse_args()
        if args.quite:
            pass
        else:
            q = raw_input("Continue [y/n]: ")
            if q == 'y':
                pass
            else:
                return None
        if rmdir(args.path, args.exception) == True:
            pass
        else:
            print rmdir(args.path, args.exception)
            print "\n"
            parser.print_help()
    else:
        parser.print_help()

if __name__ == '__main__':
    print "TARGET =", os.getcwd()
    #if len(sys.argv) > 1:
        #if sys.argv[1] == '-q' or sys.argv[1] == '--quite' or sys.argv[1] == '/q' or sys.argv[1] == '/Q' or sys.argv[1] == '\q' or sys.argv[1] == '\Q':   
            #rmdir()
        #else:
            #q = raw_input("Continue [y/n]: ")
            #if q == 'y':
                #rmdir()
    #else:
        #q = raw_input("Continue [y/n]: ")
        #if q == 'y':
            #rmdir()
            
    usage()