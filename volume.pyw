import os
import sys
if "-" in sys.argv[1]:
	# print "str(int(sys.argv[1])*10000) = -%s" % (str(abs(int(sys.argv[1]))*10000))
	os.system(r"c:\exe\nircmd.exe" + " changesysvolume -" + str(abs(int(sys.argv[1]))*10000))
else:
	# print "str(int(sys.argv[1])*10000) =", str(int(sys.argv[1])*10000)
	os.system(r"c:\exe\nircmd.exe" + " changesysvolume " + str(int(sys.argv[1])*10000))