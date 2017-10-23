import module002
import sys
import os

data = r"c:\Program Files\JGsoft\PowerGREP4\PowerGREP4.exe"

try:
	if len(sys.argv) <= 1:
		module002.main(data)	
	else:
		if (sys.argv[1] == "kill"):
			os.system("taskkill /f /im  PowerGREPUndoManager4.exe")
			os.system("taskkill /f /im  PowerGREPConversionManager.exe")
			os.system("taskkill /f /im  PowerGREP4.exe")
		else:
			pass
except IndexError, e:
	print e

