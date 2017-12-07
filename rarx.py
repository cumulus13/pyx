import os, sys, errno, string

name = os.path.split(sys.argv[0])
name2 = name[1]
#print name2

usage = """ usage : """ + name2 + """ [File Name]"""

def rarme():

	try:
		if (sys.argv > 0):
			
			#os.system('cls')
		
			data2 = sys.argv[1]
			try:
				data2b = data2.split(".")
				len_data2b = len(data2b)
				#print len_data2b
			except IndexError, e:
				data2b = data2
				
			dataz = []
			for i in range(0, (len_data2b - 1)):
				dataz.append(data2b[i])
				#print str(i)
				#print "dataz = " + dataz
			
			#print data2b[-1]
			dataxx = string.join(dataz, ".")
			#print "dataz = " + str(dataz)
			#print "dataxx = " + str(dataxx)
			
			
			
			
			#print "data2 = " ,data2, "\n"
		
			data2x  = data2.split(".")
			
			#print "data2x[0] = " ,data2x[0], "\n"
		
			os.system("rar a " + dataxx + ".rar " + data2 + " -zc:\license.txt -pblackid-licface ")
			#os.system("cls")
			print "\n\n"
			
			dataex = os.popen("rar a " + dataxx + ".rar " + data2 + " -zc:\license.txt -pblackid-licface ").readlines()
			#dataex2 = dataex.split("\n")
			print dataex[21], "\n"
			print "Process Archieving " + sys.argv[1] + "\t\t\t\t\t" + "    " + dataex[22], "\n"
			print "\n"
			os.system("rar t " + dataxx + ".rar ")
			
			
		else:
			os.system('cls')
			print "\n\n"
			print usage
			
	except IndexError, e:
		os.system('cls')
		print "\n\n"
		print "\t\t Please insert name of file want to be rar ! \n"
		print "\t\t", usage
		
		
if __name__ == '__main__':
	rarme()