import module003
import module006
import sys
import os

data_snmp = "snmp"
data_trap = "snmptrap"

filename = os.path.split(sys.argv[0])

usage = """
         use: """ + filename[1] + """ snmp [start | stop | restart] \n
                         snmptrap [start | stop | restart]\n\n""" 

def main():
	#print len(sys.argv)
	if (len(sys.argv) == 1):
		os.system("cls")
		print "\n\n"
		print usage
	else:
		if (sys.argv[1] == "snmp"):
			if (len(sys.argv) == 3):
				if (sys.argv[2] == "start"):
					module003.start(data_snmp)
					os.system("cls")
					print "\n"
				elif (sys.argv[2] == "stop"):
					module003.stop(data_snmp)
					os.system("cls")
					print "\n"
				elif (sys.argv[2] == "restart"):
					module003.restart(data_snmp)
					os.system("cls")
					print "\n"
				else:
					os.system("cls")
					print "\n\n"
					print usage	
			else:
				os.system("cls")
				print "\n\n"
				print usage	
		elif (sys.argv[1] == "snmptrap" or "trap"):
			if (sys.argv == 2):
				if (sys.argv[2] == "start"):
					module003.start(data_trap)
					os.system("cls")
					print "\n"
				elif (sys.argv[2] == "stop"):
					module003.stop(data_trap)
					os.system("cls")
					print "\n"
				elif (sys.argv[2] == "restart"):
					module003.restart(data_trap)
					os.system("cls")
					print "\n"
				else:
					os.system("cls")
					print "\n\n"
					print usage	
			else:
				os.system("cls")
				print "\n\n"
				print usage	
		else:
			os.system("cls")
			print "\n\n"
			print usage	
		

if __name__ == '__main__':

	main()
	
	print "\t\t Service " + data_snmp + " is " + module006.status(data_snmp), "\n"
	print "\t\t Service " + data_trap + " is " + module006.status(data_trap)