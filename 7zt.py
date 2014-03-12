import os
import sys

filename = os.path.split(sys.argv[0])[0]

def test(data):
	dataex = os.popen("7z t " + str(data)).readlines()
	for i in range(0, len(dataex)):
		data001 = str(dataex[i]).split(" ")
		if "Error" in data001[-1]:
			print "ERROR = " + str(dataex[i])
		elif "Failed" in data001[-1]:
			print "ERROR = " + str(dataex[i])
		elif "Method" in data001[-1]:
			print "ERROR = " + str(dataex[i])	
		else:
			pass
	print dataex[-2]
if __name__ == "__main__":
	test(sys.argv[1])