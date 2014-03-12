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

try:
    if (len(sys.argv) > 1):

        if (sys.argv[1] == '+'):
            if (sys.argv[-1] == 'linux'):
                data_ex = os.getcwd().replace('\\','/')
                data_argv = data_ex + "/" + sys.argv[2]
                data_clip_set = setText(w.CF_TEXT, data_argv)
                data_clip = getText()
                print "\n"
                print "\t Sucessfully set clipboard ! \n"
                print "\t now clipboard fill with = \"" + data_clip
            elif (sys.argv[-1] == '/'):
                data_ex = os.getcwd().replace('\\','/')
                data_argv = data_ex + "/" + sys.argv[2] + '/'
                data_clip_set = setText(w.CF_TEXT, data_argv)
                data_clip = getText()
                print "\n"
                print "\t Sucessfully set clipboard ! \n"
                print "\t now clipboard fill with = \"" + data_clip 
            elif (sys.argv[-1] == '\\'):
                data_ex = sys.argv[1].replace('/','\\')
                data_argv = data_ex + "\\" + sys.argv[2] + '\\'
                data_clip_set = setText(w.CF_TEXT, data_argv)
                data_clip = getText()
                print "\n"
                print "\t Sucessfully set clipboard ! \n"
                print "\t now clipboard fill with = \"" + data_clip 
            else:
                data_ex = os.getcwd()
                data_argv = data_ex + "\\" + sys.argv[2]
                data_clip_set = setText(w.CF_TEXT, data_argv)
                data_clip = getText()
                print "\n"
                print "\t Sucessfully set clipboard ! \n"
                print "\t now clipboard fill with = \"" + data_clip + "\""
        elif (sys.argv[1] == '/'):
            try:
                if (sys.argv[2] == '/'):
                    data_ex = os.getcwd().replace('\\','/')
                    data_clip_set = setText(w.CF_TEXT, data_ex)
                    data_clip = getText()
                    print "\n"
                    print "\t Sucessfully set clipboard ! \n"
                    print "\t now clipboard fill with = \"" + data_clip + '/'
            except IndexError, e:
                data_ex = os.getcwd().replace('\\','/')
                data_clip_set = setText(w.CF_TEXT, data_ex)
                data_clip = getText()
                print "\n"
                print "\t Sucessfully set clipboard ! \n"
                print "\t now clipboard fill with = \"" + data_clip 
        elif (sys.argv[1] == '\\'):
            try:
                if (sys.argv[2] == '\\'):
                    data_ex = os.getcwd().replace('/','\\')
                    data_clip_set = setText(w.CF_TEXT, data_ex)
                    data_clip = getText()
                    print "\n"
                    print "\t Sucessfully set clipboard ! \n"
                    print "\t now clipboard fill with = \"" + data_clip + '\\'
            except IndexError, e:
                data_ex = os.getcwd().replace('\\','/')
                data_clip_set = setText(w.CF_TEXT, data_ex)
                data_clip = getText()
                print "\n"
                print "\t Sucessfully set clipboard ! \n"
                print "\t now clipboard fill with = \"" + data_clip 
        else:
            if (sys.argv[-1] == 'linux'):
                data_argv = sys.argv[1].replace('\\','/') 
                data_clip_set = setText(w.CF_TEXT, data_argv)
                data_clip = getText()
                print "\n"
                print "\t Sucessfully set clipboard ! \n"
                print "\t now clipboard fill with = \"" + data_clip
            elif (sys.argv[-1] == '/'):
                data_argv = sys.argv[1].replace('\\','/') + '/'
                data_clip_set = setText(w.CF_TEXT, data_argv)
                data_clip = getText()
                print "\n"
                print "\t Sucessfully set clipboard ! \n"
                print "\t now clipboard fill with = \"" + data_clip 
            elif (sys.argv[-1] == '\\'):
                data_argv = sys.argv[1].replace('/','\\') + '\\'
                data_clip_set = setText(w.CF_TEXT, data_argv)
                data_clip = getText()
                print "\n"
                print "\t Sucessfully set clipboard ! \n"
                print "\t now clipboard fill with = \"" + data_clip 

            else:   
                data_argv = sys.argv[1]
                data_clip_set = setText(w.CF_TEXT, data_argv)
                data_clip = getText()
                print "\n"
                print "\t Sucessfully set clipboard ! \n"
                print "\t now clipboard fill with = \"" + data_clip + "\""
    else:
        data_ex = os.getcwd()
        data_argv = data_ex + "\\" 
        data_clip_set = setText(w.CF_TEXT, data_argv)
        data_clip = getText()

        print "\n\n"
        print "\t Please insert a Word want to be Copy ! \n"
        print "\t Default data is this path = ", data_argv
except IndexError, e:
    print "\n\n"
    print "\t ERROR : ", e

except pywintypes.error, e:
    pass





