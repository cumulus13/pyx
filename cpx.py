# Created by licface (licface@yahoo.com) version 0.0.1
# By python version 2.6.6 (r266:84297, Aug 24 2010, 18:46:32) [MSC v.1500 32 bit (Intel)]
# On Sun Jan 27 12:31:13 2013

__author__ = "licface (licface@yahoo.com)"
__version__ = "0.0.1"
__ver__ = "0.0.1"
__site__ = "http://www.licface.tk"
__donate__ = "please donate by confirm at my Mail address :)"
__about__ = "please donate by confirm at my Mail address :)"

import os
import sys
import traceback
import checkArray.checkArray as checkArray
import win32com.client as comx

filename = os.path.basename(os.path.splitext(sys.argv[0])[0])
data = []
if len(sys.argv) > 2:
    for i in range(1,len(sys.argv)):
        data.append(sys.argv[i])
else:
    pass
    
shell = comx.Dispatch("Scripting.FileSystemObject")
#print dir(shell)
#print "_"*180

def usage():
    print "\n"
    print "\t Usage: " + str(filename) + " [(folder/file)_from] [(folder/file)_to]"
    
def copy_Folder(_from,_to):
    this_realpath = os.path.realpath(_to)
    this_splitpath = os.path.dirname(this_realpath)
    print "this_splitpath = ", this_splitpath
    if os.path.isdir(_to):
        shell.CopyFolder(_from, _to)
        print "\n"
        print "\t CopyFolder: \"" + str(_from) + "\" ---> \"" + str(_to) + "\""
    elif os.path.isfile(_to):
        print "\n"
        print "\t You can't Copy a Drive to a File !!!"
        usage()
        break
    else:
        print "\n"
        print "\t Folder is Not Exist !!!\n"
        confrm = raw_input("\t Do you want to Copy(do) it ? ([[y|Y]es|ES] or [[n|N]o|O] : ")
        print "\n"
        if confrm == "y" or confrm == "Y" or confrm == "yes" or confrm == "Yes" or confrm == "YES":
            print "\t MakeFolder: \"" + str(this_splitpath) + "\" ---> \"" + str(_to) + "\""
            os.mkdir(_to)
            shell.CopyFolder(_from, _to)
            print "\n"
            print "\t CopyFolder: \"" + str(_from) + "\" ---> \"" + str(_to) + "\""
        elif confrm == "n" or confrm == "N" or confrm == "no" or confrm == "No" or confrm == "NO":
            print "\t You Not make it !\n"
            usage()
        else:
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

def doing(data):
    if len(data) < 1:
        usage()
        
    real_path1 = os.path.realpath(data[-2])
    real_path2 = os.path.realpath(data[-1])
    #print "real_path1 = ", real_path1
    #print "real_path2 = ", real_path2
    split_path1 = os.path.splitdrive(real_path1)[0]
    split_path2 = os.path.splitdrive(real_path2)[0]
    #print "split_path1 = ", split_path1
    #print "split_path2 = ", split_path2
    for i in range(0,len(data)-1):
            break
        if os.path.isfile(data[i]):
            copy_File(data[i], data[-1])
            #print os.path.__all__
        elif os.path.isdir(data[i]):
            copy_Folder(data[i], data[-1])
        else:
            usage()
            
    print "-"*65
    print "\t Space On Drive \"" + str(os.path.splitdrive(real_path1)[0]) + "\\\" =" ,cek_space(os.path.splitdrive(real_path1)[0])
    if real_path2 == os.getcwd():
        pass
    else:
        print "\t\t\t " + str(os.path.splitdrive(real_path2)[0]) + "\\\" =" ,cek_space(os.path.splitdrive(real_path2)[0])

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
    
