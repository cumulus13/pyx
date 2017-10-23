import os, errno
import mindmap
import officepro
import CDProject
import sys

usage = """
	Silahkan masukkan Pilihan [1 - 3]
"""


ket = """
            1. ConceptDraw MindMap
            2. ConceptDraw Office Pro
	    3. ConceptDraw Project
            0.Exit
"""

def main():
	os.system("cls")
	print "\n\n"
	print ket
	print "\n\n"
	print "\n\n"
	pilih = raw_input("\t\t\tMasukkan Nomor Application !  : ")
	print "\n"
	if (pilih == '1'):
		mindmap.main()
		
	elif (pilih == '2'):
		officepro.main()
			
	elif (pilih == '3'):
		CDProject.main()
	
	elif (pilih == '0'):
		os.system("cls")
		os.system("echo.")
		os.system("echo.")
		os.system("echo.")
		print "\n  \t\t\t\tThank You For Support !"
		sys.exit()
		
	else:
		os.system("cls")
		print "\n\n"
		print usage
		print "\n\n"

if __name__ == '__main__':
	main()