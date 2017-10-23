import sys
import os
import mdbsearch
import MySQLdb

filename = os.path.split(sys.argv[0])

usage = """
		Usage : """ + filename[1] + """ [host] [user] [password] [database] [search] 
		
	                (if password empty, please fill with "")
	                
	                example: + """ + filename[1] + """ localhost root "" mydb article
"""

error001 = """ 
		Please input correct options ! \n
"""

by = """\t\t\tScr1pt by blackid - livinginthecurl@gmail.com"""

try:
	if (len(sys.argv) > 1):
		host = sys.argv[1]
		user = sys.argv[2]
		paswd = sys.argv[3]
		database = sys.argv[4]
		searchdata = sys.argv[5]
 
		mdbsearch.search(host, user, paswd, database, searchdata)
		
	else:
		os.system("cls&&echo.&&echo.")
		print usage, "\n"
		print by
		
    
except IndexError, e:
	os.system("cls&&echo.&&echo.")
	print error001
	print "\n"
	print usage, "\n"
	print by
    
except MySQLdb.MySQLError, e:
	try:
		derror = str(e[1]).split(" ")
		print "\t" + (derror[0] + " " + derror[1] + " " + derror[2] + " " + derror[3] + derror[4] + " " + derror[5] + " " + derror[6]).upper() + " With :\n"
		print "\tHost           = ", sys.argv[1]
		print "\tUser           = ", sys.argv[2]
		print "\tPassword       = ", sys.argv[3]
		print "\tDatabase       = ", sys.argv[4]
		print "\tWant To Search = ", sys.argv[5] + "\n"
		print "\tPlease Check You Correct Host, User and Password for Connect to Database ! \n"
		print "\tError Code     = ", str(e[0]) + " / " + derror[7]
		
	except IndexError, e:
		os.system("cls&&echo.&&echo.")
		print "\tPlease Input Correct Option ! \n"
		print "\tPlease Check You Correct Host, User and Password for Connect to Database ! \n"
		
except NameError, e:
	os.system("cls&&echo.&&echo.")
	print "\tYou Have Syntax Error, " + str(e)
	
except IndexError, e:
	os.system("cls&&echo.&&echo.")
	print "\tPlease Input Correct Option ! \n"
	print str(e)

    
