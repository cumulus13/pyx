#!c:/Anaconda/python.exe

import os
import sys
try:
	import win32ui
except:
	pass

usage = "Usage: " + os.path.basename(sys.argv[0])[0:-4] + " [start|stop|restart]"

def stop():
	os.system('sc config "STC_Mobile Imola Modem Device Helper" start= demand > NUL')
	os.system('sc stop "STC_Mobile Imola Modem Device Helper" > NUL')
	os.system('taskkill /f /im ModemApplication.exe > NUL')
	os.system('taskkill /f /im ModemListener.exe > NUL')
	os.system('taskkill /f /im ServiceManager.exe > NUL')
	
def start():
	os.system('sc config "STC_Mobile Imola Modem Device Helper" start= demand > NUL')
	os.system('sc start "STC_Mobile Imola Modem Device Helper" > NUL')
	pwd = os.getcwd()
	os.chdir(r"c:\Program Files")
	os.startfile(r"c:\Program Files\Quick net\ModemApplication.exe")
	os.chdir(pwd)
	
if len(sys.argv) > 1:
	if sys.argv[1] == 'stop':	
		stop()
	elif sys.argv[1] == 'start':
		start()
	elif sys.argv[1] == 'restart':
		stop()
		start()
	else:
		print "\n"
		print usage
		try:
			import win32con
			win32ui.MessageBox(usage, 'Usage', win32con.MB_OK)
		except:
			pass
else:
	print "\n"
	print usage
	try:
		import win32con
		win32ui.MessageBox(usage, 'Usage', win32con.MB_OK)
	except:
		pass