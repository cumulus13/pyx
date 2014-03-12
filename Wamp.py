import os, sys, errno
import module002	#Direct Execute
import module002a,os	#Multy Direct Execute
import module003	#Service Control
import module004	#Service Status
import cekstate


wamp_apache = "wampapache"
wamp_mysql = "wampmysqld"
#wamp_tomcat = "wamptomcat"
#wamp_filezilla = "filezilla"
#wamp_mercury = "Mercury"
#wamp_hg = os.getenv("ProgramFiles") +"\\"  + r"TortoiseHg\thg.exe"
wamp_hg = [r"c:\pyx\hgserver.bat"]
wamp_hg_opt = " serve --web-conf=c:\\Apps\\hgweb\webconf.conf"
#mcontrol = r"c:\wamp\wamp_shell.bat"
gui= r"c:\wamp\wamp-control.exe"
wamp_dataconf = r"c:\wamp\apache\conf\extra\httpd-wamp.conf"
apache_dataconf = r"c:\wamp\bin\apache\Apache2.4.4\conf\httpd.conf"
vhost_dataconf = r"c:\wamp\bin\apache\Apache2.4.4\conf\extra\httpd-vhosts.conf"
proxy_dataconf = r"c:\wamp\bin\apache\Apache2.4.4\conf\extra\httpd-vhost-proxy.conf"
php_dataconf = r"c:\wamp\bin\php\php5.4.16\php.ini"
mysql_dataconf = r"c:\wamp\bin\mysql\mysql5.6.12\my.ini"
hg_dataconf = r"d:\xampp\hg\hgwebdir.conf"
head = """
          ###############################################################
          #                  WAMP Web Server Control                   #
          #                         Scr1pt by                           #
          #                          BL4CK1D                            #
          #                                                             #
          ###############################################################
          
"""

data  = os.path.split(sys.argv[0])
data1 = data[1] 

usage = """
	usage """ + data1 + """ : web        [start | stop | restart | status]  [Start Web Server(Tomcat + MySQL  ] \n
		         mysql      [start | stop | restart | status]  [Start MySQL Server       	       ] \n
		         apache     [start | stop | restart | status]  [Start apache Server              ] \n
		         hg         [start | stop | restart | status]  [Start Hg Server                  ] \n
		         control    [start | stop | restart | status]  [Start Control Servier            ] \n
		         gui        [start | stop | restart | status]  [Show Gui Control Admin           ] \n
		         config     [wamp | apache | mysql | tomcat | hg | filezilla | mercury | vhost | php | proxy ] \n
		         status	    [all | web | apache | mysql | tomcat | filezilla | mercury]
				    [Show Status Service All or One by One]
"""

def cek(data):
	try:
		if (sys.argv[2] > 1):
			if (sys.argv[2] == 'start'):
				if (len(sys.argv) == 4):
					if (sys.argv[3] == 'force'):
						module003.start(data)
					else:
						os.system('cls')
						print "\n"
						print "\tPlease Fill Option Of Service ! \n"
						print "\n"
						print usage
				else:
					module003.start(data)
					cekstate.cekstate(data)
						
			elif (sys.argv[2] == 'stop'):
				module003.stop(data)
				
			elif (sys.argv[2] == 'restart'):
				if (len(sys.argv) == 4):
					if (sys.argv[3] == 'force'):
						module003.stop(data)
						module003.start(data)
					else:
						print len(sys.argv)
						print "\n"
						print "\tPlease Fill Option Of Service ! \n"
						print "\n"
						print usage
				else:
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
		
	except KeyboardInterrupt:
		os.system('cls')
		print "\n\n"
		print "\t Bye !"
		
def cek2(data, opt=None):
	try:
		if (sys.argv[2] > 1):
			if (sys.argv[2] == 'start'):
				if (len(sys.argv) == 4):
					if (sys.argv[3] == 'force'):
						if(opt != None):
							module002a.main(data + opt)
						else:
							module002.main(data)
					else:
						os.system('cls')
						print "\n"
						print "\tPlease Fill Option Of Service ! \n"
						print "\n"
						print usage
				else:
					if(opt != None):
						module002a.main(data + opt)
					else:
						module002.main(data)
						
			elif (sys.argv[2] == 'stop'):
				data_kill = os.path.split(data)
				os.system("taskkill /f /im " + data_kill[1])
				
			elif (sys.argv[2] == 'restart'):
				if (len(sys.argv) == 4):
					if (sys.argv[3] == 'force'):
						data_kill = os.path.split(data)
						os.system("taskkill /f /im " + data_kill[1])
						module002a.start(data)
					else:
						print len(sys.argv)
						print "\n"
						print "\tPlease Fill Option Of Service ! \n"
						print "\n"
						print usage
				else:
					data_kill = os.path.split(data)
					os.system("taskkill /f /im " + data_kill[1])
					module002a.start(data)
						
			elif (sys.argv[2] == 'status'):
				data_k = os.path.split(data)
				data_a = os.popen("processx.exe").readlines()
				for i in range(0, len(data_a)):
					if data_k[1] in data_a[i]:
						print "\n"
						print "\t Process " + str(data_k[1]).split(".exe")[0] + " is Running \n"
						sys.exit()
					else:
						pass
				print "\t Process " + str(data_k[1]).split(".exe")[0] + " is NOT Running \n"
						
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
		
	except KeyboardInterrupt:
		os.system('cls')
		print "\n\n"
		print "\t Bye !"


def config(data):
	os.system("start notepad2 " + data)

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
						module003.start(wamp_apache)
						module003.start(wamp_mysql)
						
					elif (sys.argv[2] == 'stop'):
						module003.stop(wamp_apache)
						module003.stop(wamp_mysql)
						
					elif (sys.argv[2] == 'restart'):
						module003.stop(wamp_apache)
						cekstate.cekstate(wamp_apache)
						module003.stop(wamp_mysql)
						cekstate.cekstate(wamp_mysql)
						module003.start(wamp_apache)
						cekstate.cekstate(wamp_apache)
						module003.start(wamp_mysql)
						cekstate.cekstate(wamp_mysql)
						os.system("cls")
						print "\n\n"
						module004.status(wamp_apache)
						module004.status(wamp_mysql)
						
					elif (sys.argv[2] == 'status'):
						module004.status(wamp_apache)
						module004.status(wamp_mysql)
						
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
				
			except KeyboardInterrupt:
				os.system('cls')
				print "\n\n"
				print "\t Bye !"
						
		elif (sys.argv[1] == 'apache'):
			cek(wamp_apache)
				
		elif (sys.argv[1] == 'mysql'):
			cek(wamp_mysql)
				
		elif (sys.argv[1] == 'tomcat'):
			cek(wamp_tomcat)
			
		elif (sys.argv[1] == 'filezilla'):
			cek(wamp_filezilla)
			
		elif (sys.argv[1] == 'mercury'):
			cek(wamp_mercury)
			
		elif (sys.argv[1] == 'hg'):
			cek2(wamp_hg)
			
		elif (sys.argv[1] == 'config'):
			if (sys.argv[2] > 1):
				if (sys.argv[2] == "wamp"):
					config(wamp_dataconf)
				elif (sys.argv[2] == "apache"):
					config(apache_dataconf)
				elif (sys.argv[2] == "vhost"):
					config(vhost_dataconf)
				elif (sys.argv[2] == "proxy"):
					config(proxy_dataconf)
				elif (sys.argv[2] == "php"):
					config(php_dataconf)
				elif (sys.argv[2] == "mysql"):
					config(mysql_dataconf)
				elif (sys.argv[2] == "hg"):
					try:
						config(hg_dataconf)
					except NameError, e:
						print "\n"
						print "\t Not Implement yet ! \n"
						
				else:
					print "Not Yet Implement !"
			else:
					print "Not Yet Implement !"
						
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
			
			except KeyboardInterrupt:
				os.system('cls')
				print "\n\n"
				print "\t Bye !"
				
		elif (sys.argv[1] == 'status'):
			try:
				if (sys.argv[2] > 1):
					if (sys.argv[2] == 'apache'):
						module004.status(wamp_apache)
						
					elif (sys.argv[2] == 'web'):
						module004.status(wamp_apache)
						module004.status(wamp_mysql)
						
					elif (sys.argv[2] == 'mysql'):
						module004.status(wamp_mysql)
						
					elif (sys.argv[2] == 'tomcat'):
						module004.status(wamp_tomcat)
						
					elif (sys.argv[2] == 'filezilla'):
						module004.status(wamp_filezilla)
						
					elif (sys.argv[2] == 'mercury'):
						module004.status(wamp_mercury)
						
					elif (sys.argv[2] == 'hg'):
						data_s = os.path.split(wamp_hg)
						data_r = os.popen("processx.exe").readlines()
						for i in range(0, len(data_r)):
							if data_s[1] in data_r[i]:
								print "\n"
								print "\t Process " + str(data_s[1]).split(".exe")[0] + " is Running \n"
								sys.exit()
							else:
								pass
						print "\t Process " + str(data_s[1]).split(".exe")[0] + " is NOT Running \n"
						
					elif (sys.argv[2] == 'all'):
						module004.status(wamp_apache)
						module004.status(wamp_mysql)
						module004.status(wamp_tomcat)
						module004.status(wamp_filezilla)
						module004.status(wamp_mercury)
											
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
				
			except KeyboardInterrupt:
				os.system('cls')
				print "\n\n"
				print "\t Bye !"
			
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
			
except KeyboardInterrupt:
			os.system('cls')
			print "\n\n"
			print "\t Bye !"
