import os
import sys
import MySQLdb
import time
import traceback


def importfromdb(username, password, host, db, port=None):
	try:
		db = MySQLdb.connect(host,username,password,db)
		cursor = db.cursor()

		sql = "SELECT * FROM site"
		cursor.execute(sql)
		#db.commit()
		results = cursor.fetchall()
		for row in results:
			if "www." in row[1]:
				data = str(row[1]).split("www.")
				print "\t insert \"" + str(data[1]) + "\""
				os.system("addhost.ipy " + data[1])
			else:
				pass
			

	except IndexError, e:
		os.system('cls')
		data_e = traceback.format_exc()
		#print "ERROR : \n"
		#print "\t" + str(data_e)
		#print "-"*85
		print "\n"
		print usage
		print "\n"
		print "\t ------------------- script by : licface --------------------"
		
if __name__ == '__main__':
	importfromdb("root","blackid","localhost","mysite")