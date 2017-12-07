import sys
try:
    import winshell
except ImportError:
    print "Print winshell module not found !"
    print "Please install first !"
    sys.exit(0)
# import os

winshell.delete_file(sys.argv[1])
