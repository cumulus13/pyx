import argparse
import sys

class usage(object):
    def __init__(self):
        super(usage, self)
        self.parser = argparse.ArgumentParser()
        
    def usage(self):
        self.parser.add_argument('-t', '--test', help='test 001', action='store')
        args = self.parser.parse_args()
        if len(sys.argv) == 1:
            self.parser.print_help()
        else:
            print "ERHERHEGRHE"
            
            
