import os, errno
import sys
import tkMessageBox

def main():

	try:
		os.system(os.getenv("ProgramFiles") +"\\"  + r"Microsoft Office\Office12\msaccess.exe")
		
	except OSError, e:
		if e.errno == errno.ENOENT:
			tkMessageBox.showwarning("Error", "Error, Program tidak ditemukan !")
		elif e.errno == errno.ENOEXEC:
			tkMessageBox.showwarning("Error", "Error, Program tidak dapat dieksekusi !")
		else:
			tkMessageBox.showwarning("Error", "Error, Program tidak dapat berjalan di Win32 atau Command Mode ! !")
		
			
if __name__ == '__main__':
	main()