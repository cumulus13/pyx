import os, errno
import sys
import AcronisDiskEditor
import AcronisMigrateEasy
import AcronisOSSelector
import AcronisPrivacyExpertSuite
import AcronisRecoveryExpertDeluxe
import AcronisDiskDirectorSuite
import AppList

#def usage():
#            print "1. Acronis DiskEditor\n"
#            print "2. Acronis MigrateEasy\n"
#	    print "3. Acronis OS Selector\n"
#            print "4. Acronis Privacy Expert Suite\n"
#	    print "5. Acronis Recovery Expert Deluxe\n"
#	    print "6. Acronis Disk Director Suite \n"
#	    print "0. Main Menu\n"
#            print "00.Exit\n"
#            print "99.Back\n"
	    
ket ="""
            1. Acronis DiskEditor
            2. Acronis MigrateEasy
			3. Acronis OS Selector
			4. Acronis Privacy Expert Suite
			5. Acronis Recovery Expert Deluxe
			6. Acronis Disk Director Suite
			0. Main Menu
			00.Exit
			99.Back
"""
	    
def main():
	os.system("cls")
	print "\n\n"
	print ket
	#usage()
	print "\n\n"
	print "\n\n"
	pilih = raw_input("\t\t\tMasukkan Nomor Application !  : ")
	print "\n"
	if (pilih == '1'):
		AcronisDiskEditor.main()
		
	elif (pilih == '2'):
		AcronisMigrateEasy.main()
			
	elif (pilih == '3'):
		AcronisOSSelector.main()
			
	elif (pilih == '4'):
		AcronisOSSelector.main()
		
	elif (pilih == '5'):
		AcronisPrivacyExpertSuite.main()
		
	elif (pilih == '6'):
		AcronisRecoveryExpertDeluxe.main()
		
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
