import os
import sys
import module001

data = os.popen("tasklist").readlines()
cekdata = "SciTE"
#cekdata = sys.argv[1]

def cek(data_input):

	for i in range(0, len(data)):
		if cekdata in data[i]:
			return True
		else:
			pass
			#return False

def runme():

	if (cek(cekdata) == True):
		#print "ADA"
		os.system("scite2 " + sys.argv[1])
	else:
		#if (cek(cekdata) == False): 
			#print "TIDAK ADA"
			#dataexec = r"c:\Ruby\scite\SciTE.exe"
			#os.system("scite " + sys.argv[1])
			os.system("d:\pyx\scitex.exe "  + sys.argv[1])
			#module001.main(dataexec)
			
		#else:
		#	pass


if __name__ == '__main__':

	#try: 	#if you want please uncomment '#'

		#if sys.argv[1] < 1:
			#print "\t\t No Input name File ! \n"
		#else:
			#cekdata = "SciTE"
			#cekdata = sys.argv[1]
				
			#print cek(cekdata)
			runme()
	
	#except TypeError, e:	#if you want please uncomment '#'
	#	print e				#if you want please uncomment '#'