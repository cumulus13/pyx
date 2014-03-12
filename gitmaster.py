import os
import sys
import argparse

dirname = os.getcwd()
dirbase = os.path.basename(dirname)
file = os.path.basename(__file__)
DEFAULT_REPO = os.getcwd()
DEFAULT_URL = "http://gitserver.net/git"

def usage2():
    helpx = """usage: gitmaster.py [-h] [-r REPO] [-u URL] REPOSITORY

positional arguments:
  REPOSITORY            Directory of Repository

optional arguments:
  -h, --help            show this help message and exit
  -r REPO, --repo REPO  Directory of Repository
  -u URL, --url URL     Url of Git Server
"""
    print helpx

def usage3(REPO, args, parser):
    if args.repo:
        REPO = args.repo
        if args.url:
            if args.head:
                if os.path.isdir(os.path.abspath(args.repo)):
                    dirpath = os.path.abspath(args.repo)
                    #print "os.path.abspath(args.repo) =", dirpath
                    if args.head == "not" or args.head == "Not" or args.head == "NOT":
                        gitmaster(url = args.url , path = dirpath, head= " ")
                    else:
                        gitmaster(url = args.url , path = dirpath, head= " " + str(args.head))
                else:
                    print "\t Not a Git Directory !\n"
                    parser.print_help()													
            else:
                if os.path.isdir(os.path.abspath(args.repo)):
                    dirpath = os.path.abspath(args.repo)
                    #print "os.path.abspath(args.repo) =", dirpath
                    gitmaster(url = args.url , path = dirpath)
                else:
                    print "\t Not a Git Directory !\n"
                    parser.print_help()					
        else:
            if os.path.isdir(args.repo):
                os.chdir(os.path.abspath(args.repo))
                gitmaster(path=os.path.abspath(args.repo))
            else:
                print "\t Not a Git Directory !\n"
                parser.print_help()
    elif args.url:
        if args.head:
            if os.path.isdir(os.path.abspath(REPO)):
                dirpath = os.path.abspath(REPO)
                #print "os.path.abspath(args.repo) =", dirpath
                if args.head == "not" or args.head == "Not" or args.head == "NOT":
                    gitmaster(url = args.url , path = dirpath, head= " ")
                else:
                    gitmaster(url = args.url , path = dirpath, head= " " + str(args.head))
            else:
                print "\t Not a Git Directory !\n"
                parser.print_help()							
        else:
            if os.path.isdir(os.path.abspath(REPO)):
                dirpath = os.path.abspath(REPO)
                #print "os.path.abspath(args.repo) =", dirpath
                gitmaster(url = args.url , path = dirpath, head= " " + str(args.head))
            else:
                print "\t Not a Git Directory !\n"
                parser.print_help()
    elif args.head:
        if os.path.isdir(os.path.abspath(REPO)):
            dirpath = os.path.abspath(REPO)
            #print "os.path.abspath(args.repo) =", dirpath
            if args.head == "not" or args.head == "Not" or args.head == "NOT":
                gitmaster(path = dirpath, head= " ")
            else:
                gitmaster(path = dirpath, head= " " + str(args.head))
        else:
            print "\t Not a Git Directory !\n"
            parser.print_help()
    else:
        dirpath = os.path.abspath(REPO)
        gitmaster(path = dirpath)	

def usage(help=None):
    if help == None:
        if len(sys.argv) > 1:
            if sys.argv[1] == "-r" or sys.argv[1] == "-u" or sys.argv[1] == "-t":
                parser = argparse.ArgumentParser()
                parser.add_argument('-r', '--repo', help="Directory of Repository", action="store")
                parser.add_argument('-u', '--url', help="Url of Git Server", default=DEFAULT_URL, action="store")
                parser.add_argument('-t', '--head', help="Type of Master, Development, Develop or other",  action="store")
                #parser.add_argument("-v", "--verbosity", help="Show running Process", action="store_true")			
                args = parser.parse_args()
                if args.repo:
                    usage3(args.repo, args, parser)
                else:
                    if os.path.isdir(os.path.join(os.path.abspath("."),".git")):
                        os.chdir(os.path.abspath("."))
                        usage3(os.path.abspath("."), args, parser)
                    else:
                        parser.print_help()
            else:
                parser = argparse.ArgumentParser()
                parser.add_argument('REPOSITORY', help="Directory of Repository", action="store")
                parser.add_argument('-r', '--repo', help="Directory of Repository", action="store")
                parser.add_argument('-u', '--url', help="Url of Git Server", default=DEFAULT_URL, action="store")
                parser.add_argument('-t', '--head', help="Type of Master, Development, Develop or other",  action="store")
                #parser.add_argument("-v", "--verbosity", help="Show running Process", action="store_true")
                if os.path.isdir(os.path.abspath(sys.argv[1])):
                    args = parser.parse_args()
                    if args.REPOSITORY:
                        if os.path.isdir(os.path.abspath(args.REPOSITORY)):
                            usage3(args.REPOSITORY, args, parser)
                        else:
                            print "\n"
                            print "This is NOT a Git Directory (REPOSITORY)\n"
                            parser.print_help()						
                    else:
                        pass
                else:
                    for i in sys.argv:
                        if "-r" in i or "-u" in i or "-t" in i:
                            args = parser.parse_args()
                            if args.REPOSITORY:
                                if os.path.isdir(os.path.abspath(args.REPOSITORY)):
                                    usage3(args.REPOSITORY, args, parser)
                                else:
                                    print "\n"
                                    print "This is NOT a Git Directory (REPOSITORY)\n"
                                    parser.print_help()						
                            else:
                                pass
                        else:
                            parser.print_help()
                            break;
        else:
            gitmaster()
    elif help == "printhelp":
        usage2()

def gitmaster(url='http://gitserver.net/git', path=None, head=" master"):
    #print "head =", head
    if head == None or head == " None" or head == "" or head == '' or head == " ":
        head = " master"
    #print "head =", head
    print "\n"
    try:
        if path == None:
            path = dirname
            dirbase = os.path.basename(path)
        else:
            dirbase = os.path.basename(path)

        if os.path.isdir(os.path.join(os.path.abspath(path),".git")):
            os.chdir(path)
            os.system("git push " + str(url) + "/" + dirbase + str(head))
        else:
            if path != None:
                os.chdir(path)
                if os.path.isdir(os.path.join(os.path.abspath(path),".git")):
                    os.system("git push " + str(url) + "/" + dirbase + str(head))
                else:
                    print "\t this is NOT a Git Repository 3\n"
                    usage("printhelp")
            else:
                if os.path.isdir(os.path.join(os.path.abspath(dirname),".git")):
                    os.system("git push " + str(url) + "/" + dirbase + str(head))
                else:
                    print "\t There No a PATH Git Directory !\n"
                    usage("printhelp")
    except:
        usage("printhelp")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "--help" or sys.argv[1] == '-h' or sys.argv[1] == '-?' or sys.argv[1] == '?':
            usage()
        elif "http:" in sys.argv[1]:
            gitmaster(sys.argv[1])
        else:
            usage()
    else:
        if os.path.isdir(os.path.join(os.path.abspath(dirname),".git")):
            gitmaster()
        else:
            usage()
