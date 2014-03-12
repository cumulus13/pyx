import os, sys, errno
import time
	

def cek(lendata=4):
	#try:
		os.system('cls')
		print "\n"
		data = os.popen(r"c:\cygwin\bin\df.exe -h -v").readlines()
		#data2 = data.split("\n")
		
		#print data
		
		sizelen = len(data)
		
		#print "SizeLen = ", sizelen, "\n"
		
		print "  Drive Size  Used  Available  Use(%) ", "\n"
		
		for i in range(lendata, sizelen):
			datax01 =  data[i].split("/"), "\n"
			#print "datax01 = ", datax01
			datax02 = datax01[0][0].split(":")
			#print "datax01b = ", datax01[0][0]
			#print datax01
			#print datax02[0]
			#print datax01[0][0]
			#print datax02[1]
			datax03 = datax02[1].split("         ")
			#print datax03[1]
			#print datax03[2]
			#print datax03
			
			#datax04 = datax03[2].split("G")
			#print datax04[2]
			#datax05 = datax04[2].split(" ")
			#print datax05[-2]
			print "   " + datax02[0] + ":\\" + datax03[2], "\n"
			
			#datax06 = datax03[2].split("%")
			#print datax06[0]
			
		
		#print "\n\n"	
		#print data[8], "\n"
		#print data[9], "\n"
		#print data[10], "\n"
		#print data[11], "\n"
		#print data[12], "\n"
		#print data[13], "\n"
		#print data[14], "\n"
		
		
	#except IndexError, e:
		#pass
	#	print e
	
def cekwithtime(data):
	try:
		os.system('cls')
		print "\n"
		data = os.popen(r"c:\cygwin\bin\df.exe -h -v").readlines()
		#data2 = data.split("\n")
		
		#print data
		
		#sizelen = len(data)
		
		#print "SizeLen = ", sizelen, "\n"
		
		print "  Drive Size  Used  Available  Use(%) ", "\n"
		
		
		#for i in range(6, sizelen):
		#	datax01 =  data[i].split("/"), "\n"
			#print "datax01 = ", datax01
		#	datax02 = datax01[0][0].split(":")
		#	datax03 = datax02[1].split("         ")

		#	print "   " + datax02[0] + ":\\" + datax03[2], "\n"
		i = 0
		while i < data:
			cek()
			time.sleep(5)
			i = i + 1
				
	except KeyboardInterrupt, e:
		#pass
		print e
		
if __name__ == '__main__':

	try:
		if (len(sys.argv[1:]) < 1):
			cek(lendata=6)
		else:
			try:
				#cekwithtime(sys.argv[1])
				cek(lendata=int(sys.argv[1]))
			except TypeError, e:
				print "\n"
				print "\t\t Error 1 : ", e
				print "\n"
	except TypeError, e:
		print "\n"
		print "\t\t Error 2 : ", e
		print "\n"
				