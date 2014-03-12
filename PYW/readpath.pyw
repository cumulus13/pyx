import os, sys
import module002

data = open("path.txt", "r").readlines()
lendata = len(data)
#print data
datax = open("pathx.txt", "w")
datay = open("pathx.txt", "a")
for i in range(0, lendata):
	dataa = data[i].split("\n")
	datay.writelines(dataa)
	#datax.append(datax)
	#print datax

os.system(r"c:\cygwin\bin\cat.exe" + " pathx.txt")

