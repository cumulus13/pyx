import win32clipboard as w
import win32con
import sys
import os

filename = os.path.split(sys.argv[0])[1]
usage = "\t use : " + filename + " [input text file]"

def getText():
    w.OpenClipboard()
    d=w.GetClipboardData(win32con.CF_TEXT)
    w.CloseClipboard()
    return d

def setText(aType,aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(aType,aString)
    w.CloseClipboard()

def readme(data):
	data_read = open(data).read()
	#print data_read
	return data_read
	
if __name__ == '__main__':
	try:
		if len(sys.argv) > 1:
			data_pre = sys.argv[1]
			data = data_pre
			data_pre = readme(data)
			data_to = setText(w.CF_TEXT, data_pre)
			data_fn = getText()
			print "\n"
			print "\t Sucessfully set Clipborad with : \n"
			print data_fn
			print "\n"
			print "-------------------------- END OF LINE -----------\n"
		else:
			print "\n"
			print usage
	except IndexError, e:
		print "\n"
		print usage
	except IOError, e:
		print "\n"
		print "\t Sorry your input data text is not valid ! \n"	