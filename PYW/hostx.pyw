import os, errno
import sys

editor = "C:\Program Files\EditPlus 2\editplus.exe"
utama = "C:\WINDOWS\system32\drivers\etc\hosts"

def main():

	try:
		os.execlp(utama)
		
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n Program tidak ditemukan \n"
		elif e.errno == errno.ENOEXEC:
			print "\n Program bukan program excutable ! \n"
		else:
			print "\n Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"
		
			
if __name__ == '__main__':
	main()

