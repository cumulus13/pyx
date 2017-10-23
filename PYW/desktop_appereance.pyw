import os, errno
import sys
import AppList
import booter
import FlyakiteOSX
import iColorFolder
import Matrix_Screen_Locker
import Digital_Clock
import Visual_Task_Tips
import WinFlip


ket = """
                        1. Booter
			2. FlyakiteOSX
			3. iColorFolder
			4. Matrix Screen Locker
			5. TimeTools Digital Clock
			6. Visual Task Tips
			7. WinFlip
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
		booter.main()
		
	elif (pilih == '2'):
		FlyakiteOSX.main()
			
	elif (pilih == '3'):
		iColorFolder.main()
		
	elif (pilih == '4'):
		Matrix_Screen_Locker.main()
		
	elif (pilih == '5'):
		Digital_Clock.main()
			
	elif (pilih == '6'):
		Visual_Task_Tips.main()
		
	elif (pilih == '7'):
		WinFlip.main()
			
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