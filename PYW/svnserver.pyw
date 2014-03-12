import Cservice
import os
import sys
import pywintypes

apache = Cservice.WService("subversionApache-1")
subversion = Cservice.WService("subversionSubversion-1")

def usage():
	print "\n"
	print "\t\tuse : " + os.path.split(sys.argv[0])[1] + " [start|stop|restart|status]"


try:
	if(len(sys.argv) > 1):
		if sys.argv[1] == 'start':
			print "\n"
			apache.start()
			subversion.start()
			print "\t Now Service Apache is " + apache.status()
			print "\n"
			print "\t Now Service Subversion is " + subversion.status()
		elif sys.argv[1] == 'restart':
			print "\n"
			apache.restart()
			subversion.restart()
			print "\t Now Service Apache is " + apache.status()
			print "\n"
			print "\t Now Service Subversion is " + subversion.status()
		elif sys.argv[1] == 'stop':
			print "\n"
			apache.stop()
			subversion.stop()
			print "\t Now Service Apache is " + apache.status()
			print "\n"
			print "\t Now Service Subversion is " + subversion.status()
		elif sys.argv[1] == 'status':
			print "\n"
			print "\t Service Apache is " + apache.status()
			print "\n"
			print "\t Service Subversion is " + subversion.status()
	else:
		usage()
except IndexError, e:
	usage()
	
except pywintypes.error, e:
	datae01 = str(e).split(',')
	datae02 = datae01[2].split(" ")
	datae03 = datae02[-1].split(".")
	#print datae03
	if datae03[0] == "started":
		#print "\n"
		print "\t Your service not started ! "
	elif datae03[0] == "running":
		#print "\n"
		print "\t Your service has been started ! "