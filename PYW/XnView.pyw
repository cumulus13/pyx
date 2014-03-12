import os, errno

try:
	os.execlp("I:\HARD_DISK from AnyWhere\PICTURE TOOLS\XnViewU3\XnView\\xnview.exe")
	
except OSError, e:
	if e.errno == errno.ENOENT:
		print "\n Program tidak ditemukan \n"
	elif e.errno == errno.ENOEXEC:
		print "\n Program bukan program excutable ! \n"
	else:
		print "\n Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"
