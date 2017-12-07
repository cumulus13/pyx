#!c:/Python27/Python.exe
#-*- encoding: UTF-8 -*-
#encoding: UTF-8

import make_colors
import os
import sys
import argparse
import subprocess

class firewall(object):
    def __init__(self, **kwargs):
        super(firewall, self)
        
    def add(self, program, action = 'allow', table = 'both', **kwargs):
        program = os.path.abspath(program)
        if action:
            if action == '1':
                action = 'allow'
            elif action == '0':
                action == 'block'
        if table:
            if table == '1':
                table = 'in'
            elif table == '0':
                table = 'out'
        name = os.path.splitext(os.path.basename(program))[0]
        del_in = subprocess.Popen(['netsh', 'advfirewall', 'firewall', 'del', 'rule', 'name=', '"%s_in"' % name])
        del_out = subprocess.Popen(['netsh', 'advfirewall', 'firewall', 'del', 'rule', 'name=', '"%s_out"' % name])
        if table == 'both':
            add_in = ['netsh', 'advfirewall', 'firewall', 'add', 'rule', 'name=', '"%s_in"' % name, 'dir=', 'in', 'action=', '%s' % action, 'program=', '"%s"' % program]
            add_in = ['netsh', 'advfirewall', 'firewall', 'add', 'rule', 'name=', '"%s_out"' % name, 'dir=', 'out', 'action=', '%s' % action, 'program=', '"%s"' % program]
            if 'protocol' in kwargs:
                add_in = ['netsh', 'advfirewall', 'firewall', 'add', 'rule', 'name=', '"%s_in"' % name, 'dir=', 'in', 'action=', '%s' % action, 'program=', '"%s"', 'protocol=', kwargs.get('protocol')]
                add_in = ['netsh', 'advfirewall', 'firewall', 'add', 'rule', 'name=', '"%s_out"' % name, 'dir=', 'out', 'action=', '%s' % action, 'program=', '"%s"', 'protocol=', kwargs.get('protocol')]
        else:
            if table == 'in':
                add_in = ['netsh', 'advfirewall', 'firewall', 'add', 'rule', 'name=', '"%s_in"' % name, 'dir=', 'in', 'action=', '%s' % action, 'program=', '"%s"' % program]
                add_in = ['netsh', 'advfirewall', 'firewall', 'add', 'rule', 'name=', '"%s_out"' % name, 'dir=', 'out', 'action=', 'block' % action, 'program=', '"%s"' % program]
                if 'protocol' in kwargs:
                    add_in = ['netsh', 'advfirewall', 'firewall', 'add', 'rule', 'name=', '"%s_in"' % name, 'dir=', 'in', 'action=', '%s' % action, 'program=', '"%s"', 'protocol=', kwargs.get('protocol')]
                    add_in = ['netsh', 'advfirewall', 'firewall', 'add', 'rule', 'name=', '"%s_out"' % name, 'dir=', 'out', 'action=', 'block' % action, 'program=', '"%s"', 'protocol=', kwargs.get('protocol')]
            elif table == 'out':
                add_in = ['netsh', 'advfirewall', 'firewall', 'add', 'rule', 'name=', '"%s_in"' % name, 'dir=', 'in', 'action=', 'block' % action, 'program=', '"%s"' % program]
                add_in = ['netsh', 'advfirewall', 'firewall', 'add', 'rule', 'name=', '"%s_out"' % name, 'dir=', 'out', 'action=', '%s' % action, 'program=', '"%s"' % program]
                if 'protocol' in kwargs:
                    add_in = ['netsh', 'advfirewall', 'firewall', 'add', 'rule', 'name=', '"%s_in"' % name, 'dir=', 'in', 'action=', 'block' % action, 'program=', '"%s"', 'protocol=', kwargs.get('protocol')]
                    add_in = ['netsh', 'advfirewall', 'firewall', 'add', 'rule', 'name=', '"%s_out"' % name, 'dir=', 'out', 'action=', '%s' % action, 'program=', '"%s"', 'protocol=', kwargs.get('protocol')]
                    
        run_add_in = subprocess.Popen(add_in, stdout= subprocess.PIPE, shell= True)
        (out, err) = run_add_in.communicate()
        if err:
            print "ERROR: ADD INBOUND", err
        run_add_out = subprocess.Popen(add_out, stdout= subprocess.PIPE, shell= True)
        (out, err) = run_add_in.communicate()
        if err:
            print "ERROR: ADD OUTBOUND", err
            
    def usage(self):
        parse = argparse.ArgumentParser(formatter_class= argparse.RawTextHelpFormatter)
        parse.add_argument('PROGRAM', help = 'Program Execute Path', action = 'store')
        parse.add_argument('-a', '--action', help = '"allow"[1] or "block"[0]', action = 'store', type = str, default = 'allow')
        parse.add_argument('-t', '--table', help = '"in"[1] or "out"[0]', action = 'store', type = str, default = 'both')
        if len(sys.argv) == 1:
            parse.print_help()
        else:
            args = parse.parse_args()
            self.add(args.PROGRAM, args.action, args.table)

if __name__ == '__main__':
    c = firewall()
    c.usage()