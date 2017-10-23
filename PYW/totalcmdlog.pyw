import os
import sys
import MySQLdb
import datetime
import syslog
import time

conn = MySQLdb.connect("localhost", "root", "blackid", "totalcmd")

cursor = conn.cursor()

filename = r"c:\TEMP\totalcmd.log"

if (os.path.isfile(filename) == True):

    data = open(filename, "r").readlines()
    lendata = len(data)
    #print "lendata = " + str(lendata)

    if (lendata > 0):
        for i in range(0, lendata):
            data001 = data[i].split("\n")
            data002 = data001[0].split(": ")

            ddate001 = data002[0] #Riset DATA DATE TIME
            #print "ddate001 = " + ddate001 + "\n"
            ddate002 = ddate001.split(" ")
            #print "ddate002 = " + str(ddate002) + "\n"
            dTime = ddate002[1] #FIX Data TIME
            #print "dTime = " + dTime + "\n"

            decpt = '/'
            if (decpt in ddate002[0]):

                ddate003 = ddate002[0].split("/") #FIX Data Date
                #ddate004 = str(ddate002[0]).replace(decpt, "-")
                #print "ddate003 = ", str(ddate003) + "\n"
                ddate004 =  ddate003[0]
                #print ddate004[-1], "\n"
                #print ddate004[-2], "\n"

                accessDateTime = ddate003[2] + "-" + ddate004[-2] + ddate004[-1] + "-" + ddate003[1] + " " + dTime
                #print 'accessDateTime = ' + accessDateTime  + "\n"

            else:
                accessDateTime = "0000-00-00"

            #acctionDate = dDate  + " " + dTime
            #print acctionDate, "\n"

            #daction001 = data002[2]
            #print data002[1]
            try:
                dAction = data002[1] #FIX Data Action
            except IndexError, e:
                dAction = " - "

            #Test Data Len
            #datalena = len(data002)
            #if (datalena < 3):
            #    print str(i) + ". " + "\t\t ERROR !" + " Datale = " + str(datalena)
            #else:
            #    print "DATALEN = ", datalena
            #End Test Data Len

            try:

                ecpt01 = "'" 
                ecpt02 = "\\"
                if (ecpt01 in data002[2]):
                    datax = str(data002[2]).replace(str(ecpt01), str("\\'"))
                    dMsg = datax
                    #print dMsg
                elif (ecpt02 in data002[2]):
                    datax = str(data002[2]).replace(str(ecpt02), str("\\\\"))
                    dMsg = datax
                    #print dMsg + "\t\t\t\tWith ERROR"
                else:
                    dMsg = data002[2]
            except IndexError, e:
                dMsg = data002[1]
                dAction = " - "

            except KeyboardInterrupt, e:
                #os.system("cls")
                #print "\n"
                #print "\t Porcess Canceled ! "
                sys.exit()


            try:
                sql = """INSERT INTO datalog(accessTimeDate, actionMsg, description) values('""" + accessDateTime + "', '" + dAction + "', '" + dMsg + """')"""
                #print sql
                cursor.execute(sql)
                conn.commit()

                #datadiff = open(r"c:\temp\amtdiff.log", "w")
                #data_cnt = acTimeDate + " " + data_code + " " + msg + "\n"
                #datadiff.write(data_cnt)
                #print data_cnt
            except MySQLdb.MySQLError, e:
                conn.rollback()
                syslog.syslog("TotalCmdLog : FOUND : File " +  " , But MySQL Error !, System Exit\"",6,1,'localhost',516)
                sys.exit()

        syslog.syslog("TotalCmdLog : Found File " + str(filename) + " and Successfull Generate ! \"",6,1,'localhost',516)

    else:
        #msgerr01 = "TotalCmdLog : File " + str(filename) + " Not containt data ! "
        #print msgerr01
        #syslog.syslog(msgerr01,6,1,'localhost',516)
        sys.exit()
else:
    #os.system("cls")  
    syslog.syslog("TotalCmdLog : File " +  " Not Found ! \"",6,1,'localhost',516)
    sys.exit()



#os.system("cls")
#print "\n"
#datadiff.close()
conn.close()


#data_date = datetime.date.today()
#data_date_fn = str(data_date).replace("-",":")

#datatime = time.ctime()
#datatime_fn = datatime.split(" ")
dataup = open(filename, "w")
dataup.write("")
dataup.close()

