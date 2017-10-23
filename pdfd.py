import os
import sys
import subprocess

program = r'c:\Program Files\ElcomSoft\Advanced PDF Password Recovery\APDFPR.EXE'
cli = '-batch'

def decrypt(pdf_file):
	src = os.path.basename(pdf_file)
	dst = os.path.join(os.path.dirname(os.path.abspath(pdf_file)), os.path.splitext(src)[0] + " [DESCRYPT]" + os.path.splitext(src)[1])
	if os.path.isfile(os.path.join(os.path.dirname(os.path.abspath(pdf_file)), os.path.splitext(src)[0] + " [DESCRYPT]" + os.path.splitext(src)[1])) == False:
		subprocess.Popen([program, cli, pdf_file, dst, '-w'])

if __name__ == '__main__':
	decrypt(sys.argv[1])
