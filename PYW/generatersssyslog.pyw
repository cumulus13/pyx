import module006
import os
import sys
import time

def cek001():
	if (module006.status("mysql") == "START_PENDING"):
		os.system("cls")
		print "\n"
		print "\t Please Wait for A Moment . "
		time.sleep(10)
		cek002()
	elif (module006.status("mysql") == "STOPPED"):
		os.system("cls")
		print "\n"
		os.system("sysloggen -q -t:192.168.128.1 -p:516 -f:0 -s:6 -m:\"" + "(Syslog2ODBC) Please wait for A Moment . . . " + "\"")
		print "\t Please Wait for A Moment . "
		time.sleep(10)
		cek002()
	else:
		os.system("generatersssyslog.bat")
		
def cek002():
	if (module006.status("mysql") == "START_PENDING"):
		os.system("cls")
		print "\n"
		print "\t Please Wait for A Moment . . "
		time.sleep(10)
		cek003()
	elif (module006.status("mysql") == "STOPPED"):
		os.system("cls")
		print "\n"
		os.system("sysloggen -q -t:192.168.128.1 -p:516 -f:0 -s:6 -m:\"" + "(Syslog2ODBC) Please wait for A Moment . . . " + "\"")
		print "\t Please Wait for A Moment . . "
		
		time.sleep(10)
		cek003()
	else:
		os.system("generatersssyslog.bat")
		
def cek003():
	if (module006.status("mysql") == "START_PENDING"):
		os.system("cls")
		print "\n"
		print "\t Please Wait for A Moment . . . "
		time.sleep(10)
		os.system("sysloggen -q -t:192.168.128.1 -p:516 -f:0 -s:6 -m:\"I'm Sorry Your Time Out because service mysql with status START_PENDDING start with long time & Time Out Please Try again ! \"")
		os.system("cls")
		print "\n"
		print "\t I'm Sorry Your Time Out because service mysql with status START_PENDDING start with long time & Time Out Please Try again ! \n"
	elif (module006.status("mysql") == "STOPPED"):
		os.system("cls")
		print "\n"
		print "\t Please Wait for A Moment . . . "
		time.sleep(10)
		os.system("sysloggen -q -t:192.168.128.1 -p:516 -f:0 -s:6 -m:\"I'm Sorry Your Time Out because service mysql with status STOPPED start with long time & Time Out, Please Try again !\"")
		os.system("cls")
		print "\n"
		print "\t I'm Sorry Your Time Out because service mysql with status STOPPED start with long time & Time Out, Please Try again ! \n"
	else:
		os.system("generatersssyslog.bat")
		pass
		
if __name__ == '__main__':
	cek001()
	
	