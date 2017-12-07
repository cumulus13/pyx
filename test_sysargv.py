import sys
import os
data = []
for i in range(1,len(sys.argv)):
	print sys.argv[i]
	data.append("r\""+sys.argv[i]+"\"")
	
print data
dataf = open(r"c:\temp\test.txt", "w")
dataf.write(str(data))
dataf.close()
