import os
import sys
import re
import traceback

filename = os.path.split(sys.argv[0])[1] + " [file_from_rename] " + "[file_to_rename]"

def usage():
    print "\n"
    print "\t\tuse : " + str(filename) 
    
def rename_folder():
    try:
        if len(sys.argv) > 1:
            file_source = os.path.abspath(sys.argv[1])
            #file_dir_source = os.path.dirname(sys.argv[1])
            file_name_source = os.path.basename(file_source)
            if len(os.path.dirname(sys.argv[1])) < 1 or len(os.path.dirname(sys.argv[1])) == 0:
                    file_dir_source = os.getcwd()
            else:
                if os.path.isdir(os.path.dirname(sys.argv[1])):
                    file_dir_source = os.path.dirname(sys.argv[1])
                else:
                    os.system("cls")
                    usage()
                    sys.exit()
            try:
                file_dest = os.path.join(file_dir_source, sys.argv[2])
            except:
                usage()
            
            """print file_source
            print file_dir_source
            print file_name_source
            print file_dest
            """
            os.rename(file_source, file_dest)
            print "\n"
            print "rename : \"" + file_source + "\" ---> " + file_dest 
        else:
            usage()
    except:
        print "\n"
        error = sys.exc_info()
        error_1 = error[1]
        m = re.search("\[.*?\]", str(error_1))
        error_2 = str(error_1).split(str(m.group(0)))
        #print "m = ", str(m.group(0))
        print error_2[1] + " for ---> \"" + str(sys.argv[1]) + "\""
        #n = re.split("\[.*?\]", error_1)
        #print "n = ", n
    
def rename():
    try:
        if os.path.isdir(sys.argv[1]):
            rename_folder()
        else:
            if len(sys.argv) > 1:
                file_source = os.path.abspath(sys.argv[1])
                #file_dir_source = os.path.dirname(sys.argv[1])
                if len(os.path.dirname(sys.argv[1])) < 1 or len(os.path.dirname(sys.argv[1])) == 0:
                    file_dir_source = os.getcwd()
                else:
                    if os.path.isdir(os.path.dirname(sys.argv[1])):
                        file_dir_source = os.path.dirname(sys.argv[1])
                    else:
                        os.system("cls")
                        usage()
                        sys.exit()
                file_name_source = os.path.basename(file_source)
                #file_ext_source = os.path.splitext(file_name_source)
                if len(os.path.splitext(file_name_source)) > 1:
                    file_ext_source = os.path.splitext(file_name_source)[1]
                elif os.path.splitext(file_name_source)[1] == None:
                    file_ext_source = ""
                else:
                    file_ext_source = ""
                try:
                    file_dest_001 = os.path.join(file_dir_source, sys.argv[2])
                    file_dest = file_dest_001 + file_ext_source
                    #file_ext_dest = os.path.splitext(file_dest)
                    if len(os.path.splitext(file_dest)) > 1:
                        file_ext_dest = os.path.splitext(file_dest)[1]
                    elif os.path.splitext(file_dest)[1] == None:
                        file_ext_dest = ""
                    else:
                        file_ext_dest = ""

                except:
                    usage()
                
                #print "file_source = ", file_source
                #print "file_dir_source = ", file_dir_source
                #print "file_name_source = ", file_name_source
                #print "file_dest = ", file_dest
                #print "file_ext_source = ", file_ext_source
                
                os.rename(file_source, file_dest)
                print "\n"
                print "rename : \"" + file_source + "\" ---> " + os.path.join(file_dir_source, file_dest)
            else:
                usage()
    except:
        print "\n"
        #print traceback.format_exc()
        error = sys.exc_info()
        error_1 = error[1]
        try:
            m = re.search("\[.*?\]", str(error_1))
            error_2 = str(error_1).split(str(m.group(0)))
            #print "m = ", str(m.group(0))
            print error_2[1] + " for ---> \"" + str(sys.argv[1]) + "\""
            #n = re.split("\[.*?\]", error_1)
            #print "n = ", n
        except:
            pass
    
    
rename()