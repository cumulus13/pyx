import os
import sys
import argparse

class mirror:
	def __init__(self):
		pass
		
	def mirror(self,src,dst):
		os.system("mirror " + src + " " + dst)
	
	def usage(self):
		parser = argparse.ArgumentParser()
		parser.add_argument("-v","--verbosity", help="Show detail process running", action="store_true")
		parser.add_argument("SOURCE", help="Directory source to copy", type=str, action="store")
		parser.add_argument("DESTINATION", help="Directory destination", type=str, action="store")
		if len(sys.argv) > 2:
			args = parser.parse_args()
			if args.SOURCE:
				if args.DESTINATION:
					DST = os.path.join(args.DESTINATION, os.path.basename(args.SOURCE))
					#print "DST =",DST
					#print "os.path.dirname(args.SOURCE) =",os.path.basename(args.SOURCE)
					if os.path.isdir(DST):
						if args.verbosity:
							print "beginning copy ..."
							#print "PROCESS 1"
							self.mirror(args.SOURCE, DST)
						else:
							self.mirror(args.SOURCE, DST)
							#print "PROCESS 1"
					else:
						if args.verbosity:
							print "make directory",DST
							os.mkdir(DST)
						else:
							os.mkdir(DST)
						if args.verbosity:
							print "beginning copy ..."
							#print "PROCESS 2"
							self.mirror(args.SOURCE, DST)
						else:
							self.mirror(args.SOURCE, DST)
							#print "PROCESS 2"	
				else:
					print "\n"
					print "\t Please insert DESTINATION Directory Name !\n"
			else:
				print "\n"
				print "\t Please insert SOURCE Directory Name !\n"
		else:
			parser.print_help()
		
if __name__ == "__main__":
	myclass = mirror()
	myclass.usage()