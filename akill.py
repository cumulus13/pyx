import os
import sys
import subprocess
import time
import cmdw
MAX = cmdw.getWidth()

def akill(proc):
	a = subprocess.Popen(['px','-k', proc], stdout=subprocess.PIPE, shell=True)
	(out, err) = a.communicate()
	#print "out =", out
	#print "err =", err
	n = 1
	while 1:
		if 'Access is denied' in out:
			a = subprocess.Popen(['px','-k', proc], stdout=subprocess.PIPE, shell=True)
			(out, err) = a.communicate()
			sys.stdout.write(".")
			time.sleep(0.5)
			n += 1
			if n == MAX:
				break
		else:
			break
	
	
akill(sys.argv[1])