import os
import sys
import traceback
import win32com.client as comx

filename = os.path.basename(os.path.splitext(sys.argv[0])[0])
shell = comx.Dispatch("Scripting.FileSystemObject")
#print dir(shell)
#print "_"*180

def usage():
    print "\n"
    print "\t Usage: " + str(filename) + " [(folder/file)_from] [(folder/file)_to]"
    
def copy_Folder(_from,_to):
    if os.path.isdir(_to):
        shell.CopyFolder(_from, _to)
        print "\n"
        print "\t CopyFolder: \"" + str(_from) + "\" ---> \"" + str(_to) + "\""
    else:
        print "\n"
        print "\t You can't Copy a Drive to a File !!!"
        usage()
    
def copy_File(_from,_to):
    if os.path.isdir(_to):
        file_name = os.path.basename(_from)
        _tox = os.path.join(_to, file_name)
        shell.CopyFile(_from,_tox)
        print "\n"
        print "\t CopyFile: \"" + str(_from) + "\" ---> \"" + str(_tox) + "\""
    else:
        shell.CopyFile(_from,_to)
        print "\n"
        print "\t CopyFile: \"" + str(_from) + "\" ---> \"" + str(_to) + "\""
    
def cek_space(drive):
    _drive = shell.GetDrive(drive)
    return _drive.AvailableSpace

def doing(argv1,argv2=None):
    #print "argv1 = ", argv1
    #print "argv2 = ", argv2
    if os.path.isfile(argv1):
        copy_File(argv1, argv2)
        print "-"*65
        print "\t Space On Drive \"" + str(os.path.splitdrive(argv1)[0]) + "\\\" =" ,cek_space(os.path.splitdrive(argv1)[0])
        if argv2 == os.getcwd():
            pass
        else:
            print "\t\t\t " + str(os.path.splitdrive(argv2)[0]) + "\\\" =" ,cek_space(os.path.splitdrive(argv2)[0])
    elif os.path.isdir(argv1):
        copy_Folder(argv1, argv2)
        print "-"*65
        print "\t Space On Drive \"" + str(os.path.splitdrive(argv1)[0]) + "\\\" =" ,cek_space(os.path.splitdrive(argv1)[0])
        if argv2 == os.getcwd():
            pass
        else:
            print "\t\t\t " + str(os.path.splitdrive(argv2)[0]) + "\\\" =" ,cek_space(os.path.splitdrive(argv2)[0])

if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            try:
                if len(sys.argv[2]) > 1 or sys.argv[2] != "" or sys.argv[2] != " " or sys.argv[2] != None:
                    #print "AAAAAAAA"
                    doing(sys.argv[1], sys.argv[2])
                else:
                    #print "BBBBBBBB"
                    doing(sys.argv[1],os.getcwd())
            except:
                #print " Error = ", traceback.format_exc()
                try:
                    #print "CCCCCCCC"
                    doing(sys.argv[1],os.getcwd())
                except:
                    print " Error = ", traceback.format_exc()
        else:
            usage()
    except:
        print "\n"
        #print "\t",sys.exc_info(), sys.exc_info
        print " Error = ", traceback.format_exc()
    
