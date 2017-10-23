import checkArray
import sys
data = "['sat','tiga']"
cek = checkArray.checkArray()
#cek.check()
#print cek.check(data)

data2 = []
if len(sys.argv) > 2:
    for i in range(1,len(sys.argv)):
        data2.append(sys.argv[i])
else:
    pass

print "data2 = ", data2
data3 = []
print "len(data3) = ", len(data3)