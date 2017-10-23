#import ceksvc
#import  win32service

#svc = win32service.ChangeServiceConfig(

#import sys
#sys.stdout.write("HELLO")
import os
import termcolor
import subprocess
proc = subprocess.Popen(["git"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
print proc.poll()
print "program output:", termcolor.colored(out, 'red')
