import os
import sys
#import pdo
import MySQLdb

#db = pdo.connect("Module=MySQLdb;User=admin;password=blackid;db=testme")
db = MySQLdb.connect("localhost", "admin", "blackid", "mysite")
cursor = db.cursor()
cursor2 = db.cursor()

data = r"d:\xampp\apache\conf\extra\httpd-vhosts.conf"

datar = open(data, "r").readlines()
#dataf = [".com",".net"]
datag = "ServerAlias"
datah = " DocumentRoot"
datai = ["ServerAlias"," DocumentRoot"]
datac = "#"

#sql = "select site from site"
#insCMD = db.simpleCMD("insert into siteme values(" + str(i) + ", '" + datay[0] + "')")
				
#result = cursor.execute(sql)
#for row in result:
#	print row[0]
							


open(r"c:\temp\result.txt", "w")
			
for i in range(0, len(datar)):
	waitme = ". " * (i/100) 
	if datag in datar[i]:
		if datac not in datar[i]:
			dataz =  datar[i].split("ServerAlias ")
			datay = dataz[1].split("\n")
			#print "datay[0] = ", str(i) + ". " + datay[0]
			print datay[0]
			
			open(r"c:\temp\result.txt", "a").writelines(datay[0] + "=192.168.128.1" + "\n")
			
			#sql = "select site from site"
			#insCMD = db.simpleCMD("insert into siteme values(" + str(i) + ", '" + datay[0] + "')")
				
			#result = cursor.execute(sql)
			#for row in result:
			#	print row[0]
			#print result[0]
			
			#db.commit()				
			#pass
		else:
			pass
	else:
		pass
				
	
db.commit()	
db.close()