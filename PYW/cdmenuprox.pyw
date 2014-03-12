import os, errno
import sys
import AppList

ket = """
                     1.  CD Menu Pro Main Program
                     2.  CD Menu Pro Button Creator
                     3.  CD Menu Pro HTML Viewer
		     4.  CD Menu Pro Language Editor
		     5.  CD Menu Pro RTF Viewer
		     6.  CD Menu Pro Search File
		     7.  CD Menu Pro Text Viewer
		     8.  CD Menu Pro Update Manager
		     9.  CD Menu Pro ResourceBrowser
		     10. About
		     0.  Main Menu
		     00. Exit
"""

def main():
	os.system("cls")
	print "\n\n"
	print ket
	print "\n\n"
	pilih = raw_input("\t\t\tMasukkan Nomor Application !  : ")
	print "\n"
	if (pilih == "1"):
		try:
			os.execlp("C:\Program Files\KS-SW\CDMenuPro V6\CDMenuPro.exe")
		except OSError, e:
			if e.errno == errno.ENOENT:
				print "\n Program tidak ditemukan \n"
			elif e.errno == errno.ENOEXEC:
				print "\n Program bukan program excutable ! \n"
			else:
				print "\n Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"
	elif (pilih == "2"):
		try:
			os.execlp("C:\Program Files\KS-SW\CDMenuPro V6\ButtonCreator.exe")
		except OSError, e:
			if e.errno == errno.ENOENT:
				print "\n Program tidak ditemukan \n"
			elif e.errno == errno.ENOEXEC:
				print "\n Program bukan program excutable ! \n"
			else:
				print "\n Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"
	elif (pilih == "3"):
		try:
			os.execlp("C:\Program Files\KS-SW\CDMenuPro V6\CDMP_HtmlViewer.exe")
		except OSError, e:
			if e.errno == errno.ENOENT:
				print "\n Program tidak ditemukan \n"
			elif e.errno == errno.ENOEXEC:
				print "\n Program bukan program excutable ! \n"
			else:
				print "\n Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"
	elif (pilih == "4"):
		try:
			os.execlp("C:\Program Files\KS-SW\CDMenuPro V6\ CDMP_LanguageEditor.exe")
		except OSError, e:
			if e.errno == errno.ENOENT:
				print "\n Program tidak ditemukan \n"
			elif e.errno == errno.ENOEXEC:
				print "\n Program bukan program excutable ! \n"
			else:
				print "\n Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"
	elif (pilih == "5"):
		try:
			os.execlp("C:\Program Files\KS-SW\CDMenuPro V6\CDMP_RtfViewer.exe")
		except OSError, e:
			if e.errno == errno.ENOENT:
				print "\n Program tidak ditemukan \n"
			elif e.errno == errno.ENOEXEC:
				print "\n Program bukan program excutable ! \n"
			else:
				print "\n Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"
	elif (pilih == "6"):
		try:
			os.execlp("C:\Program Files\KS-SW\CDMenuPro V6\CDMP_Search.exe")
		except OSError, e:
			if e.errno == errno.ENOENT:
				print "\n Program tidak ditemukan \n"
			elif e.errno == errno.ENOEXEC:
				print "\n Program bukan program excutable ! \n"
			else:
				print "\n Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"
	elif (pilih == "7"):
		try:
			os.execlp("C:\Program Files\KS-SW\CDMenuPro V6\CDMP_TextViewer.exe")
		except OSError, e:
			if e.errno == errno.ENOENT:
				print "\n Program tidak ditemukan \n"
			elif e.errno == errno.ENOEXEC:
				print "\n Program bukan program excutable ! \n"
			else:
				print "\n Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"
	elif (pilih == "8"):
		try:
			os.execlp("C:\Program Files\KS-SW\CDMenuPro V6\KSSW_UpdateManager.exe")
		except OSError, e:
			if e.errno == errno.ENOENT:
				print "\n Program tidak ditemukan \n"
			elif e.errno == errno.ENOEXEC:
				print "\n Program bukan program excutable ! \n"
			else:
				print "\n Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"
	elif (pilih == "9"):
		try:
			os.execlp("C:\Program Files\KS-SW\CDMenuPro V6\ResourceBrowser.exe")
		except OSError, e:
			if e.errno == errno.ENOENT:
				print "\n Program tidak ditemukan \n"
			elif e.errno == errno.ENOEXEC:
				print "\n Program bukan program excutable ! \n"
			else:
				print "\n Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"
	elif (pilih == "10"):
		try:
			os.execlp("C:\Program Files\KS-SW\CDMenuPro V6\KS_SW.exe")
		except OSError, e:
			if e.errno == errno.ENOENT:
				print "\n Program tidak ditemukan \n"
			elif e.errno == errno.ENOEXEC:
				print "\n Program bukan program excutable ! \n"
			else:
				print "\n Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"
	elif (pilih == "0"):
		AppList.main()
		
	elif (pilih == "00"):
		exit()
		
	else:
		os.system("cls")
		print "\n\n"
		print AppList.warning
		
if __name__ == '__main__' :
	main()