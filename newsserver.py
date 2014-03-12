import module002
import module003
import module006
import os
import sys

def main():
	datagui = r"d:\pyx\argonews.bat"
	datasrv = "msNewsServerForm"
	#print len(sys.argv)
	try:
		if (len(sys.argv) == 1):
			os.system("cls")
			print "\n"
			#print "Service is = " + module006.status(datasrv)
			module003.main(datasrv)
		else:
			if (sys.argv[1] == "config"):
				module002.main(datagui)
				
			elif (sys.argv[1] == "gui"):
				module002.main(datagui)
				
			elif (sys.argv[1] == "start"):
				module003.start(datasrv)
			elif (sys.argv[1] == "stop"):
				module003.stop(datasrv)	
			elif (sys.argv[1] == "restart"):
				module003.restart(datasrv)
			elif (sys.argv[1] == "status"):
				module003.status(datasrv)
			else:
				module003.main(datasrv)
				
	except IOError, e:
		os.system("cls")
		print "\n\n"
		print "\t Plase Cek youre Code Syntax ! \n"
		
		
if __name__ == "__main__":
	main()
		
			
