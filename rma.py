import os, sys
import shutil
import diffmov
import traceback

__version__ = "1.0"
__author__ = "LICFACE"
__email__ = "root@licface.net"
__sdk__ = "2.7"
__build__ = "2.7"
__test__ = "0.1"
__error__ = traceback.format_exc()
__filename__ = os.path.basename(sys.argv[0])
__help__ = """  This is a multiple choise remover 
  File or Directory with python script 

  Example: - %s FILE01 [DIR02] [DIR03] [FILE/DIRXXX]

           - %s *FILE01* *DIR02* """ %(str(__filename__),str(__filename__))

class rma:
    def __init__(self):
        self.result_error = []
        self.diffmov = diffmov.DifficultRemove()

    def removeAll(self,listFrom=None):
        if listFrom != None:
            for i in listFrom:
                #os.system("move /Y \"" + str(i) + "\"" + " \"" + listTo + "\"")
                os.remove(os.path.abspath(i))
        else:
            listFrom = self.result_overwrite
            for i in listFrom:
                #os.system("move /Y \"" + str(i) + "\"" + " \"" + listTo + "\"")
                os.remove(os.path.abspath(i))
            #raise SyntaxError('LINE ERROR: 27-30')
            #print "\n"
            #print __help__

    def __removed(self,x):
        if os.path.isfile(x) == True:
            try:
                os.remove(os.path.abspath(x))
                print " REMOVED FILE: \"" + str(os.path.abspath(x)) + "\""
            except:
                #return __error__print " REMOVED FILE [ERROR]: \"" + str(os.path.abspath(x)) + "\""
                self.result_error.append(os.path.abspath(str(os.path.abspath(x))))

        elif os.path.isdir(x) == True:
            try:
                #print "BBB"
                os.rmdir(os.path.abspath(x))
                print " REMOVED DIRECTORY: \"" + str(os.path.abspath(x)) + "\""
            except:
                #return __error__
                try:
                    self.diffmov.Remove(os.path.abspath(x))
                except:                
                    print " REMOVED DIRECTORY [ERROR]: \"" + str(os.path.abspath(x)) + "\""
                    self.result_error.append(os.path.abspath(str(os.path.abspath(x))))
        elif "*" in x:
            data_remove1 = os.popen("dir /b \"" + str(x) + "\"").readlines()
            for i in data_remove1:
                if os.path.isfile(i) == True:
                    try:
                        os.remove(os.path.abspath(i))
                        print " REMOVED FILE: \"" + str(os.path.abspath(i)) + "\""
                    except:
                        #return __error__
                        print " REMOVED FILE [ERROR]: \"" + str(os.path.abspath(i)) + "\""
                        self.result_error.append(os.path.abspath(str(os.path.abspath(i))))

                elif os.path.isdir(i) == True:
                    try:
                        #print "BBB"
                        os.rmdir(os.path.abspath(i))
                        print " REMOVED DIRECTORY: \"" + str(os.path.abspath(i)) + "\""
                    except:
                        #return __error__
                        try:
                            self.diffmov.Remove(os.path.abspath(x))
                        except:
                            print " REMOVED DIRECTORY [ERROR]: \"" + str(os.path.abspath(i)) + "\""
                            self.result_error.append(os.path.abspath(str(os.path.abspath(i))))                
        else:
            #print "\n"
            #print __help__
            print " PASS [ERROR]: \"" + str(os.path.abspath(x)) + "\" [Not a FILE or DIRECTORY]"

    def main(self):
        if len(sys.argv) > 1:
            for i in sys.argv[1:]:
                self.__removed(i)
                
            if len(self.result_error) >= 1:
                print "\n\n"
                if len(self.result_error) == 1:
                    print " RESULT: ERROR", len(self.result_error), " Item: "
                    print "\t [ERROR] --> ", self.result_error[0]
                else:
                    #print "REA = ", move_class.moved()
                    #os.system("PAUSE")
                    print " RESULT: ERROR", len(self.result_error), " Items: "
                    for x in self.result_error:
                        print "\t [ERROR REMOVE] --> ", x
            else:
                print "\n\n"
                print " RESULT: ALL OK"

        else:
            print "\n"
            print __help__
            
if __name__ == '__main__':
    rc =  rma()
    rc.main()
