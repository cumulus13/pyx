import os, errno
import sys

def main():

	try:
		os.execlp("C:\WINDOWS\system32\spool\drivers\w32x86\3\fppdis3a.exe /verbose /restart /autoexit=0")
		
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n Program tidak ditemukan \n"
		elif e.errno == errno.ENOEXEC:
			print "\n Program bukan program excutable ! \n"
		else:
			print "\n Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"
		
			
if __name__ == '__main__':
	main()