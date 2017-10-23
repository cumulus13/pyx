import os
import sys
import progressbar
import time

########################################################################
class wconnect(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        super(wconnect, self)
        
    def getStatus(self):
        data1 = []
        data2 = {}
        data = os.popen('netsh wlan show interfaces').readlines()
        #print data
        #print '-' * 220
        for i in data:
            if i == '\n':
                pass
            else:
                data1.append(str(i).strip())
        #print data1
        #print '-' * 220
        for i in data1:
            data3 = str(i).split(": ")
            name = data3[0].strip()
            try:
                values = data3[1].strip()
            except:
                values = ''
            data2.update(
                {name: values,}
            )
        #print data2
        #print '-' * 220
        return data2
    
    def printstatus(self, status):
        max_len_status = []
        for i in status.keys():
            max_len_status.append(len(i))
        max_len_status = sorted(max_len_status, reverse= True)[0]
        #print status
        #print "=" * 220
        #print "status.keys() =", status.keys()
        #print "status.values() =", status.values()
        print status.keys()[0][:-1] + " " * (max_len_status - len(status.keys()[0][:-1])) + " :", status.get(status.keys()[0])
        for i in range(1, len(status)):
            print status.keys()[i] + " " * (max_len_status - len(status.keys()[i])) + " :", status.get(status.keys()[i])
        #for i in status:
            
        
    def connect(self, ssid, dev = None):
        if not dev:
            dev = ''
        bar = progressbar.ProgressBar(max_value= 100)
        os.system('netsh wlan connect {0} {1} {2} > NUL'.format(ssid, ssid, dev))
        data = self.getStatus()
        #print "data =", data
        #print '*' * 220
        #print "type(data) =", type(data)
        n = 0
        #bar.start()
        while 1:
            if data.get('SSID') == None:
                time.sleep(0.1)
                data = self.getStatus()
            else:
                if data.get('State') == "connected":
                    if data.get('SSID').lower() == str(ssid).lower():
                        bar.finish()
                        status = self.getStatus()
                        self.printstatus(status)
                        print "CONNECTED SUCCESSFULL"
                        break
                    else:
                        print "CAN'T CONNECT TO {0} !".format(ssid)
                        break;
                else:
                    data = self.getStatus()
                    n += 10
                    #if data.get('SSID').lower() == str(ssid).lower():
                        #bar.finish()
                        #status = self.getStatus()
                        #self.printstatus(status)
                        #print "CONNECTED SUCCESSFULL"
                        #break
                    #else:
                        #print "CONNECTED FAILED !"
                    bar.update(n)
                    time.sleep(0.5)
                    if n == 100:
                        print "CONNECTED FAILED !"
                        break
                            
        
        
if __name__ == '__main__':
    c = wconnect()
    c.connect(*sys.argv[1:])
        
        
        
    
    