import sys
import os
import errno

try:
	datafile = os.path.isfile(sys.argv[1])
	if (sys.argv < 1):
		os.system("cls")
		print "\n"
		print "\t\tPlease insert a name of file & what you find ? \n"
		
	else:
		
		if (datafile == True):
			data = open(sys.argv[1]).readlines()
			lendata = len(data)
			if (sys.argv[2] < 1):
				print "\t\tPlease insert What want you to find ? \n"
			else:
				i = sys.argv[2]
				for x in range(0, lendata):
					if i in data[x]:
						print "\n"
						print "\t Line : " + str(x) + ". " + data[x]
		else:
			os.system("cls")
			print "\n\n"
			print "\t Masukkan Nama File yang benar ! \n"

except IndexError, e:
	os.system("cls")
	print "\n"
	print "ERROR : " , e,  "\n"
	print "ERROR :  Masukkan nama file & opsi yang akan dicari ! \n"
				
			