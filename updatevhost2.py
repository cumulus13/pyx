import os
import sys
import MySQLdb


db = MySQLdb.connect("localhost", "admin", "blackid", "mysite")
cursor = db.cursor()
cursorz = db.cursor()

data = r"d:\xampp\apache\conf\extra\httpd-vhost-proxy.conf"

datar = open(data, "r").readlines()
#dataf = [".com",".net"]
datag = "ServerName"
datah = " DocumentRoot"
datai = ["ServerAlias"," DocumentRoot"]
datac = "#"
datad = "localhost:80"
datae = "gives"

#print datar
			
try:
	if sys.argv[1] == 'update':
		for i in range(0, len(datar)):
			waitme = ". " * (i/100) 
			if datag in datar[i]:
				if datac and datad and datae not in datar[i]:
					dataz =  datar[i].split("ServerName ")
					#print "data z = ", dataz
					datay = dataz[1].split("\n")
					#print str(i) + ". ", datay[0] 
					#print "datay[0] = ", str(i) + ". " + datay[0]
					print "insert data = " , datay[0]
					sql = "insert into site(site) values('" + datay[0] + "')"
					try:
						cursor.execute(sql)
						db.commit()
						os.system("cls")
						print "\n"
						print "\t\t Please wait " + str(waitme) 
					except:
						db.rollback()
					
					
					
				else:
					pass
			else:
				pass
				
	elif sys.argv[1] == 'delete':
		#for i in range(0, len(datar)):
		#	waitme = ". " * (i/100) 
		#	if datag in datar[i]:
		#		if datac not in datar[i]:
		#			dataz =  datar[i].split("ServerName ")
		#			datay = dataz[1].split("\n")
					#print "delete data = " , datay[0]
								
					#sql2 = "delete site where no = %d" %(i)
					#sql = "delete site from site where site like '%" + datay[0] + "%'"
		sql = "DELETE FROM site WHERE no < 99999999"
		sqlz = "delete from site where no < 999999"
					#insCMD = db.simpleCMD("insert into siteme values(" + str(i) + ", '" + datay[0] + "')")
					
		try:
			cursor.execute(sql)
			cursorz.execute(sqlz)
			db.commit()
			os.system("cls")
			print "\n"
			print "\t\t Please wait " + str(waitme) 
		except:
			db.rollback()
			#db.close()
					
			"""
			cursor.execute(sql)
			db.commit()
			#os.system("cls")
			print "\n"
			print "\t\t Please wait " + str(waitme) 
			
			"""
			#	else:
			#		pass
				
	else:
		pass
		
except IOError, e:
	print "\t\t", e

				
os.system("cls && echo. && echo.")
print "\t\t Succesfull ! \n"

	
db.close()
			
		
