import os
import sys
import win32com.client
import module002

def pdata(data):
	shell = win32com.client.Dispatch("WScript.Shell")
	shortcut = shell.CreateShortcut(r"C:\Documents and Settings\Administrator\Desktop" + "\\" + data)
	rdata = shortcut.Targetpath
	return rdata

data = os.popen("dir /b \"C:\Documents and Settings\Administrator\Desktop\*.lnk")
data_r = data.readlines()
#print data_r
os.system("cls&echo.&echo.")
len_data_r = len(data_r)
for x in range(0, len_data_r):
	if (len_data_r/2 == "1"):
		print str(x)
for i in range(0, len(data_r)):
	data_s = data_r[i].split(".lnk\n")
	data_t = data_r[i].split("\n")
	if pdata(data_t[0]) != '':
		print str(i + 1) + ". " + data_t[0].split(".lnk")[0].split(".LNK")[0]
	#print r"C:\Documents and Settings\Administrator\Desktop" + "\\" + data_t[0]

print "\n"
try:	
	data_in = input("\t Masukkan nomor aplikasi = ")
	data_u = data_r[data_in - 1].split("\n")
	#print data_u
	if pdata(data_u[0]) != '':
		data_ex = pdata(data_u[0])
		#print data_ex
		print "\n"
		print "\t Application being started !, please wait a seconds ... \n"
		module002.main(data_ex)
		
except IndexError:
	print "\n"
	print "\t Please insert a Correct number application ! \n"
	
except SyntaxError:
	print "\n"
	print "\t Insert number application to execute name of application \n"
	
#if pdata(data_t[0]) != '':
#	print pdata(data_t[0])
	
	
len_data_s = len(data_s)
for j in range(0, len_data_s -1):
	#print str(i + 1) + ". " + data_s[i] + "\n"
	#print data_s
	pass
	

