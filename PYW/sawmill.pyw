import Cservice
import os
import sys
import pywintypes


sawmill = Cservice.WService("Sawmill8")

def usage():
	print "\n"
	print "\t\tuse : " + os.path.split(sys.argv[0])[1] + " [start|stop|restart|status]"


try:
	if(len(sys.argv) > 1):
		if sys.argv[1] == 'start':
			print "\n"
			sawmill.start()
			print "\t Now Service sawmill is " + sawmill.status()
		elif sys.argv[1] == 'restart':
			print "\n"
			sawmill.restart()
			print "\t Now Service sawmill is " + sawmill.status()
		elif sys.argv[1] == 'stop':
			print "\n"
			sawmill.stop()
			print "\t Now Service sawmill is " + sawmill.status()
		elif sys.argv[1] == 'status':
			print "\n"
			print "\t Service sawmill is " + sawmill.status()
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
		print "\t Your sawmill service not started ! "
	elif datae03[0] == "running":
		#print "\n"
		print "\t Your sawmill service has been started ! "
