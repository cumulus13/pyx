import os
import sys
import msvcrt

__version__ = "0.5"
__filename__ = os.path.basename(sys.argv[0])
__author__ = "licface"
__url__ = "licface@yahoo.com"
__target__ = "all"
__build__ = "2.7"
__test__ = "0.1"

def getPutch(prompt="\t Are you want to delete the original source ? (y[[Y]es]/n[[N]o]) : "):
    for x in prompt:
        msvcrt.putch(x)
        
    z = msvcrt.getch()
    msvcrt.putch("\n")
    return z
        
def usage():
    print "\n"
    print "\t\tuse : " + os.path.split(sys.argv[0])[1] + " [file_to_rar] "

def on_rm_error(func, path, exc_info):
    os.chmod(path, stat.S_IWRITE)
    os.unlink(path)

def multi_del(data):
    #q = raw_input("\t Are you want to delete the original source ? (y[[Y]es]/n[[N]o]) : ")
    q = getPutch()
    if q == "y" or q == "Y" or q == "Yes" or q == "yes" or q == "y" or q == "Y" or q == "Yes" or q == "yes":
        for i in data:
            if os.path.isdir(os.path.abspath(i)):
                shutil.rmtree(data_rar_02,onerror = on_rm_error)
            else:
                try:
                    os.remove(os.path.abspath(i))
                except:
                    try:
                        os.system("del " + str(os.path.abspath(i)))
                    except:
                        raise ScriptError("Can't use os.system !")
    elif q == "n" or q == "N" or q == "no" or q == "No" or q == "n" or q == "N" or q == "no" or q == "No":
        sys.exit()
    else:
        print "\n"
        print "\t You no select \'Y\' or \'N\' "
        print "\t Bye ... !"
        sys.exit()

def confr_del(data):
    if isinstance(data, (list,tuple)):
        multi_del(data)
    elif os.path.isdir(data):
        #q = raw_input("\t Are you want to delete the original source folder ? (y[[Y]es]/n[[N]o]) : ")
        q = getPutch()
        if q == "y" or q == "Y" or q == "Yes" or q == "yes" or q == "y" or q == "Y" or q == "Yes" or q == "yes" :
            shutil.rmtree(data,onerror = on_rm_error)
        elif q == "n" or q == "N" or q == "no" or q == "No":
            sys.exit()
        else:
            print "\n"
            print "\t You no select \'Y\' or \'N\' "
            print "\t Bye ... !"
            sys.exit()
    else:
        #q = raw_input("\t Are you want to delete the original source ? (y[[Y]es]/n[[N]o]) : ")
        q = getPutch()
        if q == "y" or q == "Y" or q == "Yes" or q == "yes" or q == "y" or q == "Y" or q == "Yes" or q == "yes" :
            try:
                os.system("del \"" + data + "\"")
            except:
                os.remove(data)
        elif q == "n" or q == "N" or q == "no" or q == "No" or q == "n" or q == "N" or q == "no" or q == "No":
            sys.exit()
        else:
            print "\n"
            print "\t You no select \'Y\' or \'N\' "
            print "\t Bye ... !"
            sys.exit()

def multi_rar(name_rar):
    for i in sys.argv:
        if "*" in sys.argv:
            data_rar_to = os.popen("dir /b \"" + os.path.abspath(sys.argv[int(sys.argv.index("*"))])).readlines()
            for i in data_rar_to:
                x = os.path.abspath(str(i).split("\n")[0])
                os.system("rar a \"" + name_rar + ".rar\" \"" + x + "\"") 

            #os.system("rar t \"" + name_rar + ".rar\" ") 


def rarme(data):
    try:
        if(len(data) > 1):
            data_rar_01 = sys.argv[1]
            data_rar_02 = os.path.splitext(sys.argv[1])
            if len(sys.argv) == 2:	
                os.system("rar a \"" + data_rar_02[0] + ".rar\" \"" + sys.argv[1] + "\"") 
                os.system("rar t \"" + data_rar_02[0] + ".rar\" ") 
                print "\n"
                confr_del(data_rar_01)
            elif len(sys.argv) == 3:
                if data_rar_02[1] == '.rar':
                    os.system("rar a \"" + sys.argv[2] + "\" \"" + sys.argv[1] + "\"") 
                    os.system("rar t \"" + sys.argv[2] + "\" ") 
                else:
                    os.system("rar a \"" + os.path.splitext(sys.argv[3])[0] + ".rar\" \"" + sys.argv[1] + "\"") 
                    os.system("rar t \"" + os.path.splitext(sys.argv[3])[0] + ".rar\" ") 
                    print "\n"
                    confr_del(data_rar_01)
            elif len(sys.argv) > 2:
                data_rar_02 = os.path.splitext(sys.argv[-1])
                data_file_rar = []
                if data_rar_02[1] == '.rar':
                    for i in range(1,len(sys.argv) - 1):
                        os.system("rar a \"" + sys.argv[-1] + "\" \"" + sys.argv[i] + "\"") 
                        data_file_rar.append(os.path.abspath(sys.argv[i]))
                        data_file_rar.append(os.path.abspath(i))
                    os.system("rar t \"" + sys.argv[-1] + "\" ") 
                    confr_del(data_file_rar)
                elif "*" in sys.argv:
                    multi_rar(sys.argv[-1])
                else:
                    for i in range(1,len(sys.argv) - 1):
                        os.system("rar a \"" + data_rar_02[0] + ".rar\" \"" + sys.argv[i] + "\"") 
                        data_file_rar.append(os.path.abspath(sys.argv[i]))
                        data_file_rar.append(os.path.abspath(i))
                    os.system("rar t \"" + data_rar_02[0] + ".rar\" ") 
                    confr_del(data_file_rar)
        else:
            usage
    except IndexError, e:
        print "ERROR"
        print e

if __name__ == '__main__':
    try:
        data = sys.argv[1]
        rarme(data)
    except IndexError, e:
        usage()
