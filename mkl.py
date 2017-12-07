import os
import sys

if os.path.isdir(sys.argv[-1]):
    dirname = os.path.split(sys.argv[-1])[-1]
    os.system("mklink /d \"" + str(dirname) + "\" \"" + sys.argv[-1] + "\"")
elif os.path.isfile(sys.argv[-1]):
    filename = os.path.split(sys.argv[-1])[-1]
    os.system("mklink \"" + str(filename) + "\" \"" + sys.argv[-1] + "\"")
else:
    print "\n"
    print "\t Usage: %s [name_link] [directory/file path]" % (os.path.split(__file__)[-1])