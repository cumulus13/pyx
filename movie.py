#!c:/SDK/Anaconda2/python.exe

import argparse
import sys
import re
import os
from make_colors import make_colors
from pydebugger.debug import debug
import inspect
if sys.platform == 'win32':
    import msvcrt as getch
else:
    import getch

def pause(page=''):
    lineno = str(inspect.stack()[1][2])		
    if page:
        page = make_colors("[" + str(page) + "]", "lw", "bl")
    else:
        page = make_colors("[" + str(lineno) + "]", "lw", "bl")
    note = make_colors("Enter to Continue . ", "lw", "lr") + "[" + page + "] " + make_colors("x|q = exit|quit", "lw", "lr")
    print(note)
    q = getch.getch()
    if q == 'x' or q == 'q':
        sys.exit(make_colors("EXIT !", 'lw','lr'))
        
def rename(name, new_name=None, test = False, debugx = False):
    debug(name = name, debug = debugx)
    ext = ''
    dirname = os.path.dirname(name)
    debug(dirname = dirname, debug = debugx)
    if not new_name:
        new_name_1 = os.path.basename(name)
        if not new_name_1:
            print(make_colors("NOT A FILE !", 'lw','lr', ['blink']))
            sys.exit()
            
        debug(new_name_1 = new_name_1, debug = debugx)
        if os.path.isfile(new_name_1):
            new_name_1, ext = os.path.splitext(new_name_1)
        
        new_name_1 = re.sub("\.", " ", new_name_1)
        print(make_colors("NEW NAME ", 'lc') + ":" + make_colors(new_name_1, 'lw', 'lr'))
        
        year = re.findall('\d{4}', new_name_1)
        year_on_bracket = re.findall('\(\d{4}\)', new_name_1)
        debug(year = year, debug = debugx)
        debug(year_on_bracket = year_on_bracket, debug = debugx)
        
        if year and not year_on_bracket:
            year = "(%s)" % (str(year[0]))
            new_name_2 = re.sub("\d{4}", year, new_name_1, 1)
        else:
            year = year_on_bracket[0]
            new_name_2 = new_name_1
        debug(year = year, debug = debugx)
        debug(new_name_2 = new_name_2, debug = debugx)
        
        trash_name = re.findall('\d{4}\)(.+$)', new_name_2)
        debug(trash_name = trash_name, debug = debugx)
        if not trash_name:
            trash_name = re.findall('\d{4}(.+$)', new_name_2)
        debug(trash_name = trash_name, debug = debugx)
        if trash_name:
            trash_name = trash_name[0]
            debug(trash_name = trash_name, debug = debugx)
            if not trash_name == ")":
                debug(trash_name = trash_name, debug = debugx)
                new_name = new_name_2.split(trash_name)
                if new_name:
                    new_name = new_name[0]
            else:
                debug(new_name_2 = new_name_2, debug = debugx)
                new_name = new_name_2
        else:
            new_name = new_name_2
    DEST_DIR = None
    if not os.path.splitext(new_name)[1]:
        ext = os.path.splitext(name)[1]
        DEST_DIR = os.path.join(dirname, new_name)
        new_name = new_name + ext
    debug(new_name = new_name, debug = debugx)
    if not DEST_DIR:
        DEST_DIR = os.path.join(dirname, new_name)
    debug(DEST_DIR = DEST_DIR, debug = debugx)
    if not os.path.splitext(new_name)[1]:
        DEST_FILE = os.path.join(dirname, new_name) + ext
    else:
        DEST_FILE = os.path.join(dirname, new_name)
    debug(DEST_FILE = DEST_FILE, debug = debugx)
    test_str = ''
    
    if test:
        test_str = make_colors("[TEST]", 'lw','lr') + " "
    if not os.path.isdir(DEST_DIR):
        print(make_colors(test_str + "MKDIR     :", 'lw','bl') + " " + make_colors(DEST_DIR, 'b','lg'))
        if not test:
            os.makedirs(DEST_DIR)
    
    if not os.path.basename(name) == os.path.basename(DEST_FILE):
        print(test_str + make_colors("RENAME    :", 'b','ly') + " " + make_colors(name, 'lg') + " --> " + make_colors(DEST_FILE, 'ly'))
    else:
        print(test_str + make_colors("RENAME WITH SAME NAME:", 'b','ly') + " " + make_colors(name, 'lg') + " --> " + make_colors(DEST_FILE, 'ly'))
    print(test_str + make_colors("MOVE      :", 'b','ly') + " " + make_colors(DEST_FILE, 'lg') + " --> " + make_colors(DEST_DIR, 'ly'))
    if not test:
        if not os.path.basename(name) == os.path.basename(DEST_FILE):
            os.system('move "%s" "%s"'%(name, DEST_FILE))
        else:
            print(test_str + make_colors("RENAME NO NEED:", 'b','ly') + " " + make_colors(name, 'lg') + " --> " + make_colors(DEST_FILE, 'ly'))
        os.system('move "%s" "%s"'%(DEST_FILE, DEST_DIR))

def usage():
    parser = argparse.ArgumentParser(formatter_class= argparse.RawTextHelpFormatter)
    parser.add_argument('MOVIE', action = 'store', help = 'Movie name')
    parser.add_argument('-n', '--new-name', action='store', help='Alternative New Name')
    parser.add_argument('-t', '--test', action = 'store_true', help = 'Just Test, not really rename')
    parser.add_argument('-d', '--debug', action = 'store_true', help = 'Debug process')
    if len(sys.argv) == 1:
        parser.print_help()
    else:
        args = parser.parse_args()
        rename(args.MOVIE, args.new_name, args.test, args.debug)
        
if __name__ == '__main__':
    usage()
    