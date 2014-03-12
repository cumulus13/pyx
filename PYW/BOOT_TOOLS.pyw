import os, errno
import flashboot
import booter

ket = """
			1. FlashBoot
			2. Booter
			0. Main Menu
"""

warning = """
			Tidak ada pilihan yang cocok dengan yang anda masukkan ! ! ! !

			Masukkan Nomor Application dengan benar !!!!!

									enjoy by BLACKID
									-----------------
	"""

def main():
	os.system("cls")
	print "\n\n"
	print ket
	print "\n\n"
	print "\n\n"
	pilih = raw_input("\t\t\tMasukkan Nomor Application !  : ")
	print "\n"
	if (pilih == '1'):
		flashboot.main()
	elif (pilih == '2'):
		booter.main()
	else:
		os.system("cls")
		print "\n\n"
		print warning
		print "\n\n"