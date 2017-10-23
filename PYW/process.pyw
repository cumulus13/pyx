import os, sys, errno

def cek():

	try:
		if (sys.argv > 1):
		
			os.system('cls')
			print "\n"
	
			data = os.popen("processx.exe").readlines()
			
			datalen = len(data)
			
			datacek = str(sys.argv[1])
			dataps = []
			
			for j in range(0, len(datacek)):
				datax = str(datacek).replace(str(datacek[j]), str(datacek[j]).upper())
				dataps.append(datax)
			
			#print datacek ,"\n"
			
			dataps.append(datacek.upper())
			dataps.append(datacek)
			#print dataps
			#for x in range(0, len(dataps)):
			#	print dataps[x]
			
			print "     Name         " + "PID     " + "Threads     " + "Pri " + "CPU       " + "Owner" 
			print "     ------------------------------------------------------------" , "\n"
			
			for i in range(0, datalen):
				for j in range(0, len(dataps)):					
					if dataps[j] in data[i]:
						print data[i], "\n"
					
				else:
					pass
			
			#print "No Process"
			
		elif (sys.argv[1] == "kill"):
			try:
				if (sys.argv[2] > 0):
					print "Process be kill !"
					os.system("taskkill /f /im " + sys.argv[2] + ".exe")
					print "\n"
					
				else:
					print "No Process Kill "
					
			except IndexError, e:
				print "\t Please Insert Name Of Service !"
			
		else:
			#os.system('cls')
			print "No Process Found"
			#return(1)
			#print "\n\n"
			#os.system("processx.exe")
			
	except IndexError, e:
		#os.system('cls')
		print "\n\n"
		os.system("processx.exe | more")
		#print "\n\n"
		#print e
			
	
	
if __name__ == '__main__':
	cek()