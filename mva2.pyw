import optparse
import sys
import os
import traceback
import shutil
import re
import sendgrowl

__version__ = "2.4"
__author__ = "licface"
__url__ = "licface@yahoo.com"
__target__ = "all"
__build__ = "2.7"
__error__ = traceback.format_exc()
__filename__ = os.path.basename(sys.argv[0])
__help__ = """  This is a multiple choise mover
  File or Directory with python script

  Example: - %s DATA01 [DATA02] [DATA03] DIR_DESTINATION

           - %s *FILE01* [DATA02] """ %(str(__filename__),str(__filename__))
__test__ = "0.1"
__changelog__ = "change os.path.realpath --> os.path.abspath"

class process:
    def __init__(self):
        self.result_error = []
        self.result_overwrite = []
        self.publicTo = None

    def sendnotify(self, msg):
        title = "mva"
        appname = "mva"
        event = "mva - move file with pattern"
        icon = os.path.join(os.path.dirname(__file__), 'mva.png')
        growl = sendgrowl()
        growl.publish(appname, event, title, msg, iconpath=icon)

    def moveAll(self,listFrom=None,listTo=None):
        if listFrom != None:
            for i in listFrom:
                os.system("move /Y \"" + str(i) + "\"" + " \"" + listTo + "\"")
        else:
            listFrom = self.result_overwrite
            for i in listFrom:
                os.system("move /Y \"" + str(i) + "\"" + " \"" + listTo + "\"")

    def existConfr(self, _from=None, _to=None):
        if _from == None:
            for i in self.result_overwrite:
                if i != self.result_overwrite[-1]:
                    _from = i
                    _to = self.publicTo
                    q = raw_input(" FILE EXISTS: \"" + os.path.basename(_from) + "\"; Overwrite ? (y[[Y]es]/n[[N]o][ALL/all]; Default: n[N][o[O]]: ")
                    if q == "y" or q == "Y" or q == "Yes" or q == "yes" :
                        try:
                            os.system("move /Y \"" + _from + "\"" + " \"" + _to + "\"")
                        except:
                            raise WindowsError('MOVE SYSTEM ERROR: ' + str(_from))
                    elif q == "n" or q == "N" or q == "no" or q == "No":
                        pass
                    elif q == "ALL" or q == "all":
                        try:
                            self.moveAll(listTo=_to)
                            print "\n"
                            print " RESULT: ALL OK"
                            sys.exit()
                        except:
                            print "\n"
                            print __error__
                    #else:
                    #	pass
                else:
                    print "\n"
                    print __help__
                    sys.exit()

        else:
            q = raw_input(" FILE EXISTS: \"" + os.path.basename(_from) + "\"; Overwrite ? (y[[Y]es]/n[[N]o][ALL/all]; Default: n[N][o[O]]: ")
            if q == "y" or q == "Y" or q == "Yes" or q == "yes" :
                try:
                    os.system("move /Y \"" + _from + "\"" + " \"" + _to + "\"")
                except:
                    raise WindowsError('MOVE SYSTEM ERROR: ' + str(_from))
            elif q == "n" or q == "N" or q == "no" or q == "No":
                pass
            elif q == "ALL" or q == "all":
                self.moveAll(listTo=_to)
            else:
                pass
            
    def start_moved(self, pattern, _to, excp=None, verbosity=None):
        """pattern must have "*", exp: *data*, data*, *data"""
        if os.path.isdir(_to) == False:
            try:
                os.mkdir(os.path.abspath(_to))
            except:
                if verbosity:
                    print "error: ", str(__error__) 
                    self.sendnotify("error: " + str(__error__) )                
                #raise WindowsError("MAKE DIR: Can't make destination Directory")
            
        pre_dir_data = os.path.dirname(pattern)
        #print "pre_dir_data =", pre_dir_data
        if pre_dir_data == '':
            pre_dir_data = os.getcwd()
            pre_data1 = os.popen("dir /b \"" + str(pattern) + "\"").readlines()
        elif pre_dir_data == None:
            pre_dir_data = os.getcwd()
            pre_data1 = os.popen("dir /b \"" + str(pattern) + "\"").readlines()
        else:
            pre_data1 = os.popen("dir /b \"" + pattern + "\"").readlines()
        
        pre_data2 = []
        excpd = []
        #print "pre_data1 A =", pre_data1
        if not excp == None:
            #print "excp =", excp
            a = re.split("'|,", excp)
            #print "a 2 =", a
            for b in a:
                c = str(b).strip()
                #print "c =", c
                excpd.append(c)
            for d in excpd:
                e = d +  "\n"
                #print "e =", e
                del(pre_data1[pre_data1.index(e)])
        #print "pre_data1 B =", pre_data1
        for i in pre_data1:
            if os.path.abspath(str(i).split("\n")[0]) != os.path.abspath(str(_to).split("\n")[0]):
                x = os.path.join(pre_dir_data,str(i).split("\n")[0])
                pre_data2.append(x)
        pre_data2.append(_to)
        #print "pre_data2 A =", pre_data2
        for k in pre_data2:
            if os.path.abspath(__file__) in k:
                del(pre_data2[pre_data2.index(k)])
        #print "pre_data2 B =", pre_data2        
        self.moved(pre_data2)

    def moved(self, argv, excp=None, overwrite=None, verbosity=None):
        #print "ARGV 1 = ", argv
        for t in argv:
            if os.path.abspath(__file__) in t:
                del(argv[argv.index(t)])
        #print "ARGV 2 = ", argv
        to_ = os.path.abspath(argv[-1])
        #print "to_ =", to_
        if not excp == None:
            #print "excp not none =", excp
            if isinstance(excp, list):
                for j in excp:
                    c = str(j).strip()
                    del(argv[argv.index(c)])
            else:
                a = re.split("'|,", excp)
                #print "ARGV 3 =", argv
                #print "a =", a
                for b in a:
                    c = str(b).strip()
                    try:
                        del(argv[argv.index(c)])
                    except:
                        pass
                #print "ARGV 4 =", argv
        for i in range (0, len(argv) - 1):
            #print 'argv[i] =', argv[i]
            if os.path.isfile(os.path.abspath(argv[i])) == True:
                try:
                    if os.path.isfile(os.path.abspath(argv[i])):
                        shutil.move(os.path.abspath(argv[i]), to_)
                        print " MOVED FILE: \"" + os.path.abspath(argv[i]) + "\" --> " + to_
                        self.sendnotify("MOVED FILE: \"" + os.path.abspath(argv[i]) + "\" --> " + to_)
                except:
                    if verbosity:
                        print "Error: ", traceback.format_exc()
                        self.sendnotify("Error: " + traceback.format_exc())
                    print " MOVED FILE [ERROR]: \"" + os.path.abspath(argv[i]) + "\" --> " + to_ + " [ERROR]"
                    self.sendnotify("MOVED FILE [ERROR]: \"" + os.path.abspath(argv[i]) + "\" --> " + to_ + " [ERROR]")
                    self.result_error.append(os.path.abspath(argv[i]))

            elif os.path.isdir(os.path.abspath(argv[i])) == True:
                try:
                    shutil.move(os.path.abspath(argv[i]), to_)
                    print " MOVED DIRECTORY: \"" + os.path.abspath(argv[i]) + "\" --> " + to_
                    self.sendnotify("MOVED DIRECTORY: \"" + os.path.abspath(argv[i]) + "\" --> " + to_)
                except:
                    if verbosity:
                        print "Error: ", __error__
                        self.sendnotify("Error: " + str(__error__))
                    print " MOVED DIRECTORY [ERROR]: \"" + os.path.abspath(argv[i]) + "\" --> " + to_ + " [ERROR]"
                    self.sendnotify("MOVED DIRECTORY [ERROR]: \"" + os.path.abspath(argv[i]) + "\" --> " + to_ + " [ERROR]")
                    self.result_error.append(os.path.abspath(argv[i]))
            elif "*" in argv[i]:
                #print "start start move"
                if not excp == None:
                    self.start_moved(argv[i], to_, excp, verbosity)
                else:
                    self.start_moved(argv[i], to_, verbosity=verbosity)

    def usage(self, print_help=None):
        parser = optparse.OptionParser()
        parser.add_option("-e", "--excp", help="Exception Will not be moving (example: \"data1, data2,data3, data4\"), format must with single or double quota", action="store")
        parser.add_option("-w", "--overwrite", help="Overwrite moving method of All of files",  action="store_true")
        parser.add_option("-v", "--verbosity", help="Print process running", action="store_true")
        option, args_pre = parser.parse_args(sys.argv)
        #print "args_pre =", args_pre
        args = []
        for i in args_pre:
            o = os.path.abspath(i)
            args.append(o)
        help_key = ['-h', '--h', '--h', '--help', '-help', '--help']
        if print_help:
            parser.print_help()
        #print "len(sys.argv) =", len(sys.argv)
        if len(sys.argv) > 1:
            for i in help_key:
                if str(sys.argv[1]).lower() == i:
                    parser.print_help()
                    self.sendnotify(str(parser.print_help()))
                    break;
            for h in args:
                if str(h).strip in help_key:
                    del(args[args.index(h)])
            if option.excp:
                if option.verbosity:
                    self.moved(args, option.excp, verbosity=True)
                    self.check_result()
                else:
                    self.moved(args, option.excp)
                    self.check_result()
            else:
                self.moved(args)
                self.check_result()
        else:
            parser.print_help()
            self.sendnotify(str(parser.print_help()))
            

    def check_result(self):
        if len(self.result_error) == 1:
            print " RESULT: ERROR", len(self.result_error), " Item: "
            print "\t [ERROR] --> ", self.result_error[0]
            self.sendnotify(" RESULT: ERROR " + len(self.result_error) + " Item: ")
            self.sendnotify("[ERROR] --> " + str(self.result_error[0]))
        elif len(self.result_error) > 1:
            print " RESULT: ERROR", len(self.result_error), " Items: "
            self.sendnotify(" RESULT: ERROR", len(self.result_error), " Items: ")
            for x in self.result_error:
                print "\t [ERROR] --> error moving file:", x
                self.sendnotify("[ERROR] --> error moving file: " + x)
        else:
            print "\n"
            print " RESULT: ALL OK"
            self.sendnotify("RESULT: ALL OK")
            
if __name__ == '__main__':
    c = process()
    c.usage()
