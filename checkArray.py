import re
class checkArray:
    def __init__(self):
        pass
        
    def check(self,data_input):
        m1 = str(data_input).split(",")
        print "M1 = ", m1
        m = str(m1[-1])
        print "M[-1] = ", m[-1]
        #m = re.split("\[(.*?)\]", str(data_input))
        if m[-1] == "]":
            print "M = ", m
            #print "True"
            return True
        else:
            print "M = ", m
            #print "False"
            return False
        
#data = ['satu','dua','tiga']
data = '[]'
cek = checkArray()
print cek.check(data)