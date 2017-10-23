import os
import sys
import MySQLdb as db

def error_report(data):
	report =  """\t\t####################################################################
		#                                                                  #
		#  Database ERROR ! = ", """ + data + """, "             		   #
		#                                                                  #
		####################################################################\n"""
	print report
	
def search(host, user, paswd, database, dsearch):
	try:

		os.system("cls&&echo.&&echo.")
		conn = db.connect(host, user, paswd, database)
		cursor = conn.cursor()
		cursor2 = conn.cursor()
		cursor3 = conn.cursor()
		
		sql001 = "show tables"
	
		cursor.execute(sql001)
		result001 = cursor.fetchall()
		for row in result001:
			table_name = row[0]
			sql002 = "show columns from " + table_name
			cursor2.execute(sql002)
			result002 = cursor2.fetchall()
			#print "\tDatabase Name = ", dsearch
			#print "\tTable Name = ", table_name
			for rows in result002:
				columns = rows[0]
				columns_type = rows[1]
				#print columns + "|" + columns_type
				#print "len Columns = ", columns,  len(columns)
				#print "\n"
				#try:
				try:
					if rows[1] == 'datetime':
						pass
					elif rows[1] == 'date':
						pass
					elif rows[1] == 'timestamp':
						pass
					else:
						#print "\tDatabase Name = ", database
						#print "\tTable Name    = ", table_name
						#print "\tColumn Name   = ", columns
						#print "\tType Column   = ", columns_type, "\n" 
						sql003 = "select " + columns + " from " + table_name + " where " + columns + " like '%" + dsearch + "%'"
						cursor3.execute(sql003)
						result003 = cursor3.fetchall()
						for datas in result003:
							fields = datas[0]
							print "\tDatabase Name = ", database
							print "\tTable Name    = ", table_name
							print "\tColumn Name   = ", columns
							print "\tType Column   = ", columns_type, "\n" 
							print "\tResult Search = ", fields, "\n"
							print "\t-------------------------------------------------------\n"
						#else:
							#os.system("cls&&echo.&&echo.")
							#print "\t Not Found !"
						#    pass
				except db.MySQLError, e:
					error_report(str(e))
					derror = str(e)
					#print str(e)
				"""
				if len(columns) > 0 and columns_type != 'datetime':
					
					sql003 = "select " + columns + " from " + table_name + " where " + columns + " like '%" + dsearch + "%'"
					cursor3.execute(sql003)
					result003 = cursor3.fetchall()
					for datas in result003:
						fields = datas[0]
						print "\tDatabase Name = ", database
						print "\tTable Name    = ", table_name
						print "\tColumn Name   = ", columns, "\n" 
						print "\tResult Search = ", fields, "\n"
						print "\t-------------------------------------------------------\n"
				else:
					print "ERROR = ",  columns + "|" + columns_type
					
				#except:
					conn.rollback()
				"""
		conn.close() 			
		
	except IndexError, ex:
		print str(ex)
					
              
    #print "\n"
    #if (derror != Null):
	#	error_report(derror)
	
    