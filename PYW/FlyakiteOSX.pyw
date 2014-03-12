import os, errno
import sys
import FlyakiteOSX_software
import FlyakiteOSX_tools
import Tiger_System_Preferences_v2
import AppList
import desktop_appereance


ket = """
             1. Software
             2. Tools
             3. Tiger System Preferences v2
	     0. Main Menu
	     00.Exit
	     99.Back
"""

def main():
	
	os.system("cls")
	os.system("title FlyakiteOSX")
	print "\n\n"
	print ket
	print "\n\n"
	print "\n\n"
	pilih = raw_input("\t\t\tMasukkan Nomor Application !  : ")
	print "\n"
	if (pilih == '1'):
		FlyakiteOSX_software.main()
		
	elif (pilih == '2'):
		FlyakiteOSX_tools.main()
			
	elif (pilih == '3'):
		Tiger_System_Preferences_v2.main()
				
	elif (pilih == '99'):
		desktop_appereance.main()
		
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