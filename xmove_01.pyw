import sys
try:
    import winshell
except ImportError:
    print "Print winshell module not found !"
    print "Please install first !"
    sys.exit(0)
import os
import argparse
import inspect
import logging
DEBUG = True
LEN_DEBUG = 23
#from __future__ import print_function
#import fixpath
import colorama
from colorama import Fore, Back, Style


class xmove(object):

    def __init__(self):
        super(xmove, self)
        self.data_bank = []

    def debugger(self, data, defname):
        colorama.init()
        # if format_logging == None:
        #format_logging = logging.Formatter("def:%(funcName)s --> %(var)s %(space1)s = %(value)s")
        #logger = logging.getLogger('DEBUGGER')
        #logg = logging.StreamHandler()
        # logg.setFormatter(format_logging)
        # logger.addHandler(logg)
        for i in data:
            if DEBUG:
                # dlist = {}
                d = {'defname': defname, i: data.get(i)}
                # print Fore.WHITE + "self.data_bank =", self.data_bank
                # print "len(self.data_bank) =", len(self.data_bank)
                if len(self.data_bank) > 0:
                    # print "self.data_bank    =", self.data_bank
                    for a in self.data_bank:
                        for x in a:
                            if x in d.keys() and x != 'defname':
                                if d.get(x) == a.get(x):
                                    # print "d.get(x) == a.get(x) =", d.get(x) == a.get(x)
                                    # print "def:{0}{1} --> {2} {3} =
                                    # {4}".format(defname, (10 - len(defname))
                                    # * ' ', Fore.YELLOW + str(i), (LEN_DEBUG -
                                    # len(i)) * ' ', Fore.MAGENTA +
                                    # str(data.get(i)))
                                    print (Fore.GREEN + "def:{0}{1} " + Fore.GREEN + "--> " + "{2} {3} " + Fore.GREEN + "= " + "{4}").format(
                                        Fore.CYAN + defname, (10 - len(defname)) * ' ', Fore.YELLOW + str(i), (LEN_DEBUG - len(i)) * ' ', Fore.MAGENTA + str(data.get(i)))
                                    # self.data_bank.append(d)
                                else:
                                    # print "NOT d.get(x) == a.get(x) =", d.get(x) == a.get(x)
                                    # print "def:{0}{1} --> {2} {3} =
                                    # {4}".format(defname, (10 - len(defname))
                                    # * ' ', Fore.YELLOW + str(i), (LEN_DEBUG -
                                    # len(i)) * ' ', Back.RED +
                                    # str(data.get(i)))
                                    print (Fore.GREEN + "def:{0}{1} " + Fore.GREEN + "--> " + "{2} {3} " + Fore.GREEN + "= " + "{4}").format(
                                        Fore.CYAN + defname, (10 - len(defname)) * ' ', Fore.YELLOW + str(i), (LEN_DEBUG - len(i)) * ' ', Back.RED + str(data.get(i)))
                                    # self.data_bank.remove(a)
                                    self.data_bank.append(d)
                            else:
                                print (Fore.GREEN + "def:{0}{1} " + Fore.GREEN + "--> " + "{2} {3} " + Fore.GREEN + "= " + "{4}").format(
                                    Fore.CYAN + defname, (10 - len(defname)) * ' ', Fore.YELLOW + str(i), (LEN_DEBUG - len(i)) * ' ', Fore.MAGENTA + str(data.get(i)))
                else:
                    # print "len(self.data_bank) < 0"
                    print (Fore.GREEN + "def:{0}{1} " + Fore.GREEN + "--> " + "{2} {3} " + Fore.GREEN + "= " + "{4}").format(
                        Fore.CYAN + defname, (10 - len(defname)) * ' ', Fore.YELLOW + str(i), (LEN_DEBUG - len(i)) * ' ', Fore.MAGENTA + str(data.get(i)))
                    # print Fore.GREEN + "def:%s%s"%(defname, (10 -
                    # len(defname)) * ' ') + Fore.YELLOW + " --> %s" % (str(i))
                    # + " %s" % ((LEN_DEBUG - len(i)) * ' ') + Fore.MAGENTA + "
                    # = %s" % (str(data.get(i)))
                    self.data_bank.append(d)
        print Fore.GREEN + "self.data_bank 2 =", self.data_bank
        print Fore.GREEN + "-" * 220
        # print "def:{0}{1} --> {2} {3} = {4}".format(defname, (10 - len(defname)) * ' ', i, (LEN_DEBUG - len(i)) * ' ', data.get(i))
        # dlist.update()
        # data_bank.append(dlist)

        #space1 = (LEN_DEBUG - len(i)) * ' '
        #myextra = {'var': i, 'space1': space1, 'value': data.get(i),}
        # logg.setLevel(logging.ERROR)
        #logger.error(None, extra=myextra)

    def move(self, src, dst, undo=True, quite=False, auto_rename=True, recursive=None, debug=None, **kwargs):
        #format_logging = logging.Formatter("def:%(funcName)s --> %(var)s %(space1)s = %(value)s")
        #argInfo = inspect.getargvalues(inspect.currentframe()).locals
        if debug:
            self.debugger(locals(), sys._getframe().f_code.co_name)

        if "*" in src:
            return self.start_move(src, dst, undo, quite, auto_rename, recursive, **kwargs)
        else:
            # if not debug:
            return winshell.move_file(src, dst, undo, quite, auto_rename, False, **kwargs)

    def multi_move(self, src, dst, undo=True, quite=False, auto_rename=True, recursive=None, debug=None, **kwargs):
        #argInfo = inspect.getargvalues(inspect.currentframe()).locals
        if debug:
            self.debugger(locals(), sys._getframe().f_code.co_name)

        if isinstance(src, list):
            for i in src:
                if "*" in i:
                    print "start move"
                    self.start_move(src, dst, undo, quite,
                                    auto_rename, recursive, debug, **kwargs)
                else:
                    self.move(i, dst, undo, quite, auto_rename,
                              recursive, debug, **kwargs)

    def start_move(self, src, dst, undo=True, quite=False, auto_rename=True, recursive=None, debug=None, **kwargs):
        #argInfo = inspect.getargvalues(inspect.currentframe()).locals
        # print "src =", src
        # print "len(src) =", len(src)
        if debug:
            self.debugger(locals(), sys._getframe().f_code.co_name)

        list_dir = []
        ends = ''
        if "*" in src:
            if os.path.dirname(src) != '':
                dirname = os.path.dirname(src)
            else:
                dirname = os.getcwd()
            # print "dirname =", dirname
            index_start = src.index('*')
            # print "index_start =", index_start

            #example data*
            #if like: data*year, it like this
            #this limited for 1 start mark at begin, middle, & end of
            if len(src) != index_start + 1:
                ends = src[(index_start + 1):]
            if recursive:
                list_dir = []
                for root, dirs, files in os.walk(dirname):
                    if len(files) > 0:
                        for i in files:
                            list_dir.append(os.path.join(root, i))
            else:
                # print "not recursive"
                list_dir = []
                list_dir0 = os.listdir(dirname)
                # print "list_dir0 =", list_dir0
                for i in list_dir0:
                    list_dir.append(os.path.join(os.path.abspath(dirname), i))
            if os.path.abspath(dst) in list_dir:
                del(list_dir[list_dir.index(os.path.abspath(dst))])
            # print "ends =", ends
            for i in list_dir:
                if ends != '':
                    # print "ends != '' 1"
                    if str(i).endswith(ends):
                        # print "ends !       = '' 1"
                        # print "i           1 =", i
                        # print "dst         1 =", dst
                        # print "undo        1 =", undo
                        # print "quite       1 =", quite
                        # print "auto_rename 1 =", auto_rename
                        # print "recursive   1 =", recursive
                        # print "debug       1 =", debug
                        # print "**kwargs    1 =", kwargs
                        self.move(i, dst, undo, quite, auto_rename,
                                  recursive, debug, **kwargs)
                        # print "="*220
                else:
                    # print "ends == ''"
                    # print "i           2 =", i
                    # print "dst         2 =", dst
                    # print "undo        2 =", undo
                    # print "quite       2 =", quite
                    # print "auto_rename 2 =", auto_rename
                    # print "recursive   2 =", recursive
                    # print "debug       2 =", debug
                    # print "**kwargs    2 =", kwargs
                    self.move(i, dst, undo, quite, auto_rename,
                              recursive, debug, **kwargs)
                    # print "-"*220

    def run(self, src, dst, undo=True, quite=False, auto_rename=True, recursive=None, debug=None, **kwargs):
        #argInfo = inspect.getargvalues(inspect.currentframe()).locals
        if debug:
            self.debugger(locals(), sys._getframe().f_code.co_name)

        if len(src) == 1:
            self.move(src[0], dst, undo, quite, auto_rename,
                      recursive, debug, **kwargs)
        elif len(src) > 1:
            self.multi_move(src, dst, undo, quite,
                            auto_rename, recursive, debug, **kwargs)

    def help(self, strtext=None):
        import ttk
        import Tkinter

        root = Tkinter.Tk()
        root.title('Usage Help')
        ttk.Style().configure("Help", padding=6, relief="flat",
                              background="#ccc")
        if strtext == None:
            strtext = """
    Usage:  [options]

    Options:
      -h, --help                        Show this help message and exit
      -d DEST, --dest=DEST  Option Destination copy (dir), default is end of non options
      -r, --recursive                 Copy recursive, use with -i
      -u, --undo                      Whether to enable Explorer to reverse this operation
      -q, --quite                       Whether to overwrite a file without asking
      -a, --auto                        Whether to generate an automatically-renamed
                                               Alternative when the target_path already exists
        """
        # btn = ttk.Button(text="Sample")
        label = ttk.Label(text=strtext)
        label.pack()
        # btn.pack()

        root.mainloop()

    def help2(self, strtext=None):
        import win32ui
        if strtext == None:
            strtext = """
    Usage:  [options]

    Options:
      -h, --help                        Show this help message and exit
      -d DEST, --dest=DEST  Option Destination copy (dir), default is end of non options
      -r, --recursive                 Copy recursive, use with -i
      -u, --undo                      Whether to enable Explorer to reverse this operation
      -q, --quite                       Whether to overwrite a file without asking
      -a, --auto                        Whether to generate an automatically-renamed
                                               Alternative when the target_path already exists
        """
        win32ui.MessageBox(strtext, 'Help Usage', 0)

    def help3(self, strtext=None):
        from PyQt4 import QtGui, QtCore

        class Dialog(QtGui.QDialog):

            def __init__(self, data, parent=None):
                QtGui.QWidget.__init__(self, parent)
                #self.info = info
                self.data = data

                self.setGeometry(300, 300, 550, 350)
                self.setFixedSize(600, 245)
                self.setWindowTitle("Help Usage")
                self.setWindowIcon(QtGui.QIcon('Help.png'))

                self.btOK = QtGui.QPushButton('Close', self)
                self.btOK.setFocusPolicy(QtCore.Qt.NoFocus)

                self.btOK.move(280, 210)
                self.connect(self.btOK, QtCore.SIGNAL(
                    'clicked()'), QtCore.SLOT('close()'))
                self.setFocus()

                self.img_label = QtGui.QLabel(self)
                self.img_label.setMinimumSize(50, 50)
                self.img_label.setGeometry(5, 5, 50, 50)
                self.img_info = QtGui.QImage('Help.png')
                self.img_label.setPixmap(
                    QtGui.QPixmap.fromImage(self.img_info))

                self.label = QtGui.QTextEdit(self)
                self.label.setGeometry(70, 10, 520, 190)
                self.label.setFont(QtGui.QFont('Consolas', 8, 500))
                self.label.setText(self.data)
                self.label.setBackgroundRole(QtGui.QPalette.Dark)
                self.label.setAutoFillBackground(True)
                self.label.setReadOnly(True)
                # self.label.setHtml(text)

                self.setModal(True)

                self.center()

            def center(self):
                screen = QtGui.QDesktopWidget().screenGeometry()
                size = self.geometry()
                self.move((screen.width() - size.width()) / 2,
                          (screen.height() - size.height()) / 2)
        if strtext == None:
            strtext = """
Usage:  [options]

Options:
  -h, --help            Show this help message and exit
  -d DEST, --dest=DEST  Option Destination copy (dir), default is end of non options
  -r, --recursive       Copy recursive, use with -i
  -u, --undo            Whether to enable Explorer to reverse this operation
  -q, --quite           Whether to overwrite a file without asking
  -a, --auto            Whether to generate an automatically-renamed
                        Alternative when the target_path already exists"""

        app = QtGui.QApplication(sys.argv)
        icon = Dialog(strtext)
        icon.show()
        app.exec_()

    def usage(self):
        print "\n"
        usage = "FILES DESTINATION [-h] [-d [DEST [DEST ...]]] [-r] [-u] [-q] [-a]"
        parser = argparse.ArgumentParser(
            formatter_class=argparse.RawDescriptionHelpFormatter, usage=usage)
        parser.add_argument(
            'PATH', help='File/Dir and one less of destination', action='store', nargs='*')
        parser.add_argument(
            '-d', '--dest', help='Option Destination move (dir), default is end of non options', action='store', nargs='*')
        # parser.add_argument('-i', '--inside',
        # help='Move inside of path dir', action='store_true')
        parser.add_argument(
            '-r', '--recursive', help='Move recursive, use with -i', action='store_true')
        parser.add_argument(
            '-u', '--undo', help='whether to enable Explorer to reverse this operation', action='store_true', default=True)
        parser.add_argument('-q', '--quite', help='whether to overwrite a file without asking',
                            action='store_true', default=False)
        parser.add_argument(
            '-a', '--auto', help='whether to generate an automatically-renamed alternative when the target_path already exists', action='store_true', default=True)
        parser.add_argument(
            '-D', '--debug', help='Debug process', action='store_true')
        options = parser.parse_args()

        if len(sys.argv) == 1:
            if os.path.splitext(__file__)[1].lower() == ".pyw":
                try:
                    self.help3()
                except:
                    try:
                        self.help2()
                    except:
                        self.help()
            else:
                parser.print_help()
        else:
            if len(options.PATH) > 0:
                if options.dest:
                    for i in options.dest:
                        self.run(options.PATH, i, options.undo,
                                 options.quite, options.auto, options.recursive, options.debug)
                else:
                    if len(options.PATH) == 1:
                        self.run(options.PATH, os.getcwd(), options.undo,
                                 options.quite, options.auto, options.recursive, options.debug)
                    elif len(options.PATH) > 1:
                        self.run(options.PATH[0:-1], options.PATH[-1], options.undo,
                                 options.quite, options.auto, options.recursive, options.debug)
                    else:
                        print "Please definition your path dir destination ('-d') or add less one of non options as path dest dir"
                        parser.print_help()
            else:
                parser.print_help()

if __name__ == '__main__':
    c = xmove()
    c.usage()
