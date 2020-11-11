import os, errno
import sys
import traceback

def main():

	try:
		os.execlp("c:\Program Files\foobar2000\foobar2000.exe", " ")
		
	except:
		print ("ERROR:", traceback.format_exc(print_msg=True))
		
			
if __name__ == '__main__':
	main()
