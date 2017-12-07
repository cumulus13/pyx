#!c/Anaconda2/python.exe

import os
import sys
import vping
import colorama
import termcolor
import random
import inspect
import codecs
pid = os.getpid()
print "PID =", pid
import dial_polling
import subprocess
import time
import sendgrowl
import PySnarl
import configset

class huaweicontrol(object):
    def __init__(self, DEV, debug = True):
        super(huaweicontrol, self)
        self.debug = debug
        self.DEV = DEV
        configset.set_config_name('huaweicontrol.ini')
        #configset.get_config_file()        
        self.nircmd = r'c:\exe\nircmd.exe'
        if not os.path.isfile(self.nircmd):
            if configset.read_config4('NIRCMD', 'path'):
                self.nircmd = configset.read_config4('NIRCMD', 'path')
            else:
                q = raw_input(termcolor.colored('NO NIRCMCD !, PLEASE RE-DEFINITION [ENTER to EXIT]: ', 'white', 'on_red', attrs= ['blink', 'bold']))
                while 1:
                    #if q == chr(27):
                        #sys.exit(0)
                    if q == 'q':
                        sys.exit(0)
                    elif os.path.isfile(q):
                        self.nircmd = q
                        break
                    else:
                        sys.exit(0)
                #else:
                    #q = raw_input(termcolor.colored('NO NIRCMCD !, PLEASE RE-DEFINITION [ENTER to EXIT]: ', 'white', 'on_red', attrs= ['blink', 'bold']))
            
        self.APP = r'c:\Program Files\HUAWEI Modem 3.5\HUAWEI Modem 3.5.exe'
        print termcolor.colored('DEVICE: ', 'red', 'on_yellow', attrs= ['bold']) + termcolor.colored(str(self.DEV), 'white', 'on_cyan', attrs= ['bold'])
        
    def notify(self, message, event, host = '127.0.0.1', port = 23052, timeout = 15, icon_path = None):
        if not icon_path:
            icon_path = r'f:\ICONS\huawei.png'
        try:
            growl = sendgrowl.growl()
            if isinstance(host, list):
                for i in host:
                    if ":" in i:
                        host, port = str(host).split(":")
                        port = int(port)
                    else:
                        host = i
                    growl.publish('HuaweiControl', event, 'HuaweiControl', message, host, port, timeout, None, icon_path)
            else:
                growl.publish('HuaweiControl', event, 'HuaweiControl', message, host, port, timeout, None, icon_path)
        except:
            pass
        try:
            PySnarl.snShowMessage('HuaweiControl', message, 3, icon_path)
        except:
            pass
        
    def control_app(self, app_path = None, start = True):
        if app_path:
            self.APP = app_path
        if os.path.isfile(self.APP):
            dir_app_name = os.path.dirname(self.APP)
            name_app_name = os.path.basename(self.APP)
            if start:
                a = subprocess.Popen([self.APP])
                time.sleep(60)
                while 1:
                    if not a.poll():
                        print termcolor.colored('APP STARTED ', 'red', 'on_yellow', attrs= ['bold'])
                        break
                    else:
                        a = subprocess.Popen([self.APP])
                        time.sleep(60)
            else:
                a = subprocess.Popen(['c:\exe\nircmd.exe', 'closeprocess', name_app_name])
                time.sleep(60)
                while 1:
                    if not a.poll():
                        a = subprocess.Popen(['c:\exe\nircmd.exe', 'closeprocess', name_app_name])
                        time.sleep(60)
                    else:
                        print termcolor.colored('APP STOPPED ', 'red', 'on_yellow', attrs= ['bold'])
                        break
        else:
            print termcolor.colored('ERROR: ', 'white', 'on_red', attrs= ['bold']) + termcolor.colored("CAN't RUN APP", 'red', 'on_yellow', attrs= ['bold'])
            
    def dial_up(self, dev = None):
        if dev:
            self.DEV = dev
        print termcolor.colored('HungUp: ', 'red', 'on_yellow', attrs= ['bold'])
        self.notify('HungUp', 'hungup', host = ['127.0.0.1', '192.168.1.2'])
        a1 = subprocess.Popen([self.nircmd, 'rashangup', '{0}'.format(self.DEV)])
        time.sleep(3)
        while 1:
            if self.getIp(dev):
                if a1.poll() == 0:
                    a1 = subprocess.Popen([self.nircmd, 'rashangup', '{0}'.format(self.DEV)])
                else:
                    time.sleep(3)
            else:
                break
        
        print termcolor.colored('DialUp: ', 'red', 'on_yellow', attrs= ['bold'])
        self.notify('DialUp', 'dialup', host = ['127.0.0.1', '192.168.1.2'])
        a2 = subprocess.Popen([self.nircmd, 'rasdial', '{0}'.format(self.DEV)])
        time.sleep(3)
        while 1:
            if self.getIp(dev):
                break
            else:
                if a1.poll() == 0:
                    a2 = subprocess.Popen([self.nircmd, 'rasdial', '{0}'.format(self.DEV)])
                else:
                    time.sleep(3)        
        
    def printlist(self, defname=None, debug=None, **kwargs):
        if not debug:
            debug = self.debug
        color_random_1 = [colorama.Fore.GREEN, colorama.Fore.YELLOW, colorama.Fore.LIGHTBLUE_EX, colorama.Fore.LIGHTCYAN_EX, colorama.Fore.LIGHTMAGENTA_EX, colorama.Fore.GREEN, colorama.Fore.YELLOW, colorama.Fore.LIGHTBLUE_EX, colorama.Fore.LIGHTCYAN_EX, colorama.Fore.LIGHTMAGENTA_EX, colorama.Fore.GREEN, colorama.Fore.YELLOW, colorama.Fore.LIGHTBLUE_EX, colorama.Fore.LIGHTCYAN_EX, colorama.Fore.LIGHTMAGENTA_EX,
                          colorama.Fore.GREEN, colorama.Fore.YELLOW, colorama.Fore.LIGHTBLUE_EX, colorama.Fore.LIGHTCYAN_EX, colorama.Fore.LIGHTMAGENTA_EX, colorama.Fore.GREEN, colorama.Fore.YELLOW, colorama.Fore.LIGHTBLUE_EX, colorama.Fore.LIGHTCYAN_EX, colorama.Fore.LIGHTMAGENTA_EX, colorama.Fore.GREEN, colorama.Fore.YELLOW, colorama.Fore.LIGHTBLUE_EX, colorama.Fore.LIGHTCYAN_EX, colorama.Fore.LIGHTMAGENTA_EX]
        colorama.init()
        formatlist = ''
        arrow = colorama.Fore.YELLOW + ' -> '
        if not kwargs == {}:
            for i in kwargs:
                #formatlist += color_random_1[kwargs.keys().index(i)] + i + ": " + color_random_1[kwargs.keys().index(i)] + str(kwargs.get(i)) + arrow
                formatlist += termcolor.colored((i + ": "), 'white', 'on_blue') + color_random_1[
                    kwargs.keys().index(i)] + str(kwargs.get(i)) + arrow
        else:
            formatlist += random.choice(color_random_1) + " start... " + arrow
        formatlist = formatlist[:-4]

        if defname:
            formatlist = termcolor.colored(
                defname + arrow, 'white', 'on_red') + formatlist
        else:
            defname = inspect.stack()[1][3]
            formatlist = termcolor.colored(
                defname + arrow, 'white', 'on_red') + formatlist
        if debug:
            print formatlist
        return formatlist
    
        
    def getIp(self, dev = None):
        if dev:
            self.DEV = dev
        a1 = os.popen('ipconfig').readlines()
        #self.printlist(a1 = a1)
        ips = []
        ipaddress = []
        for i in a1:
            if self.DEV in i:
                #ips.append(a1[a1.index(i)])
                ips.append(a1[a1.index(i) + 3])
                ips.append(a1[a1.index(i) + 5])
        if ips:
            for i in ips:
                a2 = str(i).strip('   IPv4 Address. . . . . . . . . . . :')[:-1]
                #self.printlist(a2 = a2)
                ipaddress.append(a2)
            #self.printlist(ipaddress = ipaddress)
        return ipaddress
    
    def changeIp(self, dev = None):
        if not dev:
            print termcolor.colored('ERROR:', 'white', 'on_red', attrs= ['bold']) + termcolor.colored('NO DEVICE', 'red', 'on_yellow', attrs= ['bold'])
            self.notify('ERROR: NO DEVICE', 'error', host = ['127.0.0.1', '192.168.1.2'])
            return None
        ipaddress = self.getIp(dev)
        if ipaddress:
            print termcolor.colored('CHANGE IP TO: ', 'red', 'on_yellow', attrs= ['bold']) + termcolor.colored(str(ipaddress[0]), 'white', 'on_red', attrs= ['bold'])
            self.notify('Change IP to: %s' % str(ipaddress[0]), 'changeip', host = ['127.0.0.1', '192.168.1.2'])
            os.system('NETSH interface ip set address {0} static {1} 255.255.255.255 {2}'.format(dev, ipaddress[0], ipaddress[0]))
            if vping.vping('8.8.8.8', 5, 10):
                print termcolor.colored('SUCCESS:', 'red', 'on_yellow', attrs= ['bold']) + termcolor.colored('CONNECTED', 'white', 'on_red', attrs= ['bold'])
                self.notify('SUCCESS: CONNECTED', 'changeip', host = ['127.0.0.1', '192.168.1.2'])
                return ipaddress[0]
            else:
                print termcolor.colored('CHANGE IP TO: ', 'red', 'on_yellow', attrs= ['bold']) + termcolor.colored(str(ipaddress[1]), 'white', 'on_red', attrs= ['bold'])
                self.notify('Change IP to: %s' % str(ipaddress[1]), 'changeip', host = ['127.0.0.1', '192.168.1.2'])
                os.system('NETSH interface ip set address {0} static {1} 255.255.255.255 {2}'.format(dev, ipaddress[1], ipaddress[1]))
                if vping.vping('8.8.8.8', 5, 10):
                    print termcolor.colored('SUCCESS:', 'red', 'on_yellow', attrs= ['bold']) + termcolor.colored('CONNECTED', 'white', 'on_red', attrs= ['bold'])
                    self.notify('SUCCESS: CONNECTED', 'changeip', host = ['127.0.0.1', '192.168.1.2'])
                    return ipaddress[0]
                else:
                    print termcolor.colored('ERROR:', 'white', 'on_red', attrs= ['bold']) + termcolor.colored('CAN\'T CONNECTED', 'red', 'on_yellow', attrs= ['bold'])
                    self.notify('ERROR: CAN\'T CONNECTER', 'changeip', host = ['127.0.0.1', '192.168.1.2'])
                    return None
        else:
            termcolor.colored('NO IPADDRESS', 'white', 'on_red', attrs= ['bold'])
            self.notify('NO IPADDRESS', 'changeip', host = ['127.0.0.1', '192.168.1.2'])
            return None
            
    def navigator(self, dev = None):
        self.dial_up()
        while 1:
            if not dev:
                dev = self.DEV
            if not vping.vping('8.8.8.8', 5, 5):
                print termcolor.colored('TRY CHANGE IP', 'red', 'on_yellow', attrs= ['bold'])
                self.notify('Try Change IP', 'navigator', host = ['127.0.0.1', '192.168.1.2'])
                ipaddress = self.changeIp(dev)            
                if ipaddress:
                    print termcolor.colored('YOUR IP: ', 'red', 'on_yellow', attrs= ['bold']) + termcolor.colored(str(ipaddress), 'white', 'on_cyan', attrs= ['bold'])
                    self.notify('Your IP: %s' % str(ipaddress), 'navigator', host = ['127.0.0.1', '192.168.1.2'])
                    sys.exit(0)
                else:
                    self.dial_up()
            else:
                print termcolor.colored('HAS CONNECTED', 'red', 'on_yellow', attrs= ['bold'])
                self.notify('HAS CONNECTED', 'navigator', host = ['127.0.0.1', '192.168.1.2'])
                break
        
if __name__ == '__main__':
    c = huaweicontrol('TSEL-TIMEBASED')
    c.navigator()
    #configset.set_config_name('huaweicontrol.ini')
    #print configset.get_config_file()