import os, sys
import traceback

__version__ = "1.0"
__test__ = "0.1"
__author__ = "LICFACE"
__url__ = "licface@yahoo.com"
__email__ = "licface@yahoo.com"
__target__ = "all"
__build__ = "2.7"
__error__ = traceback.format_exc()

pdata = os.popen("cmdow /b| grep ping.exe").readlines()
for i in range(0,len(pdata)):
		x = str(pdata[i]).split("\n")
		#print x
		y = x[0]
		z = str(pdata[i]).split("     ")[0]
		
		xx = str(z).split(" ")
		yy =str(xx[0]).strip()
		#print yy
		if sys.argv[1] == "show":
				os.system(r"c:\exe\cmdow " + str(yy) + " /vis ")
		elif sys.argv[1] == "hide":
				os.system(r"c:\exe\cmdow.exe " + str(yy) + " /hid ")
		elif sys.argv[1] == "top":
				os.system(r"c:\exe\cmdow.exe " + str(yy) + " /top ")
		elif sys.argv[1] == "nor":
				os.system(r"c:\exe\cmdow.exe " + str(yy) + " /not ")
		else:
				os.system(r"c:\exe\cmdow.exe " + str(yy) + " " + str(sys.argv[1]))