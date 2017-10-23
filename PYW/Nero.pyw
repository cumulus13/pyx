import os, errno
import sys

def main():
    
       try:
           os.execlp("C:\Program Files\Nero\Nero StartSmart\NeroStartSmart.exe")
    
        
       except OSError, e:
           if e.errno == errno.ENOENT:
               print "\n\t Program tidak ditemukan !!! \n"
           elif e.errno == errno.ENOEXEC:
               print "\n\t Program tidak dapat berjalan di system operation ini !!!\n"
           else:
               print "\n Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"
    
            
if __name__ == '__main__':
    main()
        
    
