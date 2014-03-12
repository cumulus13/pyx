import os, errno
import sys
import AppList

tigad = """
			1. Blender
			2. 3D World Atlas
			0. Main Menu
"""

def blender():

	try:
		os.execlp(os.getenv("ProgramFiles") +"\\"  + r"Blender Foundation\Blender\blender.exe")

    
	except OSError, e:
    	   if e.errno == errno.ENOENT:
        	print "\n\t Program tidak ditemukan !!! \n"
    	   elif e.errno == errno.ENOEXEC:
        	print "\n\t Program tidak dapat berjalan di system operation ini !!!\n"
    	   else:
        	print "\n\t\t\t Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"
        
    

def atlas():

	try:
		os.execlp(os.getenv("ProgramFiles") +"\\"  + r"world atlas\3DWAnVLauncher.exe")

    
	except OSError, e:
    	   if e.errno == errno.ENOENT:
        	print "\n\t Program tidak ditemukan !!! \n"
    	   elif e.errno == errno.ENOEXEC:
        	print "\n\t Program tidak dapat berjalan di system operation ini !!!\n"
    	   else:
        	print "\n\t\t\t Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"


def main():
	os.system("cls")
	print "\n\n\n"
	print tigad
	print "\n\n"
	pilih = raw_input("\t\t\tMasukkan Nomor Application !  : ")
	print "\n"
	if (pilih == '1'):
		blender()
		
	if (pilih == '2'):
		atlas()
		
	if (pilih == '0'):
		AppList.main()


if __name__ == '__main__' :
	main()
