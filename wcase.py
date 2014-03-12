import os
import sys
import traceback

filename = os.path.split(sys.argv[0])[1]
usage = "\t use : " + filename + " [upper | lower | cap[italize]/first ] [all]\n\t exp : " + filename + " upper all \"c:\\test\" -- make upper for all files in directory \"c:\\test\"\n\t       " + filename + " upper all -- make upper for all files in directory where youre did\n\t       "


def to_upper(data_input):
    if os.path.isfile(data_input):
        dtemp = []
        data = os.path.splitext(data_input)
        
        if data[1] == "" or data[1] == None:
            if data[0] != "":
                e00 = str(data[0]).upper()
                dtemp.append(e00)
            else:
                pass
        else:
            if " " in data[0]:
                d01 = str(data[0]).split(" ")
                for i in d01:
                    e01 = str(i).upper()
                    dtemp.append(e01)
                d02 = str(" ").join(dtemp) + str(data[1]).lower()
            else:
                d02 = str(data[0]).upper() + str(data[1]).lower()
                
            return d02
    else:
        pass

def to_lower(data_input):
    if os.path.isfile(data_input):
        dtemp = []
        data = os.path.splitext(data_input)
        
        if data[1] == "":
            if data[0] != "":
                e00 = str(data[0]).lower()
                dtemp.append(e00)
            else:
                pass
        else:
            if " " in data[0]:
                d01 = str(data[0]).split(" ")
                for i in d01:
                    e01 = str(i).lower()
                    dtemp.append(e01)
                d02 = str(" ").join(dtemp) + str(data[1]).lower()
            else:
                d02 = str(data[0]).lower() + str(data[1]).lower()
                
            return d02
    else:
        pass

def to_capitalize(data_input):
    if os.path.isfile(data_input):
        dtemp = []
        data = os.path.splitext(data_input)
        
        if data[1] == "":
            if data[0] != "":
                e00 = str(data[0]).capitalize()
                dtemp.append(e00)
            else:
                pass
        else:
            if " " in data[0]:
                d01 = str(data[0]).split(" ")
                for i in d01:
                    e01 = str(i).capitalize()
                    dtemp.append(e01)
                d02 = str(" ").join(dtemp) + str(data[1]).lower()
            else:
                d02 = str(data[0]).capitalize() + str(data[1]).lower()
                
            return d02
    else:
        pass

def to_rename(fr,to):
    if os.path.isfile(fr):
        os.rename(fr,to)
    else:
        pass

try:
    data_out = []
    if len(sys.argv) > 3:
        if os.path.isdir(sys.argv[3]):
            if sys.argv[2] == "all":
                data = os.popen("dir /b " + str(sys.argv[3])).readlines()
                for i in data:
                    z = str(i).split("\n")
                    data_out.append(z[0])
                if sys.argv[1] == "upper":
                    data_upper = []
                    for i in data_out:
                        d01 = to_upper(str(i))
                        to_rename(i,str(d01))
                        #data_upper.append(d01)
                    #print data_upper
                elif sys.argv[1] == "lower":
                    data_lower = []
                    for i in data_out:
                        d01 = to_lower(str(i))
                        to_rename(i,str(d01))
                        #data_lower.append(d01)
                    #print data_lower
                elif sys.argv[1] == "cap" or sys.argv[1] == "capitalize" or sys.argv[1] == "first":
                    data_cap = []
                    for i in data_out:
                        d01 = to_capitalize(str(i))
                        to_rename(i,str(d01))
                        #data_cap.append(d01)
                    #print data_cap
                else:
                    print "\n"
                    print usage
            else:
                if sys.argv[2] == "-s":
                    data = sys.argv[3]
                    if sys.argv[1] == "upper":
                        data_upper = []
                        for i in range(3, len(sys.argv)):
                            d01 = to_upper(str(sys.argv[i]))
                            to_rename(sys.argv[i],str(d01))
                            data_upper.append(d01)
                        print data_upper
                    elif sys.argv[1] == "lower":
                        data_lower = []
                        for i in range(3, len(sys.argv)):
                            d01 = to_lower(str(sys.argv[i]))
                            to_rename(sys.argv[i],str(d01))
                            data_lower.append(d01)
                        print data_lower
                    elif sys.argv[1] == "cap" or sys.argv[1] == "capitalize" or sys.argv[1] == "first":
                        data_cap = []
                        for i in range(3, len(sys.argv)):
                            d01 = to_capitalize(str(sys.argv[i]))
                            to_rename(sys.argv[i],str(d01))
                            data_cap.append(d01)
                        print data_cap
                    else:
                        print "\n"
                        print usage
                else:
                    print "\n"
                    print usage
        else:
            if sys.argv[2] == "all":
                data = os.popen("dir /b ").readlines()
                for i in data:
                    z = str(i).split("\n")
                    data_out.append(z[0])
                if sys.argv[1] == "upper":
                    data_upper = []
                    for i in data_out:
                        d01 = to_upper(str(i))
                        to_rename(i,str(d01))
                        #data_upper.append(d01)
                    #print data_upper
                elif sys.argv[1] == "lower":
                    data_lower = []
                    for i in data_out:
                        d01 = to_lower(str(i))
                        to_rename(i,str(d01))
                        #data_lower.append(d01)
                    #print data_lower
                elif sys.argv[1] == "cap" or sys.argv[1] == "capitalize" or sys.argv[1] == "first":
                    data_cap = []
                    for i in data_out:
                        d01 = to_capitalize(str(i))
                        to_rename(i,str(d01))
                        #data_cap.append(d01)
                    #print data_cap
                else:
                    print "\n"
                    print usage
            else:
                print "\n"
                print usage
                
    else:
        if sys.argv[2] == "all":
            data = os.popen("dir /b ").readlines()
            for i in data:
                z = str(i).split("\n")
                data_out.append(z[0])
            if sys.argv[1] == "upper":
                data_upper = []
                for i in data_out:
                    d01 = to_upper(str(i))
                    to_rename(i,str(d01))
                    #data_upper.append(d01)
                #print data_upper
            elif sys.argv[1] == "lower":
                data_lower = []
                for i in data_out:
                    d01 = to_lower(str(i))
                    to_rename(i,str(d01))
                    #data_lower.append(d01)
                #print data_lower
            elif sys.argv[1] == "cap" or sys.argv[1] == "capitalize":
                data_cap = []
                for i in data_out:
                    d01 = to_capitalize(str(i))
                    to_rename(i,str(d01))
                    #data_cap.append(d01)
                #print data_cap
            else:
                print "\n"
                print usage
        else:
            print "\n"
            print usage

except:
    print "\n"
    print usage
    print "-"*80
    data_e = traceback.format_exc()
    print "programming development : "
    print "\t " + str(data_e)
    
    
