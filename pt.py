#!/usr/bin/python

import platform

if platform.uname()[0] == 'Windows':
    try:
        import clipboard
    except:
        import win32clipboard as w
        import win32con
else:
    try:
        import clipboard
    except:
        print "No Module name 'clipboard'"

import win32clipboard as w
import win32con
import sys
import os
#import gtk
#import gobject
import random

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

def write(path, data):
    data_read = open(path, 'w')
    data_read.write(data)
    #print data_read
    #return data_read

def add(path, data):
    data_read = open(path, 'a')
    data_read.write(data)

if __name__ == '__main__':
    try:
        if len(sys.argv) > 1:
            if sys.argv[1] == '+':
                if platform.uname()[0] == 'Windows':
                    data_fn = getText()
                else:
                    data_fn = clipboard.paste()
                add(sys.argv[2], data_fn)
                print "\n"
                data_msg_s =  "Sucessfully write add Clipborad to %s : \n" % (sys.argv[1])
                #messages = (images_path + "/images/" + images['info'], data_msg_s)
                print "\t" + data_msg_s
                #print data_fn
                print "\n"
                print "-------------------------- END OF LINE -----------\n"
            else:
                #data_pre = sys.argv[1]
                #data = data_pre
                #data_pre = readme(data)
                #data_to = setText(w.CF_TEXT, data_pre)
                if platform.uname()[0] == 'Windows':
                    data_fn = getText()
                else:
                    data_fn = clipboard.paste()
                write(sys.argv[1], data_fn)
                print "\n"
                data_msg_s =  "Sucessfully write Clipborad to %s : \n" % (sys.argv[1])
                #messages = (images_path + "/images/" + images['info'], data_msg_s)
                print "\t" + data_msg_s
                #print data_fn
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
        data_msg_e = "Sorry your input data text is not valid ! \n"	
        #messages = (images_path + "/images/" +  images['error'], data_msg_e)
        print "\t " + data_msg_e
        print "-" * 80
        print "ERROR:"
        print "\t", e

    #color_box = (("red", "white"), ("white", "blue"), ("green", "black"))
    #color_box = ("green", "black")
    #images = ("Alert2.png", None)
    #images = {'info':'Info.png', 'debug':'Debug.png', 'error':'Error.png', 'alert':'Aler.png','emergenci':'Emergenci.png', 'warning':'Warning.png', 'help':'Help.png', 'critical':'Critical.png'}
    #messages = (("Hello", "This is a popup"),
    #            ("Some Latin", "Quidquid latine dictum sit, altum sonatur."),
    #            ("A long message", "The quick brown fox jumped over the lazy dog. " * 6))

    """def notify_factory():
	#color_fix = random.choice(color_box)
	color_fix = color_box
	#message = random.choice(messages)
	message = messages
	#image = random.choice(images)
	image = images_path + "/images/" +  images['info']
	#notifier.bg_color = gtk.gdk.Color(color_fix[0])
	#notifier.fg_color = gtk.gdk.Color(color_fix[1])
	notifier.bg_color = gtk.gdk.color_parse("#333333")
	notifier.fg_color = gtk.gdk.color_parse("#E3E3E3")
	notifier.show_timeout = random.choice((True, False))
	notifier.edge_offset_x = 20
	notifier.new_popup(title=message[0], message=message[1], image=image)
	return True

    def gtk_main_quit():
	print "quitting"
	gtk.main_quit()

    notifier = NotificationStack(timeout=6) 
    gobject.timeout_add(4000, notify_factory)
    gobject.timeout_add(20000, gtk_main_quit)
    gtk.main()"""