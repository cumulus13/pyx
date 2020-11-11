from __future__ import print_function
import sys
import os
import re

def _killall(process):
    if str(process).isdigit():
        #  d1 = os.popen('tasklist /FI "PID eq {0}"'.format(process.strip())).read()
        # print("dl =",d1)
        #  pid = re.findall("\d{4,9}", d1)
        #  name = re.findall("(.*?)\.exe", d1)
        # print("name =", name)
        #  if pid:
            #  pid = int(pid[0])
        #  if name:
            #  name = name[0] + ".exe"
        #  os.system("taskkill /f /im {0}".format(name))
        os.kill(int(process), int(process))
    else:
        os.system("taskkill /f /im {0}.exe".format(process))

def killall(process):
    
    if isinstance(process, list):
        for i in process:
            _killall(i)
    else:
        _killall(process)
        
        
if __name__ == '__main__':
    killall(*sys.argv[1:])
        