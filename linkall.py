import sys
import os
import optparse

__version__ = "1.0"
__test__ = "0.1"
__author__ = "licface"
__email__ = "licface2yahoo.com"
__sdk__ = "all"

def linker(typed, src, dst):
    os.chdir(src)
    data = os.listdir(os.getcwdu())
    for i in data:
        if typed == "dir":
            if os.path.isdir(i):
                os.system("mklink /d \"" + os.path.join(dst, os.path.basename(i)) + "\" \"" + os.path.abspath(i) + "\"")
        elif typed == "files":
            if os.path.isfile(i):
                os.system("mklink \"" + os.path.join(dst, os.path.basename(i)) + "\" \"" + os.path.abspath(i) + "\"")
        elif typed == "all":
            if os.path.isfile(i):
                os.system("mklink \"" + os.path.join(dst, os.path.basename(i)) + "\" \"" + os.path.abspath(i)+ "\"")
            if os.path.isdir(i):
                os.system("mklink /d \"" + os.path.join(dst, os.path.basename(i)) + "\" \"" + os.path.abspath(i)+ "\"") 
    
def usage():
    parser = optparse.OptionParser(version=__version__+"("+__test__+")")
    parser.add_option("-s", "--source", help="Source Directory contains directory or files", action="store")
    parser.add_option("-d", "--destination", help="Destination Directory contains directory or files", action="store")
    parser.add_option("-t", "--type", help="Type Files or Directory or all (file|dir|all)", action="store")
    args, argv = parser.parse_args()
    if len(sys.argv) > 1:
        if args.type == "files":
            linker("files", args.source, args.destination)
        elif args.type == "dir":
            linker("dir", args.source, args.destination)
        elif args.type == "all":
            linker("all", args.source, args.destination)
        else:
            parser.print_help()
    else:
        parser.print_help()
        
if __name__ == "__main__":
    usage()