import os, errno
import sys

def main():

	try:
		os.execlp("C:\VueScan\vuescan.exe")
		os.system("notepad" + "O:\SCANNER TOOLS\VueScan\\serial.txt")
		
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n Program tidak ditemukan \n"
		elif e.errno == errno.ENOEXEC:
			print "\n Program bukan program excutable ! \n"
		else:
			print "\n Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"
		
			
if __name__ == '__main__':
	main()
