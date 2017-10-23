import os, errno
import sys

def main():

	try:
		os.execlp("D:\BARU001\PORTABLE_SOFT\SQLite Expert Professional v2.0.45\SQLite Expert Professional.exe")
		
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n Program tidak ditemukan \n"
		elif e.errno == errno.ENOEXEC:
			print "\n Program bukan program excutable ! \n"
		else:
			print "\n Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"
		
			
if __name__ == '__main__':
	main()
