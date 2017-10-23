import sys
import os
import win32com.client 

filename = os.path.split(sys.argv[0])[1]
usage = "\t use : " + filename + """ [name of link] [destination of link] """

def maker(target, targetpath):
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortcut(target + ".lnk")
    shortcut.Targetpath = targetpath
    shortcut.save()

def test(target):
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortcut(target)
    print dir(shortcut)
    print "shortcut = ", shortcut.TargetPath
    #shortcut2 = shortcut.Load(target)
    print "-"*180
    #print "shortcut2 = ", shortcut2

def read(target):
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortcut(target)
    print "\n"
    print "Arguments        = ", shortcut.Arguments
    print "Description      = ", shortcut.Description
    print "FullName         = ", shortcut.FullName
    print "Hotkey           = ", shortcut.Hotkey
    print "IconLocation     = ", shortcut.IconLocation
    print "TargetPath       = ", shortcut.TargetPath
    print "WindowStyle      = ", shortcut.WindowStyle
    print "WorkingDirectory = ", shortcut.WorkingDirectory


if __name__ == '__main__':
    try:
        if len(sys.argv) > 1:
            if sys.argv[1] == "read":
                read(sys.argv[2])
            elif sys.argv[1] == "write":                
                if os.path.isfile(sys.argv[3]):
                    target = sys.argv[2]
                    targetpath = sys.argv[3] 
                    maker(target, targetpath)
                else:
                    print "\n"
                    print "\t TargetPath not a file ! "
                    print usage
            elif sys.argv[1] == "test":
                test(sys.argv[2])
        else:
            print "\n"
            print "\t TargetPath not a file ! "
            print usage
    except IndexError, e:
        print "\n"
        print usage