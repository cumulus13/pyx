import os, errno
import sys
import getopt


ket = """
			Usage MySQL start    =   to Start MySQL Service
			      MySQL stop     =   to Stop  MySQL Service
	      """
ket2 = """
                1. Start MySQL Service
                2. Stop MySQL Service
		3. Status MySQl Service
                0. Exit
"""


def usage():
	
	os.system("cls")
	print "\n\n\n"
	print ket

def start():
	os.system("cls")
	print "\n\n\n\n\n"
	os.system("sc config mysql start= demand")
	os.system("sc start mysql")
	sys.exit()
	
def stop():
	os.system("cls")
	print "\n\n\n\n\n"
	os.system("sc config mysql start= disabled")
	os.system("sc stop mysql")
	sys.exit()

def status():
	os.system("cls")
	print "\n\n\n\n\n"
	os.system("psservice query mysql")
	os.system("pause >> nul")
	main()
	
def main():
	os.system("cls")
	print "\n\n\n"
	print ket2
	print "\n\n\n"
	pilih = raw_input("\t\t\tMasukkan Nomor Pilihan Anda : ")
	print "\t\t\t"
	if (pilih == '1'):
	    start()
	elif (pilih == '2'):
	    stop()
	elif (pilih == '3'):
	    status()
	elif (pilih == '0'):
	    sys.exit()
	else:
		os.system("cls")
		print "\n\n\n"
		print "\t\t\tAnda tidak memasukkan Nomor yang benar !!!"
		print "\n\n\n"
	
def utama():
	if len(sys.argv) < 1:
		usage()
		sys.exit()
	
	try:
		options = getopt.getopt(sys.argv[5:], 'start:stop:')[0]
	except getopt.GetoptError, err:
		print err
		usage()
		sys.exit()
		
	for options, value in options:
		if options == 'start':
			start()
		elif options == 'stop':
			stop()
		else:
			usage()
			sys.exit()
	
			
	
if __name__ == '__main__':
	main()
	
