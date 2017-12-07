import os
import datetime
import sys
import re

LOGPATH = r'f:\LOGCENTER\WHOSIP'

if not os.path.isdir(LOGPATH):
    os.makedirs(LOGPATH)
mydate = datetime.datetime.strftime(datetime.datetime.now(), '%d.%m.%y.%H.%M.%S')
def whosip():
    if len(sys.argv) > 1:
        ARGS = " ".join(sys.argv[1:])
        # IP = re.findall('[0-9]+(?:\.[0-9]+){3}', ARGS)[0]        
        os.system(r'c:\exe\whosipx.exe' + ' -r %s > %s' % (sys.argv[1], os.path.join(LOGPATH, sys.argv[1] + "-" + mydate + ".log")))
        if os.path.isfile(os.path.join(LOGPATH, sys.argv[1] + "-" + mydate + ".log")):
        	print "\n"
        	print open(os.path.join(LOGPATH, sys.argv[1] + "-" + mydate + ".log")).read()
        else:
        	print "\n"
        	print "ERROR !"
    else:
        print "\n"
        print "usage: whosip [ip address]"

whosip()
