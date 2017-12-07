import os
import sys

usage = "usage:",__file__," [link] [name of file]"

def main():
	#print "len(sys.argv) = ", len(sys.argv)
	if len(sys.argv) < 1:
		print "\n"
		print "\t",usage
		print "\n"
	else:
		if len(sys.argv) == 2:
			filename = os.path.split(sys.argv[1])[1]
			if filename != None or filename != '':
				os.system(r"wget.exe" + " -c -t 0 --no-check-certificate " + sys.argv[1] + " -O D:\\DOWNLOADS\\" + filename) 
			else:
				print "\n"
				print "\tERROR: Can't get Name Of File ! \n"
				print "\t",usage
				print "\n"
		else:
			os.system(r"wget.exe" + " -c -t 0 --no-check-certificate " + sys.argv[1] + " -O D:\\DOWNLOADS\\" + sys.argv[2]) 
			
if __name__ == "__main__":
	main()