import module002
import sys
import os

data = os.getenv("ProgramFiles") +"\\"  + r"JGsoft\PowerGREP4\PowerGREP4.exe"

try:
	if len(sys.argv) <= 1:
		module002.main(data)	
	else:
		if (sys.argv[1] == "kill"):
			os.system("taskkill /f /im  PowerGREPUndoManager.exe")
			os.system("taskkill /f /im  PowerGREPConversionManager.exe")
			os.system("taskkill /f /im  PowerGREP.exe")
		else:
			pass
except IndexError, e:
	print e

