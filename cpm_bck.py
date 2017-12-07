import win32clipboard as w 
import win32con
import sys
import os
import gtk
import gobject
import gtkPopupNotify
import pywintypes
#import random

#color_box = (("red", "white"), ("white", "blue"), ("green", "black"))
color_box = ("green", "black")
images = {'info':'Info.png', 'debug':'Debug.png', 'error':'Error.png', 'alert':'Alert.png','emergenci':'Emergenci.png', 'warning':'Warning.png', 'help':'Help.png', 'critical':'Critical.png'}
images_path = os.path.split(sys.argv[0])[0] + "\\images\\" 


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
		messages = (("Info", "Sucessfully set clipboard ! \n now clipboard fill with = \"" + data_clip))
		img = images_path + images['info']
		print "\t now clipboard fill with = \"" + data_clip
	    elif (sys.argv[-1] == '/'):
		data_ex = os.getcwd().replace('\\','/')
		data_argv = data_ex + "/" + sys.argv[2] + '/'
		data_clip_set = setText(w.CF_TEXT, data_argv)
		data_clip = getText()
		print "\n"
		print "\t Sucessfully set clipboard ! \n"
		messages = (("Info", "Sucessfully set clipboard ! \n now clipboard fill with = \"" + data_clip))
		img = images_path + images['info']
		print "\t now clipboard fill with = \"" + data_clip 
	    elif (sys.argv[-1] == '\\'):
		data_ex = sys.argv[1].replace('/','\\')
		data_argv = data_ex + "\\" + sys.argv[2] + '\\'
		data_clip_set = setText(w.CF_TEXT, data_argv)
		data_clip = getText()
		print "\n"
		print "\t Sucessfully set clipboard ! \n"
		messages = (("Info", "Sucessfully set clipboard ! \n now clipboard fill with = \"" + data_clip))
		img = images_path + images['info']
		print "\t now clipboard fill with = \"" + data_clip 
	    else:
		data_ex = os.getcwd()
		data_argv = data_ex + "\\" + sys.argv[2]
		data_clip_set = setText(w.CF_TEXT, data_argv)
		data_clip = getText()
		print "\n"
		print "\t Sucessfully set clipboard ! \n"
		messages = (("Info", "Sucessfully set clipboard ! \n now clipboard fill with = \"" + data_clip))
		img = images_path + images['info']
		print "\t now clipboard fill with = \"" + data_clip + "\""
	elif (sys.argv[1] == '/'):
	    try:
		if (sys.argv[2] == '/'):
		    data_ex = os.getcwd().replace('\\','/')
		    data_clip_set = setText(w.CF_TEXT, data_ex)
		    data_clip = getText()
		    print "\n"
		    print "\t Sucessfully set clipboard ! \n"
		    messages = (("Info", "Sucessfully set clipboard ! \n now clipboard fill with = \"" + data_clip))
		    img = images_path + images['info']
		    print "\t now clipboard fill with = \"" + data_clip + '/'
	    except IndexError, e:
		data_ex = os.getcwd().replace('\\','/')
		data_clip_set = setText(w.CF_TEXT, data_ex)
		data_clip = getText()
		print "\n"
		print "\t Sucessfully set clipboard ! \n"
		messages = (("Info", "Sucessfully set clipboard ! \n now clipboard fill with = \"" + data_clip))
		img = images_path + images['info']
		print "\t now clipboard fill with = \"" + data_clip 
	elif (sys.argv[1] == '\\'):
	    try:
		if (sys.argv[2] == '\\'):
		    data_ex = os.getcwd().replace('/','\\')
		    data_clip_set = setText(w.CF_TEXT, data_ex)
		    data_clip = getText()
		    print "\n"
		    print "\t Sucessfully set clipboard ! \n"
		    messages = (("Info", "Sucessfully set clipboard ! \n now clipboard fill with = \"" + data_clip))
		    img = images_path + images['info']
		    print "\t now clipboard fill with = \"" + data_clip + '\\'
	    except IndexError, e:
		data_ex = os.getcwd().replace('\\','/')
		data_clip_set = setText(w.CF_TEXT, data_ex)
		data_clip = getText()
		print "\n"
		print "\t Sucessfully set clipboard ! \n"
		messages = (("Info", "Sucessfully set clipboard ! \n now clipboard fill with = \"" + data_clip))
		img = images_path + images['info']
		print "\t now clipboard fill with = \"" + data_clip 
        else:
	    if (sys.argv[-1] == 'linux'):
		data_argv = sys.argv[1].replace('\\','/') 
		data_clip_set = setText(w.CF_TEXT, data_argv)
		data_clip = getText()
		print "\n"
		print "\t Sucessfully set clipboard ! \n"
		messages = (("Info", "Sucessfully set clipboard ! \n now clipboard fill with = \"" + data_clip))
		img = images_path + images['info']
		print "\t now clipboard fill with = \"" + data_clip
	    elif (sys.argv[-1] == '/'):
		data_argv = sys.argv[1].replace('\\','/') + '/'
		data_clip_set = setText(w.CF_TEXT, data_argv)
		data_clip = getText()
		print "\n"
		print "\t Sucessfully set clipboard ! \n"
		messages = (("Info", "Sucessfully set clipboard ! \n now clipboard fill with = \"" + data_clip))
		img = images_path + images['info']
		print "\t now clipboard fill with = \"" + data_clip 
	    elif (sys.argv[-1] == '\\'):
		data_argv = sys.argv[1].replace('/','\\') + '\\'
		data_clip_set = setText(w.CF_TEXT, data_argv)
		data_clip = getText()
		print "\n"
		print "\t Sucessfully set clipboard ! \n"
		messages = (("Info", "Sucessfully set clipboard ! \n now clipboard fill with = \"" + data_clip))
		img = images_path + images['info']
		print "\t now clipboard fill with = \"" + data_clip 

	    else:   
		data_argv = sys.argv[1]
		data_clip_set = setText(w.CF_TEXT, data_argv)
		data_clip = getText()
		print "\n"
		print "\t Sucessfully set clipboard ! \n"
		messages = (("Info", "Sucessfully set clipboard ! \n now clipboard fill with = \"" + data_clip))
		img = images_path + images['info']
		print "\t now clipboard fill with = \"" + data_clip + "\""
    else:
        data_ex = os.getcwd()
        data_argv = data_ex + "\\" 
        data_clip_set = setText(w.CF_TEXT, data_argv)
        data_clip = getText()
        
        print "\n\n"
        print "\t Please insert a Word want to be Copy ! \n"
	messages = (("Alert", "Please insert a Word want to be Copy ! \n Default data is this path = " + data_argv))
	img = images_path + images['alert']
        print "\t Default data is this path = ", data_argv
except IndexError, e:
    print "\n\n"
    print "\t ERROR : ", e
    messages = (("Error", "ERROR : " + str(e)))
    img = images_path + images['error']
 
except pywintypes.error, e:
    messages = (("Error", "ERROR : " + str(e)))
    img = images_path + images['error']
    
def notify_factory():
    #color_fix = random.choice(color_box)
    color_fix = color_box
    #message = random.choice(messages)
    message = messages
    #image = random.choice(images)
    image = img
    #notifier.bg_color = gtk.gdk.Color(color_fix[0])
    #notifier.fg_color = gtk.gdk.Color(color_fix[1])
    notifier.bg_color = gtk.gdk.color_parse("#333333")
    notifier.fg_color = gtk.gdk.color_parse("#E3E3E3")
    #notifier.show_timeout = random.choice((True, False))
    notifier.show_timeout = True
    notifier.edge_offset_x = 20
    notifier.new_popup(title=message[0], message=message[1], image=image)
    return True
	
def gtk_main_quit():
    print "quitting"
    gtk.main_quit()
	    
notifier = gtkPopupNotify.NotificationStack(timeout=1) 
gobject.timeout_add(4000, notify_factory)
gobject.timeout_add(20000, gtk_main_quit)
gtk.main()
    
    
            

    
    

   