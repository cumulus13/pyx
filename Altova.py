import os
import module002
import sys
import errno

filename = os.path.split(sys.argv[0])
usage = """ use : """ + filename[1] + " [sql | diff] \n"

try:
	if (len(sys.argv) < 1):
		os.system("cls")
		print "\n"
		print "\t" + usage
	
	elif (sys.argv[1] == "sql"):
		data1 = os.getenv("ProgramFiles") +"\\"  + r"Altova\DatabaseSpy2010\DatabaseSpy.exe"
		module002.main(data1)
	elif (sys.argv[1] == "diff"):
		data2 = os.getenv("ProgramFiles") +"\\"  + r"Altova\DiffDog2010\DiffDog.exe"
		modulr002.main(data2)
	else:
		os.system("cls")
		print "\n"
		print "\t" + usage
		
except IndexError, e:
	os.system("cls")
	print "\n"
	print "\t" + usage
	