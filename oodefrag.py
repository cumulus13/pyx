import module002
import module003
import module004
import os
import sys

file_base = os.path.split(sys.argv[0])
filename = file_base[1]
usage = "\t Use : " + filename + """ [start | stop | status]"""

data001 = "OODefragAgent"
data002 = os.getenv("ProgramFiles") +"\\"  + r"OO Software\Defrag\oodcnt.exe"

if (len(sys.argv) > 1):
	if (sys.argv[1] == "start"):
		module003.main(data001)
		module002.main(data002)
	elif (sys.argv[1] == "stop"):
		module003.main(data001)
		os.system("taskkill /f /im oodcnt.exe")
	elif (sys.argv[1] == "status"):
		#st_service = os.system("sc query " + data001)
		#print "\t Status Service is : " + str(st_service)
		module004.status(data001)
	else:
		os.system("cls")
		print "\n\n"
		print usage
else:
	os.system("cls")
	print "\n\n"
	print usage

