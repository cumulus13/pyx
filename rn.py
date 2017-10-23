import os
import sys
import re
import traceback
import argparse

__version__ = "1.0"
__filename__ = os.path.basename(sys.argv[0])
__author__ = "licface"
__url__ = "licface@yahoo.com"
__target__ = "all"
__build__ = "2.7"


def usage():
    parser = argparse.ArgumentParser()
    parser.add_argument('-e','--with-extention', help='Rename File/Dirs with extention',action='store_true')
    parser.add_argument('-n','--no-with-extention', help='No rename extention, name file/dirs only',action='store_true')
    parser.add_argument('-c','--count', help='rename with add count (000-*) if file is exists',action='store_true')
    parser.add_argument('-o', '--overwrite', help='rename file and overwrite file exists only',action='store_true')
    parser.add_argument('-s',help='start count, with end unlimited',action='store')
    parser.add_argument('-U','--upper', help='Rename file to UpperCase', action='store_true')
    parser.add_argument('-l','--lower',help='Rename file to LowerCase', action='store_true')
    parser.add_argument('-T','--tile',help='Rename file to upper for fist words Only each words', action='store_true')
    parser.add_argument('-r','--recursive', help='Rename file with/and subdirectory', action='store_true')
    parser.add_argument('-f','--find', help='Find and rename file with pattern', action='store_true')
    parser.add_argument('-p','--pattern', help='Pattern for find and rename function', action='store')
    if len(sys.argv) > 1:
        pass
    else:
        parser.print_help()


def usage2():
    print "\n"
    print "\t\tuse : " + str(__filename__) + " [directory_contain_of]\\*.xx [directory_contain_of]\\*.zz"

def ren_multi(data_list,to_rename):
    h = []
    for i in data_list:
        h.append(i)

    h.pop(-1)
    h.append(to_rename)

    z = ""
    for x in h:
        z += x

    return z

    
def rename():
    try:
        if len(sys.argv) > 1:
            if sys.argv[1][0:2] == "*." or sys.argv[1][1] == "." or "*." in sys.argv[1]:
                if sys.argv[-1][0:2] == "*." or sys.argv[-1][1] == "." or "*." in sys.argv[2] or sys.argv[2] == "-d" or sys.argv[2] == "-depth" or sys.argv[2] == "--depth":
                    if os.path.split(sys.argv[1])[0] == '':
                        dir_source = os.getcwd()
                        file_dir_source = os.path.join(os.getcwd(), sys.argv[1])
                        if sys.argv[2] == "-d" or sys.argv[2] == "-depth" or sys.argv[2] == "--depth":
                            data_source = os.popen("dir /b /s \"" + str(dir_source) + "\\\"" + "\"" + sys.argv[1] + "\"").readlines()
                            #print data_source
                            for i in data_source:
                                data_ren = os.path.join(dir_source,str(i).split("\n")[0])
                                #print "AAA"
                                #print data_ren
                                data_in = os.path.splitext(data_ren)
                                data_out = ren_multi(data_in, str(sys.argv[-1]).split("*")[-1])
                                print " RENAME: %s --> %s" %(str(data_ren),str(data_out))
                                #be Carefully
                                try:
                                    os.rename(data_ren, data_out)
                                except WindowsError:
                                    pass

                        else:
                            data_source = os.popen("dir /b \"" + str(dir_source) + "\\\"" + "\"" + sys.argv[1] + "\"").readlines()
                            #print data_source
                            for i in data_source:
                                data_ren = os.path.join(dir_source,str(i).split("\n")[0])
                                #print "BBB"
                                #print data_ren
                                data_in = os.path.splitext(data_ren)
                                data_out = ren_multi(data_in, str(sys.argv[2]).split("*")[-1])
                                print " RENAME: %s --> %s" %(str(data_ren),str(data_out))
                                #be Carefully
                                try:
                                    os.rename(data_ren, data_out)
                                except WindowsError:
                                    pass
                    else:
                        dir_source = os.path.split(sys.argv[1])[0]
                        file_dir_source = sys.argv[1]
                        if sys.argv[2] == "-d" or sys.argv[2] == "-depth" or sys.argv[2] == "--depth":
                            data_source = os.popen("dir /b /s \"" + str(dir_source) + "\\\"" + "\"" + os.path.split(sys.argv[1])[1] + "\"").readlines()
                            #print data_source
                            for i in data_source:
                                data_ren = os.path.join(dir_source,str(i).split("\n")[0])
                                #print "CCC"
                                #print data_ren
                                data_in = os.path.splitext(data_ren)
                                data_out = ren_multi(data_in, str(sys.argv[-1]).split("*")[-1])
                                print " RENAME: %s --> %s" %(str(data_ren),str(data_out))
                                #be Carefully
                                try:
                                    os.rename(data_ren, data_out)
                                except WindowsError:
                                    pass
                        else:
                            data_source = os.popen("dir /b \"" + str(dir_source) + "\\\"" + "\"" + os.path.split(sys.argv[1])[1] + "\"").readlines()
                            #print data_source
                            for i in data_source:
                                data_ren = os.path.join(dir_source,str(i).split("\n")[0])
                                #print "DDD"
                                #print data_ren
                                data_in = os.path.splitext(data_ren)
                                data_out = ren_multi(data_in, str(sys.argv[2]).split("*")[-1])
                                print " RENAME: %s --> %s" %(str(data_ren),str(data_out))
                                #be Carefully
                                try:
                                    os.rename(data_ren, data_out)
                                except WindowsError:
                                    pass
                else:
                    usage2()
            
            elif len(os.path.dirname(sys.argv[1])) < 1 or len(os.path.dirname(sys.argv[1])) == 0:
                    file_source = os.path.abspath(sys.argv[1])
                    #file_dir_source = os.path.dirname(sys.argv[1])
                    file_name_source = os.path.basename(file_source)
                    file_dir_source = os.getcwd()
                    try:
                        file_dest = os.path.join(file_dir_source, sys.argv[2])
                    except:
                        usage()
                    #Process Rename
                    if os.path.isfile(sys.argv[2]) == False:
                        os.rename(file_source,file_dest)
                        print "\n"
                        print "rename : \"" + file_source + "\" ---> " + file_dest 
                    else:
                        usage()
            else:
                if os.path.isdir(os.path.dirname(sys.argv[1])):
                    try:
                        file_dir_source = os.path.dirname(sys.argv[1])
                        file_dest = os.path.join(file_dir_source, sys.argv[2])
                    except:
                        print "\n"
                        print "\t FILE NOT FOUND: File want to rename Not Found !"
                        usage()
                    #Process Rename
                    if os.path.isfile(sys.argv[2]) == False:
                        if os.path.isfile(os.path.abspath(sys.argv[1])):
                            os.rename(sys.argv[1],file_dest)
                            print "\n"
                            print "rename : \"" + str(os.path.abspath(sys.argv
                        [1])) + "\" ---> " + file_dest 
                        else:
                            print "\n"
                            print "\t FILE NOT FOUND: File want to rename Not Found !"
                            usage()
                    else:
                        usage()
                else:
                    os.system("cls")
                    usage()
                    sys.exit()
            
        else:
            usage()
    except:
        print "\n"
        e = traceback.format_exc()
        error = sys.exc_info()
        error_1 = error[1]
        m = re.search("\[.*?\]", str(error_1))
        print "error = ", e
        #error_2 = str(error_1).split(str(m.group(0)))
        #print "m = ", str(m.group(0))
        #print error_2[1] + " for ---> \"" + str(sys.argv[1]) + "\""
        #n = re.split("\[.*?\]", error_1)
        #print "n = ", n
    
    
rename()
#print ren_multi((r"c:\Program Files\7zip\sa",".py"), ".pyw")