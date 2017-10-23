import os
import sys
import errno

filename = os.path.split(sys.argv[0])
usage = """
	usage : """ + filename[1] + """ --burn --list   [cek list data of BURN Directory ] \n
                           --burn --size   [cek list data of BURN Directory ] \n
                           --film --flist  [cek list data of FILM Directory ] \n
                           --film --fsize  [cek size data of FILM Directory ] \n
                           --music --mlist [cek list data of MUSIC Directory] \n
                           --music --msize [cek size data of MUSIC Directory] \n
                           --all           [cek size data of ALL Type Directory] \n
"""

def ceksize(data):
	if os.path.isdir(data) == True:
		os.system(r"c:\cygwin\bin\du -s -h " + data)
	else:
		pass
	
def cektree(data):
	if os.path.isdir(data) == True:
		os.system("r2.py " + data)
	else:
		pass
		
def cekjumlah(data):
	dataz = []
	if os.path.isdir(data) == True:
		datax = os.popen(r"c:\cygwin\bin\du -s -h " + data).readlines()
		datay = datax[0].split("\t")
		#print datax
		datay2 = datay[0].split("M")
		#print data + " = " + datay2[0]
		return datay2[0]
		
		#dataz.append(datay2[0])
		#dataz = int(datay2[0]) + int(datay2[0])
		#print dataz
		#print "---------------------------"
	else:
		pass
		
	#dataz.append(datay2[0])
	#print "TOTAL = ", dataz + dataz
	
def ceknone():
	cektree(r"d:\burn")
	cektree(r"e:\burn")
	cektree(r"f:\burn")
	cektree(r"g:\burn")
	cektree(r"h:\burn")
	cektree(r"i:\burn")
	cektree(r"m:\burn")
	cektree(r"k:\burn")
	cektree(r"n:\burn")
	cektree(r"o:\burn")
	
def ceksizeme():
	ceksize(r"d:\burn")
	ceksize(r"e:\burn")
	ceksize(r"f:\burn")
	ceksize(r"g:\burn")
	ceksize(r"h:\burn")
	ceksize(r"i:\burn")
	ceksize(r"m:\burn")
	ceksize(r"k:\burn")
	ceksize(r"n:\burn")
	ceksize(r"o:\burn")
	
def cekjumlahme():
	data001 = cekjumlah(r"d:\burn")
	data002 = cekjumlah(r"e:\burn")
	data003 = cekjumlah(r"f:\burn")
	data004 = cekjumlah(r"g:\burn")
	data005 = cekjumlah(r"h:\burn")
	data006 = cekjumlah(r"i:\burn")
	data007 = cekjumlah(r"m:\burn")
	data008 = cekjumlah(r"k:\burn")
	data009 = cekjumlah(r"n:\burn")
	data010 = cekjumlah(r"o:\burn")
	
	total = data001 + data002 + data003 + data004 + data005 + data006 + data007 + data008 + data009 + data010
	print total


def cekburn():
	try:
		if len(sys.argv) <= 2:
			ceknone()
		elif(sys.argv[2] == "--size"):
			ceksizeme()
		elif(sys.argv[2] == "--list"):
			ceknone()
		else:
			print "ERROR 1"
	except TypeError, e:	
		print "\t\t", e
	
def cekFILMsize():
	ceksize(r"D:\FILM")
	ceksize(r"E:\FILM")
	ceksize(r"F:\FILM")
	ceksize(r"G:\FILM")
	ceksize(r"H:\FILM")
	ceksize(r"I:\FILM")
	ceksize(r"M:\FILM")
	ceksize(r"K:\FILM")
	ceksize(r"N:\FILM")
	ceksize(r"O:\FILM")

def cekFILMtree():
	cektree(r"D:\FILM")
	cektree(r"E:\FILM")
	cektree(r"F:\FILM")
	cektree(r"G:\FILM")
	cektree(r"H:\FILM")
	cektree(r"I:\FILM")
	cektree(r"M:\FILM")
	cektree(r"K:\FILM")
	cektree(r"N:\FILM")
	cektree(r"O:\FILM")
	
def cekMUSICsize():
	ceksize(r"F:\MUSIC\0.WEST\LAGU\BURN")
	cektree(r"F:\MUSIC\0.WEST\LAGU\BURN")
	
def cekMUSIClist():
	ceklist(r"F:\MUSIC\0.WEST\LAGU\BURN")
	ceklist(r"F:\MUSIC\0.WEST\LAGU\BURN")

		
def cekMUSIC():
	try:
		if (sys.argv[2:] <= 1):
			cekteree(r"F:\MUSIC\0.WEST\LAGU\BURN")
			cekttree(r"F:\MUSIC\0.WEST\LAGU\BURN")
			
		elif (sys.argv[2] == "--msize"):
			ceksize(r"F:\MUSIC\0.WEST\LAGU\BURN")
			
		elif (sys.argv[2] == "--mlist"):
			cektree(r"F:\MUSIC\0.WEST\LAGU\BURN")
		else:
			#os.system("cls")
			print usage
	except TypeError, e:
		print "\t\t", e
	
	
def cekFILM():
	try:
		if (sys.argv[2:] <= 1):
			cekFILMtree()
			cekFILMsize()
		elif(sys.argv[2] == "--fsize"):
			cekFILMsize()
		elif(sys.argv[2] == "--flist"):
			cekFILMtree()
		else:
			#os.system("cls")
			print usage
	except TypeError, e:
		print "\t\t", e
			

if __name__ == '__main__':
	try:
		if (len(sys.argv[1:]) <= 0):
			#ceknone()
			#ceksizeme()
			os.system("cls")
			print "\n"
			print usage, "\n"
		else:
			if(sys.argv[1] == "--burn"):
				cekburn()
			elif(sys.argv[1] == "--film"):
				cekFILM()
			elif(sys.argv[1] == "--music"):
				cekMUSIC()
			elif(sys.argv[1] == "all"):
				cekburn()
				cekFILM()
				cekMUSIC()
			elif (sys.argv[1] == "jumlah"):	#Test Only
				cekjumlahme()
			else:
				print usage
	except TypeError, e:
		print "\t\t", e
			

	
	
