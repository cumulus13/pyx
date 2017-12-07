import os, errno
import sys
#import programmingX

one = sys.argv

def usage():
	print "\n\n"
	print "\t\tuse : %s file input"
	print "\n\n"
	#programmingX.utama()

def main():

	try:
		os.system("C:\jython\jython-2.1\jython.bat")
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n Program tidak ditemukan \n"
		elif e.errno == errno.ENOEXEC:
			print "\n Program bukan program excutable ! \n"
		else:
			print "\n Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"
		
			
if __name__ == '__main__':
	
     if len(sys.argv) < 7:
	usage()

     main()