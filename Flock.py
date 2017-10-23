import os,errno
import sys

def main():
	try:
		os.execlp(os.getenv("ProgramFiles") +"\\"  + r"Flock\\flock.exe")

	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n FILE TIDAK DITEMUKAN  ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n PROGRAM TIDAK DITEMUKAN ! \n"
		else:
			print "\n PERINTAH TIDAK DIKENAL ! \n"

if __name__ == '__main__':
	main()

