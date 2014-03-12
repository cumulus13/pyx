import Cservice
import sys, os

def ctr(data):
    svc = Cservice.WService(data)
    if len(sys.argv) > 2:
        if sys.argv[2] == "start":
            svc.start()
            print "\n"
            print "\t Service " + str(data) + " is " + svc.status() 
        elif sys.argv[2] == "stop":
            svc.stop()
            print "\n"
            print "\t Service " + str(data) + " is " + svc.status() 
        elif sys.argv[2] == "restart":
            svc.restart()
            print "\n"
            print "\t Service " + str(data) + " is " + svc.status() 
        elif sys.argv[2] == "status":
            print "\n"
            print "\t Service " + str(data) + " is " + svc.status() 
        else:
            print "\n"
            print "\t" + usage
    else:
        print "\n"
        print "\t" + usage
    
    
if __name__ == '__main__':
    ctr(sys.argv[1])