import os
import sys
import subprocess

__usage__ == "\t Usage: " + str(__file__) + "[-]number|mute|unmute"

if len sys.argv > 1:
	if "-" in sys.argv[1]:
		subprocess.Popen(r"c:\exe\audioApp.exe voldn",sys.argv[1])
	elif isinstance(sys.argv[1],int):
		subprocess.Popen(r"c:\exe\audioApp.exe volup",sys.argv[1])
	elif:
		subprocess.Popen(r"c:\exe\audioApp.exe",sys.argv[1])
else:
	print __usage__