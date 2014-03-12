import os
import sys

pdata = os.popen("cmdow /t").readlines()
#print pdata[1]
pdata_1 = str(pdata[1]).split("      ")
pdata_2 = str(pdata_1[0]).split(" ")
pdata_3 = str(pdata_2[0]).strip()

os.system("cmdow " + pdata_3 + " /siz " + str(sys.argv[1]) + " " + str(sys.argv[2]))