import sys
import os

data001 = os.path.split(sys.argv[2])[1]

os.system("copy /Y \"" + sys.argv[2] + "\" %CD%")
os.system(r"c:\cygwin\bin\tar.exe " + str(sys.argv[1]) + " \"" + str(data001) + "\"" )

