import os
import sys
import MySQLdb
import datetime
import syslog
import time

try:
    msgx = ""
    
    conn = MySQLdb.connect("localhost", "root", "blackid", "usblog")
    
    cursor = conn.cursor()
    
    filename = r"C:\Documents and Settings\Administrator\Application Data\USBSafelyRemove\USBSafelyRemove.log.txt"
    #filename = r"C:\Documents and Settings\Administrator\Application Data\USBSafelyRemove\USBSafelyRemove.log_test.txt"
    
    if (os.path.isfile(filename) == True):
    
        data = open(filename, "r").readlines()
        lendata = len(data)
        
        for i in range(0, lendata):
            data001 = data[i].split("\n")
            
            try:
                data002 = data001[0].split("   ")
                #print "data002 = " + str(data002) + "\n"
                
                ecpt00 = "\'s"
                ecpt01 = "\\'" 
                ecpt02 = "\\"
                ecpt03 = "\\xa"
                ecpt04 = "\',"
                
                if (ecpt04 in data002[1]):
                    datax = str(data002[1]).replace(str(ecpt04), str("\\',"))
                    msg = datax
                
                elif (ecpt00 in data002[1]):
                    datax = str(data002[1]).replace(str(ecpt00), str("\\'s"))
                    msg = datax
                
                elif (ecpt01 in data002[1]):
                    datax = str(data002[1]).replace(str(ecpt01), str("\\\'"))
                    msg = datax
                    
                elif (ecpt02 in data002[1]):
                    datax = str(data002[1]).replace(str(ecpt02), str("\\\\"))
                    msg = datax
                    
                elif (ecpt03 in data002[1]):
                    datax = str(data002[1]).replace(str(ecpt03), str(""))
                    msg = datax
                     
                else:
                    msg  =  data002[1]
                    
            except IndexError, e:
                msg = " - "
                
            #print "message = ", msg + "\n"
            
            try:
                data003 = data002[0].split(" ")
                if data003[0] != "":
                    data003a = data003[0].split(".")
                    acDate = data003a[2] + "-" + data003a[1] + "-" + data003a[0]
                    #print "acdate = " + acDate + "\n"
                else:
                    acDate = "0000-00-00"
            except IndexError, e:
                msg = data[i]
                #pass
                    
            #print acDate
            
            try:
                if (data003[1] != ""):
                    data004 = data003[1].split(":")
                    acTime = data004[0] + ":" + data004[1] + ":" + data004[2]
                    acSecond = data004[3]
                    #print data004
                else:
                    acTime = "00:00:00"
                    acSecond = "00"
                    
            except IndexError, e:
                pass
                
            acTimeDate = acDate + " " + acTime
                
            #print "acTime = " + acTime + " & " + "acSecond = " + acSecond
                
            sql = """INSERT INTO log_adm(accessTime, accessSecond, message) values('""" + acTimeDate + "', '" + acSecond + "', '" + msg + """')"""
            #print sql
            #os.system("cls")
            #print "\n\t Please wait ", "." * i
            cursor.execute(sql)
            
    else:
        #os.system("cls")
        #print "\n"
        syslog.syslog("Usblog:Admin = file " + str(filename) + " Not Found ! \n", 1, 3, "localhost", 516)
        sys.exit()
        
        
        
    #os.system("cls")
    #print "\n"
    syslog.syslog("Usblog:Admin = Successfull generate ! \n", 6, 3, "localhost", 516)
    conn.commit()
    conn.close()
    
    #os.system("d:\pyx\delusbadm.bat")
    
    datadate = datetime.date.today()
    datatime_pre = time.ctime()
    datatime = datatime_pre.split(" ")
    
    datatime_fn = str(datadate) + " " + str(datatime[3])
    
    dataup = open(r"C:\Documents and Settings\Administrator\Application Data\USBSafelyRemove\USBSafelyRemove.log_test.txt", "w")
    dataup.write(str(datatime_fn) + " " + "File Succesfull Clean Update ! \n" )
    dataup.close()
    
except conn.DatabaseError, e:
    if e[0] == 2005:
        print "\n"
        print "\t Error = Can't Connect to host '" + host + "' ! \n"
        conn.rollback()
        sys.exit()
    elif e[0] == 1045:
        print "\n"
        print "\t Error = Please cek youre username & password ! \n"
        conn.rollback()
        sys.exit()
    elif e[0] == 1049:
        print "\n"
        print "\t Error = Can't Found database '" + db + "' !\n"
        conn.rollback()
        sys.exit()
    elif e[0] == 1146:
        print "\n"
        print "\t Error = " + str(e[1])
        conn.rollback()
        sys.exit()
    elif e[0] == 1286:
        print "\n"
        print "\t Error = " + str(e[1])
        conn.rollback()
        sys.exit()
    elif e[0] == 1064:
        print "\n"
        print "\t Error = " + str(e[1])
        conn.rollback()
        sys.exit()
    else:
        print str(e)
        conn.rollback()
        sys.exit()
        
except conn.DataError, e:
    print "\t Error = " + str(e)
    conn.rollback()
    sys.exit()

    
    
