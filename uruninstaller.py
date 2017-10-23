import sys
import os, errno


try:
	os.execlp(os.getenv("ProgramFiles") +"\\"  + r"Your Uninstaller 2008\uruninstaller.exe")
except OSError, e:
	if e.errno == errno.NOENT:
		print "\n\tProgram tidak ditemukan \n"
	elif e.errno == errno.NOEXEC:
		print "\n\tProgram tidak dapat dieksekusi \n"
	else:
		print "\n\tProgram tidak dapat berjalan di Win32 atau Command Prompt Mode \n"
