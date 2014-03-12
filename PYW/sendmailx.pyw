import os, errno
import sys

def main():

	try:
		os.execlp("C:\Program Files\SendMail\SendMail.exe")

	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n\tProgram tidak ditemukan !!!\n"
		elif e.errno == errno.ENOEXEC:
			print "\n\tProgram tidak dapat dieksekusi !!! \n"
		else:
			print "\n\tProgram tidak dapat berjalan di Win32 atau Comand Prompt Mode !!! \n"

			
if __name__ == '__main__':
	main()
