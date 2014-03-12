import os
import sys
import time

qc = os.popen("c:\Windows\System32\sc.exe qc" + " " + sys.argv[-1] + " & " + "c:\Windows\System32\sc.exe query" + " " + sys.argv[-1]).read()
query = os.popen("c:\Windows\System32\sc.exe query" + " " + sys.argv[-1]).readlines()
#qc = os.popen("c:\Windows\System32\sc.exe qc" + " " + sys.argv[2]).readlines()
#print "query =", query
#service_name =  str(query[1]).split("\n")[0].split(":")

#print service_name
status = query[3].split(":")[1].split("\n")[0]
status2 = query[3].split(":")[1].split("\n")[0].split(" ")[-2].strip()
#print status2

def status():
	print qc

def cek_status():
	if status2 == "RUNNING":
		return "RUNNING"
	else:
		return status2
		
def cek_running():
	if "RUNNING" in status:
		return True
	return False
		
def restart():
	if cek_status() == "STOPPED":
		os.system("sc start " + sys.argv[2])
		time.sleep(10)
	elif cek_status() == "RUNNING":
		os.system("sc stop " + sys.argv[2])
		time.sleep(10)
		os.system("sc start " + sys.argv[2])
	elif cek_status() == "START_PENDING":
		pass
	else:
		pass
			
def start():
	if cek_status == "RUNNING":
		print "\t Service Has been STARTED"
	else:
		if cek_status() == "STOPPED":
			print "please wait ..."
			os.system("sc start " + sys.argv[2])
			time.sleep(10)
			if cek_status == "RUNNING":
				print "\t Service STARTED"
			elif cek_status == "STOPPED":
				print "\t Service Error Starting, please re-Start again "
				sys.exit()
			else:
				print "\t Service is: ", cek_status()
			
def stop():
	if cek_status == "STOPPED":
		print "\t Service Has been STOPPED"
	else:
		while cek_status != "STOPPED":
			print "please wait ..."
			time.sleep(10)
			os.system("sc stop " + sys.argv[2])
		else:
			sys.exit()
	
def usage():
	print "\n"
	print "\t usage:",__file__," [start|stop|restart|status]"
	print "\n"	
	
def main():
	if sys.argv[1] == "start":
		start()
	elif sys.argv[1] == "stop":
		stop()
	elif sys.argv[1] == "restart":
		restart()
	elif sys.argv[1] == "status":
		status()
	else:
		usage()
		
if __name__ == "__main__":
	main()
		
