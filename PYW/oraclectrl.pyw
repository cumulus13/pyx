import os, sys, errno
import module002	#Direct Execute
import module003	#Service Control
import module004	#Service Status


oracleListener = "OracleXETNSListener"
oracleAgent = "OracleXEClrAgent"
oracleXE = "OracleServiceXE"
oracleRec = "OracleMTSRecoveryService"
oracleControl = r""
gui= r""

head = """
          ###############################################################
          #                    ORACLE Server Control                    #
          #                         Scr1pt by                           #
          #                          BL4CK1D                            #
          #                                                             #
          ###############################################################
          
"""

data  = os.path.split(sys.argv[0])
data1 = data[1] 

usage = """
	usage """ + data1 + """: db         [start | stop | restart | status]  [Start All Db Services(Agent + xe + recovery + listener) ] \n
		         agent      [start | stop | restart | status]  [Start Agent Services       	  ] \n
		         xe         [start | stop | restart | status]  [Start XE Services             ] \n
		         recovery   [start | stop | restart | status]  [Start Recovery Services       ] \n
		         listener   [start | stop | restart | status]  [Start FileZilla Services      ] \n
		         status	    [all | agent | xe | recovery | listener 				  ]  
				    [Show Status Service All or One by One]
"""

def cek(dataservice):
	try:
		if (sys.argv[2] > 1):
			if (sys.argv[2] == 'start'):
				module003.start(dataservice)
						
			elif (sys.argv[2] == 'stop'):
				module003.stop(dataservice)
				
			elif (sys.argv[2] == 'restart'):
				module003.stop(dataservice)
				module003.start(dataservice)
						
			elif (sys.argv[2] == 'status'):
				module004.status(dataservice)
						
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


try:
	if (sys.argv < 1):
		os.system("cls")
		print "\n"
		print head, "\n"
		print usage
		
	else:
		if (sys.argv[1] == 'db'):
			try:
				if (sys.argv[2] > 1):
					if (sys.argv[2] == 'start'):
						#module003.start(oracleAgent)
						module003.start(oracleListener)
						#module003.start(oracleRec)
						#module003.start(oracleXE)
						
					elif (sys.argv[2] == 'stop'):
						#module003.stop(oracleAgent)
						module003.stop(oracleListener)
						#module003.stop(oracleRec)
						#module003.stop(oracleXE)
						
					elif (sys.argv[2] == 'restart'):
						#module003.stop(oracleAgent)
						module003.stop(oracleListener)
						#module003.stop(oracleRec)
						#module003.stop(oracleXE)
						#------------------------#
						#module003.start(oracleAgent)
						module003.start(oracleListener)
						#module003.start(oracleRec)
						#module003.start(oracleXE)
						
					elif (sys.argv[2] == 'status'):
						#module004.status(oracleAgent)
						module004.status(oracleListener)
						#module004.status(oracleRec)
						#module004.status(oracleXE)
						
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
						
		#elif (sys.argv[1] == 'agent'):
		#	cek(oracleAgent)
		#		
		#elif (sys.argv[1] == 'xe'):
		#	cek(oracleXE)
		#		
		#elif (sys.argv[1] == 'recovery'):
		#	cek(oracleRec)
		#	
		elif (sys.argv[1] == 'listener'):
			cek(oracleListener)
				
		elif (sys.argv[1] == 'status'):
			try:
				if (sys.argv[2] > 1):
					#if (sys.argv[2] == 'agent'):
					#	module004.status(oracleAgent)
						
					#elif (sys.argv[2] == 'xe'):
					#	module004.status(oracleXE)
						
					if (sys.argv[2] == 'listener'):
						module004.status(oracleListener)
						
					#elif (sys.argv[2] == 'recovery'):
					#	module004.status(oracleRec)
						
					elif (sys.argv[2] == 'all'):
						#module004.status(oracleAgent)
						module004.status(oracleListener)
						#module004.status(oracleRec)
						#module004.status(oracleXE)
											
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