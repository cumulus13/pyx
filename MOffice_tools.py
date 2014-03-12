import os, errno
import sys
import AppList
import Digital_Certificate_for_VBA_Projects
import Microsoft_Clip_Organizer
import Microsoft_Office_2007_Language_Settings
import Microsoft_Office_Diagnostics
import Microsoft_Office_Picture_Manager
import MOffice

ket = """
            1. Digital Certificate for VBA Projects
            2. Microsoft Clip Organizer
	    3. Microsoft Office 2007 Language Settings
	    4. Microsoft Office Diagnostics
	    5. Microsoft Office Picture Manager
            0. Main Menu
            00.Exit
            99.Back
"""

def main():
	os.system("cls")
	print "\n\n"
	print burning_tools
	print "\n\n"
	print "\n\n"
	pilih = raw_input("\t\t\tMasukkan Nomor Application !  : ")
	print "\n"
	if (pilih == '1'):
		Digital_Certificate_for_VBA_Projects.main()
		
	elif (pilih == '2'):
		Microsoft_Clip_Organizer.main()
			
	elif (pilih == '3'):
		Microsoft_Office_2007_Language_Settings.main()
		
	elif (pilih == '4'):
		Microsoft_Office_Diagnostics.main()
			
	elif (pilih == '5'):
		Microsoft_Office_Picture_Manager.main()
		
	elif (pilih == '0'):
		AppList.main()
			
	elif (pilih == '00'):
		sys.exit()
		
	elif (pilih == '99'):
		MOffice.main()
			
	else:
		os.system("cls")
		print "\n\n"
		print AppList.warning
		print "\n\n"

if __name__ == '__main__':
	main()