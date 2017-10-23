import os
import sys
import traceback
import set_global

filename = os.path.split(sys.argv[0])[0]
usage = "\t use : " + filename + " [name of file] [path of file]"
datax = []
for i in range(1,len(sys.argv)):
	#print sys.argv[i]
	datax.append(sys.argv[i])
	
try:
	if len(sys.argv) > 1:
		data_w = """
import module002a,os
data = [r""" + "\"" + str(sys.argv[2]) + "\"" """]
module002a.main(data)
"""
		if ".py" in sys.argv[1]:
			data = open(set_global.__path_master__ + "\\" + str(sys.argv[1]), "w")
			data.write(data_w)
			data.close()
		else:
			data = open(set_global.__path_master__ + "\\" + str(sys.argv[1]) + ".py", "w")
			data.write(data_w)
			data.close()
	else:
		print "\n"
		print usage
		
except:
	data_e = traceback.format_exc()
	print "\n"
	print "\t Error : "
	print "\t " + str(data_e)
		
