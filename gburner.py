import os, errno
import sys
import AppList

ket = """
                     1. Start gBurner
                     2. Help
                     0. Main Menu
		     00.Exit
"""

def main():
	os.system("cls")
	print "\n\n"
	print ket
	print "\n\n"
	pilih = raw_input("\t\t\tMasukkan Nomor Application !  : ")
	print "\n"
	if (pilih == "1"):
		try:
			os.execlp(os.getenv("ProgramFiles") +"\\"  + r"gBurner\gBurner.exe")
		except OSError, e:
			if e.errno == errno.ENOENT:
				print "\n Program tidak ditemukan \n"
			elif e.errno == errno.ENOEXEC:
				print "\n Program bukan program excutable ! \n"
			else:
				print "\n Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"
	elif (pilih == "2"):
		try:
			os.execlp(os.getenv("ProgramFiles") +"\\"  + r"gBurner\gBurner.chm")
		except OSError, e:
			if e.errno == errno.ENOENT:
				print "\n Program tidak ditemukan \n"
			elif e.errno == errno.ENOEXEC:
				print "\n Program bukan program excutable ! \n"
			else:
				print "\n Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"
	elif (pilih == "0"):
		AppList.main()
		
	elif (pilih == "00"):
		exit()
		
	else:
		os.system("cls")
		print "\n\n"
		print AppList.warning
		
if __name__ == '__main__' :
	main()