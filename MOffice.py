import os, errno
import sys
import AppList
import word
import Access
import excel
import PowerPoint
import visio
import OneNote
import MOffice_tools

ket = """
            1. Microsoft Office Word 2007
            2. Microsoft Office Access 2007
	    3. Microsoft Office Excel 2007
	    4. Microsoft Office PowerPoint 2007
	    5. Microsoft Office Visio 2007
	    6. Microsoft Office OneNote 2007
	    7. Microsoft Office Tools
            0. Main Menu
            00.Exit
            99.Back
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
		word.main()
		
	elif (pilih == '2'):
		Access.main()
			
	elif (pilih == '3'):
		excel.main()
		
	elif (pilih == '4'):
		PowerPoint.main()
		
	elif (pilih == '5'):
		visio.main()
		
	elif (pilih == '6'):
		OneNote.main()
		
	elif (pilih == '7'):
		MOffice_tools.main()
			
	elif (pilih == '0'):
		AppList.main()
		
	elif (pilih == '00'):
		sys.exit()
		
	elif (pilih == '99'):
		AppList.main()
		
	else:
		os.system("cls")
		print "\n\n"
		print AppList.warning
		print "\n\n"

if __name__ == '__main__':
	main()