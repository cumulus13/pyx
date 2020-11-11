#!c:/SDK/Anaconda2/python.exe

#this script only create a blank file on Windows encode system support
#not tested on linux
#licface (licface@yahoo.com)

import sys
import os
import clipboard
import sendgrowl
growl = sendgrowl.growl()
import PySnarl as snarl

__version__ = "1.0"
__filename__ = os.path.basename(sys.argv[0])
__usage__ = "\t use : " + __filename__ + " [name of file to create \n\n\t Example : " + __filename__ + " filetxt.py"

def usage():
	import argparse
	parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
	parser.add_argument('FILE', help='File to create, example: file1 file2 file3', action='store', nargs='*')
	if len(sys.argv) == 1:
		parser.print_help()
	else:
		args = parser.parse_args()
		#print "args.FILE =", args.FILE
		for i in args.FILE:
			if os.path.isfile(i):
				q = raw_input("Overwrite it ! [y/n]:")
				if not q == 'y':
					return False
			f = open(i,"w")
			clipboard.copy(os.path.abspath(i))
			f.close()
			#def publish(self, app, event, title, text, host='127.0.0.1', port=23053, timeout=20, icon=None, iconpath=None):
			try:
				growl.publish('mkfile', 'create', 'Make New Blank File', 'File: %s Created' % str(os.path.abspath(i)), iconpath= os.path.join(
			    os.path.dirname(__file__), 'mkfile.jpg'))
			except:
				pass
			try:
				snarl.snShowMessage('mkfile', 'Make New Blank File', 'File: %s Created' % str(os.path.abspath(i)), 20, os.path.join(
			    os.path.dirname(__file__), 'mkfile.jpg'))
			except:
				pass			
		#f.close()

#if len(sys.argv) > 1:
#    f = open(sys.argv[1],"w")
#    f.close()
    
#else:
#    print "\n"
#    print __usage__

if __name__ == '__main__':
	usage()