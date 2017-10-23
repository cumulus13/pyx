import os, errno
import sys


ket = """
		1. Zend Studio Client
		2. Zend Studio Server
		3. Zend Code Analyzer
		00.Exit
"""

warning = """
		Theare Not Number has been selected !!!!! .................................
		please select a Number if you want 
								Enjoy BLACKID
							        -----------------
"""


def main():
	os.system("cls")
	print "\n\n"
	print ket
	print "\n\n"
	pilih = raw_input("\t\t\tPlease Input Number Application for Select :  ")
	print "\n\n"
	if (pilih == '1'):	

		try:
			os.execlp("C:\Program Files\Zend\ZendStudioClient-5.0.0\\bin\ZDE.exe")
		
		except OSError, e:
			if e.errno == errno.ENOENT:
				print "\n Program tidak ditemukan \n"
			elif e.errno == errno.ENOEXEC:
				print "\n Program bukan program excutable ! \n"
			else:
				print "\n Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"
		
	elif (pilih == '2'):	

		try:
			os.execlp("C:\Program Files\Zend\ZendStudioClient-5.0.0\\bin\ZSS.exe")
		
		except OSError, e:
			if e.errno == errno.ENOENT:
				print "\n Program tidak ditemukan \n"
			elif e.errno == errno.ENOEXEC:
				print "\n Program bukan program excutable ! \n"
			else:
				print "\n Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"
	
	elif (pilih == '3'):	

		try:
			os.execlp("C:\Program Files\Zend\ZendStudioClient-5.0.0\\bin\ZendCodeAnalyzer.exe")
		
		except OSError, e:
			if e.errno == errno.ENOENT:
				print "\n Program tidak ditemukan \n"
			elif e.errno == errno.ENOEXEC:
				print "\n Program bukan program excutable ! \n"
			else:
				print "\n Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"
	
	
	else:
		os.system("cls")
		print warning
			
if __name__ == '__main__':
	main()
