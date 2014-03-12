import os, errno
import sys

def main():

	try:
		os.execlp("D:\PORTABLE_SOFT\Snagit.Portable.9.1.2-AHLY-FANS\SnagitPortable.exe")
		
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n Program tidak ditemukan \n"
		elif e.errno == errno.ENOEXEC:
			print "\n Program bukan program excutable ! \n"
		else:
			print "\n Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"
		
			
if __name__ == '__main__':
	main()
