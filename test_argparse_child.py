import test_argparse_root
import sys

class usage(test_argparse_root.usage):
    def __init__(self):
        super(usage, self)
        self.usage = test_argparse_root.usage
        
    def usage(self):
        my_usage = self.usage.usage
        print "ererer"
        self.parser.add_argument('-a', '--a',  help='Add TEst',  action='store')
        if len(sys.argv) == 1:
            self.parser.print_help()
        else:
            print "QWQWQW"
        
if __name__ == '__main__':
    c = usage()
    c.usage()