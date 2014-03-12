import module002
import sys
import os

filename = os.path.split(sys.argv[0])

usage = """\t\tuse : """ + filename[1] + """ [syslog | sender]"""

data001 = r"C:\Program Files\theone\SysLogManager Pro\bin\SysLogManagerPro.exe"
data002 = r"C:\Program Files\theone\SysLogSender\bin\SysLogSender.exe"

try:
	if (sys.argv[1] == "syslog"):
		module002.main(data001)
	elif (sys.argv[1] == "sender"):	
		module002.main(data002)
	else:
		os.system("cls")
		print "\n\n"
		print usage
except IndexError, e:
	os.system("cls")
	print "\n\n"
	print usage