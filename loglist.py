import sys
import os
import errno

usage = """ use : loglist.py  """
file1 = 'g:\\temp\list.txt'
file2 = 'g:\\temp\list2.txt'
file3 = 'g:\\temp\list3.txt'
exe = 'e:\InstantRails-2.0-win\\ruby\scite\SciTE.exe'
sprt = " "

def utama():
	try:
		os.system('start ' + exe + sprt + file1)
		os.system('start ' + exe + sprt + file2)
		os.system('start ' + exe + sprt + file3)

		
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
		utama()
		
	except IndexError, e:
		os.system("cls")
		print "\n"
		print usage

if __name__ == '__main__':
	main()
