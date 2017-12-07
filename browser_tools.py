import os, errno
import sys
import AppList

#Browser Tools#

ket = """
                        1. Internet Explorer 7
			2. Mozilla Firefox
			3. Mozilla Firefox (Safe Mode)
			4. Netscape 7.2
			5. Safari Apple
			6. Google Chrome
			7. QtWeb Internet Browser
			0. Main Menu
"""

def main():

	os.system("cls")
	print "\n\n\n"
	print ket
	print "\n\n"
	pilih = raw_input("\t\t\tMasukkan Nomor Application !  : ")
	print "\n"
	if (pilih == '1'):
		ie7()
	if (pilih == '2'):
		firefox()
	if (pilih == '3'):
		firefox_safe_mode()
	if (pilih == '4'):
		netscape()
	if (pilih == '5'):
		Safari()
	if (pilih == '6'):
		gchrome()
	if (pilih == '7'):
		QtWeb()
	if (pilih == '0'):
		AppList.main()

def ie7():

	try:
		os.execlp(os.getenv("ProgramFiles") +"\\"  + r"Internet Explorer\IEXPLORE.EXE")

    
	except OSError, e:
    	   if e.errno == errno.ENOENT:
        	print "\n\t Program tidak ditemukan !!! \n"
    	   elif e.errno == errno.ENOEXEC:
        	print "\n\t Program tidak dapat berjalan di system operation ini !!!\n"
    	   else:
        	print "\n\t\t\t Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"
        

def firefox():

	try:
		os.execlp(os.getenv("ProgramFiles") +"\\"  + r"Mozilla Firefox\\firefox.exe")

    
	except OSError, e:
    	   if e.errno == errno.ENOENT:
        	print "\n\t Program tidak ditemukan !!! \n"
    	   elif e.errno == errno.ENOEXEC:
        	print "\n\t Program tidak dapat berjalan di system operation ini !!!\n"
    	   else:
        	print "\n\t\t\t Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"
        

def firefox_safe_mode():

	try:
		os.execlp(os.getenv("ProgramFiles") +"\\"  + r"Mozilla Firefox\\firefox.exe", "-safe-mode")

    
	except OSError, e:
    	   if e.errno == errno.ENOENT:
        	print "\n\t Program tidak ditemukan !!! \n"
    	   elif e.errno == errno.ENOEXEC:
        	print "\n\t Program tidak dapat berjalan di system operation ini !!!\n"
    	   else:
        	print "\n\t\t\t Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"


def netscape():

	try:
		os.execlp(os.getenv("ProgramFiles") +"\\"  + r"Netscape\Netscape\Netscp.exe")

    
	except OSError, e:
    	   if e.errno == errno.ENOENT:
        	print "\n\t Program tidak ditemukan !!! \n"
    	   elif e.errno == errno.ENOEXEC:
        	print "\n\t Program tidak dapat berjalan di system operation ini !!!\n"
    	   else:
        	print "\n\t\t\t Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"


def QtWeb():

	try:
    		os.execlp(os.getenv("ProgramFiles") +"\\"  + r"QtWeb\QtWeb.exe")

    
	except OSError, e:
    	   if e.errno == errno.ENOENT:
        	print "\n\t Program tidak ditemukan !!! \n"
    	   elif e.errno == errno.ENOEXEC:
        	print "\n\t Program tidak dapat berjalan di system operation ini !!!\n"
    	   else:
        	print "\n\t\t\t Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"


def Safari():

	try:
    		os.execlp(os.getenv("ProgramFiles") +"\\"  + r"Safari\Safari.exe")

    
	except OSError, e:
    	   if e.errno == errno.ENOENT:
        	print "\n\t Program tidak ditemukan !!! \n"
    	   elif e.errno == errno.ENOEXEC:
        	print "\n\t Program tidak dapat berjalan di system operation ini !!!\n"
    	   else:
        	print "\n\t\t\t Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"


def gchrome():

	try:
    		os.execlp("C:\Documents and Settings\Administrator\Local Settings\Application Data\Google\Chrome\Application\chrome.exe")

    
	except OSError, e:
    	   if e.errno == errno.ENOENT:
        	print "\n\t Program tidak ditemukan !!! \n"
    	   elif e.errno == errno.ENOEXEC:
        	print "\n\t Program tidak dapat berjalan di system operation ini !!!\n"
    	   else:
        	print "\n\t\t\t Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"

		
if __name__ == '__main__':
	main()
	
	
#END Browser Tools#
