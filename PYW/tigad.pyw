import os, errno
import sys
import AppList


tigad = """
			1. Blender
			2. 3D World Atlas
			0. Main Menu
"""

warning = """
			Tidak ada pilihan yang cocok dengan yang anda masukkan ! ! ! !

			Masukkan Nomor Application dengan benar !!!!!

									enjoy by BLACKID
									-----------------
	"""

def blender():

	try:
		os.execlp("C:\Program Files\Blender Foundation\Blender\blender.exe")

    
	except OSError, e:
    	   if e.errno == errno.ENOENT:
        	print "\n\t Program tidak ditemukan !!! \n"
    	   elif e.errno == errno.ENOEXEC:
        	print "\n\t Program tidak dapat berjalan di system operation ini !!!\n"
    	   else:
        	print "\n\t\t\t Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"
        
    

def atlas():

	try:
		os.execlp("C:\Program Files\world atlas\3DWAnVLauncher.exe")

    
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
	else:
		os.system("cls")
		print "\n\n"
		print warning


if __name__ == '__main__' :
	main()
