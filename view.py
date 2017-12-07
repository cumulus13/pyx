import os
import sys
import argparse
import re
from make_colors import make_colors

class view(object):
    def __init__(self, debug = False, **kwargs):
        self.debug = debug
        
    def filter_code(self, string):
        if len(string) > 0 and string[0] == '#':
            string = make_colors(string, 'green', attrs= ['bold'])        
        attrs = ['if ', 'else', 'while ', 'print ', 'elif ', ' in ', 'return ', 'from ', 'assert', 'for ', 'range', ' open', 'try:', 'except']
        modules = ['os', ' sys', 'sys.', 'datetime', 'strftime', 'strptime', 'time', 'isinstance']
        modules_attrs = ['.system']
        if 'def' in string:
            string = string.replace('def ', make_colors('def ', 'lightred', color_type= 'colorama'))
            string1 = "".join(str(string).split('def ')[1:])
            string = string.replace(string1, make_colors(string1, 'magenta', attrs = ['bold']))
        elif 'class' in string:
            string = string.replace('class ', make_colors('class ', 'cyan', attrs= ['bold']))
        elif 'import' in string:
            string = string.replace('import ', make_colors('import ', 'magenta', attrs= ['bold']))
        elif 'object' in string:
            string = string.replace('object', make_colors('object', 'blue', attrs= ['bold']))
        else:
            string = make_colors(string, 'lightwhite', color_type= 'colorama')
        for i in modules:
            if i in string:
                string = string.replace(i, make_colors(i, 'yellow', attrs= ['bold']))
        for i in attrs:
            if i in string:
                string = string.replace(i, make_colors(i, 'green', attrs= ['bold']))
        for i in modules_attrs:
            if i in string:
                string = string.replace(i[1:], make_colors(i[1:], 'magenta', attrs= ['bold']))                        
        return string
    
    def filter_first_number(self, number_string):
        if len(number_string) == 1:
            return "0" + number_string
        else:
            return number_string

    def view(self, filepath, numbers):
        def process():
            if isinstance(numbers, list):
                for i in numbers:
                    if '-' in i:
                        fr, to = str(i).split('-')
                        for x in range(int(fr), (int(to) + 1)):
                            #print self.filter_first_number(str(range(int(fr), (int(to) + 1)).index(x))) + ". " + self.filter_code(f[x][:-1])
                            print self.filter_first_number(str(x)) + ". " + self.filter_code(f[x][:-1])
                    elif str(i).isdigit():
                        print self.filter_first_number(str(i)) + ". " + self.filter_code(f[int(i)][:-1])
            else:
                for i in f:
                    print self.filter_first_number(str(f.index(i))) + ". " + self.filter_code(str(i).split("\n", 1)[0])
    
        if os.path.isfile(filepath):
            f = open(filepath).readlines()
            process()
    
    def usage(self):
        help_line_number = """
    Line number to view:
    * single-number [n]: just view on line number
    * multiply number [n1 n2 n3 n4]: view on multiply line number, example -n 1 40 50 100
    * range number [n1-n2 n5-n6]: view on range number from - to, support multiply
        """
        parse = argparse.ArgumentParser(formatter_class = argparse.RawTextHelpFormatter)
        parse.add_argument('FILE', help = 'text file view to', action = 'store')
        parse.add_argument('-n', '--number', help = help_line_number, action = 'store', nargs = '*')
    
        args = parse.parse_args()
        if len(sys.argv) == 1:
            parse.print_help()
        else:
            self.view(args.FILE, args.number)
        
if __name__ == '__main__':
    c = view()
    c.usage()