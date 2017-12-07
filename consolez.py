#!/usr/bin/python2
# -*- encoding:utf-8 -*-
#encoding:utf8

#!/usr/bin/env python
#coding:utf-8

"""
  Author:  LICFACE --<licface@yahoo.com>
  Purpose: ConsoleZ Wrapper
  Created: 11/19/2017
"""
import subprocess
import sys
import os

class consolez(object):
    #----------------------------------------------------------------------
    def __init__(self, consolez_path = r'c:\TOOLS\ConsoleZ\Console.exe'):
        """
           consolez Wrapper 
        """
        super(consolez, self)
        self.consolez_path = consolez_path
        
    def run(self, config_xml_path, consolez_path = None):
        if not consolez_path:
            consolez_path = self.consolez_path
        if not consolez_path:
            sys.exit("NOT consolez FOUND !")
        elif not os.path.isfile(consolez_path):
            sys.exit("NOT consolez FOUND !")
        else:
            args = [consolez_path, '-c', config_xml_path, '-w', 'Django [%p]']
            a = subprocess.Popen(args, stdout= subprocess.PIPE, shell= True)
            
    def consolez_django(self):
        return self.run(r'c:\Users\root\AppData\Roaming\Console\console_django.xml')
    
    def consolez_mysql(self):
        return self.run(r'c:\Users\root\AppData\Roaming\Console\console_mysql.xml')
    
    def consolez_music(self):
        return self.run(r'c:\Users\root\AppData\Roaming\Console\console_music.xml')
    
    def usage(self):
        import argparse
        parser = argparse.ArgumentParser(formatter_class= argparse.RawTextHelpFormatter, version= '1.0')
        parser.add_argument('NAME', help = 'Console has set with name and config', action = 'store')
        parser.add_argument('-x', '--config-xml-path', help = 'config xml path', action = 'store')
        parser.add_argument('-c', '--console-path', help = 'Consolez alternative path', action = 'store')
        parser.add_argument('-n', '--name', help = 'Console has set with name and config', action = 'store')
        if len(sys.argv) == 1:
            self.run(r'c:\Users\root\AppData\Roaming\Console\console.xml')
        else:
            args = parser.parse_args()
            if args.config_xml_path:
                self.run(args.config_xml_path, args.console_path)
            if args.name or args.NAME:
                if str(args.name).strip().lower() == 'django' or str(args.NAME).strip().lower() == 'django':
                    self.consolez_django()
                elif str(args.name).strip().lower() == 'mysql' or str(args.NAME).strip().lower() == 'mysql':
                    self.consolez_mysql()
                elif str(args.name).strip().lower() == 'music' or str(args.NAME).strip().lower() == 'music':
                    self.consolez_music()
                    
if __name__ == '__main__':
    c = consolez()
    c.usage()
            
        