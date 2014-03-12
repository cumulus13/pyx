import os
import sys

data_filename  = os.path.split(sys.argv[0])
filename = data_filename[1] 

usage = """use : """ + filename + "from : to: subject: message: attachment(if there): OR just type this file with no option !"

if (len(sys.argv) == 1):
	os.system("cls")
	print "\n\n"
	fromx = raw_input("\r\t\t From = ")
	tox = raw_input("\r\t\t To = ")
	subjectx = raw_input("\r\t\t Subject = ")
	messagexx = raw_input("\r\t\t Message [type \"file\" for message from file] = ")
	if (messagexx == "file"):
		msg_file = raw_input("\r\t\t Please insert the name of file message = ")
		if os.path.isfile(msg_file):
			msgx = r'%s' % (msg_file)
			#msgx = str(msgx_pre)
		else:
			print "\r\t\t Please insert name of message file ! "
			sys.exit()
	else:
		messagex = messagexx
		data_msg = open(r"c:\temp\tmp_msg.txt", "w")
		data_msg.writelines(messagex)
		data_msg.close()
		msgx = r"c:\temp\tmp_msg.txt"
		
	attachment = raw_input("\r\t\t Attachment = ")
	
	
	if (attachment == ""):
		if (os.path.isfile(r"c:\temp\tmp_msg.txt") == True):
			os.system("c:\sendmail\sendmail.exe -messagefile=" + msgx + " -subject=" + subjectx + " " + tox)
		else:
			print "\n\n"
			print usage
	else:
		os.system("c:\sendmail\sendmail.exe -messagefile=" + msgx + " -subject=" + subjectx + " -attach= \"" + attachment + "\" " + tox)
		
elif (len(sys.argv) > 1):
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