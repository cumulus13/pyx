import os, errno
import sys
import TigerPrefs
import CPUZ
import TweakGDS
import AppList
import FlyakiteOSX

ket = """
              1. CPUZ
              2. Tiger System Preferences v2
              3. TweakGDS
	      99.Back
	      00.Exit
	      0. Main Menu
"""



def main():
	
	os.system("cls")
	os.system("title FlyakiteOSX - Tiger System Preferences v2")
	print "\n\n"
	print ket
	print "\n\n"
	print "\n\n"
	pilih = raw_input("\t\t\tMasukkan Nomor Application !  : ")
	print "\n"
	if (pilih == '1'):
		CPUZ.main()
		
	elif (pilih == '2'):
		TigerPrefs.main()
			
	elif (pilih == '3'):
		TweakGDS.main()
		
	elif (pilih == '99'):
		FlyakiteOSX.main()
			
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