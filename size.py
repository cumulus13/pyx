import os, sys, errno

def cek():

	try:
	
		if (sys.argv <> 0):
			os.system('cls')
			print "\n"
			data = os.popen(r"c:\cygwin\bin\du -s -h " + sys.argv[1]).read()
			data2 = data.split(" ")
			data3 = data2[0].split("\t")
			
			#print data3
			
			print "\t Size of " + "'" + sys.argv[1] + "'" + " = " + data3[0]
			
		else:
			print "\n\n"
			name = os.path.split(sys.argv[0])
			print "Usage : " + name[1] + " [File or Directory]"
			print "\n"
	
	except IndexError, e:
		#os.system('cls')
		print "\n\n"
		name = os.path.split(sys.argv[0])
		print "Usage : " + name[1] + " [File or Directory]"
		print "\n"
	
if __name__ == '__main__':
	cek()