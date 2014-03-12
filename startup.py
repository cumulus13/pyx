import os, errno
import sys

try:
	os.execlp("c:\XXX\secure.bat")
	#os.execlp(os.getenv("ProgramFiles") +"\\"  + r"ESET\ESET NOD32 Antivirus\egui.exe")
	
except OSError, e:
	if e.errno == errno.NOENT:
		print "\n\tProgram tidak ditemukan !!!\n"
	elif e.errno == errno.NOEXEC:
		print "\n\tProgram tidak dapat dieksekusi !!!\n"
	else:
		print "\n\tProgram tidak dapat berjalan di Win32 atau Command Prompt Mode !!! \n"
