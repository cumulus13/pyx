import os
import sys
import subprocess
__author__ = "licface(licface@yahoo.com)"
__usage__ = "\n \t" +  str(__file__) + ": [Name Of Directory]"

if len(sys.argv) > 1:
		if os.path.isdir(r"c:\Program Files\MediaMonkey") == False:
				print "\n"
				print "\t NOT FOUND: Media Monkey NOT INSTALLED !"
		elif sys.argv[1] == "-h" or sys.argv[1] == "--h" or sys.argv[1] == "--help" or sys.argv[1] == "/?":
				print __usage__
		else:
				subprocess.Popen([r"c:\Program Files\MediaMonkey\MediaMonkey (non-skinned).exe"])
				#os.spawnl(os.P_DETACH, r"c:\Program Files\TagScanner\Tagscan.exe" + " " + os.path.abspath(sys.argv[1]))
else:
		#subprocess.Popen([r"c:\Program Files\TagScanner\Tagscan.exe", os.getcwd()])\
		subprocess.Popen([r"c:\Program Files\MediaMonkey\MediaMonkey (non-skinned).exe"])