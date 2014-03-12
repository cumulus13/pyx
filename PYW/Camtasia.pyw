import os, errno
import sys


def CamMenuMaker():

	try:
		os.execlp("C:\Program Files\TechSmith\Camtasia Studio 7\CamMenuMaker.exe")

    
	except OSError, e:
    	   if e.errno == errno.ENOENT:
        	print "\n\t Program tidak ditemukan !!! \n"
    	   elif e.errno == errno.ENOEXEC:
        	print "\n\t Program tidak dapat berjalan di system operation ini !!!\n"
    	   else:
        	print "\n\t\t\t Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"
        
    

def CamMenuPlayer():

	try:
		os.execlp("C:\Program Files\TechSmith\Camtasia Studio 7\CamMenuPlayer.exe")

    
	except OSError, e:
    	   if e.errno == errno.ENOENT:
        	print "\n\t Program tidak ditemukan !!! \n"
    	   elif e.errno == errno.ENOEXEC:
        	print "\n\t Program tidak dapat berjalan di system operation ini !!!\n"
    	   else:
        	print "\n\t\t\t Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"


def CamPlay():

	try:
		os.execlp("C:\Program Files\TechSmith\Camtasia Studio 7\CamPlay.exe")

    
	except OSError, e:
    	   if e.errno == errno.ENOENT:
        	print "\n\t Program tidak ditemukan !!! \n"
    	   elif e.errno == errno.ENOEXEC:
        	print "\n\t Program tidak dapat berjalan di system operation ini !!!\n"
    	   else:
        	print "\n\t\t\t Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"

def CamRecorder():

	try:
		os.execlp("C:\Program Files\TechSmith\Camtasia Studio 7\CamRecorder.exe")

    
	except OSError, e:
    	   if e.errno == errno.ENOENT:
        	print "\n\t Program tidak ditemukan !!! \n"
    	   elif e.errno == errno.ENOEXEC:
        	print "\n\t Program tidak dapat berjalan di system operation ini !!!\n"
    	   else:
        	print "\n\t\t\t Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"
        

def CamtasiaStudio():

	try:
		os.execlp("C:\Program Files\TechSmith\Camtasia Studio 7\CamtasiaStudio.exe")

    
	except OSError, e:
    	   if e.errno == errno.ENOENT:
        	print "\n\t Program tidak ditemukan !!! \n"
    	   elif e.errno == errno.ENOEXEC:
        	print "\n\t Program tidak dapat berjalan di system operation ini !!!\n"
    	   else:
        	print "\n\t\t\t Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"
        

def CamTheater():

	try:
		os.execlp("C:\Program Files\TechSmith\Camtasia Studio 7\CamTheater.exe")

    
	except OSError, e:
    	   if e.errno == errno.ENOENT:
        	print "\n\t Program tidak ditemukan !!! \n"
    	   elif e.errno == errno.ENOEXEC:
        	print "\n\t Program tidak dapat berjalan di system operation ini !!!\n"
    	   else:
        	print "\n\t\t\t Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"


def Recovery():

	try:
		os.execlp("C:\Program Files\TechSmith\Camtasia Studio 7\Recovery.exe")

    
	except OSError, e:
    	   if e.errno == errno.ENOENT:
        	print "\n\t Program tidak ditemukan !!! \n"
    	   elif e.errno == errno.ENOEXEC:
        	print "\n\t Program tidak dapat berjalan di system operation ini !!!\n"
    	   else:
        	print "\n\t\t\t Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"


def Setup_EnSharpen_Decoder():

	try:
    		os.execlp("C:\Program Files\TechSmith\Camtasia Studio 7\Setup_EnSharpen_Decoder.exe")

    
	except OSError, e:
    	   if e.errno == errno.ENOENT:
        	print "\n\t Program tidak ditemukan !!! \n"
    	   elif e.errno == errno.ENOEXEC:
        	print "\n\t Program tidak dapat berjalan di system operation ini !!!\n"
    	   else:
        	print "\n\t\t\t Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"






head = """
			###########################################################
			#                                                         #
			#                     CAMTASIA STUDIO                     #
			#                                                         #
			#                       by BLACKID                        #
			#                                                         #
			###########################################################
"""
ket = """
			1.  Camtasia MenuMaker
			2.  Camtasia Menu Player
			3.  Camtasia Player
			4.  Camtasia Recorder
			5.  Camtasia Studio
			6.  Camtasia Theater
			7.  Camtasia Recovery
			8.  Camtasia EnSharpen Decoder
			9.  TechSmith Screen Capture Codec Instalation
"""
warning = """
			Tidak ada pilihan yang cocok dengan yang anda masukkan ! ! ! !

			Masukkan Nomor Application dengan benar !!!!!

									enjoy by BLACKID
									-----------------
	"""
def usage():
    
	try:
    		os.system("cls")

    
	except OSError, e:
    	   if e.errno == errno.ENOENT:
        	print "\n\t Program tidak ditemukan !!! \n"
    	   elif e.errno == errno.ENOEXEC:
        	print "\n\t Program tidak dapat berjalan di system operation ini !!!\n"
    	   else:
        	print "\n\t\t\t Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"

	print "\n\n\n"
	print warning

os.system("cls")
print "\n\n"
print head, "\n\n"
print ket
print "\n\n"
game = raw_input("\t\t\tMasukkan Nomor Game Untuk Main !  : ")
print "\n"
if (game == '1'):
	CamMenuMaker()

elif (game == '2'):
	CamMenuPlayer()

elif (game == '3'):
	CamPlay()

elif (game == '4'):
	CamRecorder()

elif (game == '5'):
	CamtasiaStudio()

elif (game == '6'):
	CamTheater()

elif (game == '7'):
	Recovery()

elif (game == '8'):
	Setup_EnSharpen_Decoder()

elif (game == '9'):
	TSCC()
else:
	#usage()
	print warning

if __name__ == '__main__' :
	usage()
