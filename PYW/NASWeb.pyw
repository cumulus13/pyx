import module002a
import Cservice
import os
import sys

filename = os.path.split(sys.argv[0])
usage = "\t use : " + filename[1] + " [ service [start|stop|restart] | app] \n"

try:
	if len(sys.argv) > 1:
		if sys.argv[1] == "service":
			data = "NAWebServer"
			svc = Cservice.WService(data)
			if sys.argv[2] != None:
				if sys.argv[2] == "start":
					data = "NAWebServer"
					svc.start()
				elif sys.argv[2] == "stop":
					svc.stop()
				elif sys.argv[2] == "restart":
					svc.restart()
				else:
					print "\n"
					print "\t " + usage
			else:
				print "\n"
				print "\t " + usage
		elif sys.argv[1] == "app":
			data = [r"c:\Program Files\NetworkActiv Web Server 3.5\NetworkActivWebServerV3.5.exe"]
			module002a.main(data)
		else:
			print "\n"
			print "\t " + usage
	else:
		print "\n"
		print "\t Default Option is \"app\"\n"
		default_input = raw_input("\t Do you want to start no ? (y\\n) : ")
		if default_input == "y":
			data = [r"c:\Program Files\NetworkActiv Web Server 3.5\NetworkActivWebServerV3.5.exe"]
			module002a.main(data)
		elif default_input == "n":
			print "\t bye ... \n"
			sys.exit()
		else:
			print "\n"
			print usage
			print "\t -----------------------------------------------------"
			print "\t you not select one option ! \n"
			print "\t bye ... \n"
			sys.exit()
except IndexError, e:
	print "\n"
	print "\t ERROR : " + str(e) + "\n"
	
except NameError, e:
	print "\n"
	print "\t ERROR : " + str(e) + "\n"
			