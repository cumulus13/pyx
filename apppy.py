import os 
import sys 

def main():
    os.system ("cls")
    print "\n\n"
    os.system ("dir d:\LIST_DATA_BACKUP")
    print "\n"
    print """
             1. Read Data
             2. Back
    """
    print "\n"
    pilihan = raw_input("\t\tMasukkan Pilihan Anda !:   ")
    print "\n"
    if (pilihan == '1'):
	try:
	    os.system ("scite d:\LIST_DATA_BACKUP")
	    
	except OSError, e:
	    if e.errno == errno.ENOENT:
			    print "\n Program tidak ditemukan \n"
	    elif e.errno == errno.ENOEXEC:
			    print "\n Program bukan program excutable ! \n"
	    else:
			    print "\n Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"
    elif (pilihan == '2'):
	os.system("cls")
	os.system("d:\\xxx\writelist.bat")
	sys.exit()
	
    else:
	os.system("cls")
	print "\n\n"
	print "\t\t\tMasukkan Data dengan benar !!!"
	print "\n"

if __name__ == '__main__':
    main()
    