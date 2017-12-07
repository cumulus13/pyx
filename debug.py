#-*- encoding: utf-8 -*-
#encoding: utf-8

import colorama
import termcolor
import inspect
import random

DEBUG = False

class debugger(object):
    def __init__(self, defname = None, debug = None, **kwargs):
        super(debugger, self)
        self.DEBUG = debug
        if DEBUG:
            self.DEBUG = DEBUG
        print "DEBUG =", self.DEBUG
        #self.printlist(defname, debug, **kwargs)
        
    def show_details(self, name, f):
        """Show details of a callable object."""
        print '%s:' % name
        print '\tobject:', f
        print '\t__name__:', 
        try:
            print f.__name__
        except AttributeError:
            print '(no __name__)'
        print '\t__doc__', repr(f.__doc__)
        return    
        
    def setDebug(self, debug):
        self.DEBUG = debug

    def printlist(self, defname = None, debug = None, classname = '', **kwargs):
        if not debug:
            debug = self.DEBUG
        color_random_1 = [colorama.Fore.GREEN, colorama.Fore.YELLOW, colorama.Fore.LIGHTWHITE_EX, colorama.Fore.LIGHTCYAN_EX, colorama.Fore.LIGHTMAGENTA_EX, colorama.Fore.GREEN, colorama.Fore.YELLOW, colorama.Fore.LIGHTWHITE_EX, colorama.Fore.LIGHTCYAN_EX, colorama.Fore.LIGHTMAGENTA_EX, colorama.Fore.GREEN, colorama.Fore.YELLOW, colorama.Fore.LIGHTWHITE_EX, colorama.Fore.LIGHTCYAN_EX, colorama.Fore.LIGHTMAGENTA_EX, colorama.Fore.GREEN, colorama.Fore.YELLOW, colorama.Fore.LIGHTWHITE_EX, colorama.Fore.LIGHTCYAN_EX, colorama.Fore.LIGHTMAGENTA_EX, colorama.Fore.GREEN, colorama.Fore.YELLOW, colorama.Fore.LIGHTWHITE_EX, colorama.Fore.LIGHTCYAN_EX, colorama.Fore.LIGHTMAGENTA_EX, colorama.Fore.GREEN, colorama.Fore.YELLOW, colorama.Fore.LIGHTWHITE_EX, colorama.Fore.LIGHTCYAN_EX, colorama.Fore.LIGHTMAGENTA_EX]
        colorama.init()
        formatlist = ''
        arrow = colorama.Fore.YELLOW + ' -> '
        if not kwargs == {}:
            for i in kwargs:
                #formatlist += color_random_1[kwargs.keys().index(i)] + i + ": " + color_random_1[kwargs.keys().index(i)] + str(kwargs.get(i)) + arrow
                formatlist += termcolor.colored((i + ": "), 'white', 'on_blue') + color_random_1[kwargs.keys().index(i)] + str(kwargs.get(i)) + arrow
        else:
            formatlist += random.choice(color_random_1) + " start... " + arrow
        formatlist = formatlist[:-4]
        
        if classname:
            classname = termcolor.colored(classname + arrow, 'white', 'on_red')
        else:
            for name, datax in inspect.getmembers(self, inspect.isclass):
                #print "name  :", name
                #print "datax :", repr(datax)
                if name == '__class__':
                    if '__main__' in repr(datax):
                        classname = repr(datax).split('__main__.', 1)[1][:-2]
                        classname = termcolor.colored(classname + arrow, 'white', 'on_red')

        if defname:
            formatlist = classname + termcolor.colored(defname + arrow, 'white', 'on_red') + formatlist
        else:
            defname = inspect.stack()[1][3] + "[" + str(inspect.stack()[1][2]) + "]"
            formatlist = classname + termcolor.colored(defname + arrow, 'white', 'on_red') + formatlist
        if debug:
            print formatlist
        return formatlist

#def debug(defname = None, debug = None, **kwargs):
    #c = debugger(defname, debug)
    #c.printlist(defname, debug, **kwargs)
c = debugger()
debug = c.printlist