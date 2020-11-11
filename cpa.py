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
__help__ = """  This is a multiple choise copyer 
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
        if os.path.isfile(os.path.join(os.path.dirname(__file__), 'cpa.log')):
            self.LOGS_PATH = os.path.join(os.path.dirname(__file__), 'cpa.log')
        elif self.LOGS_PATH != r'':
            if os.path.isdir(self.LOGS_PATH):
                if os.path.isfile(os.path.join(self.LOGS_PATH, 'cpa.log')):
                    self.LOGS_PATH = os.path.join(self.LOGS_PATH, 'cpa.log')
            elif os.path.isfile(self.LOGS_PATH):
                self.LOGS_PATH = self.LOGS_PATH
        else:
            self.LOGS_PATH = open(os.path.join(os.path.dirname(__file__), 'cpa.log'), 'wb')
            self.LOGS_PATH.close()
            self.LOGS_PATH = os.path.join(os.path.dirname(__file__), 'cpa.log')
        f = open(self.LOGS_PATH, 'a')
        f.write(datetime.datetime.strftime(datetime.datetime.now(), '%d-%m-%Y %H:%M:%S') + " " + str(data) + "\n")
        f.close()

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
                    q = input(make_colors(" FILE EXISTS: ", 'white', 'red') + '"' + make_colors(os.path.basename(_from), 'lightyellow') + "\"; Overwrite ? (y[[Y]es]/n[[N]o][ALL/all]; Default: n[N][o[O]]: ")
                    if q == "y" or q == "Y" or q == "Yes" or q == "yes" :
                        try:
                            os.system("copy /Y \"" + _from + "\"" + " \"" + _to + "\"")
                        except:
                            raise WindowsError('COPY SYSTEM ERROR: ' + str(_from))
                    elif q == "n" or q == "N" or q == "no" or q == "No":
                        pass
                    elif q == "ALL" or q == "all":
                        try:
                            self.copyAll(listTo=_to)
                            print("\n")
                            #print " RESULT: ALL OK"
                            print(make_colors(" RESULT:", 'white', 'yellow') + make_colors(" ALL OK", 'lightcyan'))
                            sys.exit()
                        except:
                            print("\n")
                            print(__error__)
                    #else:
                    #	pass
                else:
                    print("\n")
                    print(__help__)
                    sys.exit()

        else:
            q = input(" FILE EXISTS: \"" + os.path.basename(_from) + "\"; Overwrite ? (y[[Y]es]/n[[N]o][ALL/all]; Default: n[N][o[O]]: ")
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


    def __copyed(self,x,_to=sys.argv[-1],excp=None):
        if excp == None:
            if os.path.split(_to)[0] == '':
                _to = os.path.abspath(sys.argv[-1])
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
                    shutil.copy(x, _to)
                    #print " COPY FILE: \"" + str(x) + "\" --> \"" + os.path.abspath(sys.argv[-1]) + "\""
                    print(make_colors(" COPY FILE: ", 'lightgreen') + make_colors("\"", 'cyan') + make_colors(str(x), 'lightyellow') + make_colors('"', 'cyan') + make_colors(" --> ", 'white', attrs= ['bold']) + make_colors("\"", 'cyan') + make_colors(os.path.abspath(sys.argv[-1]), 'lightgreen') + make_colors("\"", 'cyan'))
                    self.logs("COPY FILE: \"" + str(x) + "\" --> \"" + os.path.abspath(sys.argv[-1]) + "\"")
                except:
                    #return __error__
                    #print " COPY FILE [ERROR]: \"" + str(x) + "\" --> " + os.path.abspath(_to) + " [ERROR]"
                    print(make_colors(" COPY FILE [ERROR]: ", 'white', 'red', ['bold']) + make_colors('"', 'cyan', attrs= ['bold']) + make_colors(str(x), 'yellow', attrs= ['bold']) + make_colors('"', 'cyan', attrs= ['bold']) + make_colors("-->", 'white', attrs= ['bold']) + make_colors(os.path.abspath(_to), 'green', attrs= ['bold']) + make_colors('" ', 'cyan', attrs= ['bold']) + make_colors("[ERROR]", 'white', 'red', ['bold', 'blink']))
                    self.logs("COPY FILE [ERROR]: \"" + str(x) + "\" --> " + os.path.abspath(_to) + " [ERROR]")
                    self.result_error.append(os.path.abspath(str(x)))

            elif os.path.isdir(x):
                try:
                    #print "BBB"
                    shutil.copy2(x, _to)
                    print(make_colors(" COPY DIRECTORY: ", 'lightblue') + make_colors("\"", 'cyan') + make_colors(str(x), 'lightyellow') + make_colors('"', 'cyan') + make_colors(" --> ", 'white', attrs= ['bold']) + make_colors("\"", 'cyan') + make_colors(os.path.abspath(sys.argv[-1]), 'lightgreen') + make_colors("\"", 'cyan'))
                    self.logs("COPY DIRECTORY: \"" + str(x) + "\" --> " + os.path.abspath(sys.argv[-1]))
                except:
                    print(traceback.format_exc())
                    #return __error__
                    #print " COPY DIRECTORY [ERROR]: \"" + str(x) + "\" --> \"" + os.path.abspath(_to) + "\" [ERROR]"
                    print(make_colors(" COPY DIRECTORY [ERROR]: ", 'white', 'magenta', ['bold']) + make_colors('"', 'cyan', attrs= ['bold']) + make_colors(str(x), 'yellow', attrs= ['bold']) + make_colors('"', 'cyan', attrs= ['bold']) + make_colors("-->", 'white', attrs= ['bold']) + make_colors(os.path.abspath(_to), 'green', attrs= ['bold']) + make_colors('" ', 'cyan', attrs= ['bold']) + make_colors("[ERROR]", 'white', 'red', ['bold', 'blink']))
                    self.logs("COPY DIRECTORY [ERROR]: \"" + str(x) + "\" --> \"" + os.path.abspath(_to) + "\" [ERROR]")
                    self.result_error.append(os.path.abspath(str(x)))
            else:
                print("\n")
                print(__help__)
        else:
            if excp == x:
                pass
            else:
                if os.path.isfile(x) == True:
                    try:
                        if not shutil.Error:
                            shutil.copy(x, _to)
                            #print " COPY FILE: \"" + str(x) + "\" --> \"" + os.path.abspath(_to) + "\""
                            print(make_colors(" COPY FILE: ", 'white', 'green', ['bold']) + make_colors("\"", 'cyan') + make_colors(str(x), 'lightyellow') + make_colors('"', 'cyan') + make_colors(" --> ", 'white', attrs= ['bold']) + make_colors("\"", 'cyan') + make_colors(os.path.abspath(_to), 'lightgreen') + make_colors("\"", 'cyan'))
                            self.logs("COPY FILE: \"" + str(x) + "\" --> \"" + os.path.abspath(_to) + "\"")
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
                            #print " COPY DIRECTORY: \"" + str(x) + "\" --> \"" + os.path.abspath(_to) + "\""
                            print(make_colors(" COPY DIRECTORY: ", 'white', 'blue', ['bold']) + make_colors("\"", 'cyan') + make_colors(str(x), 'lightyellow') + make_colors('"', 'cyan') + make_colors(" --> ", 'white', attrs= ['bold']) + make_colors("\"", 'cyan') + make_colors(os.path.abspath(_to), 'lightgreen') + make_colors("\"", 'cyan'))
                            self.logs("COPY DIRECTORY: \"" + str(x) + "\" --> \"" + os.path.abspath(_to) + "\"")
                        else:
                            if x != os.path.abspath(excp):
                                self.result_overwrite.append(x)
                                self.publicTo = _to
                            else:
                                pass
                    except:
                        #return __error__
                        #print " COPY DIRECTORY [ERROR]: \"" + str(x) + "\" --> \"" + os.path.abspath(_to) + "\" [ERROR]"
                        print(make_colors(" COPY DIRECTORY [ERROR]: ", 'white', 'magenta', ['bold']) + make_colors('"', 'cyan', attrs= ['bold']) + make_colors(str(x), 'lightyellow') + make_colors('"', 'cyan', attrs= ['bold']) + make_colors("-->", 'white', attrs= ['bold']) + make_colors(os.path.abspath(_to), 'green', attrs= ['bold']) + make_colors('" ', 'cyan', attrs= ['bold']) + make_colors("[ERROR]", 'white', 'red', ['bold', 'blink']))
                        self.logs("COPY DIRECTORY [ERROR]: \"" + str(x) + "\" --> \"" + os.path.abspath(_to) + "\" [ERROR]")
                        self.result_error.append(os.path.abspath(str(x)))
                else:
                    print("\n")
                    print(__help__)

    def start_copyed(self, pattern, _to=sys.argv[-1]):
        """pattern must have "*", exp: *data*, data*, *data"""
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
        pre_data1 = os.listdir(pattern)

        for i in pre_data1:
            if os.path.abspath(str(i).split("\n")[0]) != os.path.abspath(str(_to).split("\n")[0]):
                x = os.path.abspath(i)
                if sys.argv[-2] == '-e':
                    self.__copyed(x,_to,sys.argv[-1])
                else:	
                    self.__copyed(x,os.path.abspath(_to))
            else:
                pass

        return self.result_error


    def copyed(self,to_=sys.argv[-1]):
        #print "to =", to_
        if sys.argv[-2] == "-e":
            to_=sys.argv[-3]
            len_arg = len(sys.argv) - 2
        else:
            len_arg = len(sys.argv)
        #print "sys.argv =", sys.argv[:-1]
        for i in  range (1,int(len_arg) - 1):
            if os.path.isfile(sys.argv[i]) == True:
                try:
                    shutil.copy(sys.argv[i], to_)
                    print(make_colors(" COPY FILE: ", 'white', 'yellow', ['bold']) + make_colors("\"", 'cyan') + make_colors(sys.argv[i], 'lightyellow') + make_colors('"', 'cyan') + make_colors(" --> ", 'white', attrs= ['bold']) + make_colors("\"", 'cyan') + make_colors(os.path.abspath(sys.argv[-1]), 'lightgreen') + make_colors("\"", 'cyan'))
                    self.logs("COPY FILE: \"" + sys.argv[i] + "\" --> " + os.path.abspath(sys.argv[-1]))
                except:
                    #return __error__
                    print(make_colors(" COPY FILE [ERROR]: ", 'white', 'red', ['bold']) + make_colors('"', 'cyan', attrs= ['bold']) + make_colors(sys.argv[i], 'yellow', attrs= ['bold']) + make_colors('"', 'cyan', attrs= ['bold']) + make_colors("-->", 'white', attrs= ['bold']) + make_colors(os.path.abspath(sys.argv[-1]), 'green', attrs= ['bold']) + make_colors('" ', 'cyan', attrs= ['bold']) + make_colors("[ERROR]", 'white', 'red', ['bold', 'blink']))
                    self.logs("COPY FILE [ERROR]: \"" + sys.argv[i] + "\" --> " + os.path.abspath(sys.argv[-1] + " [ERROR]"))
                    self.result_error.append(os.path.abspath(sys.argv[i]))

            elif os.path.isdir(sys.argv[i]) == True:
                try:
                    #print "AAA"
                    shutil.copytree(sys.argv[i], os.path.join(to_, os.path.basename(sys.argv[i])))
                    #print " COPY DIRECTORY: \"" + sys.argv[i] + "\" --> " + os.path.abspath(sys.argv[-1])
                    print(make_colors(" COPY DIRECTORY: ", 'white', 'cyan', ['bold']) + make_colors('"', 'cyan') + make_colors(str(sys.argv[i]), 'lightyellow') + make_colors('"', 'cyan') + make_colors(" --> ", 'white', attrs= ['bold']) + make_colors('"', 'cyan') + make_colors(os.path.abspath(to_), 'lightgreen') + make_colors('"', 'cyan'))
                    self.logs("COPY DIRECTORY: \"" + sys.argv[i] + "\" --> " + os.path.abspath(sys.argv[-1]))
                except WindowsError:
                    pass
                except:
                    #return __error__
                    traceback.format_exc()
                    print(make_colors(" COPY DIRECTORY [ERROR]: ", 'white', 'magenta', ['bold']) + make_colors('"', 'cyan', attrs= ['bold']) + make_colors(sys.argv[i], 'yellow', attrs= ['bold']) + make_colors('"', 'cyan', attrs= ['bold']) + make_colors("-->", 'white', attrs= ['bold']) + make_colors(os.path.abspath(sys.argv[-1]), 'green', attrs= ['bold']) + make_colors('" ', 'cyan', attrs= ['bold']) + make_colors("[ERROR]", 'white', 'red', ['bold', 'blink']))
                    self.logs("COPY DIRECTORY [ERROR]: \"" + sys.argv[i] + "\" --> " + os.path.abspath(sys.argv[-1] + " [ERROR]"))
                    self.result_error.append(os.path.abspath(sys.argv[i]))
            elif "*" in sys.argv[i]:
                self.start_copyed(sys.argv[i],to_)
            if len(self.result_overwrite) != '':
                #print "self.result_overwrite = ", self.result_overwrite
                self.existConfr()
        return self.result_error

    def main(self):
        if os.path.isdir(sys.argv[-1]):
            print("\n")
            copyed()
        elif sys.argv[-1] == ".":
            print("\n")
            copyed(os.getcwd())
        elif sys.argv[-1] == "~":
            print("\n")
            copyed(os.getcwd())
        else:
            print("\n")
            print(__help__)
            raise SyntaxError (make_colors("Check Your Syntax !", 'white', 'red'))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        copy_class = process()
        copy_class.copyed()
        if len(copy_class.copyed()) >= 1:
            print("\n\n")
            if len(copy_class.copyed()) == 1:
                print(make_colors(" RESULT:", 'white', 'yellow', attrs= ['bold']) + make_colors(" ERROR", 'white', 'red'), make_colors(str(len(copy_class.copyed())), 'white', attrs= ['bold']), make_colors(" Item: ", 'lightyellow'))
                print("\t [ERROR] --> ", copy_class.copyed()[0])
            else:
                print("REA = ", make_colors(copy_class.copyed(), 'lightyellow'))
                sys.exit(0)
            #os.system("PAUSE")
            #for x in copy_class.copyed():
                #print " RESULT: ERROR", len(copy_class.copyed()), " Items: "
                #print "\t [ERROR] --> ", x
        else:
            print("\n\n")
            print(make_colors(" RESULT:", 'white', 'yellow') + make_colors(" ALL OK", 'lightcyan'))
    else:
        print("\n")
        print(__help__)