import os
import sys

SENDMAIL_PATH = "c:\sendmail"
SENDMAIL_CONFIG_FILE = "sendmail.ini"

data_filename  = os.path.split(sys.argv[0])
filename = data_filename[1] 

usage = """  use : """ + filename + " from : to: subject: message: attachment(if there): \n      OR just type this file with no option ! [just enter if you want input per-line]\n      [type \"exit\" or \"quit\" to exit]\n\n  use : " + filename + " setting | config [to setting file configuration] \n"

def setting():
	try:
		os.system("metapad " + str(os.path.join(SENDMAIL_PATH, SENDMAIL_CONFIG_FILE)))
	except:
		import e_console
		import traceback
		data_e = traceback.format_exc()
		e_console.Dialog("Error", str(data_e))
		
def cek_valid_setting(data):
	if "@" in str(data):
		d01 = str(data).split("@")
		myfile = open(str(os.path.join(SENDMAIL_PATH, SENDMAIL_CONFIG_FILE))).readlines()
		print myfile
		print "-"*80
		#for i in range(0,len(file)):
		#	print file[i]
		for i in range(0,len(myfile)):
			if str(d01[1]) in myfile[i]:
				print "d01 = ", d01
				print "myfile[i] = ", myfile[i]
				print "ADA"
			else:
				pass
				#print "Tidak Ada "
	else:
		print "\n"
		print "\t Not valid email address ! \n"
		return "notvalid"
	

if (len(sys.argv) == 1):
	os.system("cls")
	print "\n\n"
	print usage
	pre = raw_input("\r\t\t ")
	if pre == "exit" or pre == "quit":
		print "\t bye ........... \n"
		sys.exit()
	elif pre == "setting" or pre == "config" :
		os.system("cls")
		print "\n"
		print usage
		setting()
	else:
		os.system("cls")
		print "\n"
		print usage
		pass
	
	fromx = raw_input("\r\t\t From = ")
	while fromx == None or fromx == "":
		fromx = raw_input("\r\t\t From = ")
	else:
		if fromx == "exit" or fromx == "quit":
			sys.exit()
		elif fromx == "setting" or fromx == "config":
			setting()
		else:
			set_server = []
			get_server = []
			if "@" in fromx:
				d01 = str(fromx).split("@")
				myfile = open(str(os.path.join(SENDMAIL_PATH, SENDMAIL_CONFIG_FILE))).readlines()
				for i in range(0,len(myfile)):
					if str(d01[1]) in myfile[i]:
						get_server.append(d01[1])
						#print "d01 = ", d01
						#print "myfile[i] = ", myfile[i]
						if ";" in myfile[i]:
							print "\n"
							print "\t\t Your server mail " + str(d01[1]) + " is exit, but it is not active ! \n"
							ask_conf0 = raw_input("\r\t\t Do you want to config/change it before (Y|y|N|n) ? ")
							if ask_conf0 == "Y" or ask_conf0 == "y":
								setting()
								break
							else:
								print "\n"
								print "\t\t You not enter (Y|y|N|n), this mean youre not want to config it ! \n"
								break
								pass
						else:
							print "\n"
							print "\t\t Your server mail " + str(d01[1]) + " is your mail server.\n"
							ask_conf = raw_input("\r\t\t Do you want to config/change it before (Y|y|N|n) ? ")
							if ask_conf == "Y" or ask_conf == "y" :
								setting()
								print "\n"
								print "\t\t Please insert a from mail address again ! \n"
								fromx = raw_input("\r\t\t From = ")
								while fromx == None or fromx == "":
									fromx = raw_input("\r\t\t From = ")
								else:
									break
									if fromx == "exit" or fromx == "quit":
										sys.exit()
									else:
										d02 = str(fromx).split("@")
										if "@" in fromx:
											if str(d02[1]) in myfile[i]:
												pass
											else:
												print "\n"
												print "\t\t sorry youre not change config before, please change before and start begin ! \n"
												sys.exit()
										else:
											print "\n"
											print "\t\t Sorry youre not insert a valid mail address for 2 times ! \n, this will exit you. Please start from begin \n"
											sys.exit()
							elif ask_conf == "N" or ask_conf == "n" :
								pass
							else:
								print "\n"
								print "\t\t You not enter (Y|y|N|n), this mean youre not want to config it ! \n"
								pass
					else:
						pass
					
						#print "\n"
						#print "\t\t You email address not in configuration file, please start begin and type \"setting\" to config it before \n"
						#sys.exit()
								
			else:
					print "\n"
					print "\t\t You not insert a valid email address !, please back and insert again \n"
					sys.exit()
				
	tox = raw_input("\r\t\t To = ")
	while tox == None or tox == "":
		tox = raw_input("\r\t\t To = ")
	else:
		if tox == "exit" or fromx == "quit":
			sys.exit()
		elif tox == "setting" or tox == "config":
			setting()
		else:
			if "@" in tox:
				pass
			else:
				print "\n"
				print "\t\t You not insert a valid email address !, please back and insert again \n"
				sys.exit()
			
	subjectx = raw_input("\r\t\t Subject = ")
	while subjectx == None or subjectx == "":
		subjectx = raw_input("\r\t\t Subject = ")
	else:
		if subjectx  == "exit" or subjectx  == "quit":
			sys.exit()
		elif subjectx== "setting" or subjectx == "config":
			setting()
		else:
			pass
			
	messagexx = raw_input("""\r\t\t Message [type \"file\" for message from file] = """)
	while messagexx == None or messagexx == "":
		messagexx = raw_input("""\r\t\t Message [type \"file\" for message from file] = """)
	else:
		if messagexx  == "exit" or messagexx  == "quit":
			sys.exit()
		elif messagexx == "setting" or messagexx == "config":
			setting()
		elif (messagexx == "file"):
			msg_file = raw_input("\r\t\t Please insert the name of file message = ")
			while msg_file == None or msg_file == "" or os.path.isfile(msg_file) == False:
				msg_file = raw_input("\r\t\t Please insert the name of file message = ")
			else:
				msgx = r'%s' % (msg_file)
				#msgx = str(msgx_pre)
		else:
			messagex = messagexx
			data_msg = open(r"c:\temp\tmp_msg.txt", "w")
			data_msg.writelines(messagex)
			data_msg.close()
			msgx = r"c:\temp\tmp_msg.txt"
		
	attachment = raw_input("\r\t\t Attachment = ")
	
	if (attachment == "" or attachment == None):
		if (os.path.isfile(r"c:\temp\tmp_msg.txt") == True):
			os.system("c:\sendmail\sendmail.exe -messagefile=" + msgx + " -subject=" + subjectx + " " + tox)
		else:
			print "\n\n"
			print usage
	elif messagexx == "exit" or messagexx == "quit":
		sys.exit()
	else:
		os.system("c:\sendmail\sendmail.exe -messagefile=" + msgx + " -subject=" + subjectx + " -attach= \"" + attachment + "\" " + tox)
		
elif (len(sys.argv) > 1):
	if sys.argv[1] == "setting" or sys.argv[1] == "config":
		setting()
	else:
		os.system("cls")
		print "\n\n"
		fromz = sys.argv[1]
		toz = sys.argv[2]
		subjectz = sys.argv[3]
		messagezz = sys.argv[4]
		cekmsg = "file:"
		if (cekmsg in messagezz):
			msg_file2 = str(sys.argv[4]).split(":")
			msgz = msg_file2[1]
		else:
			messagez = messagezz
			data_msgz = open(r"c:\temp\tmp_msg.txt", "w")
			data_msgz.writelines(messagez)
			data_msgz.close()
			msgz = r"c:\temp\tmp_msg.txt"
		
		try:
			attachment2 = sys.argv[5]
			if (os.path.isfile(r"c:\temp\tmp_msg.txt") == True):			
				os.system("c:\sendmail\sendmail.exe -messagefile=" + msgz +  " -subject=" + '"' + subjectz + '"' + " -attach=" + attachment2 + " " + toz)
			else:
				print "\n\n"
				print usage
		except IndexError, e:
			os.system("c:\sendmail\sendmail.exe -messagefile=" + msgz + " -subject=" + '"' + subjectz + '"' + " " + toz)
			 
			
else:
	print "\n\n"
	print usage