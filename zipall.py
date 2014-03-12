import os
import sys

def usage():
	print "\n"
	print "\t\tuse : " + os.path.split(sys.argv[0])[1] + " [file_to_zip] "

def rarme():
	try:
		data_list = os.popen("dir /b ").readlines()
		print "############################ COMPRESS ARCHIEVE #############################\n"
		for i in range(0,len(data_list)):
			data_pack = str(data_list[i]).split("\n")
			if ".zip" in data_pack[0]:
				pass
			elif ".rar" in data_pack[0]:
				pass
			elif ".tar" in data_pack[0]:
				pass
			elif ".gz" in data_pack[0]:
				pass
			elif ".tgz" in data_pack[0]:
				pass
			elif ".bz2" in data_pack[0]:
				pass
			elif ".7z" in data_pack[0]:
				pass
			elif ".arj" in data_pack[0]:
				pass
			elif ".bzip2" in data_pack[0]:
				pass
			elif ".cab" in data_pack[0]:
				pass
			elif ".cpio" in data_pack[0]:
				pass
			elif ".deb" in data_pack[0]:
				pass
			elif ".gzip" in data_pack[0]:
				pass
			elif ".iso" in data_pack[0]:
				pass
			elif ".lha" in data_pack[0]:
				pass
			elif ".lzh" in data_pack[0]:
				pass
			elif ".rpm" in data_pack[0]:
				pass
			elif ".split" in data_pack[0]:
				pass
			elif ".swm" in data_pack[0]:
				pass
			elif ".tbz" in data_pack[0]:
				pass
			elif ".tbz2" in data_pack[0]:
				pass
			elif ".tpz" in data_pack[0]:
				pass
			elif ".wim" in data_pack[0]:
				pass
			elif ".z" in data_pack[0]:
				pass
			elif ".py" in data_pack[0]:
				pass
			elif ".pl" in data_pack[0]:
				pass
			elif ".rb" in data_pack[0]:
				pass
			elif ".cs" in data_pack[0]:
				pass
			elif ".c" in data_pack[0]:
				pass
			elif ".cpp" in data_pack[0]:
				pass
			elif "makefile" in data_pack[0]:
				pass
			elif "Makefile" in data_pack[0]:
				pass
			elif ".sh" in data_pack[0]:
				pass
			elif ".bat" in data_pack[0]:
				pass
			elif "readme" in data_pack[0]:
				pass
			elif "README" in data_pack[0]:
				pass
			elif "Readme" in data_pack[0]:
				pass
			elif ".htm" in data_pack[0]:
				pass	
			elif ".html" in data_pack[0]:
				pass
			elif ".css" in data_pack[0]:
				pass
			elif ".php" in data_pack[0]:
				pass
			elif ".vb" in data_pack[0]:
				pass
			elif ".vbs" in data_pack[0]:
				pass
			elif ".asp" in data_pack[0]:
				pass
			elif ".sln" in data_pack[0]:
				pass
			elif os.path.isdir(data_pack[0]):
				conf_dir = raw_input("\r\t Found directory \"" + str(data_pack[0]) + "\" !, Do you want to zip it ? (Y|y|N|n) : ")
				if conf_dir == "Y" or conf_dir == "y":
					data_rar_02 = data_pack[0] + "_dir"
					data_compress = data_pack[0] + "_dir"
				elif conf_dir == "N" or conf_dir == "n":
					pass
				else:
					conf_dir2 = raw_input("\r\t Corrent input, please input again ! (Y|y|N|n) : ")
					if conf_dir2 == "Y" or conf_dir2 == "y":
						data_rar_02 = data_pack[0] + "_dir"
						data_compress = data_pack[0] + "_dir"
					elif conf_dir2 == "N" or conf_dir2 == "n":
						pass
					else:
						conf_dir3 = raw_input("\r\t Corrent input again !, please input again !, this is last request ! (Y|y|N|n) : ")
						if conf_dir3 == "Y" or conf_dir3 == "y":
							data_rar_02 = data_pack[0] + "_dir"
							data_compress = data_pack[0] + "_dir"
						elif conf_dir3 == "N" or conf_dir3 == "n":
							pass
						else:
							pass
			else:
				data_rar_02 = str(data_pack[0]).split(".")
				data_compress = data_rar_02[0]
			try:
				if data_rar_02[0] != "":
					os.system("7z -tzip a \"" + data_compress + ".zip\" \"" + data_pack[0] + "\"") 
					os.system("7z t \"" + data_compress + ".zip\" ") 
				else:
					pass
			except:
				#print data_rar_02 + ".rar"
				os.system("7z -tzip a \"" + data_rar_02 + ".zip\" \"" + data_pack[0] + "\"") 
				os.system("7z t \"" + data_rar_02 + ".zip\" ") 
		print "############################ TEST ARCHIEVE #############################\n"
		os.system("7z t *.zip")
		#for i in range(0,len(data_list)):
		#	data_pack = str(data_list[i]).split("\n")
		#	data_rar_02 = str(data_pack[0]).split(".")
		#	try:
		#		if data_rar_02[0] != "":
		#			print data_rar_02[0] + ".rar"
		#			os.system("7z t \"" + data_rar_02[0] + ".zip\" ") 
		#		else:
		#			pass
		#	except:
		#		print data_rar_02 + ".rar"
		#		os.system("7z t \"" + data_rar_02 + ".zip\" ") 
		
		q = raw_input("\t Are you want to delete the original source ? (y[[Y]es]/n[[N]o]) : ")
		if q == "y" or q == "Y" or q == "Yes" or q == "yes"  :
			for i in range(0, len(data_list)):
				data_pack = str(data_list[i]).split("\n")
				if os.path.isdir(data_pack[0]):
					pass
				else:
					if ".zip" in data_pack[0]:
						pass
					else:
						print data_pack[0]
						os.system("del \"" + data_pack[0] + "\"")
		elif q == "n" or q == "N" or q == "no" or q == "No":
			sys.exit()
		else:
			print "\n"
			print "\t You no select \'Y\' or \'N\' "
			print "\t Bye ... !"
			sys.exit()
		
	except IndexError, e:
		print e
		
def test():
	#data_rar_01 = sys.argv[1]
	#data_rar_02 = os.path.splitext(data_rar_01)[0]
	data_list = os.popen("dir /b ").readlines()
	#os.system("7z -tzip a \"" + data_rar_02 + ".zip\" \"" + sys.argv[1] + "\"") 
	#os.system("7z t \"" + data_rar_02 + ".zip\" ") 
	for i in range(0,len(data_list)):
		data_pack = str(data_list[i]).split("\n")
		data_rar_02 = str(data_pack[0]).split(".")
		try:
			if data_rar_02[0] != "":
				print data_rar_02[0] + ".rar"
			else:
				pass
		except:
			print data_rar_02 + ".rar"
	print "\n"
		
		
if __name__ == '__main__':
	
	try:
		rarme()
	except IndexError, e:
		usage()
	
	#test()