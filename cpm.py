import win32clipboard as w 
import win32con
import sys
import os
import pywintypes
import traceback
import sendgrow

__version__ = "2.0"
__test__ = "0.3"
__author__ = "licface"
__url__ = "licface@yahoo.com"
__target__ = "all"
__build__ = "2.7"
__error__ = traceback.format_exc()
__filename__ = os.path.basename(sys.argv[0])
__usage__ = """\n\n
	 Please insert a Word want to be Copy ! \n
	 Default data is this path = "data_argv" """

def sendnotify(dcopy, title="CPM - Copy Clipboard", msg="now clipboard fill with = "):
    mclass = sendgrow.growl()
    icon = r'c:\pyx\redhat.png'
    event = 'CPM - Copy Clipboard'
    text =  msg + "\"" + str(dcopy) +  "\""
    appname = 'cpm'
    mclass.publish(appname, event, title, text, iconpath=icon)

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

def linuxpath():
    data_ex = os.getcwd().replace('\\','/')
    data_argv = data_ex + "/" + sys.argv[2]
    data_clip_set = setText(w.CF_TEXT, data_argv)
    data_clip = getText()
    sendnotify(data_clip)
    print "\n"
    print "\t Sucessfully set clipboard ! \n"
    print "\t now clipboard fill with = \"" + data_clip

def linuxpath2():
    data_ex = os.getcwd().replace('\\','/')
    data_argv = data_ex + "/" + sys.argv[2] + '/'
    data_clip_set = setText(w.CF_TEXT, data_argv)
    data_clip = getText()
    sendnotify(data_clip)
    print "\n"
    print "\t Sucessfully set clipboard ! \n"
    print "\t now clipboard fill with = \"" + data_clip 

def winpath(session=None):
    if session == None:
        data_ex = sys.argv[1].replace('/','\\')
        print "data_ex = ", data_ex
        data_argv = data_ex + "\\" + sys.argv[2] + '\\'
        data_clip_set = setText(w.CF_TEXT, data_argv)
        add_slash = ''
    elif session == 1:
        data_ex = os.getcwd().replace('\\','/')
        data_clip_set = setText(w.CF_TEXT, data_ex)
        add_slash = '/'
    elif session == 0:
        data_ex = os.getcwd().replace('\\','/')
        data_clip_set = setText(w.CF_TEXT, data_ex)
        add_slash = ''
    elif session == 2:
        data_ex = os.path.join(os.getcwd(),sys.argv[2].replace('/','\\'))
        print "data_ex = ", data_ex
        data_argv = data_ex + '\\'
        data_clip_set = setText(w.CF_TEXT, data_argv)
        add_slash = ''
    else:
        print __usage__
    data_clip = getText()
    sendnotify(data_clip)
    print "\n"
    print "\t Sucessfully set clipboard ! \n"
    print "\t now clipboard fill with = \"" + data_clip + add_slash

def winpath2():
    data_ex = os.getcwd()
    data_argv = data_ex + "\\" + sys.argv[2]
    data_clip_set = setText(w.CF_TEXT, data_argv)
    data_clip = getText()
    sendnotify(data_clip)
    print "\n"
    print "\t Sucessfully set clipboard ! \n"
    print "\t now clipboard fill with = \"" + data_clip + "\""

try:
    if (len(sys.argv) > 1):
        if (sys.argv[1] == '+'):
            if (sys.argv[-1] == 'linux'):
                linuxpath()
            elif (sys.argv[-1] == '/'):
                linuxpath2()
            elif (sys.argv[-1] == '\\'):
                winpath(2)
            else:
                winpath2()
        elif (sys.argv[1] == '/'):
            try:
                if (sys.argv[2] == '/'):
                    winpath(1)
            except IndexError, e:
                winpath(1)
        elif (sys.argv[1] == 'linux'):
            try:
                if (sys.argv[2] == '/'):
                    winpath(1)
            except IndexError, e:
                winpath(0)
        elif (sys.argv[1] == '\\'):
            try:
                if (sys.argv[2] == '\\'):
                    data_ex = os.getcwd().replace('/','\\')
                    data_clip_set = setText(w.CF_TEXT, data_ex)
                    data_clip = getText()
                    sendnotify(data_clip)
                    print "\n"
                    print "\t Sucessfully set clipboard ! \n"
                    #messages = (("Info", "Sucessfully set clipboard ! \n now clipboard fill with = \"" + data_clip))
                    #img = images_path + images['info']
                    print "\t now clipboard fill with = \"" + data_clip + '\\'
            except IndexError, e:
                data_ex = os.getcwd().replace('/','\\')
                data_clip_set = setText(w.CF_TEXT, data_ex)
                data_clip = getText()
                sendnotify(data_clip)
                print "\n"
                print "\t Sucessfully set clipboard ! \n"
                #messages = (("Info", "Sucessfully set clipboard ! \n now clipboard fill with = \"" + data_clip))
                #img = images_path + images['info']
                print "\t now clipboard fill with = \"" + data_clip 
        else:
            if (sys.argv[-1] == 'linux'):
                data_argv = sys.argv[1].replace('\\','/') 
                data_clip_set = setText(w.CF_TEXT, data_argv)
                data_clip = getText()
                sendnotify(data_clip)
                print "\n"
                print "\t Sucessfully set clipboard ! \n"
                #messages = (("Info", "Sucessfully set clipboard ! \n now clipboard fill with = \"" + data_clip))
                #img = images_path + images['info']
                print "\t now clipboard fill with = \"" + data_clip
            elif (sys.argv[-1] == '/'):
                data_argv = sys.argv[1].replace('\\','/') + '/'
                data_clip_set = setText(w.CF_TEXT, data_argv)
                data_clip = getText()
                sendnotify(data_clip)
                print "\n"
                print "\t Sucessfully set clipboard ! \n"
                #messages = (("Info", "Sucessfully set clipboard ! \n now clipboard fill with = \"" + data_clip))
                #img = images_path + images['info']
                print "\t now clipboard fill with = \"" + data_clip 
            elif (sys.argv[-1] == '\\'):
                data_argv = sys.argv[1].replace('/','\\') + '\\'
                data_clip_set = setText(w.CF_TEXT, data_argv)
                data_clip = getText()
                sendnotify(data_clip)
                print "\n"
                print "\t Sucessfully set clipboard ! \n"
                #messages = (("Info", "Sucessfully set clipboard ! \n now clipboard fill with = \"" + data_clip))
                #img = images_path + images['info']
                print "\t now clipboard fill with = \"" + data_clip 
            else:   
                data_argv = sys.argv[1]
                data_clip_set = setText(w.CF_TEXT, data_argv)
                data_clip = getText()
                sendnotify(data_clip)
                print "\n"
                print "\t Sucessfully set clipboard ! \n"
                #messages = (("Info", "Sucessfully set clipboard ! \n now clipboard fill with = \"" + data_clip))
                #img = images_path + images['info']
                print "\t now clipboard fill with = \"" + data_clip + "\""
    else:
        data_ex = os.getcwd()
        data_argv = data_ex + "\\" 
        data_clip_set = setText(w.CF_TEXT, data_argv)
        data_clip = getText()
        sendnotify(data_clip)

        print "\n\n"
        print "\t Please insert a Word want to be Copy ! \n"
        print "\t Default data is this path = ", data_argv
except IndexError as e:
    print "\n\n"
    print "\t ERROR : ", e
    sendnotify("ERROR: " + str(e), title="ERROR (cpm)", msg="")

except pywintypes.error as e:
    print "\n\n"
    print "\t ERROR : ", e
    sendnotify("ERROR: " + str(e), title="ERROR (cpm)", msg="")