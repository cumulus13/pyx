#!c:/SDK/Anaconda2/python.exe
from __future__ import print_function
import sys
import os
if sys.version_info.major == 2:
    from _winreg import *
else:    
    from winreg import *
import argparse
import win32con
import string
import errno
import win32com.client 
print("\n")

__version__ = "2.4"
__filename__ = os.path.basename(sys.argv[0])
__author__ = "licface"
__url__ = "licface@yahoo.com"
__target__ = "windows"
__target_test__ =  ''
__build__ = "2.7"
__sdk__ =  "2.7"
__usage__ = "Usage : " + str(__filename__) + " [option]"
__test__ = "0.3"

typeReg = ({1:"REG_SZ",2:"REG_EXPAND_SZ",3:"REG_BINARY",4:"REG_DWORD",5:"REG_DWORD_BIG_ENDIAN",6:"REG_LINK",7:"REG_MULTI_SZ",8:"REG_RESOURCE_LIST",9:"REG_FULL_RESOURCE_DESCRIPTOR",0:"REG_NONE"})

BANK_REG = {}
BANK_REG_TYPE = {}
BANK_ALL = {}

NAMELISTLNK = {}
NAMELISTLNKTODEL = {}
NAMELISTLNKTODEL_TYPE = {}

def getusername():
    u1 =  os.getenv('USERNAME')
    winver =  sys.winver
    if u1 == None or u1 == '':
        if float(winver) > 2.6:
            import  getpass
            return getpass.getuser()
        else:
            raise  SyntaxError("This is still development, I have not running on xp :), email me for the path in XP")
    else:
        return u1
    
PATH_FILELNK =  [r"c:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup", r"c:\Users" + "\\" + str(getusername()) + "\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"]
    
def readlnk(target):
    print("target =", target)
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortcut(target)
    print("shortcut =", shortcut)
    name =  os.path.splitext((os.path.split(target)[1]))[0]
    path =  shortcut.TargetPath
    type =  "LINK (.lnk)"
    NAMELISTLNK.update({name:path})
    return [name, path, type]
    
def readlnk_todel(target):
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortcut(target)    
    name = os.path.splitext(os.path.split(target)[1])[0]
    path =  shortcut.TargetPath
    NAMELISTLNKTODEL.update({name:target})
    NAMELISTLNKTODEL_TYPE.update({name:"LINK (.lnk)"})
    BANK_ALL.update({name:{path:"link"}})
    BANK_ALL.update({name:{'path': path, 'type': "LINK (.lnk)"}})
    return [name, path]
    
def prinlist(dataenum):
    print(" NAME :",dataenum[0])
    print(" PATH :",dataenum[1])
    print(" TYPE :",typeReg.get(dataenum[2]))
    print("\n")
    
def prinlistlnk(dataenum):
    print(" NAME :",dataenum[0])
    print(" PATH :",dataenum[1])
    print(" TYPE :",dataenum[2])
    print("\n")


def listautoruns(keyval=None,root_key=None,numlist=100):
    if keyval == None:
        keyval = [r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run",r"System\CurrentControlSet\Control\Terminal Server\Wds\rdpwd\StartupPrograms",r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\Userinit",r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon",r"Software\Microsoft\Windows\CurrentVersion\Run"]
    if root_key == None:
        print("\n")
        for i in range(0,3):
            try:
                root_key = OpenKey(HKEY_LOCAL_MACHINE, keyval[i],0,KEY_READ)
                for j in range(100):
                    if EnumValue(root_key, 0)[0] != '' or EnumValue(root_key, 0)[0] != None:
                        dataEnum = EnumValue(root_key, j)
                        prinlist(dataEnum)
            except:
                pass
        for x in range(4,5):
            root_key = OpenKey(HKEY_CURRENT_USER, keyval[x],0,KEY_READ)
            for y in range(30):
                try:
                    if EnumValue(root_key, 0)[0] != '' or EnumValue(root_key, 0)[0] != None:
                        dataEnum = EnumValue(root_key, y)
                        prinlist(dataEnum)
                except:
                    pass
    else:
        for j in range(int(numlist)):
            if EnumValue(root_key, 0)[0] != '' or EnumValue(root_key, 0)[0] != None:
                dataEnum = EnumValue(root_key, j)
                prinlist(dataEnum)
                
    LISTFILELNK =  []
    LISTFILELNK2 =  []
    for a in  PATH_FILELNK:
        a1 =  os.popen("dir /s /b \"" + str(a) + "\\""*.lnk").readlines()
        for b in  a1:
            LISTFILELNK.append(os.path.abspath(b))
    for c in  LISTFILELNK:
        c1 =  str(c).split("\n")[0]
        LISTFILELNK2.append(c1)
    for d in  LISTFILELNK2:
        data =  readlnk(d)
        prinlistlnk(data)
        
def listreg_todel(keyval=None,root_key=None,numlist=100):
    if keyval == None:
        keyval = [r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run",r"System\CurrentControlSet\Control\Terminal Server\Wds\rdpwd\StartupPrograms",r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\Userinit",r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon",r"Software\Microsoft\Windows\CurrentVersion\Run"]
    if root_key == None:
        print("\n")
        for i in range(0,3):
            try:
                root_key = OpenKey(HKEY_LOCAL_MACHINE, keyval[i],0,KEY_READ)
                for j in range(100):
                    if EnumValue(root_key, 0)[0] != '' or EnumValue(root_key, 0)[0] != None:
                        dataEnum = EnumValue(root_key, j)
                        BANK_REG.update({dataEnum[0]: dataEnum[1]})
                        BANK_REG_TYPE.update({dataEnum[0]: dataEnum[2]})
                        BANK_ALL.update({dataEnum[0]:{'path': dataEnum[1], 'type': dataEnum[2]}})
            except:
                pass
        for x in range(4,5):
            root_key = OpenKey(HKEY_CURRENT_USER, keyval[x],0,KEY_READ)
            for y in range(30):
                try:
                    if EnumValue(root_key, 0)[0] != '' or EnumValue(root_key, 0)[0] != None:
                        dataEnum = EnumValue(root_key, y)
                        BANK_REG.update({dataEnum[0]: dataEnum[1]})
                        BANK_REG_TYPE.update({dataEnum[0]: dataEnum[2]})
                        BANK_ALL.update({dataEnum[0]:{'path': dataEnum[1], 'type': dataEnum[2]}})
                except:
                    pass
    else:
        for j in range(int(numlist)):
            if EnumValue(root_key, 0)[0] != '' or EnumValue(root_key, 0)[0] != None:
                dataEnum = EnumValue(root_key, j)
                BANK_REG.update({dataEnum[0]: dataEnum[1]})
                BANK_REG_TYPE.update({dataEnum[0]: dataEnum[2]})
                BANK_ALL.update({dataEnum[0]:{'path': dataEnum[1], 'type': dataEnum[2]}})
            
def listlnk_todel():
    LISTFILELNK =  []
    LISTFILELNK2 =  []
    for a in  PATH_FILELNK:
        a1 =  os.popen("dir /s /b \"" + str(a) + "\\""*.lnk").readlines()
        for b in  a1:
            LISTFILELNK.append(os.path.abspath(b))
    for c in  LISTFILELNK:
        c1 =  str(c).split("\n")[0]
        LISTFILELNK2.append(c1)
    for d in  LISTFILELNK2:
        data =  readlnk_todel(d)
    
def writereg(name, value):
    keyval = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
    if not os.path.exists(keyval):
        key = CreateKey(HKEY_LOCAL_MACHINE,keyval)
    RegKey = OpenKey(HKEY_LOCAL_MACHINE,keyval,0,KEY_WRITE)
    SetValueEx(RegKey,name,0,REG_SZ, value)
    CloseKey(RegKey)
    print("\n")
    print((str("   Add Succesfull").upper()))

def readreg(name):
    try:
        keyval = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
        root_key = OpenKey(HKEY_LOCAL_MACHINE, keyval,0,KEY_READ)
        [path,regtype] = (QueryValueEx(root_key,name))
        CloseKey(root_key)
        if ("" == path):
            raise WindowsError
        else:
            print(("NAME :", name))
            print(("PATH :", path))
            print(("RegType :", regtype))
    except WindowsError:
        print("\n")
        print("\tNOT FOUND: Key Value or Subkey !")
        return [""]
    except:
        return False

def _delreg(name):
    er = ""
    keyval = [r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run",r"System\CurrentControlSet\Control\Terminal Server\Wds\rdpwd\StartupPrograms",r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\Userinit",r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon",r"Software\Microsoft\Windows\CurrentVersion\Run"]
    for i in keyval:
        try:
            key = OpenKey(HKEY_LOCAL_MACHINE,i,0,KEY_ALL_ACCESS)
            DeleteValue(key,name)
            CloseKey(key)
            #SendMessage()
            return True
        except WindowsError:
            try:
                key = OpenKey(HKEY_CURRENT_USER,i,0,KEY_ALL_ACCESS)
                DeleteValue(key,name)
                CloseKey(key)
                #SendMessage()
                return True
            except WindowsError as we:
                er = we
        except:
            pass
    return [False,we]

def delreg(name):
    if _delreg(name) == True:
        print("\n")
        print("   DELETE SUCCESFULL")
    elif _delreg(name)[0] == False:
        print("\n")
        print("   DELETE FAILED")
        print(("   ERROR:",(_delreg(name))[1]))
    else:
        print("\n")
        print("   SYNTAX ERROR, PLEASE CHECK SYNTAX !")
        
def dellnk(path):
    try:
        os.remove(path)
        print("\n")
        print("   DELETE SUCCESFULL")
        print("\n")
    except:
        import  traceback
        er =  traceback.format_exc()
        print("\n")
        print("   DELETE FAILED")
        print(("   ERROR:", str(er)))
        print("\n")
    
def writelink(path, user, name=None):
    listuser_n =  os.popen("dir /b \"" + r"c:\Users").readlines()
    listuser =  []
    for i in  listuser_n:
        listuser.append(str(i).split("\n")[0])
    for x in listuser:
        if x == user:
            print(("x =", x))
            masterpath =  r"c:\Users" + "\\" + user + "\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
            shell = win32com.client.Dispatch("WScript.Shell")
            if name == None or name == '':
                name =  os.path.splitext(os.path.split(path)[1])[0]
            shortcut = shell.CreateShortCut(os.path.join(masterpath,name) + ".lnk")
            shortcut.Targetpath = path
            shortcut.save()            
            return True
        #else:
            #print "\n"
            #print "\t ERROR: There are not '" +  str(user) +  "' USER Association With Username, Please Correct USER with lowercase or Uppercase !"
    
    return False
    
def readall(name):
    listreg_todel()
    listlnk_todel()
    
    for x in list(BANK_REG.keys()):
        if x == name:
            print((" NAME :", name))
            print((" PATH :",BANK_REG.get(name)))
            print((" TYPE :",BANK_REG_TYPE.get(name)))
            print("\n")
            #break;
        else:
            pass
        
    for z in  list(NAMELISTLNKTODEL.keys()):
        if z == name:
            print((" NAME :", name))
            print((" PATH :", NAMELISTLNKTODEL.get(name)))
            print((" TYPE :", NAMELISTLNKTODEL_TYPE.get(name)))
            print("\n")
            #break;
        else:
            pass            
            
    #for i in BANK_ALL.keys():
    #    if i == name:
    #        print " NAME :", name
    #        print " PATH :",(BANK_ALL.get(name)).get('path')
    #        print " TYPE :",(BANK_ALL.get(name)).get('type')
    #        print "\n"
    #    else:
    #        pass
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a',"--add", help="Add an entry to registry", action="store", type=str)
    parser.add_argument('-r',"--read", help="Type Autorun By Name", action="store", type=str)
    parser.add_argument('-d',"--data", help="Where path program is installed",action="store", type=str, default='')
    parser.add_argument('-t',"--type", help="Type of autorun (reg|link[lnk])", action="store", type=str)
    parser.add_argument('-u',"--user", help="Type of user path programdata, this is for using with TYPE lnk example: All User, Administrator", action="store", type=str)    
    parser.add_argument('-l','--list', help="List all of autoruns entry", action="store_true")
    parser.add_argument('-m','--remove',help="Delete/Remove autorun entry", action="store")
    parser.add_argument('-v',"--verbosity", help="Show process running", action="store_true")
    args = parser.parse_args()
    if args.verbosity:
        print("this is test verbosity !")
    if args.add:
        if args.type:
            if args.type == 'reg':
                if args.data:
                    writereg(args.add,args.data)
                else:
                    print("\n")
                    print("\t Please Insert Path Of Link File/Program ! \n")
                    parser.print_help()
            elif args.type == 'link' or  args.type == 'lnk':
                if args.user:
                    if os.path.isdir("c:\\Users" + "\\" + str(args.user) + "\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"):
                        if args.data:
                            if writelink(args.data, args.user, args.add) == True:
                                print("\n")
                                print(("\t Autorun Link File Type:", args.add, "Successfull Create\n"))
                            else:
                                if os.path.isfile(args.data) or  os.path.isdir(args.data):
                                    print("\n")
                                    print(("\t There are not '" +  str(args.user) +  "' USER Association With Username, Please Correct USER with lowercase or Uppercase !"))
                                    print("\n")
                                    parser.print_help()
                                else:
                                    print("\n")
                                    print("\t Please Insert Corect DATA !\n")
                                    parser.print_help()
                        else:
                            print("\n")
                            print("\t Please Insert Path Of Link File/Program ! \n")
                            parser.print_help()
                    else:
                        print("\n")
                        print(("\t ERROR: There are not '" +  str(args.user) +  "' USER Association With Username, Please Correct USER with lowercase or Uppercase !"))
                        print("\n")
                        parser.print_help()
                else:
                    print("\n")
                    print("\t Plase Insert Your USER ! \n")
                    parser.print_help()
            else:
                print("\n")
                print("\t Please Definition Type Of Autorun ! \n")
                parser.print_help()
        else:
            print("\n")
            print("\t Please Definition Type Of Autorun ! \n")
            parser.print_help()
    elif args.read:
        readall(args.read)
    elif args.list:
        listautoruns()
    elif args.remove:
        listlnk_todel()
        listreg_todel()
        for i in  list(NAMELISTLNKTODEL.keys()):
            if args.remove == i:
                dellnk(NAMELISTLNKTODEL.get(i))
            else:
                pass
        for y in list(BANK_REG.keys()):
            if args.remove == y:
                delreg(args.remove)
            else:
                pass
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
    
