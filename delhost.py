try:
    import clr
except ImportError:
    raise SystemError('You Must Download pythonnet before and install it !')
import sys
import os
import traceback
DLL_PATH = 'c:\Program Files\Simple DNS Plus API for .NET and COM'
if "IronPython" in sys.version:
    clr.AddReferenceToFileAndPath(os.path.join(DLL_PATH, 'SDNSAPI.dll'))
else:
    sys.path.append(DLL_PATH)
    clr.AddReference("SDNSAPI")
#clr.AddReference("SDNSAPI")
#import JHSoftware.SimpleDNSPlus as api
from JHSoftware.SimpleDNSPlus import *
try:
	filename = os.path.split(sys.argv[0])[1]
	
	usage = "\t use : " + filename + " example.com "
	
	host = "127.0.0.1"	
	port = 8053
	passwd = "blackid"
	
	conn = Connection(host, port, passwd)

	if sys.argv[1] == None:
		print usage
	else:
		if "www." in sys.argv[1]:
			print "\t Sorry !, you can't del zone with preffix \"www.\", please remove \"www.\"\n"
			print usage
		else:
			Zone = conn.RemoveZone(str(sys.argv[1]))
				
except:
	data_e = traceback.format_exc()
	print "ERROR : \n"
	print "\t" + str(data_e)
	print "-"*85
	print "\n"
	print usage