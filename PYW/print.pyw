import win32ui
import sys

def printx(data):
    dc = win32ui.CreateDC()
    dc.CreatePrinterDC()
    dc.StartDoc(data)
    
if __name__ == '__main__':
    data = sys.argv[1]
    printx(data)