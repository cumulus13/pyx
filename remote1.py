import os
import sys
import time


def start():
	print "starting VNCServer Service ..."
	os.system('sc start vncserver > NUL')
	print "running GOMTray ..."
	os.chdir(r'c:\Program Files\GRETECH\GomRemote2')
	os.startfile("GomRemote2.exe")
	print "running aWARemote Server ..."
	os.chdir(r'c:\Program Files\aWARemote Server')
	os.startfile(r"aWARemote Server.exe")
	
def stop():
	print "stopping VNCServer Service ..."
	os.system('sc stop vncserver > NUL')
	print "stopping  GOMTray ..."
	os.system("px -k GomTray.exe")
	print "stopping aWARemote Server ..."
	os.system("px -k aWARemote Server.exe")
	
def restart():
	stop()
	time.sleep(5)
	start()
	
def usage():
	print "\n"
	if len(sys.argv) == 1:
		print "usage:", sys.argv[0], "start|stop|restart"
	else:
		if sys.argv[1] == 'start':
			start()
		elif sys.argv[1] == 'stop':
			stop()
		elif sys.argv[1] == 'restart':
			restart()
		else:
			print "usage:", sys.argv[0], "start|stop|restart"
			
if __name__ == '__main__':
	usage()