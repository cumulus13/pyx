import os
import sys
import shutil

def usage():
	print "\n"
	print "\t\tuse : " + os.path.split(sys.argv[0])[1] + " [file_to_rar] "

def on_rm_error(func, path, exc_info):
    os.chmod(path, stat.S_IWRITE)
    os.unlink(path)

def pass_no(rmdir):
	q = raw_input("\t Are you want to delete the original source folder ? (y[[Y]es]/n[[N]o]) : ")
	if q == "y" or q == "Y" or q == "Yes" or q == "yes"  :
		shutil.rmtree(rmdir,onerror = on_rm_error)
	elif q == "n" or q == "N" or q == "no" or q == "No":
		sys.exit()
	else:
		print "\n"
		print "\t You no select \'Y\' or \'N\' "
		print "\t Bye ... !"
		sys.exit()

def pass_yes(file):
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

def rarme(data):
	try:
		if(len(data) > 1):
			if sys.argv[2:]:
				data_rar_path = "\"" + os.path.dirname(os.path.abspath(sys.argv[2])) + "\"\\\"" + sys.argv[1] + ".rar\"\"" 
				#print "data_rar_path = ", data_rar_path
				os.chdir(os.path.dirname(sys.argv[2]))
				os.system("rar a \"" + data_rar_path + " \"" + os.path.basename(sys.argv[2]) + "\"") 
				os.system("rar t \"" + data_rar_path) 
				print "\n"
				if os.path.isdir(sys.argv[2]):
					pass_no(sys.argv[2])
				else:
					pass_yes(sys.argv[2])
			else:
				# this may file or dir
				file_dir_base_name = os.path.basename(sys.argv[1])
				#print "file_dir_base_name = ", file_dir_base_name

				#this must a directory
				dir_name = os.path.dirname(sys.argv[1])
				#print "dir_name = ", dir_name
				
				data_rar_02 = "\"" + dir_name + "\"\\\"" + file_dir_base_name + ".rar\"\"" 
				os.chdir(dir_name)
				os.system("rar a \"" + data_rar_02 + " " + file_dir_base_name)
				os.system("rar t \"" + data_rar_02) 
				print "\n"
				if os.path.isdir(sys.argv[1]):
					pass_no(os.path.join(dir_name,file_dir_base_name))
				else:
					pass_yes(os.path.join(dir_name,file_dir_base_name))
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
			