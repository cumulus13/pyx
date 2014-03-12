import os, errno
import sys, time
import tomcatstatus



usage = """use : start | stop | restart | status | help"""

def start():
	try:
		os.system("cls")
		print "\n"
		os.system("sc start tomcat6")
		os.system("cls")
		print "\n"
		print "\t Service Has been START"
		
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n Program tidak ditemukan \n"
		elif e.errno == errno.ENOEXEC:
			print "\n Program bukan program excutable ! \n"
		else:
			print "\n Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"
	
def stop():
	try:
		os.system("cls")
		print "\n"
		os.system("net stop tomcat6")
		os.system("cls")
		print "\n"
		print "\t Service Has been STOP"
		
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n Program tidak ditemukan \n"
		elif e.errno == errno.ENOEXEC:
			print "\n Program bukan program excutable ! \n"
		else:
			print "\n Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"
		
def status():
	try:
		os.system("cls")
		#os.system("sc query tomcat6")
		print "\n"
		
		#data001 = os.popen("sc query tomcat6").readlines()
		#data002 = data001[3].split("\n")
		#data003 = data002[0].split("\n")
		#data004 = data003[0].split(": ")
		#data005 = data004[-1].split(" ")
		#print data005
		#os.system("cls");
		#print "\n"
		#print "\t Service is : ", data005[2]
		datax = "tomcat6"
		tomcatstatus.status(datax)
		
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n Program tidak ditemukan \n"
		elif e.errno == errno.ENOEXEC:
			print "\n Program bukan program excutable ! \n"
		else:
			print "\n Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"
		
	except NameError, e:
		print "\t\t", e
	

def main():
	try:
		if (sys.argv[1] == help):
			os.system("cls")
			print "\n"
			print "\t\t", usage
		elif (sys.argv[1] == "start"):
			start()
		elif (sys.argv[1] == "stop"):
			stop()
		elif (sys.argv[1] == "restart"):
			stop()
			start()
			os.system("cls")
			print "\n"
			print "\t Service Has Been RESTART"
		elif (sys.argv[1] == "status"):
			status()
		else:
			os.system("cls")
			print "\n"
			print "\t\t", usage
			
	except IndexError, e:
		os.system("cls")
		print "\n\n"
		print "\t\tPlease Input a Valid Option or Wrong Name Service\n"
		print "\t\t", usage
			
			
if __name__ == '__main__':
	main()








