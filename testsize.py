import sys
import os
from math import log

def sizeof_fmt2(num):
    """
        for actual with minus size
    """
    for x in [' bytes', ' KB', ' MB', ' GB']:
        if num < 1024.0 and num > -1024.0:
            return "%3.1f%s" % (num, x)
        num /= 1024.0
    return "%3.1f%s" % (num, ' TB')

def sizeof_fmt(num):
    for x in [' bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0

if __name__ == '__main__':
    print sizeof_fmt2(int(sys.argv[1]))
    print sizeof_fmt(int(sys.argv[1]))