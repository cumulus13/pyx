import os, sys, errno
import module002	#Direct Execute
import module003	#Service Control
import module004	#Service Status
import cekstate


appserv_apache = "apachexampplite"
appserv_mysql = "mysqlxampplite"
#gui= r"C:\AppServ\Apache2.2\bin\ApacheMonitor.exe"

head = """
          ###############################################################
          #                 XAMPPLite Web Server Control                #
          #                         Scr1pt by                           #
          #                          BL4CK1D                            #
          #                                                             #
          ###############################################################
          
"""

data  = os.path.split(sys.argv[0])
data1 = data[1] 

usage = """
	usage """ + data1 + """ : web        [start | stop | restart | status]  \n
		         mysql      [start | stop | restart | status]  [Start MySQL Server       	      ] \n
		         apache     [start | stop | restart | status]  [Start apache Server             ] \n
		         status	    [all | web | apache | mysql ]  
				    [Show Status Service All or One by One]
"""

def cek(data):
	try:
		if (sys.argv[2] > 1):
			if (sys.argv[2] == 'start'):
				module003.start(data)
				cekstate.cekstate(data)
						
			elif (sys.argv[2] == 'stop'):
				module003.stop(data)
				
			elif (sys.argv[2] == 'restart'):
				module003.stop(data)
				module003.start(data)
				cekstate.cekstate(data)
						
			elif (sys.argv[2] == 'status'):
				module004.status(data)
						
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
		if (sys.argv[1] == 'web'):
			try:
				if (sys.argv[2] > 1):
					if (sys.argv[2] == 'start'):
						module003.start(appserv_apache)
						module003.start(appserv_mysql)
						
					elif (sys.argv[2] == 'stop'):
						module003.stop(appserv_apache)
						module003.stop(appserv_mysql)
						
					elif (sys.argv[2] == 'restart'):
						module003.stop(appserv_apache)
						cekstate.cekstate(appserv_apache)
						module003.stop(appserv_mysql)
						cekstate.cekstate(appserv_mysql)
						module003.start(appserv_apache)
						cekstate.cekstate(appserv_apache)
						module003.start(appserv_mysql)
						cekstate.cekstate(appserv_mysql)
						os.system("cls")
						print "\n\n"
						module004.status(appserv_apache)
						module004.status(appserv_mysql)
						
					elif (sys.argv[2] == 'status'):
						module004.status(appserv_apache)
						module004.status(appserv_mysql)
						
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
						
		elif (sys.argv[1] == 'apache'):
			cek(appserv_apache)
				
		elif (sys.argv[1] == 'mysql'):
			cek(appserv_mysql)
						
		elif (sys.argv[1] == 'gui'):
			try:
				module002.main(gui)
					
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
					if (sys.argv[2] == 'apache'):
						module004.status(appserv_apache)
						
					elif (sys.argv[2] == 'web'):
						module004.status(appserv_apache)
						module004.status(appserv_mysql)
						
					elif (sys.argv[2] == 'mysql'):
						module004.status(appserv_mysql)
						
					elif (sys.argv[2] == 'all'):
						module004.status(appserv_apache)
						module004.status(appserv_mysql)
											
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