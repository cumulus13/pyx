import sys
import os
import traceback
import shutil
import optparse
import sendgrow

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
class process:
    def __init__(self):
        self.result_error = []
        self.result_overwrite = []
        self.publicTo = None

    def sendnotify(self, msg):
        mclass = sendgrow.growl()
        icon = os.path.join(os.path.dirname(__file__), 'cpa.png')
        print "icon =", icon
        event = 'cpa - Copy with python'
        appname = 'cpa'
        mclass.publish(appname, event, "cpa" , str(msg), iconpath=icon)

    def copyAll(self,listFrom=None,listTo=None):
        if listFrom != None:
            for i in listFrom:
                os.system("copy /Y \"" + str(i) + "\"" + " \"" + listTo + "\"")
        else:
            listFrom = self.result_overwrite
            for i in listFrom:
                os.system("copy /Y \"" + str(i) + "\"" + " \"" + listTo + "\"")
            #raise SyntaxError('LINE ERROR: 27-30')
            #print "\n"
            #print __help__

    def existConfr(self,_from=None,_to=None):
        if _from == None:
            #print self.result_overwrite
            for i in self.result_overwrite:
                if i != self.result_overwrite[-1]:
                    _from = i
                    _to = self.publicTo
                    q = raw_input(" FILE EXISTS: \"" + os.path.basename(_from) + "\"; Overwrite ? (y[[Y]es]/n[[N]o][ALL/all]; Default: n[N][o[O]]: ")
                    if q == "y" or q == "Y" or q == "Yes" or q == "yes" :
                        try:
                            os.system("COPY /Y \"" + _from + "\"" + " \"" + _to + "\"")
                        except:
                            raise WindowsError('COPY SYSTEM ERROR: ' + str(_from))
                    elif q == "n" or q == "N" or q == "no" or q == "No":
                        pass
                    elif q == "ALL" or q == "all":
                        try:
                            self.copyAll(listTo=_to)
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
                    os.system("copy /Y \"" + _from + "\"" + " \"" + _to + "\"")
                except:
                    raise WindowsError('COPY SYSTEM ERROR: ' + str(_from))
            elif q == "n" or q == "N" or q == "no" or q == "No":
                pass
            elif q == "ALL" or q == "all":
                self.copyAll(listTo=_to)
            else:
                pass


    def __copyd(self,x,_to=sys.argv[-1],excp=None):
        if excp == None:
            if os.path.split(_to)[0] == '':
                _to = os.path.abspath(sys.argv[-1])
                if os.path.isdir(_to) == False:
                    try:
                        os.mkdir(_to)
                    except:
                        raise WindowsError('MAKE DIR: Can\'t make destination Directory')
                else:
                    pass
        else:
            _to = sys.argv[-3]
            if os.path.split(_to)[0] == '':
                _to = os.path.abspath(sys.argv[-3])
                if os.path.isdir(_to) == False:
                    try:
                        os.mkdir(_to)
                    except:
                        raise WindowsError('MAKE DIR: Can\'t make destination Directory')
                else:
                    pass

        if excp == None:
            if os.path.isfile(x) == True:
                try:
                    shutil.copy2(x, _to)
                    print " COPY FILE: \"" + str(x) + "\" --> \"" + os.path.abspath(sys.argv[-1]) + "\""
                except:
                    #return __error__
                    print " COPY FILE [ERROR]: \"" + str(x) + "\" --> " + os.path.abspath(_to) + " [ERROR]"
                    self.result_error.append(os.path.abspath(str(x)))

            elif os.path.isdir(x) == True:
                try:
                    #print "BBB"
                    shutil.copy2(x, _to)
                    print " COPY DIRECTORY: \"" + str(x) + "\" --> " + os.path.abspath(sys.argv[-1])
                except:
                    #return __error__
                    print " COPY DIRECTORY [ERROR]: \"" + str(x) + "\" --> \"" + os.path.abspath(_to) + "\" [ERROR]"
                    self.result_error.append(os.path.abspath(str(x)))
            else:
                print "\n"
                print __help__
        else:
            if excp == x:
                pass
            else:
                if os.path.isfile(x) == True:
                    try:
                        if not shutil.Error:
                            shutil.copy2(x, _to)
                            print " COPY FILE: \"" + str(x) + "\" --> \"" + os.path.abspath(_to) + "\""
                        else:
                            if x != os.path.abspath(excp):
                                self.result_overwrite.append(x)
                                self.publicTo = _to
                            else:
                                pass
                    except:
                        #print __error__
                        self.result_error.append(os.path.abspath(str(x)))

                elif os.path.isdir(x) == True:
                    try:
                        if not shutil.Error:
                            shutil.copy2(x, _to)
                            print " COPY DIRECTORY: \"" + str(x) + "\" --> \"" + os.path.abspath(_to) + "\""
                        else:
                            if x != os.path.abspath(excp):
                                self.result_overwrite.append(x)
                                self.publicTo = _to
                            else:
                                pass
                    except:
                        #return __error__
                        print " COPY DIRECTORY [ERROR]: \"" + str(x) + "\" --> \"" + os.path.abspath(_to) + "\" [ERROR]"
                        self.result_error.append(os.path.abspath(str(x)))
                else:
                    print "\n"
                    print __help__

    def start_copyd(self, pattern, _to, excp=None, verbosity=None):
        """pattern must have "*", exp: *data*, data*, *data"""
        if os.path.isdir(_to) == False:
            try:
                os.mkdir(os.path.abspath(_to))
            except:
                if verbosity:
                    print "error: ", str(__error__)                 
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
        self.copyd(pre_data2)
        
    def copyd_sync(self, src, dest, verbosity=None):
        for root, dirs, files in src:
            for i in dirs:
                fr = os.path.join(root, dirs)
                dt = os.path.join(dest, dirs)
        
    def copyd_tree(self, src, dest, overwrite=None, verbosity=None):
        #print "overwrite AAA =", overwrite
        try:
            for root, dirs, files in os.walk(src):
                #to_ = os.path.join(dest, os.path.basename(os.path.abspath(src)))
                to_ = os.path.abspath(dest)
                #print "copyd_tree to_ =", to_
                #print "root =", root
                #print "os.path.abspath(src) =", os.path.abspath(src)
                if root == os.path.abspath(src):
                    if len(files) > 0:
                        for i in files:
                            x = os.path.join(root, i)
                            #print "copyd_tree i =", os.path.realpath(i)
                            #print "copyd_tree x =", os.path.realpath(x)
                            if not os.path.isdir(to_):
                                os.mkdir(to_)
                            #print "copyd_tree to_ =", to_
                            if os.path.isfile(os.path.join(to_, os.path.basename(i))):
                                if overwrite == 2:
                                    os.remove(os.path.join(to_, os.path.basename(i)))
                                    try:
                                        shutil.copy2(os.path.abspath(x), to_)
                                        print " COPY FILE: [Overwrite] \"" + os.path.abspath(x) + "\" --> " + to_
                                    except:
                                        print " COPY FILE [ERROR]: \"" + os.path.abspath(x) + "\" --> " + to_ + " [ERROR]"
                                        self.result_error.append(os.path.abspath(argv[x]))
                                else:
                                    pass
                            else:
                                try:
                                    shutil.copy2(os.path.abspath(x), to_)
                                    print " COPY FILE: \"" + os.path.abspath(x) + "\" --> " + to_
                                except:
                                    print " COPY FILE [ERROR]: \"" + os.path.abspath(x) + "\" --> " + to_ + " [ERROR]"
                                    self.result_error.append(os.path.abspath(argv[x]))                                    
                    if len(dirs) > 0:
                        if os.path.isdir(to_):
                            for i in dirs:
                                x = os.path.join(root, i)
                                #print "copyd_tree i 2 =", os.path.realpath(i)
                                #print "copyd_tree x 2 =", os.path.realpath(x)
                                #if not os.path.isdir(to_):
                                #    os.mkdir(to_)
                                #print "copyd_tree to_ =", to_
                                to__ = os.path.join(to_, i)
                                #print "to_ =", to__
                                if os.path.isdir(to__):
                                    #print "to_ is directory"
                                    if overwrite == 2:
                                        #print "overwrite folder"
                                        os.remove(to__)
                                        #print "remove overwrite folder"
                                        try:
                                            shutil.copytree(os.path.abspath(x), to__)
                                            print " COPY DIRECTORY: [Overwrite] \"" + os.path.abspath(x) + "\" --> " + to__
                                        except:
                                            print " COPY DIRECTORY [ERROR]: \"" + os.path.abspath(x) + "\" --> " + to__ + " [ERROR]"
                                            self.result_error.append(os.path.abspath(x))                                            
                                    else:
                                        pass
                                else:
                                    #print "to_ is NOT directory"
                                    try:
                                        shutil.copytree(os.path.abspath(x), to__)
                                        print " COPY DIRECTORY: \"" + os.path.abspath(x) + "\" --> " + to__
                                    except:
                                        print " COPY DIRECTORY [ERROR]: \"" + os.path.abspath(x) + "\" --> " + to__ + " [ERROR]"
                                        self.result_error.append(os.path.abspath(x))                                        
                        else:
                            shutil.copytree(root, to_, True)
                print "-" * 120
        except:
            er = traceback.format_exc()
            if verbosity == 1:
                print "\tError =", er

    def copyd(self, argv, excp=None, overwrite=None, new=None, self_copy=None, verbosity=None):
        #print "excp =", excp
        #print "overwrite =", overwrite
        #print "new =", new
        #print "self_copy =", self_copy
        #print "verbosity =", verbosity
        for t in argv:
            if os.path.abspath(__file__) in t:
                del(argv[argv.index(t)])
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

        for i in range (0 , len(argv) - 1):
            if self_copy:
                to_ = os.path.dirname(argv[0])
            else:
                to_ = os.path.abspath(argv[-1])
            if os.path.isfile(os.path.abspath(argv[i])) == True:
                try:
                    to_ = os.path.join(to_, os.path.basename(argv[i + 1]))
                    shutil.copy2(argv[i], to_)
                    print " COPY FILE: \"" + argv[i] + "\" --> " + to_
                except:
                    #return __error__
                    print " COPY FILE [ERROR]: \"" + argv[i] + "\" --> " + to_ + " [ERROR]"
                    self.sendnotify(" COPY FILE [ERROR]: \"" + argv[i] + "\" --> " + to_ + " [ERROR]")
                    self.result_error.append(os.path.abspath(sys.argv[i]))

            elif os.path.isdir(argv[i]) == True:
                try:
                    if os.path.isdir(os.path.abspath(to_)):
                        if overwrite > 0:
                            if new:
                                pass
                            to_ = to_
                            #print "to_ =", to_
                            self.copyd_tree(argv[i], to_, overwrite, verbosity)
                        else:
                            if new: #include option
                                to_ = os.path.join(to_, os.path.basename(os.path.abspath(argv[i]))) #copy in directory
                            try:
                                shutil.copytree(argv[i], to_, True)
                                print " COPY DIRECTORY: \"" + argv[i] + "\" --> " + to_
                            except:
                                if verbosity == 2:
                                    er =  traceback.format_exc_syslog_growl()
                                    print "error =", er
                    else:
                        #os.mkdir(os.path.abspath(to_))
                        try:
                            if new:
                                to_ = os.path.join(to_, os.path.basename(os.path.abspath(argv[i])))
                            else:
                                to_ = to_
                            shutil.copytree(argv[i], to_, True)
                            print " COPY DIRECTORY: \"" + argv[i] + "\" --> " + to_
                        except:
                            if verbosity == 1:
                                er =  traceback.format_exc_syslog_growl()
                                print "error =", er
                except:
                    if verbosity == 1:
                        er =  traceback.format_exc()
                        print "\tERROR =", er
                    print " COPY DIRECTORY [ERROR]: \"" + argv[i] + "\" --> " + to_ + " [ERROR]"
                    self.sendnotify("COPY DIRECTORY [ERROR]: \"" + argv[i] + "\" --> " + to_ + " [ERROR]")
                    self.result_error.append(os.path.abspath(argv[i]))

            elif "*" in sys.argv[i]:
                #print "start start move"
                if not excp == None:
                    self.start_copyd(argv[i], to_, excp, verbosity)
                else:
                    self.start_copyd(argv[i], to_, verbosity=verbosity)

    def usage(self, print_help=None):
        usage = "usage: %s [option] \n\ndefault will make a dir if destination not a file or directory" %(str(os.path.basename(__file__)))
        parser = optparse.OptionParser(usage)
        parser.add_option("-e", "--excp", help="Exception Will not be copying (example: \"data1, data2,data3, data4\"), format must with single or double quota", action="store")
        parser.add_option("-f", "--full", help="Copy into directory it, which not make a dir first   -ff | --fullfull copy into directory it and overwrite all of file to", action="count")
        parser.add_option("-i", "--include", help="Copy into directory with make directory first (default)", action="store_true")
        parser.add_option("-s", "--self", help="Copy into self directory source", action="store_true")
        parser.add_option("-v", "--verbosity", help="Print process running                               -vv | --verbosityverbosity Print process running and error warning", action="count")
        option, args_pre = parser.parse_args(sys.argv)
        #print "args_pre =", args_pre
        args = []
        for i in args_pre:
            o = os.path.abspath(i)
            args.append(o)
            help_key = ['-h', '--h', '--h', '--help', '-help', '--help']
        if print_help:
            print "RRRRRRRRRRRRR"
            parser.print_help()
            self.sendnotify(str(parser.print_help()))
            #print "len(sys.argv) =", len(sys.argv)
        if len(sys.argv) > 1:
            for i in help_key:
                if str(sys.argv[1]).lower() == i:
                    print "WWWWWWWWWWWWWWWW"
                    parser.print_help()
                    self.sendnotify(str(parser.print_help())) 
                    break;
            for h in args:
                if str(h).strip in help_key:
                    del(args[args.index(h)])
            if option.self:
                if option.include:
                    self.copyd(args, option.excp, option.full, option.include, True, option.verbosity)
                else:
                    self.copyd(args, option.excp, option.full, self_copy=True, verbosity=option.verbosity)
            elif option.include:
                if option.self:
                    self.copyd(args, option.excp, option.full, option.include, True, option.verbosity)
                else:
                    self.copyd(args, option.excp, option.full, option.include, verbosity=option.verbosity)
            else:
                self.copyd(args)
            self.check_result()                
        else:
            parser.print_help()   
            self.sendnotify(str(parser.print_help())) 

    def check_result(self):
        if len(self.result_error) == 1:
            print " RESULT: ERROR", len(self.result_error), " Item: "
            self.sendnotify(" RESULT: ERROR " + str(len(self.result_error)) + " Item: ")
            print "\t [ERROR] --> ", self.result_error[0]
            self.sendnotify("[ERROR] --> " + self.result_error[0])
        elif len(self.result_error) > 1:
            print " RESULT: ERROR", len(self.result_error), " Items: "
            self.sendnotify("RESULT: ERROR " + str(len(self.result_error)) + " Items: ")
            for x in self.result_error:
                print "\t [ERROR] --> error moving file:", x
                self.sendnotify("[ERROR] --> error moving file: " + str(x))
        else:
            print "\n"
            print " RESULT: ALL OK"
            self.sendnotify(" RESULT: ALL OK")

if __name__ == '__main__':
    c = process()
    c.usage()