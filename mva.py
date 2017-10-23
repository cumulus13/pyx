import sys
import os
import traceback
import shutil
import datetime

__version__ = "2.2"
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


    def __moved(self,x,_to=sys.argv[-1],excp=None):
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
                    shutil.move(x, _to)
                    print " MOVED FILE: \"" + str(x) + "\" --> \"" + os.path.abspath(sys.argv[-1]) + "\""
                    self.logs("MOVED FILE: \"" + str(x) + "\" --> \"" + os.path.abspath(sys.argv[-1]) + "\"")
                except:
                    #return __error__
                    print " MOVED FILE [ERROR]: \"" + str(x) + "\" --> " + os.path.abspath(_to) + " [ERROR]"
                    self.logs("MOVED FILE [ERROR]: \"" + str(x) + "\" --> " + os.path.abspath(_to) + " [ERROR]")
                    self.result_error.append(os.path.abspath(str(x)))

            elif os.path.isdir(x) == True:
                try:
                    #print "BBB"
                    shutil.move(x, _to)
                    print " MOVED DIRECTORY: \"" + str(x) + "\" --> " + os.path.abspath(sys.argv[-1])
                    self.logs("MOVED DIRECTORY: \"" + str(x) + "\" --> " + os.path.abspath(sys.argv[-1]))
                except:
                    #return __error__
                    print " MOVED DIRECTORY [ERROR]: \"" + str(x) + "\" --> \"" + os.path.abspath(_to) + "\" [ERROR]"
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
                            print " MOVED FILE: \"" + str(x) + "\" --> \"" + os.path.abspath(_to) + "\""
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
                            print " MOVED DIRECTORY: \"" + str(x) + "\" --> \"" + os.path.abspath(_to) + "\""
                            self.logs("MOVED DIRECTORY: \"" + str(x) + "\" --> \"" + os.path.abspath(_to) + "\"")
                        else:
                            if x != os.path.abspath(excp):
                                self.result_overwrite.append(x)
                                self.publicTo = _to
                            else:
                                pass
                    except:
                        #return __error__
                        print " MOVED DIRECTORY [ERROR]: \"" + str(x) + "\" --> \"" + os.path.abspath(_to) + "\" [ERROR]"
                        self.logs("MOVED DIRECTORY [ERROR]: \"" + str(x) + "\" --> \"" + os.path.abspath(_to) + "\" [ERROR]")
                        self.result_error.append(os.path.abspath(str(x)))
                else:
                    print "\n"
                    print __help__

    def start_moved(self, pattern, _to=sys.argv[-1]):
        """pattern must have "*", exp: *data*, data*, *data"""
        if os.path.isdir(_to) == False:
            try:
                os.mkdir(os.path.abspath(_to))
            except:
                raise WindowsError("MAKE DIR: Can't make destination Directory")
        else:
            pass
        pre_dir_data = os.path.dirname(pattern)
        #if pre_dir_data == "*":
        #	pre_data1 = os.popen("dir /b \"" + str(pattern) + "\"").readlines()
        if pre_dir_data == '':
            pre_dir_data = os.getcwd()
            pre_data1 = os.popen("dir /b \"" + str(pattern) + "\"").readlines()
        elif pre_dir_data == None:
            pre_dir_data = os.getcwd()
            pre_data1 = os.popen("dir /b \"" + str(pattern) + "\"").readlines()
        else:
            pre_data1 = os.popen("dir /b \"" + pattern + "\"").readlines()

        for i in pre_data1:
            #print "I = ",os.path.abspath(str(i).split("\n")[0])
            #print "to = ",os.path.abspath(str(_to).split("\n")[0])
            if os.path.abspath(str(i).split("\n")[0]) != os.path.abspath(str(_to).split("\n")[0]):
                x = os.path.join(pre_dir_data,str(i).split("\n")[0])
                if sys.argv[-2] == '-e':
                    self.__moved(x,_to,sys.argv[-1])
                else:	
                    #print "X --> ",x
                    #print "_to --> ", os.path.abspath(_to)
                    self.__moved(x,os.path.abspath(_to))
            else:
                pass

        return self.result_error


    def moved(self,to_=sys.argv[-1]):
        if sys.argv[-2] == "-e":
            to_=sys.argv[-3]
            len_arg = len(sys.argv) - 2
        else:
            len_arg = len(sys.argv)

        for i in  range (1,int(len_arg) - 1):
            if os.path.isfile(sys.argv[i]) == True:
                try:
                    shutil.move(sys.argv[i], to_)
                    print " MOVED FILE: \"" + sys.argv[i] + "\" --> " + os.path.abspath(sys.argv[-1])
                    self.logs("MOVED FILE: \"" + sys.argv[i] + "\" --> " + os.path.abspath(sys.argv[-1]))
                except:
                    #return __error__
                    print " MOVED FILE [ERROR]: \"" + sys.argv[i] + "\" --> " + os.path.abspath(sys.argv[-1] + " [ERROR]")
                    self.logs("MOVED FILE [ERROR]: \"" + sys.argv[i] + "\" --> " + os.path.abspath(sys.argv[-1] + " [ERROR]"))
                    self.result_error.append(os.path.abspath(sys.argv[i]))

            elif os.path.isdir(sys.argv[i]) == True:
                try:
                    shutil.move(sys.argv[i], to_)
                    print " MOVED DIRECTORY: \"" + sys.argv[i] + "\" --> " + os.path.abspath(sys.argv[-1])
                    self.logs("MOVED DIRECTORY: \"" + sys.argv[i] + "\" --> " + os.path.abspath(sys.argv[-1]))
                except:
                    #return __error__
                    print " MOVED DIRECTORY [ERROR]: \"" + sys.argv[i] + "\" --> " + os.path.abspath(sys.argv[-1] + " [ERROR]")
                    self.logs("MOVED DIRECTORY [ERROR]: \"" + sys.argv[i] + "\" --> " + os.path.abspath(sys.argv[-1] + " [ERROR]"))
                    self.result_error.append(os.path.abspath(sys.argv[i]))
            elif "*" in sys.argv[i]:
                self.start_moved(sys.argv[i],to_)
                if len(self.result_overwrite) != '':
                    #print "self.result_overwrite = ", self.result_overwrite
                    self.existConfr()
        return self.result_error

    def main(self):
        if os.path.isdir(sys.argv[-1]):
            print "\n"
            moved()
        elif sys.argv[-1] == ".":
            print "\n"
            moved(os.getcwd())
        elif sys.argv[-1] == "~":
            print "\n"
            moved(os.getcwd())
        else:
            print "\n"
            print __help__
            raise SyntaxError ("Check Your Syntax !")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        move_class = process()
        move_class.moved()
        if len(move_class.moved()) >= 1:
            print "\n\n"
            if len(move_class.moved()) == 1:
                print " RESULT: ERROR", len(move_class.moved()), " Item: "
                print "\t [ERROR] --> ", move_class.moved()[0]
            else:
                print "REA = ", move_class.moved()
                os.system("PAUSE")
                for x in move_class.moved():
                    print " RESULT: ERROR", len(move_class.moved()), " Items: "
                    print "\t [ERROR] --> ", x
        else:
            print "\n\n"
            print " RESULT: ALL OK"

    else:
        print "\n"
        print __help__