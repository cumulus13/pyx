import os, errno
import sys
import iColorFolder
import ObjectDock
import RKLauncher
import SearchSpy
import Tiger_System_Preferences
import UberIcon
import WinRoll
import YzShadow
import AppList
import FlyakiteOSX


ket = """
             1. iColorFolder
             2. ObjectDock
             3. RK Launcher
	     4. SearchSpy
             5. Tiger System Preferences
             6. UberIcon
	     7. WinRoll
             8. Y'z Shadow
             0. Main Menu
	     00.Exit
	     99.Back
"""

def main():
	
	os.system("cls")
	os.system("title FlyakiteOSX - Software")
	print "\n\n"
	print ket
	print "\n\n"
	print "\n\n"
	pilih = raw_input("\t\t\tMasukkan Nomor Application !  : ")
	print "\n"
	if (pilih == '1'):
		iColorFolder.main()
		
	elif (pilih == '2'):
		ObjectDock.main()
			
	elif (pilih == '3'):
		RKLauncher.main()
		
	elif (pilih == '4'):
		SearchSpy.main()
		
	elif (pilih == '5'):
		Tiger_System_Preferences.main()
			
	elif (pilih == '6'):
		UberIcon.main()
		
	elif (pilih == '7'):
		WinRoll.main()
		
	elif (pilih == '8'):
		YzShadow.main()
			
	elif (pilih == '0'):
		AppList.main()
		
	elif (pilih == '99'):
		FlyakiteOSX.main()
		
	elif (pilih == '00'):
		exit()
			
	else:
		os.system("cls")
		print "\n\n"
		print AppList.warning
		print "\n\n"

if __name__ == '__main__' :
	main()