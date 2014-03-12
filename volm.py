import os
import sys
import subprocess

__usage__ = "\n\t Usage: " + str(__file__) + "  [-]number|mute|unmute"
print len(sys.argv[1])
if len (sys.argv) > 1:
	if "-" in sys.argv[1]:
		os.system(r"c:\exe\audioApp.exe voldn " + sys.argv[1])
	elif sys.argv[1] == "show":
		subprocess.Popen("c:\Windows\System32\SndVol.exe -f")
	elif len(sys.argv[1]) == 2:
		os.system(r"c:\exe\audioApp.exe volup " + sys.argv[1])
	else:
		os.system(r"c:\exe\audioApp.exe " + " " + sys.argv[1])
else:
	print __usage__