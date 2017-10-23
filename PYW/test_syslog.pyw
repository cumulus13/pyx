import syslog
import sys


syslog.syslog('this is test error syslog don\'t worry be  happy !', int(sys.argv[2]), int(sys.argv[1]), 'localhost', int(sys.argv[3]))
