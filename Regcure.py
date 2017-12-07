import os, errno
import sys

try:
	os.execlp(os.getenv("ProgramFiles") +"\\"  + r"RegCure\RegCure.exe")

except OSError, e:
	if e.errno == errno.ENOENT:
		print "\n\tProgram tidak ditemukan \n"
	elif e.errno == errno.ENOEXEC:
		print "\n\tProgram tidak dapat dieksekusi \n"
	else:
		print "\n\tProgram tidak dapat berjalan di Win32 atau Command Prompt Mode \n"

