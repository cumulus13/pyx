import os
import sys
import win32com.client
import module002
try:
	import dplay
except:
	print '\t WARNING : Module \"dplay NOT FOUND, it will be pass ! \n'

username = os.getenv("USERNAME")
winver = int(sys.getwindowsversion()[0])

def pdata(desktop_name,data=None):
	if data == None:
		datad = os.popen("dir /b \"c:\documents and settings\\" + str(desktop_name) + "\desktop\*.lnk")
		return datad
	else:
		shell = win32com.client.Dispatch("WScript.Shell")
		if winver < 6:
			#print "winver 1 = ",winver
			datad = os.popen("dir /b \"c:\documents and settings\\" + str(desktop_name) + "\desktop\*.lnk")
			shortcut = shell.CreateShortcut(r"C:\Documents and Settings\\" + str(desktop_name) +  "\Desktop" + "\\" + data)
		elif winver > 5:
			#print "winver 2 = ",winver
			datad = os.popen("dir /b \"C:\Users\\" + str(os.getenv("username")) + "\desktop\*.lnk")
			shortcut = shell.CreateShortcut(r"C:\Users\\" + str(desktop_name) +  "\Desktop" + "\\" + data)
		else:
			print "\n"
			print "\tWhat Your Win Version ?\n"
		rdata = shortcut.Targetpath
		return [rdata,datad]

#import _winreg
#print "username + ", _winreg.expandenvironmentstrings(u"%username%")
#print "username ", os.path.basename(os.getenv("USERPROFILE"))
#print "get username = ", username

if username != None or username != '':
	if username != os.path.basename(os.getenv("USERPROFILE")):
		print '\n\tWho Are You ! \n'
		sys.exit()
	else:
		#data = os.popen("dir /b \"c:\documents and settings\\" + str(os.getenv("username")) + "\desktop\*.lnk")
		data = pdata(username)
		#print "DATA = ", data.readlines()
else:
	print '\n\tUsername Not Detection ! \n'
	sys.exit()

#print "DATA = ", data
if winver < 6:
	datax = os.popen("dir /b \"c:\Documents and Settings\All Users\Desktop\*.lnk")
elif winver > 5:
	datax = os.popen("dir /b \"c:\Users\Public\Desktop\*.lnk")
data_r = data.readlines()
datax_r = datax.readlines()
#print "datax_r = ",datax_r
os.system("cls&echo.&echo.")

for i in range(0, len(data_r)):
	data_s = data_r[i].split(".lnk\n")
	data_t = data_r[i].split("\n")
	if pdata(username,data_t[0])[0] != '':
		print str(i + 1) + ". " + data_t[0].split(".lnk")[0].split(".LNK")[0]
	#print r"C:\Documents and Settings\Administrator\Desktop" + "\\" + data_t[0]

for y in range(0, len(datax_r)):
	datax_s = datax_r[y].split(".lnk\n")
	datax_t = datax_r[y].split("\n")
	if winver < 6:
		if pdata("All Users",datax_t[0])[0] != '':
			print str(y + 1 + len(data_r)) + ". " + datax_t[0].split(".lnk")[0].split(".LNK")[0]
	elif winver > 5:
		if pdata("Public",datax_t[0])[0] != '':
			print str(y + 1 + len(data_r)) + ". " + datax_t[0].split(".lnk")[0].split(".LNK")[0]
	#print r"C:\Documents and Settings\All Users\Desktop" + "\\" + data_t[0]

print "\n"
try:	
	data_in = input("\t Masukkan nomor aplikasi = ")
	#print "len(data_r) = ", len(data_r)
	#print "len(datax_r) = ", len(datax_r)
	if (data_in - 1) > len(data_r):
		data_u = datax_r[data_in - (len(data_r) + 1)].split("\n")
		data_ex = pdata("All Users",data_u[0])[0]
		module002.main(data_ex)
	else:
		data_u = data_r[data_in - 1].split("\n")
		data_ex = pdata(username,data_u[0])[0]
		module002.main(data_ex)

	#print "data_u = ", data_u

	"""
	if pdata(data_u[0],"Administrator") != '':
		print "ME"
		data_ex = pdata(data_u[0])
		#print data_ex
		print "\n"
		dsound = "Application being started.wav"
		print "\t Application being started !, please wait a seconds ... \n"
		print "data_ex = ", data_ex
		#dplay.play(dsound)
		#module002.main(data_ex)

	elif pdata(datax_u[0],"All Users") != '':
		print "YOU"
		datax_ex = pdata(datax_u[0])
		#print data_ex
		print "\n"
		dsound = "Application being started.wav"
		print "\t Application being started !, please wait a seconds ... \n"
		print "datax_ex = ", datax_ex
		#dplay.play(dsound)
		#module002.main(datax_ex)
			
	"""	
except IndexError, e:
	import traceback
	print "\t ERROR = ", traceback.format_exc()
	print "\n"
	dsound = "insert a Correct number.wav"
	print "\t Please insert a Correct number application ! \n"
	#dplay.play(dsound)
	
except SyntaxError, e:
	print "\n"
	dsound = "not insert number.wav"
	print "\t Insert number application to execute name of application \n"
	#dplay.play(dsound)
	
except NameError, e:
	sys.exit()
	

