import os, sys, errno, string

name = os.path.split(sys.argv[0])
name2 = name[1]
dataxx = "Me"
usage = """ usage : """ + name2 + """ [File Name]"""

def rarme():
    try:
        if (sys.argv > 0):

            #os.system('cls')
            data2 = sys.argv[1]

            if data2 == "-d":
                data3 = sys.argv[2]
                name_pre = os.path.splitext(sys.argv[2])[0]
                print "name_pre = ", str(name_pre)
                try:
                    if "\\" in data3:
                        data2c = str(name_pre).split("\\")  #for windows
                        data2b = data2c[-1]
                        name_dir_a = str(sys.argv[2]).split("\\")[-1]
                        name_dir_b = os.path.splitext(name_dir_a)
                        name_dir_001 = name_dir_b[0]
                        #print "data2b_A = ", data2b
                        #print "name_dir_001_A = ", name_dir_001
                        #print "dataxx_A = ", dataxx
                        #print "data_A = ", sys.argv[2]
                    else:
                        data2b = os.path.splitext(data3)
                        name_dir_001 = str(data2b[0])
                        print "name_dir_001 = ", str(data2b[0])
                        #print "data2b_B = ", data2b
                        #print "name_dir_001_B = ", name_dir_001
                        #print "dataxx_B = ", dataxx
                        #print "data_A = ", sys.argv[2]
                    len_data2b = len(data2b)
                except IndexError, e:
                    data2b = data3

                if (os.path.isdir(r'%tmp%\\' + dataxx)):
                    os.system("mkdir " + r"%tmp%\\" + '"' + dataxx + '"')
                    os.system("7z x " + "\"" + sys.argv[2] + "\"" + " -o" + "\"" + r"%tmp%\\" + dataxx + "\\\"" + name_dir_001 + "\""  + ' & c:\Apps\Snarl_CMD_1.0\Snarl_CMD.exe snShowMessage 20 "7zx [7z x]" "DONES" "f:\ICONS\7z.png"')
                    print "\n"
                else:
                    os.system("7z x " + "\"" + sys.argv[2] + "\"" + " -o" + "\"" + r"%tmp%\\Me" + "\"" + "\\\"" + name_dir_001 + "\""  + ' & c:\Apps\Snarl_CMD_1.0\Snarl_CMD.exe snShowMessage 20 "7zx [7z x]" "DONES" "f:\ICONS\7z.png"')
                    print "\n"

            elif data2 == "usage":
                os.system('cls')
                print "\n\n"
                print usage	

            else:             
                if (os.path.isdir(r'%tmp%\\' + dataxx)):
                    os.system("mkdir " + r"%tmp%\\" + '"' + dataxx + '"')
                    os.system("7z x " + '"' + sys.argv[1] + '"' + " -o" + "\"" + r"%tmp%\\" + dataxx + "\"" + ' & c:\Apps\Snarl_CMD_1.0\Snarl_CMD.exe snShowMessage 20 "7zx [7z x]" "DONES" "f:\ICONS\7z.png"')
                    print "\n"
                else:
                    os.system("7z x " + '"' + sys.argv[1] + '"' + " -o" + "\"" + r"%tmp%\\Me" + "\"" + ' & c:\Apps\Snarl_CMD_1.0\Snarl_CMD.exe snShowMessage 20 "7zx [7z x]" "DONES" "f:\ICONS\7z.png"')
                    print "\n"

        else:
            os.system('cls')
            print "\n\n"
            print usage	
    except IndexError, e:
        os.system('cls')
        print "\n\n"
        print "\t\t Please insert name of file want to be Decompress ! \n"
        print "\t\t", usage


if __name__ == '__main__':
    rarme()