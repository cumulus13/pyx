#!c:/Python27/Python.exe
#-*- encoding: UTF-8 -*-
#encoding: UTF-8

import make_colors
import os
import sys
import argparse
import subprocess
import re

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
            add_out = ['netsh', 'advfirewall', 'firewall', 'add', 'rule', 'name=', '"%s_out"' % name, 'dir=', 'out', 'action=', '%s' % action, 'program=', '"%s"' % program]
            if kwargs.get('protocol'):
                add_in = ['netsh', 'advfirewall', 'firewall', 'add', 'rule', 'name=', '"%s_in"' % name, 'dir=', 'in', 'action=', '%s' % action, 'program=', '"%s"'% program, 'protocol=', kwargs.get('protocol')]
                add_out = ['netsh', 'advfirewall', 'firewall', 'add', 'rule', 'name=', '"%s_out"' % name, 'dir=', 'out', 'action=', '%s' % action, 'program=', '"%s"'% program, 'protocol=', kwargs.get('protocol')]
        else:
            if table == 'in':
                add_in = ['netsh', 'advfirewall', 'firewall', 'add', 'rule', 'name=', '"%s_in"' % name, 'dir=', 'in', 'action=', '%s' % action, 'program=', '"%s"' % program]
                add_out = ['netsh', 'advfirewall', 'firewall', 'add', 'rule', 'name=', '"%s_out"' % name, 'dir=', 'out', 'action=', 'block' % action, 'program=', '"%s"' % program]
                if kwargs.get('protocol'):
                    add_in = ['netsh', 'advfirewall', 'firewall', 'add', 'rule', 'name=', '"%s_in"' % name, 'dir=', 'in', 'action=', '%s' % action, 'program=', '"%s"'% program, 'protocol=', kwargs.get('protocol')]
                    add_out = ['netsh', 'advfirewall', 'firewall', 'add', 'rule', 'name=', '"%s_out"' % name, 'dir=', 'out', 'action=', 'block' % action, 'program=', '"%s"'% program, 'protocol=', kwargs.get('protocol')]
            elif table == 'out':
                add_in = ['netsh', 'advfirewall', 'firewall', 'add', 'rule', 'name=', '"%s_in"' % name, 'dir=', 'in', 'action=', 'block' % action, 'program=', '"%s"' % program]
                add_out = ['netsh', 'advfirewall', 'firewall', 'add', 'rule', 'name=', '"%s_out"' % name, 'dir=', 'out', 'action=', '%s' % action, 'program=', '"%s"' % program]
                if kwargs.get('protocol'):
                    add_in = ['netsh', 'advfirewall', 'firewall', 'add', 'rule', 'name=', '"%s_in"' % name, 'dir=', 'in', 'action=', 'block' % action, 'program=', '"%s"'% program, 'protocol=', kwargs.get('protocol')]
                    add_out = ['netsh', 'advfirewall', 'firewall', 'add', 'rule', 'name=', '"%s_out"' % name, 'dir=', 'out', 'action=', '%s' % action, 'program=', '"%s"' % program, 'protocol=', kwargs.get('protocol')]
                    
        run_add_in = subprocess.Popen(add_in, stdout= subprocess.PIPE, shell= True)
        (out, err) = run_add_in.communicate()
        if err:
            print "ERROR: ADD INBOUND", err
        run_add_out = subprocess.Popen(add_out, stdout= subprocess.PIPE, shell= True)
        (out, err) = run_add_out.communicate()
        if err:
            print "ERROR: ADD OUTBOUND", err
            
    def add_ip(self, remoteip, protocol, action = 'allow', table = 'both', **kwargs):
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
        #name = os.path.splitext(os.path.basename(program))[0]
        name = str(remoteip)
        if protocol:
            del_in = subprocess.Popen(['netsh', 'advfirewall', 'firewall', 'del', 'rule', 'name=', '"%s_in_%s"' % (name, protocol)])
            del_out = subprocess.Popen(['netsh', 'advfirewall', 'firewall', 'del', 'rule', 'name=', '"%s_out_%s"' % (name, protocol)])            
        else:
            del_in1 = subprocess.Popen(['netsh', 'advfirewall', 'firewall', 'del', 'rule', 'name=', '"%s_in_tcp"' % name])
            del_out1 = subprocess.Popen(['netsh', 'advfirewall', 'firewall', 'del', 'rule', 'name=', '"%s_out_tcp"' % name])
            del_in2 = subprocess.Popen(['netsh', 'advfirewall', 'firewall', 'del', 'rule', 'name=', '"%s_in_udp"' % name])
            del_out2 = subprocess.Popen(['netsh', 'advfirewall', 'firewall', 'del', 'rule', 'name=', '"%s_out_udp"' % name])
        if table == 'both':
            if not protocol:
                add_in1 = ['netsh', 'advfirewall', 'firewall', 'add', 'rule', 'name=', '"%s_in_tcp"' % name, 'dir=', 'in', 'action=', '%s' % action, 'remoteip=', remoteip, 'protocol=', 'tcp']
                add_in2 = ['netsh', 'advfirewall', 'firewall', 'add', 'rule', 'name=', '"%s_in_udp"' % name, 'dir=', 'in', 'action=', '%s' % action, 'remoteip=', remoteip, 'protocol=', 'udp']
                add_out1 = ['netsh', 'advfirewall', 'firewall', 'add', 'rule', 'name=', '"%s_out_tcp"' % name, 'dir=', 'out', 'action=', '%s' % action, 'remoteip=', remoteip, 'protocol=', 'tcp']
                add_out2 = ['netsh', 'advfirewall', 'firewall', 'add', 'rule', 'name=', '"%s_out_udp"' % name, 'dir=', 'out', 'action=', '%s' % action, 'remoteip=', remoteip, 'protocol=', 'udp']
                run_add_in1 = subprocess.Popen(add_in1, stdout= subprocess.PIPE, shell= True)
                (out, err) = run_add_in1.communicate()
                if err:
                    print "ERROR: ADD INBOUND", err
                run_add_out1 = subprocess.Popen(add_out1, stdout= subprocess.PIPE, shell= True)
                (out, err) = run_add_out1.communicate()
                if err:
                    print "ERROR: ADD OUTBOUND", err                
                run_add_in2 = subprocess.Popen(add_in2, stdout= subprocess.PIPE, shell= True)
                (out, err) = run_add_in2.communicate()
                if err:
                    print "ERROR: ADD INBOUND", err
                run_add_out2 = subprocess.Popen(add_out2, stdout= subprocess.PIPE, shell= True)
                (out, err) = run_add_out2.communicate()
                if err:
                    print "ERROR: ADD OUTBOUND", err                
            else:
                add_in = ['netsh', 'advfirewall', 'firewall', 'add', 'rule', 'name=', '"%s_in_%s"' % (name, protocol), 'dir=', 'in', 'action=', '%s' % action, 'remoteip=', '"%s"' % remoteip, 'protocol=', protocol]
                add_out = ['netsh', 'advfirewall', 'firewall', 'add', 'rule', 'name=', '"%s_out_%s"' % (name, protocol), 'dir=', 'out', 'action=', 'block' % action, 'remoteip=', '"%s"' % remoteip, 'protocol=', protocol]
                run_add_in = subprocess.Popen(add_in, stdout= subprocess.PIPE, shell= True)
                (out, err) = run_add_in.communicate()
                if err:
                    print "ERROR: ADD INBOUND", err
                run_add_out = subprocess.Popen(add_out, stdout= subprocess.PIPE, shell= True)
                (out, err) = run_add_out.communicate()
                if err:
                    print "ERROR: ADD OUTBOUND", err                
        else:
            if not protocol:
                if table == 'in':
                    add_in1 = ['netsh', 'advfirewall', 'firewall', 'add', 'rule', 'name=', '"%s_in_tcp"' % name, 'dir=', 'in', 'action=', '%s' % action, 'remoteip=', remoteip, 'protocol=', 'tcp']
                    add_in2 = ['netsh', 'advfirewall', 'firewall', 'add', 'rule', 'name=', '"%s_in_udp"' % name, 'dir=', 'in', 'action=', '%s' % action, 'remoteip=', remoteip, 'protocol=', 'udp']
                    run_add_in1 = subprocess.Popen(add_in1, stdout= subprocess.PIPE, shell= True)
                    (out, err) = run_add_in1.communicate()
                    if err:
                        print "ERROR: ADD INBOUND", err
                    run_add_in2 = subprocess.Popen(add_in2, stdout= subprocess.PIPE, shell= True)
                    (out, err) = run_add_in2.communicate()
                    if err:
                        print "ERROR: ADD OUTBOUND", err                    
                elif table == 'out':
                    add_out1 = ['netsh', 'advfirewall', 'firewall', 'add', 'rule', 'name=', '"%s_out_tcp"' % name, 'dir=', 'out', 'action=', '%s' % action, 'remoteip=', remoteip, 'protocol=', 'tcp']
                    add_out2 = ['netsh', 'advfirewall', 'firewall', 'add', 'rule', 'name=', '"%s_out_udp"' % name, 'dir=', 'out', 'action=', '%s' % action, 'remoteip=', remoteip, 'protocol=', 'udp']
                    run_add_out1 = subprocess.Popen(add_out1, stdout= subprocess.PIPE, shell= True)
                    (out, err) = run_add_out1.communicate()
                    if err:
                        print "ERROR: ADD INBOUND", err
                    run_add_out2 = subprocess.Popen(add_out2, stdout= subprocess.PIPE, shell= True)
                    (out, err) = run_add_out2.communicate()
                    if err:
                        print "ERROR: ADD OUTBOUND", err                    
                
            else:
                if table == 'in':
                    add_in = ['netsh', 'advfirewall', 'firewall', 'add', 'rule', 'name=', '"%s_in"' % name, 'dir=', 'in', 'action=', '%s' % action, 'remoteip=', '"%s"' % remoteip, 'protocol=', protocol]
                    add_out = ['netsh', 'advfirewall', 'firewall', 'add', 'rule', 'name=', '"%s_out"' % name, 'dir=', 'out', 'action=', 'block' % action, 'remoteip=', '"%s"' % remoteip, 'protocol=', protocol]
                elif table == 'out':
                    add_in = ['netsh', 'advfirewall', 'firewall', 'add', 'rule', 'name=', '"%s_in"' % name, 'dir=', 'in', 'action=', 'block' % action, 'remoteip=', remoteip, 'protocol=', protocol]
                    add_out = ['netsh', 'advfirewall', 'firewall', 'add', 'rule', 'name=', '"%s_out"' % name, 'dir=', 'out', 'action=', '%s' % action, 'remoteip=', remoteip, 'protocol=', protocol]
                run_add_in = subprocess.Popen(add_in, stdout= subprocess.PIPE, shell= True)
                (out, err) = run_add_in.communicate()
                if err:
                    print "ERROR: ADD INBOUND", err
                run_add_out = subprocess.Popen(add_out, stdout= subprocess.PIPE, shell= True)
                (out, err) = run_add_out.communicate()
                if err:
                    print "ERROR: ADD OUTBOUND", err                
                    
        #run_add_in = subprocess.Popen(add_in, stdout= subprocess.PIPE, shell= True)
        #(out, err) = run_add_in.communicate()
        #if err:
            #print "ERROR: ADD INBOUND", err
        #run_add_out = subprocess.Popen(add_out, stdout= subprocess.PIPE, shell= True)
        #(out, err) = run_add_out.communicate()
        #if err:
            #print "ERROR: ADD OUTBOUND", err
            
    def usage(self):
        parse = argparse.ArgumentParser(formatter_class= argparse.RawTextHelpFormatter)
        parse.add_argument('RULE', help = 'Program Execute Path or Remote Ip Address', action = 'store')
        parse.add_argument('-a', '--action', help = '"allow"[1] or "block"[0]', action = 'store', type = str, default = 'block')
        parse.add_argument('-t', '--table', help = '"in"[1] or "out"[0]', action = 'store', type = str, default = 'both')
        parse.add_argument('-p', '--protocol', help = 'Protocol "TCP" or "UDP", default="BOTH"', action = 'store')
        if len(sys.argv) == 1:
            parse.print_help()
        else:
            args = parse.parse_args()
            if re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", args.RULE) != []:
                self.add_ip(args.RULE, args.protocol, args.action, args.table)
            else:
                self.add(args.RULE, args.action, args.table, protocol = args.protocol)

if __name__ == '__main__':
    c = firewall()
    c.usage()