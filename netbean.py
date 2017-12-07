import os, errno
import sys

def main():

	try:
		os.execlp(os.getenv("ProgramFiles") +"\\"  + r"NetBeans 6.7.1\\bin\\netbeans.exe")
		
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n Program tidak ditemukan \n"
		elif e.errno == errno.ENOEXEC:
			print "\n Program bukan program excutable ! \n"
		else:
			print "\n Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"
		
			
if __name__ == '__main__':
	main()
