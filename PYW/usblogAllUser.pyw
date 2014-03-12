import os
import sys
import MySQLdb
import datetime
import dateutil
import time

msgx = ""

conn = MySQLdb.connect("localhost", "root", "blackid", "usblog")

cursor = conn.cursor()

filename = r"C:\Documents and Settings\All Users\Application Data\USBSRService\USBSRService.log.txt"

if (os.path.isfile(filename) == True):

    data = open(filename, "r").readlines()
    lendata = len(data)
    
    for i in range(0, lendata):
        data001 = data[i].split("\n")
        
        try:
            data002 = data001[0].split("   ")
            
            ecpt01 = "'" 
            ecpt02 = "\\"
            if (ecpt01 in data002[1]):
                datax = str(data002[1]).replace(str(ecpt01), str("\\'"))
                msg = datax
                
            elif (ecpt02 in data002[1]):
                datax = str(data002[1]).replace(str(ecpt02), str("\\\\"))
                msg = datax
                
            else:
                msg  =  data002[1]
                
        except IndexError, e:
            msg = " - "
            
        ##print "message = ", msg
        
        try:
            data003 = data002[0].split(" ")
            if data003[0] != "":
                data003a = data003[0].split(".")
                acDate = data003a[2] + "-" + data003a[1] + "-" + data003a[0]
                ##print acDate
            else:
                acDate = "0000-00-00"
        except IndexError, e:
            msg = data[i]
            #pass
                
        ##print acDate
        
        try:
            if (data003[1] != ""):
                data004 = data003[1].split(":")
                acTime = data004[0] + ":" + data004[1] + ":" + data004[2]
                acSecond = data004[3]
                ##print data004
            else:
                acTime = "00:00:00"
                acSecond = "00"
                
        except IndexError, e:
            pass
            
        acTimeDate = acDate + " " + acTime
            
        ##print "acTime = " + acTime + " & " + "acSecond = " + acSecond
            
        try:
            sql = """INSERT INTO datalog(accessTime, accessSecond, message) values('""" + acTimeDate + "', '" + acSecond + "', '" + msg + """')"""
            #print sql
            cursor.execute(sql)
            conn.commit()
            
            datadiff = open(r"C:\temp\USBSRService.log.txt.bck", "w")
            data_cnt = str(data003) + " " + str(msg) + "\n"
            datadiff.write(data_cnt)
            ##print data_cnt
        except MySQLdb.MySQLError, e:
            conn.rollback()
            os.system("""SyslogGen -q -t:192.168.128.1 -p:516 -f:14 -s:6 -m:"FOUND : """ + str(filename) + """, But MySQL Error !, System Exit""")
            os.system("""SyslogGen -q -t:192.168.128.1 -p:523 -f:0 -s:6 -m:"FOUND : """ + str(filename) + """, But MySQL Error !, System Exit""")
            #sys.exit()
        
    
    
else:
    #os.system("cls")
    #print "\n"
    os.system("""SyslogGen -q -t:192.168.128.1 -p:516 -f:14 -s:6 -m:"File """ + str(filename) + """ Not Found ! """)
    os.system("""SyslogGen -q -t:192.168.128.1 -p:523 -f:0 -s:6 -m:"File """ + str(filename) + """ Not Found ! """)
    sys.exit()
    
    
    
#os.system("cls")
#print "\n"
os.system("""SyslogGen -q -t:192.168.128.1 -p:516 -f:14 -s:6 -m:"Found File """ + str(filename) + """ and Successfull Generate ! """)
os.system("""SyslogGen -q -t:192.168.128.1 -p:523 -f:0 -s:6 -m:"Found File """ + str(filename) + """ and Successfull Generate ! """)
datadiff.close()
conn.close()

os.system("d:\pyx\delusballuser.bat")

#data_date = datetime.date.today()
#data_date_fn = str(data_date).replace("-",":")

#datatime = time.ctime()
#datatime_fn = datatime.split(" ")

#dataup = open(r"c:\temp\amt.log", "w")
#dataup.write(str(data_date) + " " + str(datatime_fn) + " " + "[5200]" + " " + "File Succesfull Clean Update ! \n" )
    
