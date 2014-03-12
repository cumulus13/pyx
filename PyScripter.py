import os
import errno
import sys
import module002

data = os.getenv("ProgramFiles") +"\\"  + r'PyScripter\PyScripter.exe'

head = """ 			   PyScripter Controller
				by BLACKID

		       ****************************

"""

v23 = "--PYTHON23"
v24 = "--PYTHON24"
v25 = "--PYTHON25"
v26 = "--PYTHON26"
v30 = "--PYTHON30"
v31 = "--PYTHON31"
v32 = "--PYTHON32"

name_data = os.path.split(sys.argv[0])
rname_data = name_data[1]

usage = """ 	usage :  """ + rname_data + """ [version of python (23,24,25,26,30,31,32)]

		 (example : """ + rname_data + """ 23 (this mean is, start python version 2.3)"""

def startbegin(datax):

	sprt = " "

	try:
		os.system("start " + data + sprt + datax)
        #os.execlp(data, sys.argv[1])

	except OSError, e:

		if e.errno == errno.ENOEXEC:
			os.system("cls")
			print "\n"
			print "\t\t Program Tidak Dapat Di Eksekusi !"

		elif e.errno == errno.ENOENT:
			os.system("cls")
			print "\n"
			print "\t\t Program Tidak Dapat Ditemukan !"

		else:
			os.system("cls")
			print "\n"
			print "\t\t Program Tidak Dapat Berjalan Pada Mode System Operasi Win32 !"

	except IndexError, e:

		os.system("cls")
		print "\n\n"
		print "\t\t Program Error On Script !"


def startend():
	try:
		if (sys.argv[1] > 1):
			if (sys.argv[1] == '23'):
				startbegin(v23)

			elif (sys.argv[1] == '24'):
				startbegin(v24)

			elif (sys.argv[1] == '25'):
				startbegin(v25)

			elif (sys.argv[1] == '26'):
				startbegin(v26)

			elif (sys.argv[1] == '30'):
				startbegin(v30)

			elif (sys.argv[1] == '31'):
				startbegin(v31)

			elif (sys.argv[1] == '32'):
				startbegin(v32)

			else:
				os.system('cls')
				print "\n\n"
				print head, "\n"
				print usage

		else:
			os.system('cls')
			print "\n\n"
			print head, "\n"
			print usage


	except IndexError, e:
		os.system('cls')
		print "\n"
		print head, "\n"
		print usage
		print "\n"
		print "\tPlease Fill Option ! \n"
		module002.main(data)


	except TypeError, e:
		os.system('cls')
		print "\n"
		print "\tPlease Cek Script is Correct ! \n"
		print "\n"

if __name__ == '__main__':
	startend()