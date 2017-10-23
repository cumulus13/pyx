import win32api
import os
import MySQLdb as DB
import datetime
import time

#os.system("cls")
#print "\n\n"

data = win32api.GlobalMemoryStatusEx()
mb = float(1024 * 1024 * 10)
mb2 = float(1024 * 1024)
gb = float(1024 * 1024 * 1024)

TotalPageFile = data['TotalPageFile']
AvailVirtual  = data['AvailVirtual'] 
MemoryLoad    = data['MemoryLoad']
MemoryFree    = 100 - MemoryLoad
TotalPhys     = data['TotalPhys']
AvailExtendedVirtual = data['AvailExtendedVirtual']
TotalVirtual  = data['TotalVirtual']
AvailPhys     = data['AvailPhys']
AvailPageFile = data['AvailPageFile']

data_TotalPageFile = "TotalPageFile        = %0.2f0 Mb" %(float(TotalPageFile) / mb)
data_AvailVirtual  = "AvailVirtual         = %0.2f0 Mb" %(float(AvailVirtual) / mb)
data_TotalPhys     = "TotalPhys            = %0.2f0 Gb" %(float(TotalPhys) / gb)
data_TotalVirtual  = "TotalVirtual         = %0.2f0 Mb" %(float(TotalVirtual) / mb)
data_AvailPhys     = "AvailPhys            = %0.2f0 Mb" %(float(AvailPhys) / mb2)
data_AvailPageFile = "AvailPageFile        = %0.2f0 Mb" %(float(AvailPageFile) / mb)

data_TotalPageFile2 = "%0.2f0" %(float(TotalPageFile) / mb) #Mb
data_AvailVirtual2  = "%0.2f0" %(float(AvailVirtual) / mb) #Mb
data_TotalPhys2     = "%0.2f0" %(float(TotalPhys) / gb) #Gb
data_TotalPhys3     = "%0.2f0" %(float(TotalPhys) / mb2) #Mb
data_TotalVirtual2  = "%0.2f0" %(float(TotalVirtual) / mb) #Mb
data_AvailPhys2     = "%0.2f0" %(float(AvailPhys) / mb2) #Mb
data_UsePhys2       = "%0.2f0" %((float(TotalPhys) /gb) - (float(AvailPhys) / gb))  #Gb
data_UsePhys3       = "%0.2f0" %((float(TotalPhys) /mb2) - (float(AvailPhys) / mb2))  #Mb
data_AvailPageFile2 = "%0.2f0" %(float(AvailPageFile) / mb)  #Mb
data_MemoryLoad = MemoryLoad #%
data_Memory_Free = MemoryFree #%

data_date001 = datetime.datetime.today()
data_date002 = str(data_date001)

try:
    data_date003 = data_date002.split(".")
    data_second = data_date003[1]          #FIX Data Second
except IndexError, e:
    data_second = "00000"
    
try:    
    data_date004 = data_date003[0].split(" ")
    data_date = data_date004[0]
except IndexError, e:
    data_date = "0000-00-00"
    
try:
    data_time = data_date004[1]
except IndexError, e:
    data_time = "00:00:00"
    
try:
    dataReport = data_date003[0]
except IndexError, e:
    dataReport = "000-00-00 00:00:00"

#print "\t TotalPhys = " + str(data_TotalPhys2) + "\n"
#print "\t AvailPhys = " + str(data_AvailPhys2) + "\n"
#print "\t UsePhys2 = " + str(data_UsePhys2)  + "\n"
#print "\t UsePhys3 = " + str(data_UsePhys3)  + "\n"
#print "\t TotalPageFile = " + str(data_TotalPageFile2) + "\n"
#print "\t AvailVirtual = " + str(data_AvailVirtual2) + "\n"
#print "\t TotalVirtual = " + str(data_TotalVirtual2) + "\n"
#print "\t AvailPageFile = " + str(data_AvailPageFile2) + "\n"
#print "\t MemoryLoad = " + str(data_MemoryLoad)  + "\n"
#print "\t Memory_Free = " + str(data_Memory_Free) + "\n"
#print "\t AvailExtendedVirtual = " + str(AvailExtendedVirtual) + "\n\n"

conn = DB.connect("localhost", "root", "blackid", "memory")

cursor = conn.cursor()

try:
    sql = """INSERT INTO datalog(TotalPageFile, AvailVirtual, TotalPhys1, TotalPhys2, TotalVirtual, AvailPhys, UsePhys1, UsePhys2, AvailPageFile, MemoryLoad, MemoryFree, AvailExtendedVirtual, datereport, datereportsecond) values('""" + str(data_TotalPageFile2) + "', '" + str(data_AvailVirtual2) + "', '" + str(data_TotalPhys2) +"', '" + str(data_TotalPhys3) + "', '" + str(data_TotalVirtual2) + "', '" + str(data_AvailPhys2) + "', '" + str(data_UsePhys2) + "', '" + str(data_UsePhys3) + "', '" + str(data_AvailPageFile2) + "', '" + str(data_MemoryLoad) + "', '" + str(data_Memory_Free) + "', '" + str(AvailExtendedVirtual) + "', '" + str(dataReport) + "', " + data_second + ")"

    #print sql

    cursor.execute(sql)
    conn.commit()
    #os.system("""sysloggen -q -t:192.168.128.1 -p:516 -f:0 -s:6 -m:"Memory Status Update """ + str(dataReport) + " " + str(data_second) + "\"")
    os.system("""sysloggen -q -t:192.168.128.1 -p:523 -f:0 -s:6 -m:"Memory Status Update """ + str(dataReport) + " " + str(data_second) + "\"")
except MySQLdb.MySQLError, e:
    conn.rollback()
    os.system("""sysloggen -q -t:192.168.128.1 -p:516 -f:0 -s:6 -m:"MySQL Error to Update Status Memory !" """)
    
conn.close()


