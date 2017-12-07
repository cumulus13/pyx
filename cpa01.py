# import shutil
# import os
# import sys

# class cpa(object):
# 	def __init__(self):
# 		super(cpa, self)
# 		self.error_report = []

# 	def error(self, value=True, clear=None):
# 		if clear:
# 			return self.error_report = []
# 		else:
# 			return self.error_report.append(value)

# 	def overWrite(self, path, dest=None):
# 		# if overwrite:
# 		if dest:
# 			# if os.path.isdir(dest):
# 			dest_overwrite_check = os.path.join(os.path.abspath(dest), os.path.basename(path))
# 			if os.path.isfile(path)
# 				os.rmdir(dest_overwrite_check)
# 				shutil.copy2(path, dest)
# 			# elif os.path.isfile(dest):
# 			# 	if str(os.path.basename(path)).lower() == str(os.path.basename(dest)):
# 			# 		os.remove(dest)
# 			# else:
# 			# 	pass
# 		else:
# 			return error()

# 	def copyd(self, path, overwrite=None, inside=True, dest=None, makedir=None):
# 		if isinstance(path, list):
# 			pass
# 		else:
# 			# if os.path.isfile(path):
# 			# if inside:
# 			if dest:
# 				if os.path.isdir(dest):
# 					if inside: #default True and always
# 						if overwrite:
# 							self.overWrite(path, dest)
# 						else:
# 							shutil.copy2(path, dest)
# 					else:
# 						if os.path.exists(os.path.abspath(dest), os.path.basename(path)):
# 							q = raw_input("\t Directory/File is exists !, Do you want to overwrite, structure will be overwrite too [y/n]: ")
# 							if str(q).lower() == 'y':
# 								if os.path.isdir(path):
# 									os.removedirs(os.path.exists(os.path.abspath(dest), os.path.basename(path)))
# 									shutil.copytree(path, dest)
# 								elif os.path.isfile(path):
# 									if os.path.isdir(dest):
# 										os.removedirs(os.path.exists(os.path.abspath(dest), os.path.basename(path)))
# 										shutil.copyfile(path, dest)
# 									elif os.path.isfile(path):
# 										os.remove(os.path.exists(os.path.abspath(dest), os.path.basename(path)))
# 										shutil.copyfile(path, dest)
# 								else:
# 									return error()

# 				else:
# 					if makedir:
# 						os.makedirs(dest)
# 						if overwrite:
# 							self.overWrite(path, dest)
# 						else:
# 							shutil.copy2(path, dest)
# 					else:
# 						return error()
# 			else:
# 				return error()
# 			# else:
# 			# 	dest = os.getcwd()
# 			# 	if os.path.isdir(dest):
# 			# 		if overwrite:
# 			# 			self.overWrite(path, dest)
# 			# 		else:
# 			# 			shutil.copy2(path, dest)
# 			# 	else:
# 			# 		if makedir:
# 			# 			os.makedirs(dest)
# 			# 			if overwrite:
# 			# 				self.overWrite(path, dest)
# 			# 			else:
# 			# 				shutil.copy2(path, dest)
# 			# 		else:
# 			# 			return error()
				
# 			# elif os.path.isdir(path):
# 			# 	if inside:
# 			# 		if dest:
# 			# 			if os.path.isdir(dest):
# 			# 				if overwrite:
# 			# 					self.overWrite(path, dest)
# 			# 				else:
# 			# 					shutil.copy2(path, dest)
# 			# 			else:
# 			# 				if makedir:
# 			# 					os.makedirs(dest)
# 			# 					if overwrite:
# 			# 						self.overWrite(path, dest)
# 			# 					else:
# 			# 						shutil.copy2(path, dest)
# 			# 				else:
# 			# 					return error()
# 			# 		else:
# 			# 			return error()
# 			# 	else:
# 			# 		dest = os.getcwd()
# 			# 		if os.path.isdir(dest):
# 			# 			if overwrite:
# 			# 				self.overWrite(path, dest)
# 			# 			else:
# 			# 				shutil.copy2(path, dest)
# 			# 		else:
# 			# 			if makedir:
# 			# 				os.makedirs(dest)
# 			# 				if overwrite:
# 			# 					self.overWrite(path, dest)
# 			# 				else:
# 			# 					shutil.copy2(path, dest)
# 			# 			else:
# 			# 				return error()

#######################################################################################################################

import sys
import os
import traceback
import shutil

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

class process(object):
    def __init__(self):
        super(process, self)
        self.result_error = []
        self.result_overwrite = []
        self.publicTo = None

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

    def start_copyd(self, pattern, _to=sys.argv[-1]):
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
                    self.__copyd(x,_to,sys.argv[-1])
                else:	
                    #print "X --> ",x
                    #print "_to --> ", os.path.abspath(_to)
                    self.__copyd(x,os.path.abspath(_to))
            else:
                pass

        return self.result_error


    def copyd(self,to_=sys.argv[-1]):
        to_ = os.path.abspath(to_)
        if sys.argv[-2] == "-e":
            to_= os.path.abspath(sys.argv[-3])
            len_arg = len(sys.argv) - 2
        else:
            len_arg = len(sys.argv)

        for i in range (1,int(len_arg) - 1):
            if os.path.isfile(sys.argv[i]) == True:
                try:
                    shutil.copy2(sys.argv[i], to_)
                    print " COPY FILE: \"" + sys.argv[i] + "\" --> " + os.path.abspath(sys.argv[-1])
                except:
                    #return __error__
                    print " COPY FILE [ERROR]: \"" + sys.argv[i] + "\" --> " + os.path.abspath(sys.argv[-1] + " [ERROR]")
                    self.result_error.append(os.path.abspath(sys.argv[i]))

            elif os.path.isdir(sys.argv[i]) == True:
                try:
                    if os.path.isdir(os.path.abspath(to_)):
                        to_ = os.path.join(to_, os.path.basename(os.path.abspath(sys.argv[i])))
                        try:
                            shutil.copytree(sys.argv[i], to_, True)
                            print " COPY DIRECTORY: \"" + sys.argv[i] + "\" --> " + os.path.abspath(sys.argv[-1])
                        except:
                            pass
                    else:
                        os.mkdir(os.path.abspath(to_))
                        try:
                            to_ = os.path.join(to_, os.path.basename(os.path.abspath(sys.argv[i])))
                            shutil.copytree(sys.argv[i], to_, True)
                        except:
                            pass
                        
                except:
                    #return __error__
                    print " COPY DIRECTORY [ERROR]: \"" + sys.argv[i] + "\" --> " + os.path.abspath(sys.argv[-1] + " [ERROR]")
                    self.result_error.append(os.path.abspath(sys.argv[i]))
                    print "\tERROR =", traceback.format_exc()
            elif "*" in sys.argv[i]:
                self.start_copyd(sys.argv[i],to_)
                if len(self.result_overwrite) != '':
                    #print "self.result_overwrite = ", self.result_overwrite
                    self.existConfr()
        return self.result_error

    def main(self):
        if os.path.isdir(sys.argv[-1]):
            print "\n"
            copyd()
        elif sys.argv[-1] == ".":
            print "\n"
            copyd(os.getcwd())
        elif sys.argv[-1] == "~":
            print "\n"
            copyd(os.getcwd())
        else:
            print "\n"
            print __help__
            raise SyntaxError ("Check Your Syntax !")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        copy_class = process()
        copy_class.copyd()
        if len(copy_class.copyd()) >= 1:
            print "\n\n"
            if len(copy_class.copyd()) == 1:
                print " RESULT: ERROR", len(copy_class.copyd()), " Item: "
                print "\t [ERROR] --> ", copy_class.copyd()[0]
            else:
                print "REA = ", copy_class.copyd()
                os.system("PAUSE")
                for x in copy_class.copyd():
                    print " RESULT: ERROR", len(copy_class.copyd()), " Items: "
                    print "\t [ERROR] --> ", x
        else:
            print "\n\n"
            print " RESULT: ALL OK"

    else:
        print "\n"
        print __help__