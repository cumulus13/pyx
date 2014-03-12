import os, errno

try:
	os.execlp(os.getenv("ProgramFiles") +"\\"  + r"KS-SW\CDMenuPro V6\CDMenuPro.exe")
except OSError, e:
	if e.errno == errno.ENOENT:
		print "\n Program tidak ditemukan \n"
	elif e.errno == errno.ENOEXEC:
		print "\n Program bukan program excutable ! \n"
	else:
		print "\n Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"