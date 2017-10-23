import os
import sys

file = os.path.abspath(sys.argv[1])
ext = os.path.splitext(sys.argv[1])[1]
os.system("attrib -r -a -s -h -i *" + ext)