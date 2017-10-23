import os
import sys
import argparse
from optparse import OptionParser

__version__ = "1.0"
__test__ = "1.0"
__author__ = "licface"
__email__ = "licface@yahoo.com"
__sdk__ = "2.7"
__build__ = "2.7"
__platform__ = "windows"


class closed:
    def __init__(self):
        self.nircmd = r"c:\EXE\nircmd.exe"
        
    def sprocess(self, pattern):
        intlist_pre = []
        intlist = []
        pid = []
        a = os.popen(r"c:\exe\processx.exe | grep " + pattern).readlines()
        for i in a:
            i1 = str(i).split(" ")
            #print i1
            for x in i1:
                #print x
                i2 = ''
                try:
                    i2 = int(x)
                except:
                    pass
                if isinstance(i2,  int):
                    intlist_pre.append(i2)
            intlist.append(intlist_pre)
            intlist_pre = []
        #print intlist
        for z in intlist:
            pid.append(z[0])
        #print pid
        return pid
    
    def nclose(self, pid):
        os.system(self.nircmd + " closeprocess /" + str(pid))
    
    def close(self, name):
        os.system(self.nircmd + " closeprocess " + str(name))
        
    def usage(self):
        print "\n"
        #print (str(os.path.splitext(os.path.basename(__file__))[0]))
        #usage = "%s PROCESS_NAME [options]" % (str(os.path.splitext(os.path.basename(__file__))[0]))
        usage = "usage: %s PROCESS_NAME [options]" % (str(os.path.splitext(os.path.basename(__file__))[0]))
        parser = OptionParser(usage=usage)
        parser.add_option("-v", "--verbosity", help="verbosity running process", action="store_true")
        parser.add_option('-n', '--name', help="regex or realname of process, Example: %s plore"%(os.path.basename(str(__file__))), action="store", dest="name", type=str)
#        parser.add_option('PROCESSNAME', help="name process to be close", action="store")
        parser.add_option('-k', '--kill', help="name process to be close", action="store")
        (options, args) = parser.parse_args()
        
        #parser = argparse.ArgumentParser(usage=usage, argument_default="PROCESS_NAME")
        #parser = argparse.ArgumentParser(argument_default="PROCESS_NAME")
        #parser.add_argument("-v", "--verbosity", help="verbosity running process", action="store_true")        
        #parser.add_argument('-n', '--name', help="regex or realname of process, Example: %s plore"%(os.path.basename(str(__file__))), action="store", dest="name", type=str)
        #parser.add_argument('-k', '--kill', help="name process to be close", action="store")
        #args = parser.parse_args()
        """
        if args.kill:
            try:
                process = int(args.kill)
            except:
                process = args.kill
            if isinstance(process, int):
                self.nclose(process)
            else:
                self.close(process)
        elif args.name:
            print "ERERHE"
            print args.name
            pid = self.sprocess(args.name)
            for i in pid:
                print "PID =", pid
                self.nclose(i)
            #elif sys.argv[1] == "-h" or sys.argv[1] == "--h" or sys.argv[1] == "--help" or sys.argv[1] == "-help":
            #    parser.print_help()
        else:
            if len(sys.argv) > 1:
                try:
                    process = int(sys.argv[1])
                except:
                    process = sys.argv[1]
                if isinstance(process, int):
                    self.nclose(process)
                else:
                    self.close(process)                    
            else:
                parser.print_help()
        """
        if options.kill:
            try:
                process = int(args.kill)
            except:
                process = options.kill
            if isinstance(process, int):
                self.nclose(process)
            else:
                self.close(process)
        elif options.name:
            pid = self.sprocess(options.name)
            for i in pid:
                print "PID =", pid
                self.nclose(i)
        else:
            if len(sys.argv) > 1:
                try:
                    process = int(sys.argv[1])
                except:
                    process = sys.argv[1]
                if isinstance(process, int):
                    self.nclose(process)
                else:
                    self.close(process)                    
            else:
                parser.print_help()
                
if __name__ == "__main__":
    myclass = closed()
    myclass.usage()
