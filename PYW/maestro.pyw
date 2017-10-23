import os
import module002
import sys
import errno

filename = os.path.split(sys.argv[0])
usage = """ use : """ + filename[1] + " [mysql | oracle] \n"

try:
	if (len(sys.argv) < 1):
		os.system("cls")
		print "\n"
		print "\t" + usage
	
	elif (sys.argv[1] == "oracle"):
		data1 = r"C:\Program Files\SQL Maestro Group\Oracle Maestro\OracleMaestro.exe"
		module002.main(data1)
	elif (sys.argv[1] == "mysql"):
		data2 = r"D:\PORTABLE_SOFT\Portable SQL Maestro\SQL Maestro for MySQL.exe"
		module002.main(data2)
	elif (sys.argv[1] == "mssql"):
		data3 = r"C:\Program Files\SQL Maestro Group\MS SQL Maestro\MsMaestro.exe"
		module002.main(data3)
	else:
		os.system("cls")
		print "\n"
		print "\t" + usage
		
except IndexError, e:
	os.system("cls")
	print "\n"
	print "\t" + usage
	