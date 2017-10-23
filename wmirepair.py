import os
import sys
import subprocess
import logging
import sys
import shutil
import datetime
import time
import psutil
import threading
import multiprocessing
#import inspect
#from functools import wraps

class repair:
    def __init__(self, parent=None):
        self.format_log = '%(asctime)-15s %(def)s %(pid)s %(message)s'
        logging.basicConfig(format=self.format_log)
        self.extra = {}
        self.logger = logging.getLogger('WMIRepair')
        self.repository_dir = r"d:\BACKUP_DATA\WMIMGMT"
        self.dll_dir = os.path.join(os.getenv('SystemRoot'), "System32\Wbem")
        self.inf_dir = os.path.join(os.getenv('SystemRoot'), "inf")
        self.cpid = ''
        
    def formatdate(self):
        dt = datetime.datetime.now()
        d2 = dt.strftime('%Y%m%d_%H%M%S')
        return d2
    
    def check_pid(self, pid):
        if os.name == 'posix':
            def pid_exists(pid):
                """Check whether pid exists in the current process table."""
                import errno
                if pid < 0:
                    return False
                try:
                    os.kill(pid, 0)
                except OSError as e:
                    return e.errno == errno.EPERM
                else:
                    return True
        else:
            print "AA"
            def pid_exists(pid):
                import ctypes
                kernel32 = ctypes.windll.kernel32
                SYNCHRONIZE = 0x100000
        
                process = kernel32.OpenProcess(SYNCHRONIZE, 0, pid)
                if process != 0:
                    kernel32.CloseHandle(process)
                    return True
                else:
                    return False
        pid_exists(pid)
        
    def pid_running(self, pid):
        import ctypes
        kernel32 = ctypes.windll.kernel32
        SYNCHRONIZE = 0x100000
    
        process = kernel32.OpenProcess(SYNCHRONIZE, 0, pid)
        if process != 0:
            kernel32.CloseHandle(process)
            return True
        else:
            return False
    
    def getpid(self, pid):
        if psutil.pid_exists(pid):
            return True
        else:
            return False
        
    def controlWmiSvc(self, myname):
        self.extra.update({'def': 'DEF: ' + myname})
        pid = subprocess.Popen(['net', 'STOP', 'Winmgmt', '/yes'],stdout=subprocess.PIPE, stderr=subprocess.PIPE).pid
        self.extra.update({'pid': 'PID: ' + str(pid)})
        self.logger.warning('Stop service: %s', 'Winmgmt + Dependency', extra=self.extra)
        #pid = subprocess.Popen(['net', 'STOP', 'Apache249'],stdout=subprocess.PIPE, stderr=subprocess.PIPE).pid
        #print "pid =", pid
        i = 0
        while i < 20:
            i = i + 1
            if self.getpid(pid) == True:
                sys.stdout.write(".")
                time.sleep(5)
            else:
                break
            return True
        return False
    
    def controlPid(self, myname, pid):
            i = 0
            while i < 20:
                i = i + 1
                if self.getpid(pid) == True:
                    sys.stdout.write(".")
                    time.sleep(5)
                else:
                    break
                return True
            return False    
        

    def MethodA(self):
        myname = sys._getframe().f_code.co_name
        self.extra.update({'def': 'DEF: ' + myname})
        if self.controlWmiSvc(myname):
            src = os.path.join(self.dll_dir, "Repository")
            dst = os.path.join(self.repository_dir, "repository_" + self.formatdate())
            shutil.copytree(src, dst)
            shutil.rmtree(src)
            os.makedirs(src)
            os.chdir(self.dll_dir)
            self.logger.warning('Register File Dll', extra=self.extra)
            os.system("for /f %s in ('dir /b *.dll') do regsvr32 /s %s")
            q = ''
            print "\n"
            while not q == 'y':
                q = raw_input("\t Computer must restart, Do you want to restart now ! (y/n): ")
                if q == 'n':
                    break
                elif q == 'y':
                    self.logger.warning('Restart Computer in %s Second', '1', extra=self.extra)
                    os.system("shutdown -r -t 1 -f")
        
    def MethodB(self):
        myname = sys._getframe().f_code.co_name
        self.extra.update({'def': 'DEF: ' + myname})
        if self.controlWmiSvc(myname):
            self.extra.update({'pid': 'PID: ' + str(os.getpid())})
            if os.path.isfile(os.path.join(self.inf_dir, "wbemoc.inf")):
                d = subprocess.Popen(['rundll32', 'SETUPAPI.DLL,InstallHinfSection', 'DefaultInstall', '132', os.path.join(self.inf_dir, "wbemoc.inf")],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                pid = d.pid
                err, out = d.communicate()
                self.extra.update({'pid': 'PID: ' + str(pid)})
                self.logger.warning('Install File INF: %s', 'wbemoc.inf', extra=self.extra)
                self.logger.info('%s', out, extra=self.extra)
            else:
                pid = os.getpid()
                self.extra.update({'pid': 'PID: ' + str(pid)})
                self.logger.warning('File INF Not FOUND: %s', 'wbemoc.inf', extra=self.extra)
                return False
            pid = subprocess.Popen(['net', 'START', 'Winmgmt', '/yes'],stdout=subprocess.PIPE, stderr=subprocess.PIPE).pid
            self.extra.update({'pid': 'PID: ' + str(pid)})
            self.logger.warning('Start service: %s', 'Winmgmt + Dependency', extra=self.extra)
            q = ''
            print "\n"
            while not q == 'y':
                q = raw_input("\t Computer must restart, Do you want to restart now ! (y/n): ")
                if q == 'n':
                    break
                elif q == 'y':
                    self.logger.warning('Restart Computer in %s Second', '1', extra=self.extra)
                    os.system("shutdown -r -t 1 -f")            
            
    def MethodB1(self):
        data = os.system("wmic /NAMESPACE:\\\\root path \"__namespace.name='wmi'\" delete")
        
    def MethodB(self):
        myname = sys._getframe().f_code.co_name
        self.extra.update({'def': 'DEF: ' + myname})
        if self.controlWmiSvc(myname):
            self.extra.update({'pid': 'PID: ' + str(os.getpid())})
            self.logger.warning('Delete wmi namespace: %s', 'wmi Instance deletion', extra=self.extra)
            #p = subprocess.Popen(["wmic", "/NAMESPACE:" + "\\" + "root path \"__namespace.name='wmi'\" delete"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            #err, out = p.communicate()
            #p = subprocess.Popen(['wmic', "/NAMESPACE:\\root", "path", "\"__namespace.name='wmi'\"", "delete"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            #p = threading.Thread(name="MethodB", target=self.MethodB1)
            #out = multiprocessing.log_to_stderr()
            #p = multiprocessing.Process(name="MethodB", target=self.MethodB1)
            #p.daemon = True
            #p.start()
            #p.join()
            os.system("wmic /NAMESPACE:\\\\root path \"__namespace.name='wmi'\" delete")
            #self.extra.update({'pid': 'PID: ' + str(p.pid)})
            #self.logger.warning('%s', out , extra=self.extra)
            self.extra.update({'pid': 'PID: ' + str(os.getpid())})
            pid = subprocess.Popen(['mofcomp', os.path.join(self.dll_dir, 'wmi.mof')],stdout=subprocess.PIPE, stderr=subprocess.PIPE).pid
            self.extra.update({'pid': 'PID: ' + str(os.getpid())})
            self.logger.warning('Start service: %s', 'Winmgmt + Dependency', extra=self.extra)
            pid = subprocess.Popen(['net', 'STOP', 'Winmgmt', '/yes'],stdout=subprocess.PIPE, stderr=subprocess.PIPE).pid
            self.extra.update({'pid': 'PID: ' + str(pid)})
            self.logger.warning('Start service: %s', 'Winmgmt + Dependency', extra=self.extra)
            q = ''
            print "\n"
            while not q == 'y':
                q = raw_input("\t Computer must restart, Do you want to restart now ! (y/n): ")
                if q == 'n':
                    break
                elif q == 'y':
                    self.logger.warning('Restart Computer in %s Second', '1', extra=self.extra)
                    os.system("shutdown -r -t 1 -f")            
            
    def MethodC(self):
        myname = sys._getframe().f_code.co_name
        self.extra.update({'def': 'DEF: ' + myname})
        if self.controlWmiSvc(myname):
            pid = subprocess.Popen(['regsvr32', os.path.join(self.dll_dir, 'wmidcprv.dll')]).pid
            self.extra.update({'pid': 'PID: ' + str(pid)})
            self.logger.warning('register file dll: %s', 'wmidcprv.dll', extra=self.extra)
            os.chdir(self.dll_dir)
            #pid = subprocess.Popen(['for', '%%i', 'in', '(*.dll)', 'do', 'regsvr32', '-s', '%%i']).pid
            os.system('for %i in (*.dll) do regsvr32 -s %i')
            pid = os.getpid()
            self.extra.update({'pid': 'PID: ' + str(pid)})
            self.logger.warning('register all of file dll in : %s', str(self.dll_dir), extra=self.extra)
            os.chdir(self.dll_dir)
            #pid = subprocess.Popen(['for', '%%i', 'in', '(*.exe)', 'do', '%%i', '/RegServer']).pid
            os.system('for %i in (*.exe) do %i /RegServer')
            self.extra.update({'pid': 'PID: ' + str(pid)})
            self.logger.warning('register all of file exe in : %s', str(self.dll_dir), extra=self.extra)
            pid = subprocess.Popen(['net', 'START', 'Winmgmt', '/yes'],stdout=subprocess.PIPE, stderr=subprocess.PIPE).pid
            self.extra.update({'pid': 'PID: ' + str(pid)})
            self.logger.warning('Start service: %s', 'Winmgmt + Dependency', extra=self.extra)
            q = ''
            print "\n"
            while not q == 'y':
                q = raw_input("\t Computer must restart, Do you want to restart now ! (y/n): ")
                if q == 'n':
                    break
                elif q == 'y':
                    self.logger.warning('Restart Computer in %s Second', '1', extra=self.extra)
                    os.system("shutdown -r -t 1 -f")            
            
    def MethodD(self):
        myname = sys._getframe().f_code.co_name
        self.extra.update({'def': 'DEF: ' + myname})
        if self.controlWmiSvc(myname):
            pid = subprocess.Popen(['mofcomp', os.path.join(self.dll_dir, 'wmi.mof')])
            self.extra.update({'pid': 'PID: ' + str(pid)})
            self.logger.warning('register file mof : %s', 'wmi.mof', extra=self.extra)
            pid = subprocess.Popen(['net', 'START', 'Winmgmt', '/yes'],stdout=subprocess.PIPE, stderr=subprocess.PIPE).pid
            self.extra.update({'pid': 'PID: ' + str(pid)})
            self.logger.warning('Start service: %s', 'Winmgmt + Dependency', extra=self.extra)
            q = ''
            print "\n"
            while not q == 'y':
                q = raw_input("\t Computer must restart, Do you want to restart now ! (y/n): ")
                if q == 'n':
                    break
                elif q == 'y':
                    self.logger.warning('Restart Computer in %s Second', '1', extra=self.extra)
                    os.system("shutdown -r -t 1 -f")            
            
    def MethodE(self):
        myname = sys._getframe().f_code.co_name
        self.extra.update({'def': 'DEF: ' + myname})
        if self.controlWmiSvc(myname):
            pid = subprocess.Popen(['winmgmt', '/salvagerepository', self.dll_dir])
            self.logger.warning('salvage repository winmgmt', extra=self.extra)
            pid = subprocess.Popen(['winmgmt', '/resetrepository', self.dll_dir])
            self.logger.warning('reset repository winmgmt', extra=self.extra)
            pid = subprocess.Popen(['net', 'START', 'Winmgmt', '/yes'],stdout=subprocess.PIPE, stderr=subprocess.PIPE).pid
            self.extra.update({'pid': 'PID: ' + str(pid)})
            self.logger.warning('Start service: %s', 'Winmgmt + Dependency', extra=self.extra)
            q = ''
            print "\n"
            while not q == 'y':
                q = raw_input("\t Computer must restart, Do you want to restart now ! (y/n): ")
                if q == 'n':
                    break
                elif q == 'y':
                    self.logger.warning('Restart Computer in %s Second', '1', extra=self.extra)
                    os.system("shutdown -r -t 1 -f")            
            
    def Verify(self):
        myname = sys._getframe().f_code.co_name
        self.extra.update({'def': 'DEF: ' + myname})
        if self.controlWmiSvc(myname):
            print "\n"
            data = subprocess.Popen(['winmgmt', '/verifyrepository'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = data.communicate()
            pid = data.pid
            self.extra.update({'pid': 'PID: ' + str(pid)})
            self.logger.warning('Verify WMI: %s', 'winmgmt', extra=self.extra)            
            if "WMI repository is consistent" in out:
                print out
                return True
            else:
                if len(str(err).strip()) > 0:
                    print "ERROR:", err
                return False
            
    def WmiDiag(self):
        myname = sys._getframe().f_code.co_name
        self.extra.update({'def': 'DEF: ' + myname})
        pid = subprocess.Popen(['c:\Apps\wmidiag\WMIDiag.vbs', 'NoEcho'], stdout=subprocess.PIPE, stderr=subprocess.PIPE).pid()
        if self.controlPid(myname, pid):
            return None
            
    def myname_test(self):
        print(inspect.stack()[0][0].f_code.co_name)
        print(inspect.stack()[0][3])
        print(inspect.currentframe().f_code.co_name)
        print(sys._getframe().f_code.co_name)
        
    def usage(self):
        import optparse
        method = {1: 'MethodA', 2: 'MethodB', 3: 'MethodC', 4: 'MethodD', 5: 'MethodE'}
        parser = optparse.OptionParser()
        parser.add_option('-m', '--method', help="Method to use it", action="store", type=int)
        parser.add_option('-l', '--listmethod', help="List method to use it", action="store_true")
        parser.add_option('-f', '--verify', help="Verify wmidiag", action="store_true")
        parser.add_option('-d', '--diag', help="Diagnostic WMI", action="store_true")
        option, argv = parser.parse_args()
        if len(sys.argv) > 1:
            if option.method:
                #locals()['self.'+ method[option.method]()]
                if option.method == 1:
                    self.MethodA()
                elif option.method == 2:
                    self.MethodB()
                elif option.method == 3:
                    self.MethodC()
                elif option.method == 4:
                    self.MethodD()
                elif option.method == 5:
                    self.MethodE()                
            elif option.listmethod:
                print "\n"
                print "      Method: "
                for i in range (1, len(method)):
                    print "\t", str(i) + ".", method[i]
            elif option.verify:
                self.Verify()
            elif option.diag:
                self.WmiDiag()
            else:
                parser.print_help()
        else:
            parser.print_help()
        


if __name__ == "__main__":
    c = repair()
    #c.MethodA()
    c.usage()


"""def tmp_wrap(func):
    @wraps(func)
    def tmp(*args, **kwargs):
        print func.__name__
        return func(*args, **kwargs)
    return tmp

@tmp_wrap
def my_funky_name():
    print "STUB"

my_funky_name()
"""