import sys
import os
import errno
import TuneUp2011x
import module002

os.system("cls")
os.system("echo.")
os.system("echo.")

usage = """use: sys.argv[0] --list     = list Executable File \n
		 --main     = Start Main Application """

def list():
	datalist = os.popen("dir /b \os.getenv("ProgramFiles") +"\\"  + r"TuneUp Utilities 2011\"\*.exe | more").readlines()
	#print datalist
	lendata = len(datalist)
	print "list of file : \n", 
	for i in range(0, lendata):
		datalist02 = datalist[i].split(".exe")
		print "\t\t - ", datalist02[0] 


def main():
	TuneUp2011x.main()
	print "TEST"


if __name__ == '__main__':
	try:		

		if sys.argv[1] == '--list':
			list()

		elif sys.argv[1] == '--main':
			main()
			
		else:
			try:
				datax1 = sys.argv[1]
				datax2 = os.getenv("ProgramFiles") +"\\"  + r"TuneUp Utilities 2011\\"
				datax3 = datax2 + datax1
				print "\t\t Program being Starting !"
				module002.main(datax3)
				
			except IndexError, e:
				print "\n\n"
				print "\t\tERROR 1 : ", e, "\n"
				print usage

	except IndexError, e:
		print "\n\n"
		print "\t\tERROR 2 : ", e, "\n"
		print usage

