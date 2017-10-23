import os
import sys
import traceback
import subprocess

try:
	mypath = os.getcwd()
	archivepath = os.path.abspath(sys.argv[1])
	if len(sys.argv) == 2:
		os.chdir(r'c:\Program Files\7-Zip')
		subprocess.Popen(['7zg.exe', 'x', str(archivepath), '-o{0}'.format(mypath)])
	else:
		extract_to = os.path.abspath(sys.argv[2])
		os.chdir(r'c:\Program Files\7-Zip')
		subprocess.Popen(['7zg.exe', 'x', str(archivepath), '-o{0}'.format(extract_to)])
except:
	traceback.format_exc()