#!c:/SDK/Anaconda2/python.exe
from __future__ import print_function
from datetime import datetime
from make_colors import make_colors
print("\n")
print (datetime.strftime(datetime.now(), make_colors('%Y', 'lw', 'bl') + '/' + make_colors('%m', 'b', 'lg') + '/' + make_colors('%d', 'lw', 'm') + " " + make_colors('%H:%M:%S', 'b', 'lc') + make_colors('.%f', 'lw', 'lr')))