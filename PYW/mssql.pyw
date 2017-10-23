import os, sys, errno
import module002	#Direct Execute
import module003	#Service Control
import module004	#Service Status

mssql_server = "MSSQL$SQLEXPRESS"
mssql_helper = "MSSQLServerADHelper"
mssql_browser = "SQLBrowser"
mssql_writer = "SQLWriter"

head = """
          ###############################################################
          #                Microsoft SQL Server Control                 #
          #                         Scr1pt by                           #
          #                          BL4CK1D                            #
          #                                                             #
          ###############################################################
          
"""

data  = os.path.split(sys.argv[0])
data1 = data[1] 

usage = """
	usage """ + data1 + """: db         [start | stop | restart | status]  [Start All Db Services(Agent + xe + recovery + listener) ] \n
		         server      [start | stop | restart | status]  [Start Agent Services       	  ] \n
		         browser      [start | stop | restart | status]  [Start XE Services             ] \n
		         writer      [start | stop | restart | status]  [Start Recovery Services       ] \n
		         helper      [start | stop | restart | status]  [Start FileZilla Services      ] \n
		         status	     [all | agent | xe | recovery | listener 				  ]  
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
						module003.start(mssql_helper)
						module003.start(mssql_server)
						module003.start(mssql_writer)
						module003.start(mssql_browser)
						
					elif (sys.argv[2] == 'stop'):
						module003.stop(mssql_helper)
						module003.stop(mssql_server)
						module003.stop(mssql_writer)
						module003.stop(mssql_browser)
						
					elif (sys.argv[2] == 'restart'):
						module003.stop(mssql_helper)
						module003.stop(mssql_server)
						module003.stop(mssql_writer)
						module003.stop(mssql_browser)
						#------------------------#
						module003.start(mssql_helper)
						module003.start(mssql_server)
						module003.start(mssql_writer)
						module003.start(mssql_browser)
						
					elif (sys.argv[2] == 'status'):
						module004.status(mssql_helper)
						module004.status(mssql_server)
						module004.status(mssql_writer)
						module004.status(mssql_browser)
						
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
						
		elif (sys.argv[1] == 'helper'):
			cek(mssql_helper)
				
		elif (sys.argv[1] == 'browser'):
			cek(mssql_browser)
				
		elif (sys.argv[1] == 'writer'):
			cek(mssql_writer)
			
		elif (sys.argv[1] == 'server'):
			cek(mssql_server)
				
		elif (sys.argv[1] == 'status'):
			try:
				if (sys.argv[2] > 1):
					if (sys.argv[2] == 'helper'):
						module004.status(mssql_helper)
						
					elif (sys.argv[2] == 'browser'):
						module004.status(mssql_browser)
						
					if (sys.argv[2] == 'server'):
						module004.status(mssql_server)
						
					elif (sys.argv[2] == 'writer'):
						module004.status(mssql_writer)
						
					elif (sys.argv[2] == 'all'):
						module004.status(mssql_helper)
						module004.status(mssql_server)
						module004.status(mssql_writer)
						module004.status(mssql_browser)
											
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