import re
class checkArray:
    def __init__(self):
        pass
        
    def check(self,data_input):
        m = re.split("\[(.*?)\]", str(data_input))
        if m[-1] == "":
            #print "True"
            return True
        else:
            #print "False"
            return False