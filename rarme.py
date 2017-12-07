import os
import sys
import msvcrt
import shutil

__version__ = "0.5"
__filename__ = os.path.basename(sys.argv[0])
__author__ = "licface"
__url__ = "licface@yahoo.com"
__target__ = "all"
__build__ = "2.7"
__test__ = "0.1"

class rarme(object):
    def __init__(self):
        super(rarme, self)

    def getPutch(self, prompt="\t Are you want to delete the original source ? (y[[Y]es]/n[[N]o]) : "):
        for x in prompt:
            msvcrt.putch(x)
            
        z = msvcrt.getch()
        msvcrt.putch("\n")
        return z
        
    def on_rm_error(self, func, path, exc_info):
        os.chmod(path, stat.S_IWRITE)
        os.unlink(path)

    def multi_del(self, data):
        q = self.getPutch()
        if q == "y" or q == "Y" or q == "Yes" or q == "yes" or q == "y" or q == "Y" or q == "Yes" or q == "yes":
            for i in data:
                if os.path.isdir(os.path.abspath(i)):
                    shutil.rmtree(data_rar_02, onerror = on_rm_error)
                else:
                    try:
                        os.remove(os.path.abspath(i))
                    except:
                        try:
                            os.system("del " + str(os.path.abspath(i)) + " > NUL")
                        except:
                            raise ScriptError("Can't use os.system !")

        elif q == "n" or q == "N" or q == "no" or q == "No" or q == "n" or q == "N" or q == "no" or q == "No":
            sys.exit()
        else:
            print "\n"
            print "\t You no select \'Y\' or \'N\' "
            print "\t Bye ... !"
            sys.exit()

    def confr_del(self, data):
        if isinstance(data, (list,tuple)):
            self.multi_del(data)

        elif os.path.isdir(data):
            q = self.getPutch()
            if q == "y" or q == "Y" or q == "Yes" or q == "yes" or q == "y" or q == "Y" or q == "Yes" or q == "yes" :
                shutil.rmtree(data,onerror = on_rm_error)
            elif q == "n" or q == "N" or q == "no" or q == "No":
                sys.exit()
            else:
                print "\n"
                print "\t You no select \'Y\' or \'N\' "
                print "\t Bye ... !"
                sys.exit()
        else:
            q = self.getPutch()
            if q == "y" or q == "Y" or q == "Yes" or q == "yes" or q == "y" or q == "Y" or q == "Yes" or q == "yes" :
                try:
                    os.remove(data)
                except:
                    os.system("del \"" + data + "\" > NUL")
            elif q == "n" or q == "N" or q == "no" or q == "No" or q == "n" or q == "N" or q == "no" or q == "No":
                sys.exit()
            else:
                print "\n"
                print "\t You no select \'Y\' or \'N\' "
                print "\t Bye ... !"
                sys.exit()

    def rarme(self, data, out=None, ext=None):
        if(len(data) > 0):
            if ext:
                if not ext[0] == '.':
                    ext = "." + ext
                if not os.path.splitext(data)[1] == ext:
                    return False

            if out:
                if os.path.splitext(out)[1] == ".rar\" \"":
                    out = out
                else:
                    out = out + ".rar\" \""
            else:
                out = data + ".rar\" \""

            os.system("rar a \"" + out + data + "\"") 
            os.system("rar t \"" + out)
            return True

    def multi_rar(self, data, out=None, ext=None):
        if isinstance(data, list):
            for i in data:
                self.rarme(i, out, ext)
        elif "*" in data:
            if os.path.dirname(data) == '':
                data = os.getcwd()
            else:
                data = os.path.dirname(data)

            data = os.listdir(data)
            data1 = []
            for i in data:
                data1.append(os.path.join(data, i))
            for i in data1:
                self.rarme(i, out, ext)

        else:
            self.rarme(data, out)
        self.confr_del(data)

    def testme(self, data, out=None, ext=None):
        if(len(data) > 0):
            if ext:
                if not ext[0] == '.':
                    ext = "." + ext
                print "Ext =", ext
                if not os.path.splitext(data)[1] == ext:
                    return False
            print "data =", data

    def usage(self):
        import argparse
        parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
        parser.add_argument('PATH', help='File/Dir/*', action='store')
        parser.add_argument('-o', '--out', help='Option Out name', action='store')
        parser.add_argument('-e', '--ext', help='Rar with extention only', action='store')
        if len(sys.argv) == 1:
            parser.print_help()
        else:
            args = parser.parse_args()
            self.multi_rar(args.PATH, args.out, args.ext)

if __name__ == '__main__':
    c = rarme()
    c.usage()
    # data = "bbbb.txt"
    # c.testme(data, ext=".txt")
