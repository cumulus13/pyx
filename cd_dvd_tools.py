import os, errno
import sys
import easy_boot
import cdmaster32
import ultraiso
import gburner
import cdcheck
import cdmenuprox
import AppList

ket = """
                        1. EasyBoot
			2. CDMaster32
			3. UltraISO
			4. gBurner
			5. CDCheck
			6. CDMenuPro V6
			0. Main Menu
		       00. Exit	
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
		easy_boot.main()
		
	elif (pilih == '2'):
		cdmaster32.main()
			
	elif (pilih == '3'):
		ultraiso.main()
		
	elif (pilih == '4'):
		gburner.main()
		
	elif (pilih == '5'):
		cdcheck.main()
			
	elif (pilih == '6'):
		cdmenuprox.main()
		
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