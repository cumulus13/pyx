import os
import urllib

def pre_rename(filename):
	name = urllib.unquote_plus(filename)
	return name
	
def rename(filename):
	if pre_rename(filename) != filename:
		os.rename(filename, pre_rename(filename))
		
if __name__ == '__main__':
	import sys
	rename(sys.argv[1])
	#print pre_rename(sys.argv[1])