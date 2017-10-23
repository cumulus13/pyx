import os
import sys
import errno

try:
	os.execlp("C:\Program Files\CodeBlocks\codeblocks.exe")
except OSError, e:
	if e.errno == errno.ENOENT:
		print "\n\rProgram tidak ditemukan !!!!\n"
	elif e.errno == errno.ENOEXEC:
		print "\n\tProgram tidak dapat diexecute !!!!\n"
	else:
		print "\n\tProgram tidak dapat berjalan di Win32 atau Command Prompt Mode \n"
