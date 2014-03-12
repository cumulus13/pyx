import os
import sys
import module002
import module003
import cekrun
import Cservice
import pywintypes
import array
import dplay2

filename = os.path.split(sys.argv[0])
usage = """use : """ + filename[1] + """ [ kill | help | |gui | config ]"""
usage2 = """use : """ + filename[1] + """ [ start | stop | restart | status | kill | help | |gui | config ]"""

def main(data):
	try:
		if (len(sys.argv) > 1):
			if(sys.argv[1] == 'kill' or 'stop'):
				if len(data) > 1:
					for i in range(0, len(data)):
						data_app2 = os.path.split(data[i])	
						os.system("taskkill /f /im " + data_app2[1])
				else:
					data_app = os.path.split(data[0])
					os.system("taskkill /f /im " + data_app[1])
					
			elif(sys.argv[1] == 'help'):
				print "\n"
				print "\t", usage
			else:
				print "\n"
				print "\t", usage
		else:
			for i in range(0, len(data)):
				module002.main(data[i])
	except IndexError, e:
		print "\n"
		print "\t", usage
		
def services(data):
	try:
		if(len(sys.argv) > 1):
			if(sys.argv[1] == "stop"):
				for i in range (0,10):
					try:
						Cservice.WService(data[i]).stop()
						print "\n"
						data_status = Cservice.WService(data[i]).status()
						dplay2.play(data[i], data_status)
						print "\t Service " + data[i] + " is " + data_status
					except pywintypes.error, e:
						pass
			elif(sys.argv[1] == "start"):
				for i in range (0, 10):
					try:
						Cservice.WService(data[i]).start()
						print "\n"
						data_status = Cservice.WService(data[i]).status()
						dplay2.play(data[i], data_status)
						print "\t Service " + data[i] + " is " + data_status
					except pywintypes.error, e:
						pass
			elif(sys.argv[1] == "restart"):
				for i in range (0, 10):
					try:
						Cservice.WService(data[i]).restart
						print "\n"
						data_status = Cservice.WService(data[i]).status()
						dplay2.play(data[i], data_status)
						print "\t Service " + data[i] + " is " + data_status
					except pywintypes.error, e:
						pass
			elif(sys.argv[1] == "status"):
				for i in range (0, 10):
					print "\n"
					data_status = Cservice.WService(data[i]).status()
					dplay2.play(data[i], data_status)
					print "\t Service " + data[i] + " is " + data_status
			else:
				print "\n"
				print "\t" + usage2
		else:
			print "\n"
			print "\t" + usage2
					
	except IndexError, e:
		print "\n\n"
		pass
		#print "\t ERROR = ", str(e)
		
def services2(data, svc):
	try:
		if(len(sys.argv) > 1):
			if(sys.argv[1] == "stop"):
				#for x in range (0,10):
				#	#try:
				#	appname = os.path.split(data[x])[1]
				#	os.system("taskkill /f /im " + str(appname))
				#	print "\n"
				#	print "\t Program " + data[x] + " is killed ! \n"
					#except pywintypes.error, e:
					#	pass
				for i in range (0, len(svc)):
					try:
						Cservice.WService(svc[i]).stop()
						
						print "\n"
						data_status = Cservice.WService(svc[i]).status()
						dplay2.play(svc[i], data_status)
						print "\t Service " + svc[i] + " is " + data_status
					except pywintypes.error, e:
						
						for x in range (0, len(svc)):
							try:
								Cservice.WService(svc[x]).stop()
							except pywintypes.error, e:
								pass
							print "\n"
							data_status = Cservice.WService(svc[i]).status()
							dplay2.play(svc[x], data_status)
							print "\t Service " + svc[x] + " is " + data_status
							
					print "\n"
					appname = os.path.split(data[i])[1]
					os.system("taskkill /f /im " + str(appname))
					dplay2.dplay2(appname, " is killed !")
					print "\n"
					print "\t Program " + appname.split(".exe")[0] + " is killed !"
					
					#except pywintypes.error, e:
					#	pass
			elif(sys.argv[1] == "start"):
				#for x in range (0,10):
				#	#try:
				#	appname = os.path.split(data[x])[1]
				#	os.system(data[x])
				#	print "\n"
				#	print "\t Program " + data[x] + " has been started ! \n"
					#except pywintypes.error, e:
					#	pass
				for i in range (0, len(svc)):
					try:
						Cservice.WService(svc[i]).start()
						print "\n"
						data_status = Cservice.WService(svc[i]).status()
						dplay2.play(data[i], data_status)
						print "\t Service " + data[i] + " is " + data_status
						appname = os.path.split(data[i])[1]
						os.system(data[x])
						dplay2.dplay2(data[i], " has been started !")
						print "\n"
						print "\t Program " + data[i] + " has been started ! \n"
					except pywintypes.error, e:
						pass
					
			elif(sys.argv[1] == "status"):
				
				for i in range (0, len(svc)):
					print "\n"
					data_status = Cservice.WService(svc[i]).status()
					dplay2.play(svc[i], data_status)
					print "\t Service " + svc[i] + " is " + data_status
					appname = os.path.split(data[i])[1]			
					cekrun.cek2(appname.split(".exe")[0])
					
					
				#for
					#try:
					#appname = os.path.split(data[x])[1]
					#cekrun.cek2(appname.split(".exe")[0])
					#print "\n"
					#print "\t Program " + data[x] + " has been started ! \n"
				
			else:
				print "\n"
				print "\t" + usage2
		else:
			print "\n"
			print "\t" + usage2
					
	except IndexError, e:
		print "\n\n"
		pass
		#print "\t ERROR = ", str(e)
	except pywintypes.error, e:
		print "\n"
		print "\t ERROR = ", str(e)
		for i in range (0, len(svc)):
			print "\n"
			data_status = Cservice.WService(svc[i]).status()
			dplay2.play(svc[i], data_status)
			print "\t Service " + svc[i] + " has been " + data_status

def services3(data):
	try:
		if(len(sys.argv) > 1):
			if(sys.argv[1] == "stop"):
				for i in range (0,10):
					try:
						os.system("sc stop " + data[i])
						print "\n"
						data_status = os.system("sc query " + data[i])
						dplay2.play(data[i], data_status)
						print "\t Service " + data[i] + " is " + data_status
					except pywintypes.error, e:
						pass
			elif(sys.argv[1] == "start"):
				for i in range (0, 10):
					try:
						os.system("sc start " + data[i])
						print "\n"
						data_status = os.system("sc query " + data[i])
						dplay2.play(data[i], data_status)
						print "\t Service " + data[i] + " is " + data_status
					except pywintypes.error, e:
						pass
			elif(sys.argv[1] == "restart"):
				for i in range (0, 10):
					try:
						Cservice.WService(data[i]).restart
						print "\n"
						data_status = Cservice.WService(data[i]).status()
						dplay2.play(data[i], data_status)
						print "\t Service " + data[i] + " is " + data_status
					except pywintypes.error, e:
						pass
			elif(sys.argv[1] == "status"):
				for i in range (0, 10):
					print "\n"
					data_status = os.system("sc query " + data[i])
					dplay2.play(data[i], data_status)
					print "\t Service " + data[i] + " is " + data_status
			else:
				print "\n"
				print "\t" + usage2
		else:
			print "\n"
			print "\t" + usage2
					
	except IndexError, e:
		print "\n\n"
		pass
		#print "\t ERROR = ", str(e)

def services4(data, svc):
	try:
		if(len(sys.argv) > 1):
			if(sys.argv[1] == "stop"):
				for i in range (0, len(svc)):
					try:
						os.system("sc stop " + svc[i])
						
						print "\n"
						data_status = os.system("sc query " + svc[i])
						dplay2.play(svc[i], data_status)
						print "\t Service " + svc[i] + " is " + data_status
					except pywintypes.error, e:
						
						for x in range (0, len(svc)):
							try:
								os.system("sc stop " + svc[x])
							except pywintypes.error, e:
								pass
							print "\n"
							data_status = os.system("sc query " + svc[x])
							dplay2.play(svc[x], data_status)
							print "\t Service " + svc[x] + " is " + data_status
							
					print "\n"
					appname = os.path.split(data[i])[1]
					os.system("taskkill /f /im " + str(appname))
					dplay2.dplay2(appname, " is killed !")
					print "\n"
					print "\t Program " + appname.split(".exe")[0] + " is killed !"
					
			elif(sys.argv[1] == "start"):
				for i in range (0, len(svc)):
					try:
						os.system("sc start " + svc[i])
						print "\n"
						data_status = os.system("sc query " + svc[i])
						dplay2.play(svc[i], data_status)
						print "\t Service " + svc[i] + " is " + data_status
						appname = os.path.split(data[i])[1]
						os.system(data[x])
						dplay2.dplay2(data[i], " has been started !")
						print "\n"
						print "\t Program " + data[i] + " has been started ! \n"
					except pywintypes.error, e:
						pass
					
			elif(sys.argv[1] == "status"):
				
				for i in range (0, len(svc)):
					print "\n"
					data_status = os.system("sc query " + svc[i])
					dplay2.play(svc[i], data_status)
					print "\t Service " + svc[i] + " is " + data_status
					appname = os.path.split(data[i])[1]			
					cekrun.cek2(appname.split(".exe")[0])
				
			else:
				print "\n"
				print "\t" + usage2
		else:
			print "\n"
			print "\t" + usage2
					
	except IndexError, e:
		print "\n\n"
		pass
	except pywintypes.error, e:
		print "\n"
		print "\t ERROR = ", str(e)
		for i in range (0, len(svc)):
			print "\n"
			data_status = os.system("sc query " + svc[i])
			dplay2.play(svc[i], data_status)
			print "\t Service " + svc[i] + " has been " + data_status
		
		
def main2(data,service):
	data_app = os.path.split(data)
	try:
		if (len(sys.argv) > 1):
			if(sys.argv[1] == 'kill'):
				os.system("taskkill /f /im " + data_app[1])
				module003.stop(service)
			elif(sys.argv[1] == 'help'):
				print "\n"
				print "\t", usage2
			elif(sys.argv[1] == "start" or "stop" or "restart" or "status"):
				if(sys.argv[1] == "restart"):
					os.system("taskkill /f /im " + data_app[1])
					module003.main(service)
				elif(sys.argv[1] == "start"):
					module002.main(data)
					module003.main(service)
				elif(sys.argv[1] == "stop"):
					os.system("taskkill /f /im " + data_app[1])
					module003.main(service)
				elif(sys.argv[1] == "status"):
					module003.main(service)
					cekrun.cek2(data_app[1].split(".exe")[0])
				else:
					pass
			else:
				print "\n"
				print "\t", usage2
		else:
			module003.start(service)
			module002.main(data)
	except IndexError, e:
		print "\n"
		print "\t", usage2
		
if __name__ == '__main__':
	try:
		main(sys.argv[1])
	except IndexError, e:
		pass
		