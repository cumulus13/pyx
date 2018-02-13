import sys
import os
import traceback
import shutil
import datetime
from make_colors import make_colors

__version__ = "2.2"
__author__ = "licface"
__url__ = "licface@yahoo.com"
__target__ = "all"
__build__ = "2.7"
__error__ = traceback.format_exc(print_msg= False)
__filename__ = os.path.basename(sys.argv[0])
__help__ = """  This is a multiple choise mover 
  File or Directory with python script 

  Example: - %s DATA01 [DATA02] [DATA03] DIR_DESTINATION

           - %s *FILE01* [DATA02] """ %(str(__filename__),str(__filename__))
__test__ = "0.2"

class process:
    def __init__(self):
        self.result_error = []
        self.result_overwrite = []
        self.publicTo = None
        self.LOGS_PATH = r""

    def logs(self, data):
        if os.path.isfile(os.path.join(os.path.dirname(__file__), 'mva.log')):
            self.LOGS_PATH = os.path.join(os.path.dirname(__file__), 'mva.log')
        elif self.LOGS_PATH != r'':
            if os.path.isdir(self.LOGS_PATH):
                if os.path.isfile(os.path.join(self.LOGS_PATH, 'mva.log')):
                    self.LOGS_PATH = os.path.join(self.LOGS_PATH, 'mva.log')
            elif os.path.isfile(self.LOGS_PATH):
                self.LOGS_PATH = self.LOGS_PATH
        else:
            self.LOGS_PATH = open(os.path.join(os.path.dirname(__file__), 'mva.log'), 'wb')
            self.LOGS_PATH.close()
            self.LOGS_PATH = os.path.join(os.path.dirname(__file__), 'mva.log')
        f = open(self.LOGS_PATH, 'a')
        f.write(datetime.datetime.strftime(datetime.datetime.now(), '%d-%m-%Y %H:%M:%S') + " " + str(data) + "\n")
        f.close()

    def moveAll(self,listFrom=None,listTo=None):
        if listFrom != None:
            for i in listFrom:
                os.system("move /Y \"" + str(i) + "\"" + " \"" + listTo + "\"")
        else:
            listFrom = self.result_overwrite
            for i in listFrom:
                os.system("move /Y \"" + str(i) + "\"" + " \"" + listTo + "\"")
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
                    q = raw_input(make_colors(" FILE EXISTS: ", 'white', 'red') + '"' + make_colors(os.path.basename(_from), 'lightyellow', color_type= 'colorama') + "\"; Overwrite ? (y[[Y]es]/n[[N]o][ALL/all]; Default: n[N][o[O]]: ")
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
                            #print " RESULT: ALL OK"
                            print make_colors(" RESULT:", 'white', 'yellow') + make_colors(" ALL OK", 'lightcyan', color_type= 'colorama')
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


    def __moved(self,x,_to,excp=None):
        if excp == None:
            if os.path.split(_to)[0] == '':
                _to = os.path.abspath(_to)
                if os.path.isdir(_to) == False:
                    try:
                        os.mkdir(_to)
                    except:
                        raise WindowsError(make_colors("MAKE DIR: Can't make destination Directory", 'white', 'red'))
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
                        raise WindowsError(make_colors("MAKE DIR: Can't make destination Directory", 'white', 'red'))
                else:
                    pass

        if excp == None:
            x = str(os.path.abspath(x))
            #from fspath import FSPath
            #x = FSPath(os.path.abspath(x))
            #print "os.path.isfile(x) =", os.path.isfile(x)
            #print "os.path.isdir(x) =", os.path.isdir(x)
            #print "x =", x
            #print "type(x) =", type(x)            
            if os.path.isfile(x):
                try:
                    shutil.move(x, _to)
                    #print " MOVED FILE: \"" + str(x) + "\" --> \"" + os.path.abspath(sys.argv[-1]) + "\""
                    print make_colors(" MOVED FILE: ", 'lightgreen', color_type= 'colorama') + make_colors("\"", 'cyan') + make_colors(str(x), 'lightyellow', color_type= 'colorama') + make_colors('"', 'cyan') + make_colors(" --> ", 'white', attrs= ['bold']) + make_colors("\"", 'cyan') + make_colors(os.path.abspath(sys.argv[-1]), 'lightgreen', color_type= 'colorama') + make_colors("\"", 'cyan')
                    self.logs("MOVED FILE: \"" + str(x) + "\" --> \"" + os.path.abspath(sys.argv[-1]) + "\"")
                except:
                    #return __error__
                    #print " MOVED FILE [ERROR]: \"" + str(x) + "\" --> " + os.path.abspath(_to) + " [ERROR]"
                    print make_colors(" MOVED FILE [ERROR]: ", 'white', 'red', ['bold']) + make_colors('"', 'cyan', attrs= ['bold']) + make_colors(str(x), 'yellow', attrs= ['bold']) + make_colors('"', 'cyan', attrs= ['bold']) + make_colors("-->", 'white', attrs= ['bold']) + make_colors(os.path.abspath(_to), 'green', attrs= ['bold']) + make_colors('" ', 'cyan', attrs= ['bold']) + make_colors("[ERROR]", 'white', 'red', ['bold', 'blink'])
                    self.logs("MOVED FILE [ERROR]: \"" + str(x) + "\" --> " + os.path.abspath(_to) + " [ERROR]")
                    self.result_error.append(os.path.abspath(str(x)))

            elif os.path.isdir(x):
                try:
                    #print "BBB"
                    shutil.move(x, _to)
                    print make_colors(" MOVED DIRECTORY: ", 'lightblue', color_type= 'colorama') + make_colors("\"", 'cyan') + make_colors(str(x), 'lightyellow', color_type= 'colorama') + make_colors('"', 'cyan') + make_colors(" --> ", 'white', attrs= ['bold']) + make_colors("\"", 'cyan') + make_colors(os.path.abspath(sys.argv[-1]), 'lightgreen', color_type= 'colorama') + make_colors("\"", 'cyan')
                    self.logs("MOVED DIRECTORY: \"" + str(x) + "\" --> " + os.path.abspath(sys.argv[-1]))
                except:
                    print traceback.format_exc()
                    #return __error__
                    #print " MOVED DIRECTORY [ERROR]: \"" + str(x) + "\" --> \"" + os.path.abspath(_to) + "\" [ERROR]"
                    print make_colors(" MOVED DIRECTORY [ERROR]: ", 'white', 'magenta', ['bold']) + make_colors('"', 'cyan', attrs= ['bold']) + make_colors(str(x), 'yellow', attrs= ['bold']) + make_colors('"', 'cyan', attrs= ['bold']) + make_colors("-->", 'white', attrs= ['bold']) + make_colors(os.path.abspath(_to), 'green', attrs= ['bold']) + make_colors('" ', 'cyan', attrs= ['bold']) + make_colors("[ERROR]", 'white', 'red', ['bold', 'blink'])
                    self.logs("MOVED DIRECTORY [ERROR]: \"" + str(x) + "\" --> \"" + os.path.abspath(_to) + "\" [ERROR]")
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
                            shutil.move(x, _to)
                            #print " MOVED FILE: \"" + str(x) + "\" --> \"" + os.path.abspath(_to) + "\""
                            print make_colors(" MOVED FILE: ", 'white', 'green', ['bold']) + make_colors("\"", 'cyan') + make_colors(str(x), 'lightyellow', color_type= 'colorama') + make_colors('"', 'cyan') + make_colors(" --> ", 'white', attrs= ['bold']) + make_colors("\"", 'cyan') + make_colors(os.path.abspath(_to), 'lightgreen', color_type= 'colorama') + make_colors("\"", 'cyan')
                            self.logs("MOVED FILE: \"" + str(x) + "\" --> \"" + os.path.abspath(_to) + "\"")
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
                            shutil.move(x, _to)
                            #print " MOVED DIRECTORY: \"" + str(x) + "\" --> \"" + os.path.abspath(_to) + "\""
                            print make_colors(" MOVED DIRECTORY: ", 'white', 'blue', ['bold']) + make_colors("\"", 'cyan') + make_colors(str(x), 'lightyellow', color_type= 'colorama') + make_colors('"', 'cyan') + make_colors(" --> ", 'white', attrs= ['bold']) + make_colors("\"", 'cyan') + make_colors(os.path.abspath(_to), 'lightgreen', color_type= 'colorama') + make_colors("\"", 'cyan')
                            self.logs("MOVED DIRECTORY: \"" + str(x) + "\" --> \"" + os.path.abspath(_to) + "\"")
                        else:
                            if x != os.path.abspath(excp):
                                self.result_overwrite.append(x)
                                self.publicTo = _to
                            else:
                                pass
                    except:
                        #return __error__
                        #print " MOVED DIRECTORY [ERROR]: \"" + str(x) + "\" --> \"" + os.path.abspath(_to) + "\" [ERROR]"
                        print make_colors(" MOVED DIRECTORY [ERROR]: ", 'white', 'magenta', ['bold']) + make_colors('"', 'cyan', attrs= ['bold']) + make_colors(str(x), 'lightyellow', color_type= 'colorama') + make_colors('"', 'cyan', attrs= ['bold']) + make_colors("-->", 'white', attrs= ['bold']) + make_colors(os.path.abspath(_to), 'green', attrs= ['bold']) + make_colors('" ', 'cyan', attrs= ['bold']) + make_colors("[ERROR]", 'white', 'red', ['bold', 'blink'])
                        self.logs("MOVED DIRECTORY [ERROR]: \"" + str(x) + "\" --> \"" + os.path.abspath(_to) + "\" [ERROR]")
                        self.result_error.append(os.path.abspath(str(x)))
                else:
                    print "\n"
                    print __help__

    def start_moved(self, pattern, _to, excepts = None):
        """pattern must have "*", exp: *data*, data*, *data"""
        LISTDIR = True
        if os.path.isdir(_to) == False:
            try:
                os.mkdir(os.path.abspath(_to))
            except:
                raise WindowsError(make_colors("MAKE DIR: Can't make destination Directory", 'white', 'red'))
        else:
            pass
        if pattern == '*':
            pattern = os.getcwd()
        #pre_data1 = os.popen("dir /b \"" + pattern + "\"").readlines()
        try:
            pre_data1 = os.listdir(pattern)
        except:
            pre_data1 = os.popen('DIR /b "' + pattern + '"').readlines()
            LISTDIR = False

        for i in pre_data1:
            if os.path.abspath(str(i).split("\n")[0]) != os.path.abspath(str(_to).split("\n")[0]):
                if not LISTDIR:
                    x = os.path.abspath(i[:-1])
                else:
                    x = os.path.abspath(i)
                #self.__moved(x,os.path.abspath(_to), excepts)
                self.moved(x, _to, excepts)
            else:
                pass

        return self.result_error

    def run(self, fr_, to_, excepts = None, test = False):
        if os.path.isfile(fr_) == True:
            try:
                shutil.move(fr_, to_)
                print make_colors(" MOVED FILE: ", 'white', 'yellow', ['bold']) + make_colors("\"", 'cyan') + make_colors(fr_, 'lightyellow', color_type= 'colorama') + make_colors('"', 'cyan') + make_colors(" --> ", 'white', attrs= ['bold']) + make_colors("\"", 'cyan') + make_colors(os.path.abspath(to_), 'lightgreen', color_type= 'colorama') + make_colors("\"", 'cyan')
                self.logs("MOVED FILE: \"" + fr_ + "\" --> " + os.path.abspath(to_))
            except:
                #return __error__
                print make_colors(" MOVED FILE [ERROR]: ", 'white', 'red', ['bold']) + make_colors('"', 'cyan', attrs= ['bold']) + make_colors(fr_, 'yellow', attrs= ['bold']) + make_colors('"', 'cyan', attrs= ['bold']) + make_colors("-->", 'white', attrs= ['bold']) + make_colors(os.path.abspath(to_), 'green', attrs= ['bold']) + make_colors('" ', 'cyan', attrs= ['bold']) + make_colors("[ERROR]", 'white', 'red', ['bold', 'blink'])
                self.logs("MOVED FILE [ERROR]: \"" + fr_ + "\" --> " + os.path.abspath(to_ + " [ERROR]"))
                self.result_error.append(os.path.abspath(fr_))

        elif os.path.isdir(fr_) == True:
            try:
                shutil.move(fr_, to_)
                #print " MOVED DIRECTORY: \"" + i + "\" --> " + os.path.abspath(to_)
                print make_colors(" MOVED DIRECTORY: ", 'white', 'cyan', ['bold']) + make_colors('"', 'cyan') + make_colors(str(fr_), 'lightyellow', color_type= 'colorama') + make_colors('"', 'cyan') + make_colors(" --> ", 'white', attrs= ['bold']) + make_colors('"', 'cyan') + make_colors(os.path.abspath(to_), 'lightgreen', color_type= 'colorama') + make_colors('"', 'cyan')
                self.logs("MOVED DIRECTORY: \"" + fr_ + "\" --> " + os.path.abspath(to_))
            except:
                #return __error__
                traceback.format_exc()
                print make_colors(" MOVED DIRECTORY [ERROR]: ", 'white', 'magenta', ['bold']) + make_colors('"', 'cyan', attrs= ['bold']) + make_colors(i, 'yellow', attrs= ['bold']) + make_colors('"', 'cyan', attrs= ['bold']) + make_colors("-->", 'white', attrs= ['bold']) + make_colors(os.path.abspath(to_), 'green', attrs= ['bold']) + make_colors('" ', 'cyan', attrs= ['bold']) + make_colors("[ERROR]", 'white', 'red', ['bold', 'blink'])
                self.logs("MOVED DIRECTORY [ERROR]: \"" + fr_ + "\" --> " + os.path.abspath(to_ + " [ERROR]"))
                self.result_error.append(os.path.abspath(fr_))
        elif "*" in i:
            self.start_moved(fr_,to_)
            if len(self.result_overwrite) != '':
                #print "self.result_overwrite = ", self.result_overwrite
                self.existConfr()        

    def moved(self, fr_, to_, excepts = None, test = False):
        #print "to =", to_
        #if sys.argv[-2] == "-e":
            #to_=sys.argv[-3]
            #len_arg = len(sys.argv) - 2
        #else:
            #len_arg = len(sys.argv)
        ##print "sys.argv =", sys.argv
        if isinstance(fr, list):
            for i in fr:
                if os.path.isfile(i) == True:
                    try:
                        shutil.move(i, to_)
                        print make_colors(" MOVED FILE: ", 'white', 'yellow', ['bold']) + make_colors("\"", 'cyan') + make_colors(i, 'lightyellow', color_type= 'colorama') + make_colors('"', 'cyan') + make_colors(" --> ", 'white', attrs= ['bold']) + make_colors("\"", 'cyan') + make_colors(os.path.abspath(to_), 'lightgreen', color_type= 'colorama') + make_colors("\"", 'cyan')
                        self.logs("MOVED FILE: \"" + i + "\" --> " + os.path.abspath(to_))
                    except:
                        #return __error__
                        print make_colors(" MOVED FILE [ERROR]: ", 'white', 'red', ['bold']) + make_colors('"', 'cyan', attrs= ['bold']) + make_colors(i, 'yellow', attrs= ['bold']) + make_colors('"', 'cyan', attrs= ['bold']) + make_colors("-->", 'white', attrs= ['bold']) + make_colors(os.path.abspath(to_), 'green', attrs= ['bold']) + make_colors('" ', 'cyan', attrs= ['bold']) + make_colors("[ERROR]", 'white', 'red', ['bold', 'blink'])
                        self.logs("MOVED FILE [ERROR]: \"" + i + "\" --> " + os.path.abspath(to_ + " [ERROR]"))
                        self.result_error.append(os.path.abspath(i))

                elif os.path.isdir(i) == True:
                    try:
                        shutil.move(i, to_)
                        #print " MOVED DIRECTORY: \"" + i + "\" --> " + os.path.abspath(to_)
                        print make_colors(" MOVED DIRECTORY: ", 'white', 'cyan', ['bold']) + make_colors('"', 'cyan') + make_colors(str(i), 'lightyellow', color_type= 'colorama') + make_colors('"', 'cyan') + make_colors(" --> ", 'white', attrs= ['bold']) + make_colors('"', 'cyan') + make_colors(os.path.abspath(to_), 'lightgreen', color_type= 'colorama') + make_colors('"', 'cyan')
                        self.logs("MOVED DIRECTORY: \"" + i + "\" --> " + os.path.abspath(to_))
                    except:
                        #return __error__
                        traceback.format_exc()
                        print make_colors(" MOVED DIRECTORY [ERROR]: ", 'white', 'magenta', ['bold']) + make_colors('"', 'cyan', attrs= ['bold']) + make_colors(i, 'yellow', attrs= ['bold']) + make_colors('"', 'cyan', attrs= ['bold']) + make_colors("-->", 'white', attrs= ['bold']) + make_colors(os.path.abspath(to_), 'green', attrs= ['bold']) + make_colors('" ', 'cyan', attrs= ['bold']) + make_colors("[ERROR]", 'white', 'red', ['bold', 'blink'])
                        self.logs("MOVED DIRECTORY [ERROR]: \"" + i + "\" --> " + os.path.abspath(to_ + " [ERROR]"))
                        self.result_error.append(os.path.abspath(i))
                elif "*" in i:
                    self.start_moved(i,to_)
                    if len(self.result_overwrite) != '':
                        #print "self.result_overwrite = ", self.result_overwrite
                        self.existConfr()
        else:
            self.run(fr_, to_, excepts, test)
            
        return self.result_error

    #def main(self):
        #if os.path.isdir(sys.argv[-1]):
            #print "\n"
            #moved()
        #elif sys.argv[-1] == ".":
            #print "\n"
            #moved(os.getcwd())
        #elif sys.argv[-1] == "~":
            #print "\n"
            #moved(os.getcwd())
        #else:
            #print "\n"
            #print __help__
            #raise SyntaxError (make_colors("Check Your Syntax !", 'white', 'red'))

    def usage(self):
        import argparse
        parser = argparse.ArgumentParser(formatter_class= argparse.RawTextHelpFormatter)
        parser.add_argument('PATH', help = 'Files or Directorys move to', action = 'store', nargs = '*')
        parser.add_argument('-d', '--destination', help = 'Destination Folder move to', action = 'store')
        parser.add_argument('-e', '--except', help = 'Exception', action = 'store', dest = 'excepts', nargs = '*')
        parser.add_argument('-t', '--test', help = 'Test move, not actualy move, test running only', action = 'store_true')

        if len(sys.argv) == 1:
            parser.print_help()
        else:
            args = parser.parse_args()
            print "args =", args
            if args.destination:
                fr = args.PATH
                to = args.destination
            else:
                to = args.PATH[-1]
                fr = args.PATH[0:-1]
            #self.moved(fr, to, args.excepts, args.test)


if __name__ == '__main__':
    move_class = process()
    #move_class.moved()
    move_class.usage()
    #if len(sys.argv) > 1:
        #move_class = process()
        #move_class.moved()
        #if len(move_class.moved()) >= 1:
            #print "\n\n"
            #if len(move_class.moved()) == 1:
                #print make_colors(" RESULT:", 'white', 'yellow', attrs= ['bold']) + make_colors(" ERROR", 'white', 'red'), make_colors(str(len(move_class.moved())), 'white', attrs= ['bold']), make_colors(" Item: ", 'lightyellow', color_type= 'colorama')
                #print "\t [ERROR] --> ", move_class.moved()[0]
            #else:
                #print "REA = ", make_colors(move_class.moved(), 'lightyellow', color_type= 'colorama')
                #sys.exit(0)
                ##os.system("PAUSE")
                ##for x in move_class.moved():
                    ##print " RESULT: ERROR", len(move_class.moved()), " Items: "
                    ##print "\t [ERROR] --> ", x
        #else:
            #print "\n\n"
            #print make_colors(" RESULT:", 'white', 'yellow') + make_colors(" ALL OK", 'lightcyan', color_type= 'colorama')

    #else:
        #print "\n"
        #print __help__