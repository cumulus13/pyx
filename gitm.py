import clipboard
import os

GIT_BIN = r'c:\apps\git\bin\git.exe'
#print "os.getcwd", os.getcwd()
message = clipboard.paste().replace('\n', '')
#message = message.replace(' ', '')
print "message =", message
#a = os.system(GIT_BIN + ' commit -m ' + message)
#print "a =", a