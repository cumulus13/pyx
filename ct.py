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
import sys
import os
#import gtk
#import gobject
import random

filename = os.path.split(sys.argv[0])[1]
usage = "\t use : " + filename + " [input text file]"


def getText():
    w.OpenClipboard()
    d = w.GetClipboardData(win32con.CF_TEXT)
    w.CloseClipboard()
    return d


def setText(aType, aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(aType, aString)
    w.CloseClipboard()


def readme(data, line_number=None, without_line_number_print=False):
    if line_number != None:
        data_read = open(data).readlines()
        if isinstance(line_number, list):
            data1 = []
            for i in line_number:
                if without_line_number_print:
                    data1.append(data_read[int(i)].encode('utf-8'))
                else:
                    data1.append(str(i) + ". " + data_read[int(i)].encode('utf-8'))
            return "".join(data1).strip()
        else:
            return data_read[int(line_number).encode('utf-8')]
    else:
        data_read = open(data).read()
        # print data_read
        return data_read.encode('utf-8')

def usage():
    import argparse
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('FILENAME', help='File TXT or contained string to be copy', action='store')
    parser.add_argument('-l', '--line', help='Line Number', nargs='*', action='store')
    parser.add_argument('-w', '--without-line-number-print', help='Copy string without line number if copy based on line number', action='store_true')
    if len(sys.argv) == 1:
        parser.print_help()
    else:
        args = parser.parse_args()
        try:
            data_pre = readme(args.FILENAME, args.line, args.without_line_number_print)
            print "data_pre =", data_pre
            try:
                data_to = setText(w.CF_TEXT, data_pre)
                data_fn = getText()
            except:
                data_to = clipboard.copy(data_pre)
                data_fn = clipboard.paste()
            print "\n"
            data_msg_s = "Sucessfully set Clipborad with : \n"
            #messages = (images_path + "/images/" + images['info'], data_msg_s)
            print "\t" + data_msg_s
            # print data_fn
            print "\n"
            print "-------------------------- END OF LINE -----------\n"
        except IOError, e:
            print "\n"
            data_msg_e = "Sorry your input data text is not valid ! \n"
            messages = (images_path + "/images/" + images['error'], data_msg_e)
            print "\t " + data_msg_e

if __name__ == '__main__':
    usage()
    # try:
    #     data_pre = sys.argv[1]
    #     data = data_pre
    #     data_pre = readme(data)
    #     if len(sys.argv) > 1:
    #         # if platform.uname()[0] == 'Windows':
    #         try:
    #             data_to = setText(w.CF_TEXT, data_pre)
    #             data_fn = getText()
    #         except:
    #             data_to = clipboard.copy(data_pre)
    #             data_fn = clipboard.paste()
    #         # elif platform.uname()[0] == 'Linux':
    #         #     data_to

    #         print "\n"
    #         data_msg_s = "Sucessfully set Clipborad with : \n"
    #         #messages = (images_path + "/images/" + images['info'], data_msg_s)
    #         print "\t" + data_msg_s
    #         # print data_fn
    #         print "\n"
    #         print "-------------------------- END OF LINE -----------\n"
    #     else:
    #         print "\n"
    #         print usage
    # except IndexError, e:
    #     print "\n"
    #     print usage
    # except IOError, e:
    #     print "\n"
    #     data_msg_e = "Sorry your input data text is not valid ! \n"
    #     messages = (images_path + "/images/" + images['error'], data_msg_e)
    #     print "\t " + data_msg_e

    #color_box = (("red", "white"), ("white", "blue"), ("green", "black"))
    # color_box = ("green", "black")
    #images = ("Alert2.png", None)
    # images = {'info': 'Info.png', 'debug': 'Debug.png', 'error': 'Error.png', 'alert': 'Aler.png',
              # 'emergenci': 'Emergenci.png', 'warning': 'Warning.png', 'help': 'Help.png', 'critical': 'Critical.png'}
    # messages = (("Hello", "This is a popup"),
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
