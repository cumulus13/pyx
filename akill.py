import os
import sys
import subprocess
import time
import cmdw
MAX = cmdw.getWidth()

def akill1(proc):
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

def akill2(process, sleep=300):
	import psutil
	try:
		while 1:
			for i in psutil.process_iter():
				#  print("name =", i.name(), "pid =", i.pid)
				if isinstance(process, list):
					for p in process:
						if p.lower() in i.name().lower():
							print("NAME: ", i.name())
							print("PID : ", i.pid)
							os.kill(i.pid, i.pid)
				else:
					if process.lower() in i.name().lower():
						print("NAME: ", i.name())
						print("PID : ", i.pid)
						os.kill(i.pid, i.pid)
			time.sleep(sleep)
						
	except:
		pass
	
akill2(sys.argv[1:])