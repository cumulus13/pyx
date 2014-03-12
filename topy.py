import os
import sys

try:
	data = os.path.splitext(sys.argv[1])
	data_src = data[0]
	data_dest = data_src + ".py"
	print data_dest
	os.rename(sys.argv[1], data_dest)
	
	
except IndexError, e:
	print "\t ERROR = ", str(e)
	