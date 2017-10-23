import module002a
import os
import sys

data = [r"c:\Program Files\DreamMail4\DM2005.exe"]
#data_rapp = os.path.split(data);
#filename = os.path.split(sys.argv[0])
#usage = """ use : """ + filename[1] + """[ kill | help ] """

#try:
#	if (len(sys.argv) > 1):
#		if(sys.argv[1] == 'kill'):
#			os.system("taskkill /f /im " + data_rapp[1])
#		elif(sys.argv[1] == 'help'):
#			print "\n"
#			print "\t", usage
#		else:
#			print "\n"
#			print "\t", usage
#	else:
#		module002.main(data)
#except IndexError, e:
#	print "\n"
#	print "\t", usage

module002a.main(data)