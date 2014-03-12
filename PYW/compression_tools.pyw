import os, errno
import sys
import AppList
import zip7
import ultraiso
import winimage
import winrarx

ket = """
                        1. 7-Zip
			2. UltraISO
			3. WinImage
			4. WinRAR
			0. Main Menu
			00.Exit 
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
		zip7.main()
		
	elif (pilih == '2'):
		ultraiso.main()
			
	elif (pilih == '3'):
		winimage.main()
		
	elif (pilih == '4'):
		winrarx.main
		
	elif (pilih == '0'):
		AppList.main()
		
	elif (pilih == '00'):
		exit()
			
	else:
		os.system("cls")
		print "\n\n"
		print AppList.warning
		print "\n\n"

if __name__ == '__main__' :
	main()