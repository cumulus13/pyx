import os
import sys
import traceback
from subprocess import Popen

filename = os.path.split(sys.argv[0])[0]
usage = "\t use: " + filename + " [file image] [/thumb] [file image] "

try:
	if sys.argv[1] == "/t" or sys.argv[1] == "-t":
		Popen([os.getenv("ProgramFiles") +"\\"  + r"IrfanView\i_view32.exe ", "/thumbs " + sys.argv[2]])

	else:
		Popen([os.getenv("ProgramFiles") +"\\"  + r"IrfanView\i_view32.exe " , sys.argv[1]])
except:
	print "\n"
	print usage
	print "\n"
	e = traceback.format_exc()
	print "\t ERROR : \n"
	print "\t " + str(e)
