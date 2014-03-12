import os, errno
import sys
#from PyQt4.QtGui import *
#from PyQt4.QtCore import *

def main():

	try:
		os.execlp(os.getenv("ProgramFiles") +"\\"  + r"CDBurnerXP\cdbxppx.exe")
		
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n Program tidak ditemukan \n"
			#QMessageBox.warning("Program tidak ditemukan", unicode(e))
		elif e.errno == errno.ENOEXEC:
			print "\n Program bukan program excutable ! \n"
			#QMessageBox.warning("Program bukan program excutable !", unicode(e))
		else:
			print "\n Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"
			#QMessageBox.warning("Error, Program tidak dapat berjalan di Win32 atau Command Mode ! ", unicode(e))
		
			
if __name__ == '__main__':
	main()
