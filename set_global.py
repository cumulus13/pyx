import os
import sys

__path_module__ = os.path.dirname(sys.argv[0])
__path_master__ = os.path.dirname(sys.argv[0])

if  os.getenv("programfiles") == None or os.getenv("programfiles") == "":
		__path_program__ = r"c:\Program Files"
elif  os.getenv("programfiles") != None or os.getenv("programfiles") != "":
		if os.path.isdir(os.getenv("programfiles")):
				__path_program__  = os.getenv("programfiles")
		else:
				raise 'ERROR Get os.getenv("programfiles")'
else:
		__path_program__ = os.getenv("programfiles")


def test():
	print __path_module__
	print "\n"
	print __path_master__

#test()
