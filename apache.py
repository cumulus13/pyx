import Cservice
import pywintypes
import dplay2
import argparse
import sys
import time

#workstation = WService.WService("Workstation")
#workstation.start()
#workstation.fetchstatus("running", 10)
#workstation.stop()
#workstation.fetchstatus("stopped")

svc_ctr = Cservice.WService("wampapache")

def usage():
    print "\n"
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbosity", help="Show Detail Process running", action="store_true")
    parser.add_argument("-c", "--config", help="Set config start Process (auto|demand|disable|delayed-auto)", action="store", type=str)
    parser.add_argument("CONF", help="start|stop|restart|status", action="store", type=str)
    #print "len(sys.argv) =", len(sys.argv)
    if len(sys.argv) > 1:
        args =  parser.parse_args()
        if args.CONF:
            if args.CONF == "start":
                if args.verbosity:
                    print "\t set", svc_ctr.getname()[0], "to start/running ...\n"
                    time.sleep(2)
                control("start")
            elif args.CONF == "stop":
                if args.verbosity:
                    print "\t set", svc_ctr.getname()[0], "to stop ...\n"
                    time.sleep(2)
                control("stop")
            elif args.CONF == "restart":
                if args.verbosity:
                    print "\t set", svc_ctr.getname()[0], "to restart/re-running ...\n"
                    #time.sleep(2)
                control("restart")
                control("status")
            elif args.CONF == "status":
                if args.verbosity:
                    print "\t get service status of", svc_ctr.getname()[0], " ...\n"
                    time.sleep(2)
                control("status")
            else:
                parser.print_help()
        else:
            parser.print_help()
            
        if args.config:
            if args.verbosity:
                print "\t set", svc_ctr.getname()[0], "to start with", args.config, "\n"
                time.sleep(2)
            setstart(args.config)
    else:
        parser.print_help()

def control(status):
    if status == "start":
        svc_ctr.start()
    elif status == "stop":
        svc_ctr.stop()
    elif status == "restart":
        svc_ctr.restart()
    elif status == "status":
        print "\t Service", svc_ctr.getname()[0], "is", svc_ctr.status()
        
def setstart(start):
    svc_ctr.setstartup(start)
    
if __name__ == "__main__":
    usage()