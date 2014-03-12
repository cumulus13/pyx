import sys
import os
import errno

usage = """ use : vix [File Want to Edit]"""
file = r'd:\\pyx\vid.bat'
sprt = " "

def vim():
	try:
		os.system('start ' + file + sprt + sys.argv[1] )

		
		#os.execlp("consolesmall.exe")
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"


def main():
	try:	
		vim()
		
	except IndexError, e:
		os.system("cls")
		print "\n"
		print usage

if __name__ == '__main__':
	main()
