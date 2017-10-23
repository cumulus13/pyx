import os
import sys
import argparse
import sendgrowl
import clipboard
import re

PATH_APP = r'c:\exe\cpathx.exe'


def addpath(path, add=None):
    # print "PATH =", path
    if add != None:
        os.system(PATH_APP + " " + path + '\\' + add)
    else:
        os.system(PATH_APP + " " + path)
        
def copyPath(path):
    if isinstance(path, list):
        if '+' in path:
            path.remove('+')
        if len(path) > 1:
            a_path = '\\'.join(path)
        else:
            a_path = path[0]
    else:
        a_path = str(path).replace('+', '')
    return os.path.abspath(a_path)

def replace(data, filename, noext=True):
    if noext:
        pass
    else:
        filename, ext = os.path.splitext(filename)
    if isinstance(data, list):
        for i in data:
            fr, to = i.split(":")
            if to == '':
                to = ' '
            if fr == '':
                fr = ' '
            filename = str(filename).replace(fr, to)
    else:
        fr, to = data.split(":")
        if to == '':
            to = ' '
        if fr == '':
            fr = ' '
        filename = str(filename).replace(fr, to)
    if noext:
        return filename
    else:
        return filename + ext

def usage():
    #parser = optparse.OptionParser()
    parser = argparse.ArgumentParser(formatter_class= argparse.RawTextHelpFormatter)
    parser.add_argument('PATH', help = 'Path', nargs = '*')
    parser.add_argument('-a', '--absolute',
                      help='Copy Absoulte Path name only', action='store_true')
    parser.add_argument(
        '-b', '--base', help='Copy Base name only', action='store_true')
    parser.add_argument(
        '-d', '--dir', help='Copy Directory name only', action='store_true')
    parser.add_argument('-s', '--string',
                      help='Copy argument string only', action='store_true')
    parser.add_argument('-S', '--string-no-ext',
                      help='Copy argument string only without extention', action='store_true')
    parser.add_argument('-r', '--replace', help='Replace custom string example: a:b c:d pattern:replace', action='store', nargs = '*')
    
    if len(sys.argv) == 1:
        copypath(os.getcwd)
    else:
        args = parser.parse_args()
        path = args.PATH
        path = "\\".join(path)
        print "PATH 0 =", path
        if args.base:
            copyPath(os.path.basename(path))
        elif args.dir:
            copyPath(os.path.dirname(path))
        elif args.string:
            clipboard.copy(path)
        elif args.string:
            clipboard.copy(os.path.splitext(path)[0])
        elif args.replace:
            for i in args.replace:
                pattern, repl = str(i).split(":")
                path = str(path).replace(pattern, repl)
        else:
            copyPath(path)
                
    
    #if len(sys.argv) == 1:
        ## parser.print_help()
        #addpath(os.getcwd())
    #else:
        #options, args = parser.parse_args()
        #BASE_DIR = os.getcwd()
        #linux = False
        #if len(args) > 0:
            #if "/" == args[-1]:
                #del(args[-1])
                #linux = True
            ## print "args 1        =", args
            ## print "len(args)     =", len(args)
        #if options.absolute:
            #if len(args) > 0:
                #if args[0][1] == ":":
                    #path = "\\".join(args)
                #else:
                    #path = "\\".join(args)
                    #path = os.path.abspath(path)
            #else:
                #path = os.path.abspath(os.getcwd())

        #if options.base:
            #if len(args) > 0:
                #if args[0][1] == ":":
                    #path = "\\".join(args)
                    #path = os.path.basename(path)
                #else:
                    #path = "\\".join(args)
                    #path = os.path.abspath(path)
                    #path = os.path.basename(path)
            #else:
                #path = os.path.abspath(os.getcwd())
                #path = os.path.basename(path)

        #elif options.dir:
            #if len(args) > 0:
                #if args[0][1] == ":":
                    #path = "\\".join(args)
                    #path = os.path.dirname(path)
                #else:
                    #path = "\\".join(args)
                    #path = os.path.abspath(path)
                    #path = os.path.dirname(path)
            #else:
                #path = os.path.dirname(os.getcwd())
        #elif options.string:
            #path = path = "\\".join(args)
            #if options.replace:
                #path = replace(options.replace, path, False)
        #elif options.string_no_ext:
            #path = path = "\\".join(args)
            #path = os.path.splitext(path)[0]
            #if options.replace:
                #path = replace(options.replace, path, True)
        #else:
            #if len(args) > 0:
                #if args[0][1] == ":":
                    #path = "\\".join(args)
                #else:
                    #path = "\\".join(args)
                    #path = os.path.abspath(path)
            #else:
                #path = os.getcwd()
        #if linux:
            #path = str(path).replace('\\', '/')
        #addpath(path)

if __name__ == '__main__':
    usage()
