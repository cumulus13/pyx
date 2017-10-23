import Cservice
import os
import sys
import pywintypes
import module006
import dplay2
import e_console
import traceback

svc_name = "apache2.2"
apache = Cservice.WService("apache2.2")

def usage():
	print "\n"
	print "\t\tuse : " + os.path.split(sys.argv[0])[1] + " [start|stop|restart|status]"
	data = "use : " + os.path.split(sys.argv[0])[1] + " [start|stop|restart|status]"
	return data

def main1():
	try:
		if(len(sys.argv) > 1):
			if sys.argv[1] == 'start':
				print "\n"
				apache.start()
				dplay2.play(svc_name, 'Will be starter')
				print "\t Now Service Apache is " + module006.status(svc_name)
			elif sys.argv[1] == 'restart':
				print "\n"
				apache.restart()
				dplay2.play(svc_name, 'Will be restart')
				if module006.status(svc_name) == "START_PENDING":
					data_st_pre = str(module006.status(svc_name)).split("_")
					data_st = data_st_pre[0] + " " + data_st_pre[1]
				else:
					data_st = module006.status(svc_name)
				dplay2.play(svc_name, data_st)
				print "\t Now Service Apache is " + module006.status(svc_name)
			elif sys.argv[1] == 'stop':
				print "\n"
				apache.stop()
				dplay2.play(svc_name, 'Will be stop')
				if module006.status(svc_name) == "START_PENDING":
					data_st_pre = str(module006.status(svc_name)).split("_")
					data_st = data_st_pre[0] + " " + data_st_pre[1]
				else:
					data_st = module006.status(svc_name)
				dplay2.play(svc_name, data_st)
				print "\t Now Service Apache is " + module006.status(svc_name)
			elif sys.argv[1] == 'status':
				print "\n"
				if module006.status(svc_name) == "START_PENDING":
					data_st_pre = str(module006.status(svc_name)).split("_")
					data_st = data_st_pre[0] + " " + data_st_pre[1]
				else:
					data_st = module006.status(svc_name)
				dplay2.play(svc_name, data_st)
				print "\t Service Apache is " + module006.status(svc_name)
				#"\t Service Apache is " + module006.status(svc_name) < sys.stdout
			elif sys.argv[1] == 'status2':
				print "\n"
				st = os.popen("sc query apache2.2").readlines()
				dplay2.play(svc_name, str(st[3]).split(" ")[-2])
				print "\t Service Apache is " + str(st[3]).split(" ")[-2] + " [" + str(st[3]).split(" ")[-4] + "]"
		else:
			usage()
	except IndexError, e:
		usage()
	except pywintypes.error, e:
		datae01 = str(e).split(',')
		datae02 = datae01[2].split(" ")
		datae03 = datae02[-1].split(".")
		#print datae03
		if datae03[0] == "started":
			#print "\n"
			print "\t Your apache service not started ! "
		elif datae03[0] == "running":
			#print "\n"
			print "\t Your apache service has been started ! "
			
def main2():
	try:
		if(len(sys.argv) > 1):
			if sys.argv[1] == 'start':
				print "\n"
				apache.start()
				dplay2.play(svc_name, 'Will be starter')
				print "\t Now Service Apache is " + module006.status(svc_name)
			elif sys.argv[1] == 'restart':
				print "\n"
				apache.restart()
				dplay2.play(svc_name, 'Will be restart')
				if module006.status(svc_name) == "START_PENDING":
					data_st_pre = str(module006.status(svc_name)).split("_")
					data_st = data_st_pre[0] + " " + data_st_pre[1]
				else:
					data_st = module006.status(svc_name)
				dplay2.play(svc_name, data_st)
				print "\t Now Service Apache is " + module006.status(svc_name)
			elif sys.argv[1] == 'stop':
				print "\n"
				apache.stop()
				dplay2.play(svc_name, 'Will be stop')
				if module006.status(svc_name) == "START_PENDING":
					data_st_pre = str(module006.status(svc_name)).split("_")
					data_st = data_st_pre[0] + " " + data_st_pre[1]
				else:
					data_st = module006.status(svc_name)
				dplay2.play(svc_name, data_st)
				print "\t Now Service Apache is " + module006.status(svc_name)
			elif sys.argv[1] == 'status':
				print "\n"
				if module006.status(svc_name) == "START_PENDING":
					data_st_pre = str(module006.status(svc_name)).split("_")
					data_st = data_st_pre[0] + " " + data_st_pre[1]
				else:
					data_st = module006.status(svc_name)
				dplay2.play(svc_name, data_st)
				print "\t Service Apache is " + module006.status(svc_name)
				#"\t Service Apache is " + module006.status(svc_name) < sys.stdout
			elif sys.argv[1] == 'status2':
				print "\n"
				st = os.popen("sc query apache2.2").readlines()
				dplay2.play(svc_name, str(st[3]).split(" ")[-2])
				print "\t Service Apache is " + str(st[3]).split(" ")[-2] + " [" + str(st[3]).split(" ")[-4] + "]"
			else:
				data_usage = usage()
				dinfo = e_console.main("info", data_usage)
		else:
			data_usage = usage()
			dinfo = e_console.main("info", data_usage)
	except IndexError, e:
		data_usage = usage()
		data_error = traceback.format_exc()
		e_console.main("info", data_error + "\n" + data_usage)
	except pywintypes.error, e:
		datae01 = str(e).split(',')
		datae02 = datae01[2].split(" ")
		datae03 = datae02[-1].split(".")
		#print datae03
		if datae03[0] == "started":
			#print "\n"
			print "\t Your apache service not started ! "
			dplay2.play("apache2.2", 'service not started !')
			data_error = traceback.format_exc()
			e_console.main("error", data_error + "\n" + "Your apache service not started ! ")
		elif datae03[0] == "running":
			#print "\n"
			print "\t Your apache service has been started ! "
			dplay2.play("apache2.2", 'service has been started !')
			data_error = traceback.format_exc()
			e_console.main("error", data_error + "\n" + "Your apache service has been started ! ")
			
if __name__ == '__main__':
	if os.path.splitext(sys.argv[0])[1] == ".pyw":
		main2()
	elif os.path.splitext(sys.argv[0])[1] == ".py":
		main()
	else:
		print "\t This not program executeable ! \n"