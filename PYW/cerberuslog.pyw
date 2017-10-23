import os
import sys
import MySQLdb
import datetime
import dateutil
import time

conn = MySQLdb.connect("localhost", "root", "blackid", "cerberuslog")

cursor = conn.cursor()

filename = r"C:\Program Files\Cerberus\log\server.1.log"

if (os.path.isfile(filename) == True):

    data = open(filename, "r").readlines()
    lendata = len(data)
    
    if (lendata < 1):
        os.system("sysloggen -t:192.168.128.1 -p:516 -f:1 -s:1 -m:\"File Not Present (creberusLog) ! \"")
        os.system("cls")
        sys.exit()
    else:
    
        for i in range(0, lendata):
            data001 = data[i].split("\n")
            #print data001[0]
            data002 = data001[0].split("]:")
            if (data002[0] == ''):  #This Like ['']
                pass
            else:
                data003 = data002[0].split(" ") #Data DATE Test
                #print data003
                try:
                    datamsg01 = data002[1] #Riset Message
                    datamsg02 = datamsg01.split(" - ")
                    
                    try:
                        ecpt01 = "'" 
                        ecpt02 = "\""
                        ecpt03 = "\\"
                        if (ecpt01 in datamsg02[1]):
                            datax = str(data002[1]).replace(str(ecpt01), str("\\'"))
                            msg = datax
                            #print "Datax = ", datax
                        elif (ecpt02 in datamsg02[1]):
                            datax = str(data002[1]).replace(str(ecpt02), str("\\\""))
                            msg = datax
                            #print "Datax = ", datax
                        elif (ecpt03 in datamsg02[1]):
                            datax = str(datamsg02[1]).replace(str(ecpt03), str("\\\\"))
                            msg = datax
                            #print "Datax = ", datax
                        else:
                            msg = datamsg02[1] # MEssage FIx
                    except IndexError, e:
                        pass
                    
                    
                    datacode01 = datamsg02[0]
                    datacode02 = datacode01.split("[")
                    actMsg = datacode02[0] #ActionMessage FIX
                    #print actMsg
                    datacode03 = datacode02[1].split("]")
                    #print datacode03
                    codeMsg = datacode03[0] #Code Message FIX
                    
                    
                    
                    datadate01 = data003[0].split("[") #Riset Date Time
                    
                    dateMsg = datadate01[1] #Data Date FIX
                    #print datadate01
                    #print data003[1]
                    timeMsg = data003[1] #Data Time FIX
                except IndexError, e:
                    dateMsg = "0000-00-00"
                    timeMsg = "00:00:00"
                    actMsg = " - "
                    codeMsg = " - "
                    msg = data[i]
            
            
            acTimeDate = dateMsg + " " + timeMsg
        
            try:
                sql = """INSERT INTO datalog(accessDateTime, actionMsg, severity, message) values('""" + acTimeDate + "', '" + actMsg + "', '" + codeMsg + "', '" + msg +  """')"""
                print str(i) + ". " + sql
                cursor.execute(sql)
                conn.commit()
                
            #    datadiff = open(r"c:\temp\amtdiff.log", "w")
            #    data_cnt = acTimeDate + " " + data_code + " " + msg + "\n"
                #datadiff.write(data_cnt)
                #print data_cnt
            except MySQLdb.MySQLError, e:
                conn.rollback()
                os.system("sysloggen -q -t:192.168.128.1 -p:516 -f:14 -s:6 -m:\"FOUND : ," + str(filename) + " But MySQL Error !, System Exit, Error in Line " + str(i) + "\"")
                os.system("sysloggen -q -t:192.168.128.1 -p:523 -f:0 -s:6 -m:\"FOUND : ," + str(filename) + " But MySQL Error !, System Exit, Error in Line " + str(i) + "\"")
                
                #sys.exit()
    
else:
    os.system("cls")
    print "\n"
    os.system("sysloggen -q -t:192.168.128.1 -p:516 -f:14 -s:6 -m:\"File " + str(filename) + " Not Found ! , Error in Line " + str(i) + "\"")
    os.system("sysloggen -q -t:192.168.128.1 -p:523 -f:0 -s:6 -m:\"File " + str(filename) + " Not Found ! , Error in Line " + str(i) + "\"")
    sys.exit()
    
    

os.system("sysloggen -q -t:192.168.128.1 -p:516 -f:14 -s:6 -m:\"Found File " + str(filename) + " & Successfull Generate ! \"")
os.system("sysloggen -q -t:192.168.128.1 -p:523 -f:0 -s:6 -m:\"Found File " + str(filename) + " & Successfull Generate ! \"")
os.system("cls")
print "\n"
print "\t\t Successfull Generate !"
#datadiff.close()
conn.close()


dataup = open(filename, "w")
dataup.write("")
dataup.close()
    
