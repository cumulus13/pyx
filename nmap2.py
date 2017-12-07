import os
import datetime
import sys
import re

LOGPATH = r'f:\LOGCENTER\NMAP'

if not os.path.isdir(LOGPATH):
    os.makedirs(LOGPATH)
mydate = datetime.datetime.strftime(datetime.datetime.now(), '%d.%m.%y.%H.%M.%S')
def nmap():
    if len(sys.argv) > 1:
        ARGS = " ".join(sys.argv[1:])
        IP = re.findall('[0-9]+(?:\.[0-9]+){3}', ARGS)[0]        
        os.system('start cmd /k "mode 100,54 & mo BL=3000 & cls & "' + r'c:\PROGRA~1\Nmap\nmap.exe' + ' -oN %s ' % (os.path.join(LOGPATH, IP + "-" + mydate + ".log")) + " ".join(sys.argv[1:]))
    else:
        os.system(r'c:\PROGRA~1\Nmap\nmap.exe -h')

nmap()
