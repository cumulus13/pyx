import md5
import sys
import argparse
import cpmm as cpm
import win32clipboard as w 

def usage():
    parser =  argparse.ArgumentParser()
    parser.add_argument("INPUT", help="Input which conver to MD5", action="store")
    parser.add_argument("-v", "--verbosity", help="Show process running", action="store_true")
    if len(sys.argv) > 1:
        args =  parser.parse_args()
        if args.INPUT:
            md5maker(args.INPUT)
        else:
            parser.print_help()
    else:
        parser.print_help()
        #pass
    
def md5maker(data):
    a =  md5.new(str(data)).hexdigest()
    print "\n"
    print "\t MD5 =", a
    setclipboard(a)
    return a

def setclipboard(clip):
    cpm.setText(w.CF_TEXT, clip)
    cget = cpm.getText()
    cpm.sendnotify(cget)
    
if __name__ == "__main__":
    usage()