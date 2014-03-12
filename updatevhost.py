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

#print datar
			
try:
	if sys.argv[1] == 'update':
		for i in range(0, len(datar)):
			waitme = ". " * (i/100) 
			if datag in datar[i]:
				if datac not in datar[i]:
					dataz =  datar[i].split("ServerAlias ")
					datay = dataz[1].split("\n")
					#print "datay[0] = ", str(i) + ". " + datay[0]
					print "insert data = " , datay[0]
								
					sql = "insert into site(site) values('" + datay[0] + "')"
					#insCMD = db.simpleCMD("insert into siteme values(" + str(i) + ", '" + datay[0] + "')")
					try:
						cursor.execute(sql)
						db.commit()
						os.system("cls")
						print "\n"
						print "\t\t Please wait " + str(waitme) 
					except:
						db.rollback()
						#db.close()
								
				else:
					pass
	elif sys.argv[1] == 'insert_locate':
		for i in range(0, len(datar)):
			waitme = ". " * (i/100) 
			if datah in datar[i]:
				if datac not in datar[i]:
					dataz =  datar[i].split("DocumentRoot ")
					datay = dataz[1].split("\n")
					#print "datay[0] = ", str(i) + ". " + datay[0]
					print "insert data = " , datay[0]
					datax = os.path.split(datay[0])
					print "datax = " , datax			
					#sql = "insert into site(locate) values('" + datay2[0] + "')"
					sql = """update site set locate=('" + datay[0] + "') where site like '%""" + datax[1] + "%'"
					#insCMD = db.simpleCMD("insert into siteme values(" + str(i) + ", '" + datay[0] + "')")
					"""
					try:
						cursor.execute(sql)
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
								
				else:
					pass
					
	elif sys.argv[1] == 'delete':
		#for i in range(0, len(datar)):
		#	waitme = ". " * (i/100) 
		#	if datag in datar[i]:
		#		if datac not in datar[i]:
		#			dataz =  datar[i].split("ServerAlias ")
		#			datay = dataz[1].split("\n")
					#print "delete data = " , datay[0]
								
					#sql2 = "delete site where no = %d" %(i)
					#sql = "delete site from site where site like '%" + datay[0] + "%'"
		sql = "DELETE FROM site WHERE no < 99999999";
					#insCMD = db.simpleCMD("insert into siteme values(" + str(i) + ", '" + datay[0] + "')")
					
		try:
			cursor.execute(sql)
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
				#else:
					#pass
except IndexError, e:
	print e
		
	
	
	
"""

for i in range(0, len(datar)):
	
	waitme = ". " * (i/100) 
	for j in range(0, len(datai)):
		if datai[0] in datar[i]:
			if datac not in datar[i]:
				dataz =  datar[i].split("ServerAlias ")
				datay = dataz[1].split("\n")
				print "datay[0] = ", str(i) + ". " + datay[0]
					
				sql = "insert into site(site) values('" + datay[0] + "')"
				#insCMD = db.simpleCMD("insert into siteme values(" + str(i) + ", '" + datay[0] + "')")
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
						
		elif datai[1] in datar[i]:
			if datac not in datar[i]:
				dataz2 =  datar[i].split("DocumentRoot ")
				#print "dataz2 = " , dataz2
				datay2 = dataz2[1].split("\n")
				#print "dataz2[0] = ", str(i) + ". " + datay2[0]
				print "datay[0] = " ,datay2[0]
						
				#sql2 = "insert into site(locate) values('" + datay2[0] + "')"
				#sql2 = "insert into site(locate) values('" + datay2[0] + "') where no = %d" % (i)
				datax = os.path.split(datay2[0])
				print "datax = ", datax
				sql2 = "update site set locate=('" + datay2[0] + "') where site like '%" + datax[0] + "%'"
				#sql2 = "update site set locate=('" + datay2[0] + "') where site no= %d" %(i) 
				#sql2 = "update site set locate=('" + datay2[0] + "') where no = %d" % (i)
				#sql2 = "insert into site(locate) values('" + datay2[0] + "') where no = " + str(i + 1)
				#insCMD = db.simpleCMD("insert into siteme values(" + str(i) + ", '" + datay[0] + "')")
				
				try:
					cursor2.execute(sql2)
					db.commit()
					os.system("cls")
					print "\n"
					print "\t\t Please wait " + str(waitme) 
				except e:
					db.rollback()	
					#open("error.txt", "w")
					#open("error.txt", "a")
					#open("error.txt", "w").writelines(str(e))
				
				cursor2.execute(sql2)
				db.commit()
				#os.system("cls")
				print "\n"
				print "\t\t Please wait " + str(waitme) 
			else:
				pass	
		
		else:
			pass
"""	
os.system("cls && echo. && echo.")
print "\t\t Succesfull ! \n"

	
db.close()
			
		
