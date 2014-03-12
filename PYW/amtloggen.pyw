import os
import sys
import MySQLdb
import datetime
import dateutil
import time

conn = MySQLdb.connect("localhost", "root", "blackid", "amtlog")

cursor = conn.cursor()

filename = r"c:\temp\amt.log"

if (os.path.isfile(filename) == True):

    data = open(r"c:\temp\amt.log", "r").readlines()
    lendata = len(data)
    
    if (lendata > 1):
    
        for i in range(0, lendata):
            data001 = data[i].split("\n")
            data002 = data001[0].split("]  ")
            data003 = data002[0].split(" ")
            try:
                ecpt01 = "'" 
                ecpt02 = "\\"
                if (ecpt01 in data002[1]):
                    datax = str(data002[1]).replace(str(ecpt01), str("\\'"))
                    msg = datax
                    #print "Datax = ", datax
                elif (ecpt02 in data002[1]):
                    datax = str(data002[1]).replace(str(ecpt02), str("\\\\"))
                    msg = datax
                    #print "Datax = ", datax
                else:
                    msg  =  data002[1]
            except IndexError, e:
                pass
                
            try:
                acTimeDate = data003[0] + " " + data003[1]
                #print acTimeDate
            except IndexError, e:
                pass
                
            try:
                data004 = data003[2].split("[")
                #print data004[0]
                data_code = data004[1]
                #print data_code
               
                
                sql = """INSERT INTO datalog(accessTime, code, message) values('""" + acTimeDate + "', '" + data_code + "', '" + msg + """')"""
                print sql
                cursor.execute(sql)
                conn.commit()
                
                    
                #data_cnt = acTimeDate + " " + data_code + " " + msg + "\n"
                #datadiff.write(data_cnt)
                #print data_cnt
            
            except IndexError, e:
                os.system("""sysloggen -q -t:192.168.128.1 -p:516 -f:14 -s:6 -m:"ERROR: amt.log, in Line """ + str(data[i]))
                
            except MySQLdb.MySQLError, e:
                conn.rollback()
                os.system("""sysloggen -q -t:192.168.128.1 -p:516 -f:14 -s:6 -m:"FOUND : amt.log, But MySQL Error !, System Exit""")
                os.system("""sysloggen -q -t:192.168.128.1 -p:523 -f:14 -s:6 -m:"FOUND : amt.log, But MySQL Error !, System Exit""")
                #sys.exit()
        
    else:
        os.system("""sysloggen -q -t:192.168.128.1 -p:516 -f:14 -s:6 -m:"ERROR: File amt.log, is NO DATA """)
        sys.exit()
            
else:
    os.system("cls")
    print "\n"
    os.system("""sysloggen -q -t:192.168.128.1 -p:516 -f:14 -s:6 -m:"File amt.log Not Found ! """)
    os.system("""sysloggen -q -t:192.168.128.1 -p:523 -f:14 -s:6 -m:"File amt.log Not Found ! """)
    sys.exit()
    
    
    
#os.system("cls")
#print "\n"
os.system("""sysloggen -q -t:192.168.128.1 -p:516 -f:14 -s:6 -m:"Found File amt.log Successfull Generate ! """)
os.system("""sysloggen -q -t:192.168.128.1 -p:523 -f:14 -s:6 -m:"Found File amt.log Successfull Generate ! """)

conn.close()

datadiff = open(r"c:\temp\amt.log", "w")
datadiff.write(" ")
datadiff.close()

#data_date = datetime.date.today()
#data_date_fn = str(data_date).replace("-",":")

#datatime = time.ctime()
#datatime_fn = datatime.split(" ")

#dataup = open(r"c:\temp\amt.log", "w")
#dataup.write(str(data_date) + " " + str(datatime_fn) + " " + "[5200]" + " " + "File Succesfull Clean Update ! \n" )
    
