import os, errno
import sys

def main():

	try:
		os.execlp("C:\Program Files\RouterSim\CCNA6\CCNA6.exe" "C:\PROGRA~1\ROUTER~1\CCNA6\CCNA6.exe")
		
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n Program tidak ditemukan \n"
		elif e.errno == errno.ENOEXEC:
			print "\n Program bukan program excutable ! \n"
		else:
			print "\n Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"
		
			
if __name__ == '__main__':
	main()
