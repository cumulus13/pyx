import os
import sys
"""
   Search File or Directory in PATH Environment
"""
PATH  = os.getenv("PATH")
def usage():
    print "\n"
    print "\t Usage: ",os.path.split(__file__)[1],"[File to Search]"

def search():
    result = []
    PATH2 = str(PATH).split(";")
    for i in range(0,len(PATH2)):
        print "  Search in",str(PATH2[i]).strip(),"..."
        dsearch = os.popen("dir /s /b \"" + str(PATH2[i]).strip() + "\\\"\"*" + sys.argv[1] + "*\"").readlines()
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
                print "\t FOUND: [%s]" %(os.path.abspath(f))
                result.append(os.path.abspath(f))
                
    if len(result) > 1:
        print "\n"
        print "  FOUND %d File/Directory in PATH: "%(len(result))
        print "\n"
        for g in range(0, len(result)):
            print "\t",str((g + 1)) + ".","[" + str(PATH2[i]).strip() + "] -->",result[g]
    else:
        pass

if __name__ == "__main__":
    if len(sys.argv) > 1:
        search()
    else:
        usage()