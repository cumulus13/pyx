import os, errno
import sys

def main():

	try:
		os.execlp("K:\PROGRAMMING_STUDIO\CQT_STUDIO\qtjambi-win32-gpl-4.4.3_01\qtjambix.exe")
		
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n Program tidak ditemukan \n"
		elif e.errno == errno.ENOEXEC:
			print "\n Program bukan program excutable ! \n"
		else:
			print "\n Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"
		
			
if __name__ == '__main__':
	main()
