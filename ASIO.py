import os, errno
import sys

ket = """
		1. ASIOALL Control Panel
		2. User Manual (PDF)
		3. Exit
"""

warning = """
		Masukkan Pilihan yang Benar !!!!!!!!!
"""

def main():
	os.system("cls")
	print "\n\n"
	print ket
	print "\n\n"
	print "\n\n"
	pilih = raw_input("\t\t\tMasukkan Nomor Application !  : ")
	print "\n\n"
	if (pilih == '1'):
		try:
			os.execlp(os.getenv("ProgramFiles") +"\\"  + r"ASIO4ALL v2\\a4apanel.EXE")		
		
		except OSError, e:
			if e.errno == errno.ENOENT:
				print "\n Program tidak ditemukan \n"
			elif e.errno == errno.ENOEXEC:
				print "\n Program bukan program excutable ! \n"
			else:
				print "\n Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"
				
	elif (pilih == '2'):
		try:
			os.system("\os.getenv("ProgramFiles") +"\\"  + r"ASIO4ALL v2\ASIO4ALL v2 Instruction Manual.pdf\"")
			os.system("pause >> nul")
		
		except OSError, e:
			if e.errno == errno.ENOENT:
				print "\n Program tidak ditemukan \n"
			elif e.errno == errno.ENOEXEC:
				print "\n Program bukan program excutable ! \n"
			else:
				print "\n Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"
				
	elif (pilih == '3'):
		sys.system("cls")
		sys.exit()

	else:
		print warning
			
if __name__ == '__main__':
	main()
