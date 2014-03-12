import Cservice
import os
import sys
import pywintypes


visualsvn = Cservice.WService("VisualSVNServer")

def usage():
	print "\n"
	print "\t\tuse : " + os.path.split(sys.argv[0])[1] + " [start|stop|restart|status]"


try:
	if(len(sys.argv) > 1):
		if sys.argv[1] == 'start':
			print "\n"
			visualsvn.start()
			print "\t Now Service visualsvn is " + visualsvn.status()
		elif sys.argv[1] == 'restart':
			print "\n"
			visualsvn.restart()
			print "\t Now Service visualsvn is " + visualsvn.status()
		elif sys.argv[1] == 'stop':
			print "\n"
			visualsvn.stop()
			print "\t Now Service visualsvn is " + visualsvn.status()
		elif sys.argv[1] == 'status':
			print "\n"
			print "\t Service visualsvn is " + visualsvn.status()
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
		print "\t Your VisualSVN service not started ! "
	elif datae03[0] == "running":
		#print "\n"
		print "\t Your VisualSVN service has been started ! "