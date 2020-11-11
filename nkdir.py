# !python2
from __future__ import print_function

import argparse
import sys
import os
import re
from pydebugger.debug import debug
#import clipboard

def rename(src, dst = None, movie = False, pattern = None, title = False):
    src = os.path.realpath(src)
    ext = os.path.splitext(src)[1]
    #print("ext =", ext)
    if not dst:
        dst = src        
    src_base = os.path.dirname(src)
    src_name = os.path.basename(src)
    #print("src_name 0 =", src_name)
    year = []
    if pattern:
        if isinstance(pattern, list):
            for i in pattern:
                #print("i =", i)
                _ft, _to = str(i).strip().split(":")
                if _ft == ".":
                    _ft = "\."
                if _to == "s":
                    _to = " "
                #print("_ft =", _ft)
                #print("_to =", _to)
                #print("src_name 1 =", src_name)
                src_name = re.sub(_ft, _to, src_name)
                #print("src_name x =", src_name)
        else:
            if ":" in pattern:
                _ft, _to = str(pattern).strip().split(":")
                src_name = re.sub(_ft, _to, src_name)
    if movie:
        #print('src_name =', src_name)
        c = re.findall("\(\d{4}\)", src_name)
        #print("c =", c)
        if not c:
            debug(src_base = src_base)
            #print("src_base =", src_base)
            other = re.findall('(?<=\d{4})(.*)', src_name)
            #print("other =", other)
            src_name = re.sub(other[0], "", src_name)
            #print("src_name 2 =", src_name)
            year = re.findall("\d{4}", src_name)
            #print("year =", year)
            if year:
                year = "(" + str(year[0]).strip() + ")"
                src_name = re.sub("\d{4}", year, src_name)
        else:
            other = re.findall('(?<=\(\d{4}\))(.*)', src_name)
            src_name = re.sub(other[0], "", src_base)
    else:
        ext = ""
    dst = os.path.join(src_base, src_name)
    if title:
        dst = str(dst).title()
        #print("src =", src)
    #print("dst =", dst)
    os.rename(src, dst + ext)
    os.makedirs(dst)
    
def usage():
    parser = argparse.ArgumentParser(formatter_class = argparse.RawTextHelpFormatter)
    parser.add_argument("SRC", action = "store", help = "Rename from ")
    parser.add_argument("-d", '--dst', action = "store", help = "Rename to ")
    parser.add_argument('-m', '--movie', action = "store_true", help = "is movie name")
    parser.add_argument('-p', '--pattern', action ='store', help = "pattern rename, format: from_word:to_word, example: badworld:goodworld, data1:data2, ...", nargs = "*")
    parser.add_argument('-t', '--title', action = 'store_true', help = 'make upper on each of first letter')
    if len(sys.argv) == 1:
        parser.print_help()
    else:
        args = parser.parse_args()
        rename(args.SRC, args.dst, args.movie, args.pattern, args.title)
        
if __name__ == '__main__':
    usage()