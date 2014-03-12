import os
import sys
import cekstate

filename = os.path.split(sys.argv[0])
usage = "\t use: " + filename[1] + """ [name of service] """

try:
	data = sys.argv[1]
	
	cekstate.cekstate2(data)
except IndexError, e:
	os.system("cls")
	print "\n"
	print usage