import shutil
import os
import sys
import argparse

class mt(object):
    def __init__(self, path = None, dst = None):
        """initialize"""
        super(mt, self)
        self.path = path
        self.dst = dst
        self.files_moved = []

    def onerror(self, path):
        """handle error os.walk"""
        print "ERROR:", path

    def prepare(self, path = None, string = None):
        """Check path consistent"""
        start = False
        end = False
        #string = ""
        if path == None:
            if not self.path == None:
                path = self.path
            else:
                return False
        if '*' in path:
            #print "AAA"
            if os.path.dirname(path) != '':
                path = os.path.dirname(path)
            else:
                if path.index('*') == 0 and path[-1] != '*':
                    start = False
                    end = True
                    string = path[1:]
                    path = os.getcwd()
                elif path.index('*') == -1 and path[0] != '*':
                    start = True
                    end = False
                    string = path[:-1]
                    path = os.getcwd()
                elif path.index('*') == 0 and path[0] == '*':
                    start = False
                    end = True
                    string = path[1:-1]
                    path = os.getcwd()
            #print "start  1:", start
            #print "end    1:", end
            #print "string 1:", string
            #print "-" * 120
            return start, end, path, string
        else:
            #print "BBB"
            start = False
            end = False
            #print "start  2:", start
            #print "end    2:", end
            #print "string 2:", string
            #print "-" * 120
            return start, end, path, string

    def moveWalk(self, path = None, tfiles = None, tdirs = None):
        """move walk action"""

        if path == None:
            if not self.path == None:
                path = self.path
            else:
                return False        
        #if dst == None:
            #if self.dst != None:
                #dst = self.dst
            #else:
                #dst = os.getcwd()

        #start, end, path, string = self.prepare(path, string)
        #print "start  3:", start
        #print "end    3:", end
        #print "string 3:", string
        #print "-" * 120        
        #print "-" * 120
        #print "self.prepare(path, string) =",self.prepare(path, string)
        if tfiles:
            for root, dirs, files in os.walk(path, onerror= self.onerror):
                #print "ROOT  =", root
                #print "DIRS  =", dirs
                #print "FILES =", files
                if len(files) > 0:
                    for i in files:
                        mf = os.path.join(root, i)
                        self.files_moved.append(mf)
        elif tdirs:
            for root, dirs, files in os.walk(path):
                #print "ROOT  =", root
                #print "DIRS  =", dirs
                #print "FILES =", files
                if len(dirs) > 0:
                    for i in dirs:
                        mf = os.path.join(root, i)
                        self.files_moved.append(mf)            
        return self.files_moved

    def moveTree(self, path = None, dst = None, string = None, overwrite = None, tdirs = None):
        """main move action"""
        #print "start move ..."
        if path == None:
            if not self.path == None:
                path = self.path
            else:
                return False

        if dst == None:
            if self.dst != None:
                dst = self.dst
            else:
                dst = os.getcwd()
        
        start, end, path, string = self.prepare(path, string)
        #print "start  3:", start
        #print "end    3:", end
        #print "string 3:", string
        #print "-" * 120
        if tdirs:
            files = self.moveWalk(path, tdir= True)
        else:
            files = self.moveWalk(path, tfiles= True)
        #print "FILEX =", files
        #print "string =", string
        for mf in files:
            if start:
                print "FFF"
                if str(mf).startswith(string):
                    if overwrite:
                        #print "OVERWRITE"
                        if mf == os.path.join(dst, os.path.basename(mf)):
                            pass
                        else:
                            if os.path.exists(os.path.join(dst, os.path.basename(mf))):
                                os.remove(os.path.join(dst, os.path.basename(mf)))
                    try:
                        shutil.move(mf, dst)
                    except:
                        print "warning:", traceback.format_exc()
                        pass

            elif end:
                #print "EEE"
                if str(mf).endswith(string):
                    if overwrite:
                        #print "OVERWRITE"
                        if mf == os.path.join(dst, os.path.basename(mf)):
                            pass
                        else:
                            if os.path.exists(os.path.join(dst, os.path.basename(mf))):
                                os.remove(os.path.join(dst, os.path.basename(mf)))
                    try:
                        shutil.move(mf, dst)
                    except:
                        print "warning:", traceback.format_exc()
                        pass
            elif string:
                #print "GGG"
                #print "os.path.basename(mf) =", os.path.basename(mf)
                if "'" == string[0]:
                    if "'" == string[-1]:
                        string = string[1:-1]
                    else:
                        string = string[1:]
                if '"' == string[0]:
                    if '"' == string[-1]:
                        string = string[1:-1]
                    else:
                        string = string[1:]                
                #print "string 2             =", string
                #print "string in str(os.path.basename(mf)) =", string in str(os.path.basename(mf))
                if string in str(os.path.basename(mf)):
                    #print "GGG 1"
                    if overwrite:
                        #print "OVERWRITE"
                        if mf == os.path.join(dst, os.path.basename(mf)):
                            pass
                        else:
                            if os.path.exists(os.path.join(dst, os.path.basename(mf))):
                                os.remove(os.path.join(dst, os.path.basename(mf)))
                    try:
                        shutil.move(mf, dst)
                    except:
                        print "warning:", traceback.format_exc()
                        pass
                
    def usage(self):
        '''
            Usage help
           
            Default moving is files type

            usage: mt.py [-h] [-D] [-s STRING] [-p PATH] [-d DST] [-o] STRING
            
            positional arguments:
               PATTERN              string/pattent containt moving to, pattent may
                                    containt char "*"
        
            optional arguments:
              -h, --help            show this help message and exit
              -D, --dirs            Move directory type
              -s STRING, --string STRING
                                    Optional string containt, if option --dirs containt
                                    char "*", so string will fill with string after or/and
                                    before char it
              -p PATH, --path PATH  Optional Source Path files/directory, default path is
                                    None and this directory
              -d DST, --dst DST     Optional Destination Move Path, default dst
                                    (destination) is None and this directory
              -o, --overwrite       Overwrite files or directory
        '''

        parser = argparse.ArgumentParser()
        parser.add_argument('PATTERN', help = 'string/pattern containt moving to, pattent may containt char "*"', action = 'store')
        parser.add_argument('-D', '--dirs', help = 'Move directory type', action = 'store_true')
        parser.add_argument('-s', '--string', help = 'Optional string containt, if option --dirs containt char "*", so string will fill with string after or/and before char it', action = 'store', type = str)
        parser.add_argument('-p', '--path', help = 'Optional Source Path files/directory, default path is None and this directory', action = 'store')
        parser.add_argument('-d', '--dst', help = 'Optional Destination Move Path, default dst (destination) is None and this directory', action = 'store')
        parser.add_argument('-o', '--overwrite', help = 'Overwrite files or directory', action = 'store_true')
        if len(sys.argv) > 1:
            args = parser.parse_args()
            if args.path:
                self.moveTree(args.path, args.dst, args.string, args.overwrite, args.dirs)
            else:
                self.moveTree(args.PATTERN, args.dst, args.string, args.overwrite, args.dirs)
        else:
            print "\n"
            print "\tDefault moving is files type"
            print "\n"
            parser.print_help(file=None)

if __name__ == "__main__":
    c = mt()
    c.usage()
    #c.moveTree(sys.argv[1], sys.argv[2], sys.argv[3], True)