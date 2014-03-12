import sys
import os
import errno
import console

usage = """ use : console [commandline]"""

def startme():
	try:
		os.execlp("consoleme.exe", sys.argv[1] , sys.argv[2])

	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"

def main():
	try:
		startme()
	except IndexError, e:
		#os.system("cls")
		#print "\n"
		#print usage
		console.normal()

if __name__ == '__main__':
	main()
