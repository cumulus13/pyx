import os
import sys

data001 = os.popen("echo %PATH%").readlines()
data002 = str(data001).replace("ython25", "ython26")
os.system("set PATH=" + data002)
#os.popen("set PATH=" + str(data002) + ";%PATH%")
#data003 = os.popen("echo %PATH%").readlines()
#print data003
os.popen("echo %PATH%")