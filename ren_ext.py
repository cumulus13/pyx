import os
import sys
import datetime

def getdatetime_now():
    dt = datetime.datetime.now()
    d2 = dt.strftime('%Y%m%d_%H%M%S')
    return d2

PATTERN = []
if os.name == 'nt':
    PATTERN = os.popen("dir /s /b | grep .%s"%(sys.argv[1])).readlines()
else:
    for root, dirs, files in os.walk("."):
        #print "files =", files
        for i in files:
            if ".MP3" in i:
                PATTERN.append(os.path.abspath(os.path.join(root, i)))
        
#print PATTERN
#print "-" * 120
PATTERN_CLEAN = []
for i in PATTERN:
    #print "i =", i
    a = str(i).split("\n")[0]
    #print "os.path.splitext(i) =", os.path.splitext(a)
    #print "os.path.splitext(i)[-1] =", os.path.splitext(a)    
    #print "a =", a
    #print "-" * 120
    if os.path.isfile(a):
        if os.path.splitext(a)[-1] == ".MP3":
            PATTERN_CLEAN.append(a)

f = open(getdatetime_now() + ".txt", "w")
for i in PATTERN_CLEAN:
    b = os.path.splitext(i)
    os.renames(i, os.path.join(b[0] + ".mp3"))
    #print "Z =", os.path.join(b[0] + ".mp3")
    f.writelines(i + " --> " + os.path.join(b[0] + ".mp3\n"))
f.close()