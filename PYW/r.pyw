import sys
import os

#print os.getcwd()
usage = """use : """ + sys.argv[0] + """ Directory"""
try:
	os.system("cls")
	print "\n"
	datain = sys.argv[1]
	datain2 = datain.split("\n")
	#print "datain2 = ", datain2
	if (len(datain2) < 1):
		print "\t " + usage
	#elif (os.path.isdir(datain2) == False):
	#	print usage
	else:
		data = os.popen("""tree /A /F """ + '"' + datain2[0] + '"').readlines()
		#print "data = ", data
		for i in range(2, len(data)):
			data2 = data[i].split("\n")
			print data2[0]
			
	quest = raw_input("Return to list data ? (y/n) ")
	qqq =  quest[0]
	#print qqq
	if (qqq == "y"):
		os.system('cls')
		print "\n"
		os.system("lss")
		
	elif (qqq == "yes"):
		os.system('cls')
		print "\n"
		os.system("lss")
		
	elif (qqq == "n"):
		pass
	elif (qqq == "m"):
		#os.system("cd /d " + '"' + sys.argv[1] + '"')
		os.system("cd /d " + '"' + sys.argv[1] + '"')
	elif (qqq == " " or "" or Null or null):
		pass
	elif (qqq == "\n"):
		pass
	else:
		pass

except IndexError, e:
	os.system('cls')
	print "\n\n"
	print "\t ERROR : ", e
	print "\n"
	print "\t " + usage
	print "\n"
	os.system("lss")
except IOError, e:
	pass
	
