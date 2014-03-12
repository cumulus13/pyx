import os
import sys
import winsound
import pyttsx
import time

data_name = os.path.split(sys.argv[0])
filename = data_name[1]
result_cek = ["Sub items Errors", "Everything is Ok"]
#print result_cek[0]
rst_cek = "Wrong password"
rst_cek2 = "Sub items Errors"
rst_cek3 =  "Everything is Ok"

usage = "\t\tUsage : " + filename + " rar_file  wordlist[*.*] \n\n" + "\t\t#################################################################\n" + "\t\t#\t\t\t\t\t\t\t\t#\n" + "\t\t#       This Only For Archieve With Containt A Password !       #\n" + "\t\t#\t\t\t\t\t\t\t\t#\n" +"\t\t#     Please make sure youre Archieve Containt A Password !     #\n" + "\t\t#\t\t\t\t\t\t\t\t#\n" + "\t\t#################################################################\n"

try:
	if (sys.argv[1] == "help"):
		os.system("cls")
		print "\n"
		print usage
	elif (sys.argv[1] == "--help"):
		os.system("cls")
		print "\n"
		print usage
	elif (sys.argv[1] == "-?"):
		os.system("cls")
		print "\n"
		print usage
	elif (sys.argv[1] == "-h"):
		os.system("cls")
		print "\n"
		print usage
	else:	
		#data = open(sys.argv[2]).readlines()
		dataQ = open(sys.argv[2])
		data = dataQ.readlines()
		len_data = len(data)
		#print "len_data = ", len_data, "\n"
		dataQ.seek(len_data)
		#print "dataQ.tell() = ", dataQ.tell()
		
		for x in range(1, len(data)):
			#print str(data[-x])
			
			dataz = str(data[-x]).split("\n")
			if (dataz[0] != ''):
				dataxxx = str(dataz[0])
				#print "dataxxx = ", dataxxx
				break
			else:
				pass
		os.system("cls")
		print "\n"
		print "\t File Rar   : " + sys.argv[1] + "\n"
		print "\t Wordlist   : " + sys.argv[2] + "\n\n"
	
		for i in range(0, len(data)):
			data01 = data[i].split("\n")
			dataQ.seek(i)
			#print "dataQ.tell(i) = ", dataQ.tell(), "\n"
			if (data01[0] != ''):
				#print str(i) + ". " + str(data01)
				try:
					data_file = r"\"" + sys.argv[1] + "\""
					cek_rar = os.popen("7z t \"" + sys.argv[1] + "\" -p\"" + str(data01[0]) + "\"").readlines()
					#cek_rar = os.popen("7z t " + r"\"" + sys.argv[1] + "\" -p" + str(data01[0])).readlines()
					#print cek_rar[-2]
					#print cek_rar, "\n"
					#print "cek_rar[-5] = ", cek_rar[-2]
					#print "\n"
					#print str(data01[0]), "\n"
					#print "-----------------------------------------------------------\n"
					
					if (rst_cek in cek_rar[-5]):
						print "\t\t Cek For Password : \"" + str(data01[0]) + "\" is FALSE"
					elif (rst_cek in cek_rar[-4]):
						print "\t\t Cek For Password : \"" + str(data01[0]) + "\" is FALSE"
					elif (rst_cek in cek_rar[-2]):
						print "\t\t Cek For Password : \"" + str(data01[0]) + "\" is FALSE"
					elif (rst_cek2 in cek_rar[-2]):
						print "\t\t Cek For Password : \"" + str(data01[0]) + "\" is FALSE"
					#else:
					#	if (rst_cek2 in cek_rar[-2]):
					#		print "\n\n"
					#		print "\t\t PASSWORD FOUND ! OR but, CONTAINT ERROR ? \n"
					#		print "\t\t Cek For Password : \"" + str(data01[0]) + "\" is True"
					#		print "\n"
					#		print "\t\t Password file " + sys.argv[1] + ": \"" + str(data01[0]) + "\""
					#		print "\n"
					#		print "\t\t---- Sript By BL4CK1D ----"
					#		break
					#		sys.exit()
					#	else:
					#		print "\n\n"
					#		print "\t\t PASSWORD FOUND ! \n"
					#		print "\t\t Cek For Password : \"" + str(data01[0]) + "\" is True"
					#		print "\n"
					#		print "\t\t Password file " + sys.argv[1] + ": \"" + str(data01[0]) + "\""
					#		print "\n"
					#		print "\t\t---- Sript By BL4CK1D ----"
					#		break
					#		sys.exit()
				
					else:
						#if (rst_cek2 in cek_rar[-2]):
						#	#print "cek_rar[-2] = ", cek_rar[-2]
						#	print "\n\n"
						#	print "\t\t PASSWORD FOUND ! OR but, CONTAINT ERROR ? \n"
						#	print "\t\t Cek For Password : \"" + str(data01[0]) + "\" is True"
						#	print "\n"
						#	print "\t\t Password file " + sys.argv[1] + ": \"" + str(data01[0]) + "\""
						#	print "\n"
						#	print "\t\t---- Sript By BL4CK1D ----"
						#	break
						#	sys.exit()
						#else:
						if False:
							print "\n"
							print "\t\tSorry, PASSWORD NOT FOUND ! \n\n"
							dNotsound = r"d:\SOUND\Pass Not  Found.wav"
							winsound.PlaySound(dNotsound, winsound.SND_ALIAS)
							sys.exit()
						else:
							#print "cek_rar[-2] = ", cek_rar[-2], "\n"
							#print "cek_rar[-4] = ", cek_rar[-4], "\n"
							#print "cek_rar[-5] = ", cek_rar[-5], "\n"
							print "\n\n"
							print "\t\t PASSWORD FOUND ! \n"
							print "\t\t Cek For Password : \"" + str(data01[0]) + "\" is True"
							dNotsound = r"d:\SOUND\Pass Found.wav"
							winsound.PlaySound(dNotsound, winsound.SND_ALIAS)
							engine = pyttsx.init()
							rate = engine.getProperty('rate')
							engine.setProperty('rate', rate-30)
							engine.say("The password is " + str(data01[0]))
							engine.runAndWait()
							print "\n"
							print "\t\t Password file " + sys.argv[1] + ": \"" + str(data01[0]) + "\""
							print "\n"
							
							if (rst_cek2 in cek_rar[-2]):
								#print "cek_rar[-2] = ", cek_rar[-2]
								print "\n\n"
								print "\t\t PASSWORD FOUND ! OR but, CONTAINT ERROR ? \n"
								print "\t\t Cek For Password : \"" + str(data01[0]) + "\" is True"
								print "\n"
								#print "\t\t Password file " + sys.argv[1] + ": \"" + str(data01[0]) + "\""
								#print "\n"
								#print "\t\t---- Sript By BL4CK1D ----"
								#break
								#sys.exit()
							else:
								print "\t\t----- RarCracker V2 -----\n"
								print "\t\t---- Sript By BL4CK1D ----"
								os.system("PAUSE > c:\\temp\None")
								#break
								sys.exit()
							
					
					#for z in range(0, len(cek_rar)):
					#	datacl01 = str(cek_rar[z]).split("\n")
					#	print str(z) + ". " + datacl01[0]
				
						
					#	if (rst_cek in datacl01):
					#		pass
					#	else:
					#		if (rst_cek2 in datacl01):
					#			print "\n\n"
					#			print "\t\t PASSWORD FOUND ! OR is NOT CONTAINT PASSWORD ? \n"
					#			print "\t\t Cek For Password : \"" + str(data01[0]) + "\" is True"
					#			print "\n"
					#			print "\t\t Password file " + sys.argv[1] + ": \"" + str(data01[0]) + "\""
					#			break
						#	sys.exit()
						#else:
						#	pass
							#print "\n\n"
						#print "\t\t Cek For Password : \"" + str(data01[0]) + "\" is FALSE"
						
				except IndexError, e:
					os.system("cls")
					print "\n"
					print usage
			
			else:
				pass
			
			if (dataQ.tell() == len_data - 1):	
				print "\n\n"
				print "\t\tSorry, PASSWORD NOT FOUND ! \n\n"
				dNotsound = r"d:\SOUND\Pass Not  Found.wav"
				winsound.PlaySound(dNotsound, winsound.SND_ALIAS)
				print "\t\t----- RarCracker V2 -----\n"
				print "\t\t---- Sript By BL4CK1D ----"
				#os.system("PAUSE >> ")
				sys.exit()
			else:
				pass
				
		#cek_rar2 = os.popen("7z t \"" + sys.argv[1] + "\" -p" + str(dataxxx)).readlines()
		#if (rst_cek in cek_rar2[5]):
		#	print "\n\n"
		#	print "\t\tSorry, PASSWORD NOT FOUND ! \n\n"
		#	print "\t\t---- Sript By BL4CK1D ----"
		#else:
		#	print "\n"
		#	print "\t\t---- Sript By BL4CK1D ----"
		if False:
			print "\n"
			print "\t\t----- RarCracker V2 -----\n"
			print "\t\t---- Sript By BL4CK1D ----"
		else:
			None
	
except IndexError, e:
	#os.system("cls")
	print "\n"
	print "\t\tPlease fill for correct Option !!!!! \n"
	print usage

except KeyboardInterrupt, q:
	os.system("cls")
	print "\n"
	print "\t\t You Cancel Operation !!!\n"
	print "\n"
	print "\t\t----- RarCracker V2 -----\n"
	print "\t\t---- Sript By BL4CK1D ----"








