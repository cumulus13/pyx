import os
import sys

filename = os.path.split(sys.argv[0])

usage = """usage : """ + filename[1] + """ start | stop | restart """

try:
	if (len(sys.argv) < 2):
		os.system("cls")
		print "\n"
		print usage
	else:
		if (sys.argv[1] == "start"):
			os.system("d:\pyx\syslog2odbcd.bat")
			os.system("sysloggen -q -t:192.168.128.1 -p:516 -f:0 -s:6 -m:\"Syslog2ODBC Start Now !\"")
			os.system("cls")
			print "\n"
			print "\t Syslog2ODBC Start Now ! "
		elif (sys.argv[1] == "stop"):
			os.system("kill /f /im syslog2odbc.exe")
			os.system("sysloggen -q -t:192.168.128.1 -p:516 -f:0 -s:6 -m:\"Syslog2ODBC Stop Now !\"")
			os.system("cls")
			print "\n"
			print "\t Syslog2ODBC Stop Now ! "
		elif (sys.argv[1] == "restart"):
			os.system("kill /f /im syslog2odbc.exe")
			os.system("d:\pyx\syslog2odbcd.bat")
			os.system("sysloggen -q -t:192.168.128.1 -p:516 -f:0 -s:6 -m:\"Syslog2ODBC Restart Done ! \"")
			os.system("cls")
			print "\n"
			print "\t Syslog2ODBC Restart Done ! "
		else:
			os.system("cls")
			print "\n\n"
			print usage
except TypeError, e:
	os.system("sysloggen -q -t:192.168.128.1 -p:516 -f:0 -s:6 -m:\"Syslog2ODBC ERROR Starting !\"")
	os.system("cls")