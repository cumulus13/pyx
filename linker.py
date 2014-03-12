import sys
import os
import win32com.client 

filename = os.path.split(sys.argv[0])[1]
usage = "\t use : " + filename + """ [name of link] [destination of link] """

def maker(target, targetpath):
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(target + ".lnk")
    shortcut.Targetpath = targetpath
    shortcut.save()
    
    
if __name__ == '__main__':
    try:
        if os.path.isfile(sys.argv[2]):
            target = sys.argv[1]
            targetpath = sys.argv[2] 
            maker(target, targetpath)
        else:
            print "\n"
            print "\t TargetPath not a file ! "
            print usage
    except IndexError, e:
        print "\n"
        print usage