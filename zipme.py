import os
import sys

def usage():
	print "\n"
	print "\t\tuse : " + os.path.split(sys.argv[0])[1] + " [file_to_zip] "

def rarme(data):
	try:
		if(len(data) > 1):
			data_rar_01 = sys.argv[1]
			if sys.argv[2:]:
				data_rar_02 = sys.argv[2]
				os.system("7z -tzip a \"" + data_rar_02 + ".zip\" \"" + sys.argv[1] + "\"") 
				os.system("7z t \"" + data_rar_02 + ".zip\" ") 
				print "\n"
				if os.path.isdir(data_rar_01):
					pass
				else:
					q = raw_input("\t Are you want to delete the original source ? (y[[Y]es]/n[[N]o]) : ")
					if q == "y" or q == "Y" or q == "Yes" or q == "yes"  :
						os.system("del \"" + data_rar_01 + "\"")
					elif q == "n" or q == "N" or q == "no" or q == "No":
						sys.exit()
					else:
						print "\n"
						print "\t You no select \'Y\' or \'N\' "
						print "\t Bye ... !"
						sys.exit()
			else:	
				data_rar_02 = os.path.splitext(data_rar_01)[0]
				os.system("7z -tzip a \"" + data_rar_02 + ".zip\" \"" + sys.argv[1] + "\"") 
				os.system("7z t \"" + data_rar_02 + ".zip\" ") 
				print "\n"
				if os.path.isdir(data_rar_01):
					pass
				else:
					q = raw_input("\t Are you want to delete the original source ? (y/n) : ")
					if q == "y":
						os.system("del \"" + data_rar_01 + "\"")
					elif q == "Y":
						os.system("del \"" + data_rar_01 + "\"")
					elif q == "n":
						sys.exit()
					elif q == "N":
						sys.exit()
					else:
						print "\n"
						print "\t You no select \'Y\' or \'N\' "
						print "\t Bye ... !"
						sys.exit()
		else:
			usage
	except IndexError, e:
		print e
		
if __name__ == '__main__':
	try:
		data = sys.argv[1]
		rarme(data)
	except IndexError, e:
		usage()
			