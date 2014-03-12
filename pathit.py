import win32clipboard as w 
import win32con
import sys
import os

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

data_argv = sys.argv[1]
data_clip_set = setText(w.CF_TEXT, data_argv)
data_clip = getText()

print "\n"
print "\t Sucessfully set clipboard ! \n"
print "\t now clipboard fill with = \"" + data_clip + "\""