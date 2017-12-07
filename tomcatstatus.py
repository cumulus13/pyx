import os
import sys, errno

try:
	def status(service):
		data001 = os.popen("sc query " + service).readlines()
		data002 = data001[3].split("\n")
		data003 = data002[0].split("\n")
		data004 = data003[0].split(": ")
		data005 = data004[-1].split(" ")
		
		#data001a = data001[0].split(" 1060")
		#data001b = data001a[0].split("OpenService ")
		
		#print data001b[1]
		
		#if (data001b[1] == "FAILED"):
		#	print "\t\t Please Insert The Correct Name Service !"
		#else:
		os.system("cls");
		print "\n"
		print "\t Service is : ", data005[2]
			
		return data005[2]
		
except IndexError, e:
	print "ERROR With Status : ", e
	print "\n"
	print "\t Service is : ", data005[2]