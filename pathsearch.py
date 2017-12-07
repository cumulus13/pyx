import os
import sys
from make_colors import make_colors
"""
   Search File or Directory in PATH Environment
"""
PATH  = os.getenv("PATH")
def usage():
    print "\n"
    print "\t Usage: ",os.path.split(__file__)[1],"[File to Search]"
    
def search():
    result = []
    result_path = []
    PATH2 = str(PATH).split(";")
    for i in range(0,len(PATH2)):
        print "  Search in", make_colors(str(PATH2[i]).strip(), 'yellow'),"..."
        if 'win' in sys.platform:
            dsearch = os.popen("dir /s /b \"" + str(PATH2[i]).strip() + "\\\"\"*" + sys.argv[1] + "*\"").readlines()
        else:
            dsearch = []
            for root, dirs, files in os.walk(path):
                if len(files) > 0:
                    for i in files:
                        dsearch.append(os.path.join(root, i))
        d1 = str(sys.argv[1]).split('*')
        # print len(d1)
        if len(d1) > 0:
            if d1[0] == None or d1[0] == '':
                d = d1[1]
            else:
                d = d1[0]
        for x in dsearch:
            if d in x:
                e = str(x).split("\n")
                f = str(e[0])
                print "\t " + make_colors("FOUND:", 'white', 'red', ['bold', 'blink']) + " " + "[" + make_colors("%s"%(os.path.abspath(f)), 'blue', 'white') + "]"
                result.append(os.path.abspath(f))
                result_path.append(PATH2[i])
                
    if len(result) > 1:
        print "\n"
        print "  " + make_colors("FOUND %d File/Directory in PATH: "%(len(result)), 'white', 'blue')
        print "\n"
        for g in range(0, len(result)):
            print "\t",str((g + 1)) + ".","[" + make_colors(str(result_path[range(0, len(result)).index(g)]).strip(), 'yellow') + "] " + make_colors("-->", 'green'), make_colors(result[g], 'cyan')
    else:
        pass

if __name__ == "__main__":
    if len(sys.argv) > 1:
        search()
    else:
        usage()