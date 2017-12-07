import os
import sys
import datetime
import subprocess

TPATH = os.getenv('TEMP')
def usage():
	print "\n"
	print "\t Usage:",os.path.split(__file__)[1]," [string] [PATH]"
	
def search(strfind,path):
	#print "d =", "dir /s  \"" + str(path) + "\"\\" + str(strfind)
	d = os.popen("dir /s  \"" + str(path) + "\"\\" + str(strfind)).read()
	suffix = str(datetime.date.isoformat(datetime.datetime.now())).replace('-','.')
	f = open(os.path.join(TPATH,"search."+ suffix + ".txt"), 'w')
	f.write(d)
	f.close()
	subprocess.Popen([r"c:\Program Files\Programmer's Notepad\pn.exe", os.path.join(TPATH,"search."+ suffix + ".txt")])
	
	
if __name__ == "__main__":
	if len(sys.argv) == 1:
		usage()
	else:
		if sys.argv[2] == ".":
			search(sys.argv[1], os.getcwd())
		else:
			search(sys.argv[1], sys.argv[2])