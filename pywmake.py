#!c:/SDK/Anaconda2/python.exe
from __future__ import print_function
import os
import sys
import traceback
from make_colors import make_colors

ROOT_PATH = r"d:\TOOLS\pyx\\"

def maker(file_exc, saveas=None):
	appname = os.path.abspath(file_exc[0])
	filename = os.path.split(sys.argv[0])[0]
	destname = os.path.splitext(os.path.split(appname)[1])[0] + ".pyw"
	if saveas:
		destname = os.path.split(saveas)[1]
		if not os.path.splitext(saveas)[1] == '.pyw':
			destname = destname + ".pyw"
	file_exc.remove(file_exc[0])
	file_exc.insert(0, appname)
	try:
		data_w = """
import module002a,os
data = """ + str(file_exc) + """
module002a.main(data)
"""
		data = open(ROOT_PATH + destname, "w")
		data.write(data_w)
		data.close()

	except:
		data_e = traceback.format_exc()
		print ("\n")
		print ("\t Error : ")
		print ("\t " + str(data_e))
		
def usage():
	import argparse
	parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
	parser.add_argument('APPS', help='Program/App executable with(out) arguments', action='store', nargs='*')
	parser.add_argument('-o', '--saveas', help='optional save as name, default is app/program name', action='store')
	if len(sys.argv) == 1:
		parser.print_help()
	else:
		args = parser.parse_args()
		maker(args.APPS, args.saveas)
		
if __name__ == '__main__':
	usage()