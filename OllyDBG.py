import os, errno
import sys

def main():

    print "\t\t Olly Debug Software \n"
    print "\t\t\t by BLACKID \n"
    print "\t 1. OllyDBG 1  \n"
    print "\t 2. OllyDBG 2  \n"
    option = raw_input("\t\tMasukkan Pilihan Anda      :  ")
    if (option == '1'):
	try:
	    os.execlp("E:\OllyDBG_CiM's Edition\RAMODBG\RAMODBG\OLLYDBG.exe")
        
	except OSError, e:
	    if e.errno == errno.ENOENT:
		print "\n Program tidak ditemukan \n"
	    elif e.errno == errno.ENOEXEC:
		print "\n Program bukan program excutable ! \n"
	    else:
		print "\n Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"
      
    elif (option == '2'):
	try:
	    os.execlp("E:\OllyDBG_CiM's Edition\ollydbg.exe")
        
	except OSError, e:
	    if e.errno == errno.ENOENT:
		print "\n Program tidak ditemukan \n"
	    elif e.errno == errno.ENOEXEC:
		print "\n Program bukan program excutable ! \n"
	    else:
		print "\n Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"

    else :
	os.system("cls")
	print "\n\n"
        print "\t\t Error Program Tidak ditemukan !!!!!!!!! \n"
          
if __name__ == '__main__':
	main()
