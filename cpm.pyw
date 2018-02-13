#!/usr/bin/python

import sys
import os
if sys.platform == 'win32':
    import win32clipboard as w 
    import win32con
    import pywintypes
    import winsound
else:
    import clipboard
import traceback
import tracert  
import sendgrowl

__version__ = "2.0"
__test__ = "0.3"
__author__ = "licface"
__url__ = "licface@yahoo.com"
__target__ = "all"
__build__ = "2.7"
__error__ = traceback.format_exc(print_msg= False)
__filename__ = os.path.basename(sys.argv[0])
__usage__ = """\n\n
	 Please insert a Word want to be Copy ! \n
	 Default data is this path = "data_argv" """

CLIP_APP = 'c:\TOOLS\EXE\cpath.exe'

def play(sound_file):
    winsound.PlaySound(sound_file, winsound.SND_ALIAS)    

def sendnotify(dcopy, title="CPM - Copy Clipboard", msg="now clipboard fill with = "):
    try:
        mclass = sendgrow.growl()
        icon = r'f:\ICONS\FatCow_Icons32x32\clipboard_empty.png'
        event = 'CPM - Copy Clipboard'
        text =  msg + "\"" + str(dcopy) +  "\""
        appname = 'cpm'
        mclass.publish(appname, event, title, text, iconpath=icon)
    except:
        #traceback.format_exc()
        pass

def getText():
    try:
        import clipboard
        return clipboard.paste()
    except:
        #traceback.format_exc()
        w.OpenClipboard() 
        d=w.GetClipboardData(win32con.CF_TEXT) 
        w.CloseClipboard() 
        return d 

def setText(aType,aString):
    if os.path.isfile(CLIP_APP):
        os.system(CLIP_APP + " " + aString)
    else:
        try:
            import clipboard
            clipboard.copy(aString)
        except:
            w.OpenClipboard()
            w.EmptyClipboard()
            w.SetClipboardData(aType,aString)
            sound_file = r'f:\SOUNDS\OTHER\sent.wav'
            play(sound_file)
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
        #print "data_ex = ", data_ex
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
        #print "data_ex = ", data_ex
        data_argv = data_ex + '\\'
        data_clip_set = setText(w.CF_TEXT, data_argv)
        add_slash = ''
    else:
        print __usage__
    data_clip = getText()
    sendnotify(data_clip)
    if os.path.basename(sys.executable).lower() == 'python.exe':
        print "\n"
        print "\t Sucessfully set clipboard ! \n"
        print "\t now clipboard fill with = \"" + str(data_clip) + add_slash

def winpath2():
    data_ex = os.getcwd()
    #data_argv = data_ex + "\\" + sys.argv[2]
    data_argv = os.path.join(data_ex, os.path.abspath('\\'.join(sys.argv[2:])))
    data_clip_set = setText(w.CF_TEXT, data_argv)
    data_clip = getText()
    sendnotify(str(data_argv))
    if os.path.basename(sys.executable).lower() == 'python.exe':
        print "data_argv =", data_argv
        print "\n"
        print "\t Sucessfully set clipboard ! \n"
        print "\t now clipboard fill with = \"" + str(data_argv) + "\""

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
                #print "AAA"
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
                    if os.path.basename(sys.executable).lower() == 'python.exe':
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
                if os.path.basename(sys.executable).lower() == 'python.exe':
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
                if os.path.basename(sys.executable).lower() == 'python.exe':
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
                if os.path.basename(sys.executable).lower() == 'python.exe':
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
                if os.path.basename(sys.executable).lower() == 'python.exe':
                    print "\n"
                    print "\t Sucessfully set clipboard ! \n"
                    #messages = (("Info", "Sucessfully set clipboard ! \n now clipboard fill with = \"" + data_clip))
                    #img = images_path + images['info']
                    print "\t now clipboard fill with = \"" + data_clip 
            else:   
                data_argv = sys.argv[1]
                data_clip_set = setText(w.CF_TEXT, data_argv)
                data_clip = getText()
                sendnotify(data_argv)
                if os.path.basename(sys.executable).lower() == 'python.exe':
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
        if os.path.basename(sys.executable).lower() == 'python.exe':
            print "\n\n"
            print "\t Please insert a Word want to be Copy ! \n"
            print "\t Default data is this path = ", data_argv
except IndexError as e:
    traceback.format_exc()
    print "\n\n"
    print "\t ERROR : ", e
    sendnotify("ERROR: " + str(e), title="ERROR (cpm)", msg="")

except pywintypes.error as e:
    print "\n\n"
    print "\t ERROR : ", e
    sendnotify("ERROR: " + str(e), title="ERROR (cpm)", msg="")