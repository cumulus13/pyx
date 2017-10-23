import os
import sys

class vcar:
    def __init__(self, parent=None):
        self.data = []
        self.databank = []
    
    def getFile(self):
        a = os.listdir(os.getcwd())
        for i in a:
            if os.path.splitext(os.path.abspath(i))[1] == 'vcf':
                self.data.append(os.path.abspath(i))
    
    def parse(self, data):
        if isinstance(data, list):
            pass
        else:
            return False
    
    def read(self):
        self.getFile()
        varChk = ['VERSION', 'N', 'FN', 'X-NICKNAME', 'TEL', 'NOTE', 'X-TINES_CONTACTED', 'X-LAST_TIME_CONTACTED', 'ENAIL', 'X-INTERNET', 'PHOTO']
        dataLine = []
        for i in self.data:
            data = open(i).readlines()
            for line in data:
                if line == 'BEGIN':
                    if len(dataLine) > 0:
                        self.databank.append(dataLine)
                    dataLine = []
                    continue
                dataLine.append(line)
                    
                
            