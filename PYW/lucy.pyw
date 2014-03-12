import os
import sys
import pyttsx
import time
import win32api

#class answer:
#	def __init__(self,data, parent=None):
#		self.data = data
#		
#	def cek(self):
#		if 'date' in self.data:
			

def cek_memory(z,identity=None):
	
	engine = pyttsx.init()
	rate = engine.getProperty('rate')
	data = win32api.GlobalMemoryStatusEx()
	mb = float(1024 * 1024 * 10)
	mb2 = float(1024 * 1024)
	gb = float(1024 * 1024 * 1024)
	
	TotalPageFile = data['TotalPageFile']
	AvailVirtual  = data['AvailVirtual'] 
	MemoryLoad    = data['MemoryLoad']
	MemoryFree    = 100 - MemoryLoad
	TotalPhys     = data['TotalPhys']
	AvailExtendedVirtual = data['AvailExtendedVirtual']
	TotalVirtual  = data['TotalVirtual']
	AvailPhys     = data['AvailPhys']
	AvailPageFile = data['AvailPageFile']
	
	data_TotalPageFile = "Total PageFile,         %0.2f0 Mega Byte" %(float(TotalPageFile) / mb) + '.'
	data_AvailVirtual  = "Availaible Virtual,     %0.2f0 Mega Byte" %(float(AvailVirtual) / mb) + '.'
	data_TotalPhys     = "Total Physical,         %0.2f0 Giga Byte" %(float(TotalPhys) / gb) + '.'
	data_TotalVirtual  = "Total Virtual,          %0.2f0 Mega Byte" %(float(TotalVirtual) / mb) + '.'
	data_UsedPhys       = "Used Physical,          %0.2f0 Mega Byte" %((float(TotalPhys) /mb2) - (float(AvailPhys) / mb2)) + '.'
	data_AvailPhys     = "Availaible Physical,    %0.2f0 Mega Byte" %(float(AvailPhys) / mb2) + '.'
	data_AvailPageFile = "Availaible PageFile,    %0.2f0 Mega Byte" %(float(AvailPageFile) / mb) + '.'
	data_MemoryLoad = "Memory Load!.            %d" %(MemoryLoad) + '% !.'
	data_MemoryFree = "Memory Free!.            %d" %(MemoryFree) + '% !.'
	data_AvailExtendedVirtual = "Availaible Extended Virtual,    %d" %(AvailExtendedVirtual) + ' !'
	
	cek = {'Total PageFile':data_TotalPageFile,
			'Availaible Virtual':data_AvailVirtual,
			'Memory Load':data_MemoryLoad,
			'Memory Free':data_MemoryFree,
			'Total Physical':data_TotalPhys,
			'Availaible Extended Virtual':data_AvailExtendedVirtual,
			'Total Virtual':data_TotalVirtual ,
			'Availaible Physical':data_AvailPhys,
			'Availaible PageFile':data_AvailPageFile,
			'Data Used Physical':data_UsedPhys
		   }
	if identity == 'full':
		engine.setProperty('rate', rate-(-35+int(z))) #95
		engine.say('Status Of Computer is')
		engine.runAndWait()
		for x in cek:
			time.sleep(1)
			engine.setProperty('rate', rate-(z-40)) #40
			engine.say(str(cek[x]))
			engine.runAndWait()
	elif identity == 'complete':
		for x in cek:
			time.sleep(1)
			engine.say(str(cek[x]))
			engine.runAndWait()
	else:
		time.sleep(1)
		engine.setProperty('rate', rate-60)
		engine.say(str(data_MemoryLoad))
		engine.runAndWait()
		time.sleep(1)
		engine.setProperty('rate', rate-75)
		engine.say(str(data_MemoryFree))
		engine.runAndWait()

def main():
	import time
	data001 = time.strftime("%Y-%m-%d", time.localtime())
	data002 = time.strftime("%H:%M:%S", time.localtime())
	cektime = time.strftime("%H", time.localtime())
	
	if int(cektime) < 11:
		result_day = "Morning !"
	elif int(cektime) < 15:
		result_day = "Day !"
	elif int(cektime) < 18:
		result_day = "Affternoon !"
	elif int(cektime) < 23:
		result_day = "Night !"
	elif int(cektime) < 24:
		result_day = "Late Night !"
	else:
		result_day = "Morning !"
	
	os.system("cls")
	print "\n\n"
	
	import pyttsx
	import time
	import getpass
	engine = pyttsx.init()
	rate = engine.getProperty('rate')
	engine.setProperty('rate', rate-30)
	#engine.say("Who, are, you ?")
	#engine.runAndWait()
	input_name = raw_input(">> Login : ")
	input_pass = getpass.getpass(">> Password: ") 
	engine.say("Please insert youre password !")
	engine.runAndWait()
	
	if input_pass == " ":
		engine.say("Please insert youre password !")
		engine.runAndWait()
		#time.sleep(1)
		input_pass = getpass.getpass(">> Password: ") 
		if input_pass != "blackid":
			engine.say("Please insert youre password again!")
			engine.runAndWait()
			#time.sleep(1)
			input_pass = getpass.getpass(">> Password: ") 
			if input_pass != "blackid":
				engine.say("Please insert youre password again!")
				engine.runAndWait()
				time.sleep(1)
				input_pass = getpass.getpass(">> Password: ") 
			else:
				engine.setProperty('rate', rate-30)
				engine.say("Iam sorry you can't access the system, bye ...")
				engine.runAndWait()
				sys.exit()
				#pass
		else:
			engine.setProperty('rate', rate-30)
			engine.say("Iam sorry you can't access the system, bye ...")
			engine.runAndWait()
			#pass
			sys.exit()
	else:
		engine.setProperty('rate', rate-30)
		engine.say("Iam sorry you can't access the system, bye ...")
		engine.runAndWait()	
		#pass
		sys.exit()
		
	os.system("cls")
	print "\n\n"
	engine.setProperty('rate', rate-55)
	engine.say("Good " + str(result_day) + " " + str(input_name) + "! ")
	engine.runAndWait()
	print ">> Good " + str(result_day) + " " + str(input_name) + "! "
	print ">> How are you today ?"
	engine.say('How are you today?')
	engine.runAndWait()
	d001 = raw_input(">> ")
	if d001 == "fine":
		time.sleep(1)
		print ">> Iam too "
		engine.say('iam too')
		engine.runAndWait()
		time.sleep(1)
		engine.say('Do you want to know. The status of computer now.')
		engine.runAndWait()
		a0000 = raw_input("\r>> ")
		if a0000 == 'yes':
			cek_memory(+40,'full')
		elif a0000 == 'Yes':
			cek_memory(10,'full')
		elif a0000 == 'no':
			pass
		elif a0000 == 'No':
			pass
		else:
			pass
		print ">> Do you want to know. How fine your wife this day ? "
		engine.say('Do you want to know. How fine your wife this day ?')
		engine.runAndWait()
		a000 = raw_input("\r>> ")
		if "no" in a000:
			pass
		elif "No" in a000:
			pass
		elif "yes" in a000:
			time.sleep(1)
			print ">> Nurul, youre wife  fine this day "
			engine.say('Nurul, youre wife  fine this day')
			engine.runAndWait()
		else:
			pass
		a001 = raw_input("\r>> ")
		if "date" in a001:
			time.sleep(1)
			print ">> Date Now.  " + str(data001)
			engine.say('Date Now.  ' + str(data001) + str("!"))
			engine.runAndWait()
			a002 = raw_input("\r>> ")
			if "time" in a002:
				time.sleep(1)
				print ">> Time Now.  " + str(data002)
				engine.say('Time Now.  ' + str(data002) + str("!"))
				engine.runAndWait()
			else:
				time.sleep(1)
				print ">> Nice Day "
				engine.say('Nice Day')
				engine.runAndWait()
		elif "name" in a001:
			time.sleep(1)
			print ">> my name  Mary "
			engine.say('my name  Mary')
			engine.runAndWait()
		elif "time" in a001:
			time.sleep(1)
			print ">> Time Now.  " + str(data002)
			engine.say("Time Now.  " + str(data002) + str("!")) 
			engine.runAndWait()
			a003 = raw_input("\r>> ")
			if "date" in a003:
				time.sleep(1)
				print ">> Date Now.  " + str(data001)
				engine.say("Date Now.  " + str(data001) + str("!"))
				engine.runAndWait()
			else:
				time.sleep(1)
				print ">> Nice Day "
				engine.say('Nice Day')
				engine.runAndWait()
		else:
			time.sleep(1)
			print ">> Nice Day "
			engine.say('Nice Day')
			engine.runAndWait()
	else:
		time.sleep(1)
		print ">> What happen hadi ? "
		engine.say("What happen " + str(input_name) + "?")
		engine.runAndWait()
		d002 = raw_input(">> ")
		time.sleep(1)
		print ">> may I call a doctor ? "
		engine.setProperty('rate', rate-80)
		engine.say("may I call a doctor ? ")
		engine.runAndWait()
		d003 = raw_input("\r>> ")
		if "no" in d003:
			time.sleep(1)
			print ">> OK. please take a care, becarefull ? "
			engine.setProperty('rate', rate-80)
			engine.say("OK. please take a care. becarefull ? ")
			engine.runAndWait()
		elif "yes" in d003:
			time.sleep(1)
			print ">> OK. while a seconds ? "
			engine.say("OK. while a seconds ? ")
			engine.runAndWait()
		else:
			time.sleep(1)
			print ">> How well did you ? "
			engine.say("How well did you ? ")
			engine.runAndWait()
		
	d00x = raw_input(">> ")
	if d00x == '':
		time.sleep(1)
		print ">> Thank you ! "
		engine.setProperty('rate', rate)
		engine.say("Thank you !")
		engine.runAndWait()
	elif d00x == None:
		time.sleep(1)
		print ">> Thank you ! "
		engine.setProperty('rate', rate)
		engine.say("Thank you !")
		engine.runAndWait()
	

if __name__ == '__main__':
	#cek_memory(40,'full')
	main()

"""engine = pyttsx.init()
voices = engine.getProperty('voices')
for voice in voices:
   engine.setProperty('voice', voice.id)
   engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()

"""