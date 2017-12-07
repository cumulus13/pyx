import os
import sys
import traceback

__version__ = "0.1"
__test__ = "0.1"
__author__ = "LICFACE"
__url__ = "licface@yahoo.com"
__email__ = "licface@yahoo.com"
__target__ = "all"
__build__ = "2.7"
__error__ = traceback.format_exc()
__usage__ = "Usage: " + str(__file__) + " "

pdata = os.popen("cmdow.exe /t").readlines()

def hideme():
	for i in range(0,len(pdata)):
		j = str(pdata[i]).split("\n")
		#print j[0]
		#print os.path.splitext(__file__)[0]
		#if str(os.path.splitext(__file__)[0]) in j[0]:
		if " - hideme.py" in j[0]:
			#print j[0]
			x = str(str(j[0]).split(" 1 ")[0]).strip()
			#print x
			y = str(x).split(" 1 ")
			#print y[0]
			os.system("cmdow.exe " + str(y[0]) + " /hid ")
		else:
			pass
			
hideme()
				
				