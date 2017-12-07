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
    #print "len(sys.argv) =", len(sys.argv)
    try:
        if len(sys.argv) > 2:
            if os.path.isfile(sys.argv[2]):
                target = os.path.join(r"C:\Users\All Users\Desktop",sys.argv[1])
                targetpath = sys.argv[2] 
                maker(target, targetpath)
            else:
                print "\n"
                print "\t TargetPath not a file ! "
                print usage
        else:
            if os.path.isfile(sys.argv[1]) or  os.path.isfile(sys.arvg[1]):
                target_pre =  os.path.split(sys.argv[1])
                #print "target = ", target_pre
                targetpath =  target_pre[0]
                targetname =  str(os.path.splitext(target_pre[1])[0]).capitalize()
                target = os.path.join(r"C:\Users\All Users\Desktop", targetname)
                #print "targetname = ", targetname
                maker(target, sys.argv[1])
            else:
                import  traceback
                print "\n"
                print "Error: ", traceback.format_exc()
                print usage                
            
    except IndexError, e:
        import  traceback
        print "\n"
        print "Error: ", traceback.format_exc()
        print usage