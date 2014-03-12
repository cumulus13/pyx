import os, errno
import sys

def nero():
		try:
		    os.execlp(os.getenv("ProgramFiles") +"\\"  + r"Nero\Nero 7\Nero StartSmart\NeroStartSmart.exe", "-ScParameter=8")

		    
		except OSError, e:
		    if e.errno == errno.ENOENT:
		        print "\n\t Program tidak ditemukan !!! \n"
		    elif e.errno == errno.ENOEXEC:
		        print "\n\t Program tidak dapat berjalan di system operation ini !!!\n"
		    else:
		        print "\n Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"
		        
		    
