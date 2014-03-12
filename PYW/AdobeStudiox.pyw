import os, errno
import sys
import AdobeContribute
import AdobeDreamweaver
import AdobeFireworks
import AdobeFlash
import AdobeIllustrator
import AdobePhotoshop
import Adobe_Reader_8
import Adobe_Reader_8_Pro
import AppList

ket = """
            1. Adobe Dreamweaver
            2. Adobe Flash
	    3. Adobe Photoshop
	    4. Adobe Contribute
	    5. Adobe Fireworks
	    6. Adobe Illustrator
	    7. Adobe Reader 8
	    8. Adobe Reader 8 Pro
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
		AdobeDreamweaver.main()
		
	elif (pilih == '2'):
		AdobeFlash.main()
			
	elif (pilih == '3'):
		AdobePhotoshop.main()
			
	elif (pilih == '4'):
		AdobeContribute.main()
		
	elif (pilih == '5'):
		AdobeFireworks.main()
			
	elif (pilih == '6'):
		AdobeIllustrator.main()
		
	elif (pilih == '7'):
		Adobe_Reader_8.main()
		
	elif (pilih == '8'):
		Adobe_Reader_8_Pro.main()
		
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
