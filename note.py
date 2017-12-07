import os, errno

try:
	os.execlp(os.getenv("ProgramFiles") +"\\"  + r"EditPlus 2\editplus.exe")
except OSError, e:
	if e.errno == errno.ENOENT:
		print "\n Program tidak ditemukan \n"
	elif e.errno == errno.ENOEXEC:
		print "\n Program bukan program excutable ! \n"
	else:
		print "\n Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"
		
		
**************************************************************************************************		
		
print "\n\n"
	pilih = raw_input("\t\t\tMasukkan Nomor Application !  : ")
	print "\n"
	
	
warning = """
			Tidak ada pilihan yang cocok dengan yang anda masukkan ! ! ! !

			Masukkan Nomor Application dengan benar !!!!!

									enjoy by BLACKID
									-----------------
	"""