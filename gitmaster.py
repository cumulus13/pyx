import os
import sys

dirname = os.getcwd()
dirbase = os.path.basename(dirname)
file = os.path.basename(__file__)

def usage():
	print "\n"
	print "\t Usage:",file," [url]\n"
	print "\t example:",file," http://gitserver.net/git/repo"
	print "\n"
	
def gitmaster(url='http://gitserver.net/git'):
	try:
		if os.path.isdir(os.path.join(os.path.abspath(dirname),".git")):
			os.system("git push " + str(url) + "/" + dirbase + " master")
	except:
		usage()
		
if __name__ == "__main__":
	if len(sys.argv) > 1:
		if sys.argv[1] == "--help" or sys.argv[1] == '-h' or sys.argv[1] == '-?' or sys.argv[1] == '?':
			usage()
		elif "http:" in sys.argv[1]:
			gitmaster(sys.argv[1])
		else:
			usage()
	else:
		if os.path.isdir(os.path.join(os.path.abspath(dirname),".git")):
			gitmaster()
		else:
			usage()
	