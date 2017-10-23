import module002
import sys
import os
data = os.getenv("ProgramFiles") +"\\"  + r"FirefoxPreloader\FirefoxPreloader.exe"
usage = """use  : """ + os.path.split(sys.argv[0].split(".")[0])[1] +  """ [kill | help] """

try:
	len_data = len(sys.argv)
	#print "len_data = ", len_data, "\n"
	if (len_data < 2):		
		module002.main(data)
	else:
		if (sys.argv[1] == "kill"):
			module002.kill(data)
		elif (sys.argv[1] == "help"):
			print "\n\t " + usage
		else:
			print "\n\t " + usage

except IndexError, e:
	print "\n"
	print "ERROR : ", str(e)
