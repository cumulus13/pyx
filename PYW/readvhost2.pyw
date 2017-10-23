import os
import sys
import MySQLdb


#db = MySQLdb.connect("localhost", "admin", "blackid", "mysite")
#cursor = db.cursor()

data = r"d:\xampp\apache\conf\httpd.conf"

datar = open(data, "r").readlines()
#dataf = [".com",".net"]
datag = "ServerName"
datah = " DocumentRoot"
datai = ["ServerAlias"," DocumentRoot"]
datac = "#"
datad = "localhost:80"
datae = "gives"

open(r"c:\temp\result2.txt", "w")
			
for i in range(0, len(datar)):
	#waitme = ". " * (i/100) 
	if datag in datar[i]:
		if datac and datad and datae not in datar[i]:
			dataz =  datar[i].split("ServerName ")
			#print "data z = ", dataz
			datay = dataz[1].split("\n")
			#print str(i) + ". ", datay[0] 
			#print "datay[0] = ", str(i) + ". " + datay[0]
			print datay[0]
			open(r"c:\temp\result2.txt", "a").writelines(datay[0] + "=192.168.128.1" + "\n")
			#sql = "insert into site(site) values('" + datay[0] + "')"
			#try:
			#	cursor.execute(sql)
			#	db.commit()
			#	os.system("cls")
			#	print "\n"
			#	print "\t\t Please wait " + str(waitme) 
			#except:
			#	db.rollback()
					
					
					
		else:
			pass
	else:
		pass