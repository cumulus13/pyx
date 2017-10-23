import os
import sys
import MySQLdb

filename = os.path.split(sys.argv[0])[1]
usage = "\t Use " + filename + """ [name of site] 
         example : """ + filename + """ www.example.com
"""


def add():
	try:
		db = MySQLdb.connect("localhost", "admin", "blackid", "mysite")
		cursor = db.cursor()
		
		if len(sys.argv) > 1:
			sql = "delete from site where site = '" + sys.argv[1] + "'"
			cursor.execute(sql)
			db.commit()
			db.close()
		else:
			os.system('cls')
			print "\n"
			print usage
			sys.exit()
	except IndexError, e:
		os.system('cls')
		print "\n"
		print "\t ERROR = " + str(e)
		
		
if __name__ == '__main__':
	add()