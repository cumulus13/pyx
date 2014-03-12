import Cservice
import os
import sys
import pywintypes
import dplay2


datasvc = Cservice.WService("O&O CleverCache")

def usage():
	print "\n"
	print "\t\tuse : " + os.path.split(sys.argv[0])[1] + " [start|stop|restart|status]"


try:
	if(len(sys.argv) > 1):
		if sys.argv[1] == 'start':
			print "\n"
			datasvc.start()
			dplay2.play('O&O CleverCache', datasvc.status())
			print "\t Now Service O&O CleverCache is " + datasvc.status()
		elif sys.argv[1] == 'restart':
			print "\n"
			datasvc.restart()
			dplay2.play('O&O CleverCache', datasvc.status())
			print "\t Now Service O&O CleverCache is " + datasvc.status()
		elif sys.argv[1] == 'stop':
			print "\n"
			datasvc.stop()
			dplay2.play('O&O CleverCache', datasvc.status())
			os.system("taskkill /f /im ooccctrl.exe")
			print "\t Now Service O&O CleverCache is " + datasvc.status()
		elif sys.argv[1] == 'status':
			print "\n"
			dplay2.play('O&O CleverCache', datasvc.status())
			print "\t Service O&O CleverCache is " + datasvc.status()
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
		print "\t Your O&O CleverCache service not started ! "
	elif datae03[0] == "running":
		#print "\n"
		print "\t Your O&O CleverCache service has been started ! "