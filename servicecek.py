import os, sys, errno

def cek():

	try:
		os.system('cls')
		print "\n"
	
		data = os.popen("psservice.exe").readlines()
			
		#print data
			
		datalen = len(data)
			
		#datacek = sys.argv[1] 
			
		#print datalen
			
		#print "     Name         " + "PID     " + "Threads     " + "Pri " + "CPU       " + "Owner" 
		#print "     ------------------------------------------------------------" , "\n"
			
		for i in range(0, datalen):
			if "SERVICE_NAME:" in data[i]:
				datax = data[i]
				#print data[i], "\n"
				#print datax
				
				datalen2 = len(datax)
				
				print datalen2
				
				#for j in range
				
				#if sys.argv[1] in datax[i]
				#print data[i + 1], "\n"
				#print data[i + 2], "\n"
				#print data[i + 4], "\n"
				
			elif "STATE" in data[i]:
					print data[i]
					
					print "---------------------------------------"	
			
			else:
				pass
			
		#print "No Process"
			
		#else:
		#	os.system('cls')
		#	print "No Process Found"
		#	#return(1)
		#	#print "\n\n"
		#	#os.system("processx.exe")
			
	except IndexError, e:
		os.system('cls')
		print "\n\n"
		print "Error With Status : 1. " + e
		#os.system("processx.exe | more")
		#print "\n\n"
		#print e
			
	
	
if __name__ == '__main__':
	cek()