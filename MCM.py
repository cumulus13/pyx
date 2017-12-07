import os, sys, errno
import module002	#Direct Execute
import module003	#Service Control
import module004	#Service Status


msmtp = "MerakSMTP"
mpop  = "MerakPOP3"
mim	 = "MerakIM"
mcalendar = "MerakCalendar"
mcontrol = "MerakControl"
mgui = os.getenv("ProgramFiles") +"\\"  + r"Merak\loader.exe"

head = """
          ###############################################################
          #            IceWrap Merak Email Server Control               #
          #                         Scr1pt by                           #
          #                          BL4CK1D                            #
          #                                                             #
          ###############################################################
          
"""

data  = os.path.split(sys.argv[0])
data1 = data[1] 

usage = """
	usage """ + data1 + """ : mail      [start | stop | status]  [Start mail Server     ]
		       im        [start | stop | status]  [Start Im Server       ]
		       groupware [start | stop | status]  [Start Groupware Server]
		       control   [start | stop | status]  [Start Control Servier ]
		       gui       [start | stop | status]  [Show Gui Control Admin]
		       status	 [all | mail | im | calendar | control]  [Show Status Service All or One by One]
"""

try:
	if (sys.argv < 1):
		os.system("cls")
		print "\n"
		print head, "\n"
		print usage
		
	else:
		if (sys.argv[1] == 'mail'):
			try:
				if (sys.argv[2] > 1):
					if (sys.argv[2] == 'start'):
						module003.start(mpop)
						module003.start(msmtp)
						
					elif (sys.argv[2] == 'stop'):
						module003.stop(mpop)
						module003.stop(msmtp)
						
					elif (sys.argv[2] == 'status'):
						module004.status(msmtp)
						module004.status(mpop)
						
					else:
						os.system('cls')
						print "\n"
						print head, "\n"
						print usage
				
				else:
						os.system('cls')
						print "\n\n"
						print head, "\n"
						print usage
						
			except IndexError, e:
				os.system('cls')
				print "\n"
				print "\tPlease Fill Option Of Service ! \n"
				print "\n"
				print usage
				
			except TypeError, e:
				os.system('cls')
				print "\n"
				print "\tPlease Cek Name Of Service is Correct ! \n"
				print "\n"
						
		elif (sys.argv[1] == 'im'):
			try:
				if (sys.argv[2] > 1):
					if (sys.argv[2] == 'start'):
						module003.start(mim)
						
					elif (sys.argv[2] == 'stop'):
						module003.stop(mim)
						
					elif (sys.argv[2] == 'status'):
						module004.status(mim)
						
					else:
						os.system('cls')
						print "\n\n"
						print head, "\n"
						print usage
				
				else:
						os.system('cls')
						print "\n\n"
						print head, "\n"
						print usage
					
					
			except IndexError, e:
				os.system('cls')
				print "\n"
				print "\tPlease Fill Option Of Service ! \n"
				print "\n"
				print usage
				
			except TypeError, e:
				os.system('cls')
				print "\n"
				print "\tPlease Cek Name Of Service is Correct ! \n"
				print "\n"
				
		elif (sys.argv[1] == 'groupware'):
			try:
				if (sys.argv[2] > 1):
					if (sys.argv[2] == 'start'):
						module003.start(mcalendar)
						
					elif (sys.argv[2] == 'stop'):
						module003.stop(mcalendar)
						
					elif (sys.argv[2] == 'status'):
						module004.status(mcalendar)
						
					else:
						os.system('cls')
						print "\n\n"
						print head, "\n"
						print usage
				
				else:
						os.system('cls')
						print "\n\n"
						print head, "\n"
						print usage
					
					
			except IndexError, e:
				os.system('cls')
				print "\n"
				print "\tPlease Fill Option Of Service ! \n"
				print "\n"
				print usage
				
			except TypeError, e:
				os.system('cls')
				print "\n"
				print "\tPlease Cek Name Of Service is Correct ! \n"
				print "\n"
				
		elif (sys.argv[1] == 'control'):
			try:
				if (sys.argv[2] > 1):
					if (sys.argv[2] == 'start'):
						module003.start(mcontrol)
						
					elif (sys.argv[2] == 'stop'):
						module003.stop(mcontrol)
						
					elif (sys.argv[2] == 'status'):
						module004.status(mcontrol)
						
					else:
						os.system('cls')
						print "\n\n"
						print head, "\n"
						print usage
				
				else:
						os.system('cls')
						print "\n\n"
						print head, "\n"
						print usage
						
			except IndexError, e:
				os.system('cls')
				print "\n"
				print "\tPlease Fill Option Of Service ! \n"
				print "\n"
				print usage
				
			except TypeError, e:
				os.system('cls')
				print "\n"
				print "\tPlease Cek Name Of Service is Correct ! \n"
				print "\n"
						
		elif (sys.argv[1] == 'gui'):
			try:
				module002.main(mgui)
					
			except IndexError, e:
				os.system('cls')
				print "\n"
				print "\tPlease Fill Option Of Service ! \n"
				print "\n"
				print usage
				
			except TypeError, e:
				os.system('cls')
				print "\n"
				print "\tPlease Cek Name Of Service is Correct ! \n"
				print "\n"
				
		elif (sys.argv[1] == 'status'):
			try:
				if (sys.argv[2] > 1):
					if (sys.argv[2] == 'im'):
						module004.status(mim)
						
					elif (sys.argv[2] == 'mail'):
						module004.status(msmtp)
						module004.status(mpop)
						
					elif (sys.argv[2] == 'groupware'):
						module004.status(mcalendar)
						
					elif (sys.argv[2] == 'control'):
						module004.status(mcontrol)
						
					elif (sys.argv[2] == 'all'):
						module004.status(msmtp)
						module004.status(mpop)
						module004.status(mim)
						module004.status(mcalendar)
						module004.status(mcontrol)
											
					else:
						os.system('cls')
						print "\n\n"
						print head, "\n"
						print usage
				
				else:
						os.system('cls')
						print "\n\n"
						print head, "\n"
						print usage
						
			except IndexError, e:
				os.system('cls')
				print "\n"
				print "\tPlease Fill Option Of Service ! \n"
				print "\n"
				print usage
				
			except TypeError, e:
				os.system('cls')
				print "\n"
				print "\tPlease Cek Name Of Service is Correct ! \n"
				print "\n"
			
		else:
			os.system('cls')
			print "\n\n"
			print head, "\n"
			print usage
			
		
			
except IndexError, e:
			os.system('cls')
			print "\n"
			print "\tPlease Fill Name Of Service ! \n"
			print "\n"
			print usage