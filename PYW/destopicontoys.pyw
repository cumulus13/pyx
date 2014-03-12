import os, errno
import sys

usage = """use start | stop | restart """

def start():
	try:
		os.execlp("C:\Program Files\Desktop Icon Toy\DesktopIconToy.exe")
		
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n Program tidak ditemukan \n"
		elif e.errno == errno.ENOEXEC:
			print "\n Program bukan program excutable ! \n"
		else:
			print "\n Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"
	
def stop():
	try:
		os.execlp("taskkill /f /im DesktopIconToy.exe")
		
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n Program tidak ditemukan \n"
		elif e.errno == errno.ENOEXEC:
			print "\n Program bukan program excutable ! \n"
		else:
			print "\n Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"
		
	

def main():

	if (sys.argv(1) == start):
		start()
	elif (sys.argv(1) == stop):
		stop()
	elif (sys.argv(1) == restart):
		stop()
		start()
	else:
		print usage
		
			
if __name__ == '__main__':
	main()
