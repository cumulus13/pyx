import datetime
import time
import os
import sys

data = time.gmtime()
data2 = time.ctime()
data3 = data2.split(" ")
data5 = str(data[7])

#print data, "\n"
#print data3, "\n"
datenow = data3[2] + "." + data3[1] + "." + data3[4] + "_" \
        + str(data5[0]) + str(data5[1]) + "." + str(data[4]) \
        + "." + str(data[5])

#print datenow
#print data5[0] + data5[1]
try:
    os.system("mkdir D:\\xampp\\apache\\conf\\extra\\BACKUPCONF\\" + datenow)
    os.system("mkdir D:\\xampp\\apache\\conf\\BACKUPCONF\\" + datenow)
    
    os.system("copy D:\\xampp\\apache\\conf\\httpd.conf " + "D:\\xampp\\apache\\conf\\BACKUPCONF\\" + datenow + "\\httpd(" + datenow + ").conf")
    os.system("copy D:\\xampp\\apache\\conf\\extra\\*.conf " + "D:\\xampp\\apache\\conf\\extra\\BACKUPCONF\\" + datenow + "\\*.(" + datenow + ").conf")
    os.system("cls && echo. && echo.")
    print "\t\t Backup Successfull ! \n"
    
except IOError, e:
    print e
    
except TypeError, e:
    print e
    
except SystemError, e:
    print e
    
except EOFError, e:
    print e
    
except IndentationError, e:
    print e
    
except KeyError, e:
    print e
    
except NotImplementedError, e:
    print e
    
except OSError, e:
    print e
    
except StandardError, e:
    print e
    
except SyntaxError, e:
    print e
    
except ValueError, e:
    print e
    
except WindowsError, e:
    print e
    
except ZeroDivisionError, e:
    print e

