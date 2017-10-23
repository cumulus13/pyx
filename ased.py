import os, errno
import sys

try:
	os.execlp(os.getenv("ProgramFiles") +"\\"  + r"Ased\\ased3.0b16.exe")

    
except OSError, e:
    if e.errno == errno.ENOENT:
        print "\n\t Program tidak ditemukan !!! \n"
    elif e.errno == errno.ENOEXEC:
        print "\n\t Program tidak dapat berjalan di system operation ini !!!\n"
    else:
        print "\n Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"
        
    
