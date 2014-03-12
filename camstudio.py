import os, errno

try:
	os.execlp(os.getenv("ProgramFiles") +"\\"  + r"TechSmith\Camtasia Studio 6\CamtasiaStudio.exe")
except OSError, e:
	if e.errno == errno.ENOENT:
		print "\n Program tidak ditemukan \n"
	elif e.errno == errno.ENOEXEC:
		print "\n Program bukan program excutable ! \n"
	else:
		print "\n Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"