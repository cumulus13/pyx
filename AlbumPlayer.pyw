import module002
import sys
import os

try:
	if (len(sys.argv) > 1):
		if (sys.argv[1] == "kill"):
			os.system("processx -k AP_Extensions.exe")
			os.system("processx -k AlbumPlayerMiniWindow.exe")
			os.system("processx -k AlbumPlayer.exe")
		else:
			pass
	else:
		data = os.getenv("ProgramFiles") +"\\"  + r"AlbumPlayer\AlbumPlayer.exe"
		module002.main(data)
except IndexError, e:
	print "\n\n"
	print "\t ", str(e)
	
