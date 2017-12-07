import os, errno
import sys
import AppList
import Force_System_File_Update
import Current_User_Settings
import Rebuild_Icon_Cache
import System_Files_Updater
import FlyakiteOSX

ket = """
            1. Force System File Update
            2. Current User Settings
            3. Rebuild Icon Cache
            4. System Files Updater
	    99.Back
	    00.Exit
	    0. Main Menu
"""

def main():
	
	os.system("cls")
	os.system("title FlyakiteOSX - Tools")
	print "\n\n"
	print ket
	print "\n\n"
	print "\n\n"
	pilih = raw_input("\t\t\tMasukkan Nomor Application !  : ")
	print "\n"
	if (pilih == '1'):
		Force_System_File_Update.main()
		
	elif (pilih == '2'):
		Current_User_Settings.main()
			
	elif (pilih == '3'):
		Rebuild_Icon_Cache.main()
		
	elif (pilih == '4'):
		System_Files_Updater.main()
		
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