import os, errno
import sys

try:
	os.execlp("C:\Program Files\SiMoCo\simoco.exe")

except OSError, e:
	if e.errno == NOENT:
		print "\n\tProgram tidak ditemukan \n"
	elif e.errno == NOEXEC:
		print "\n\tProgram tidak dapat dieksekusi \n"
	else:
		print "\n\tProgram tidak dapat berjalan di Win32 atau Command Prompt Mode \n"

