from __future__ import print_function
import os
import sys
import time

def getStatus(interface=None, verbose=False):
    # print "XXX"
    if verbose:
        a = os.system("netsh wlan show interface {0}".format(str(interface)))
    else:
        a = os.system('netsh wlan show interface | grep -iE "state|name|ssid"'.format(str(interface)))
    # print 'aaa'
    if a == 1:
        # print "bbb"
        if verbose:
            a = os.system("netsh interface ip show interface {0}".format(str(interface)))
        else:
            a = os.system('netsh wlan show interface {0} | grep -iE "state|name|ssid"'.format(str(interface)))

def setLife(life, dev):
    if life == 'up':
        os.system('netsh interface set interface %s enable' %(dev))
    elif life == 'down':
        os.system('netsh interface set interface %s disabled' %(dev))
    elif life == 'restart':
        os.system('netsh interface set interface %s disabled' %(dev))
        time.sleep(1)
        os.system('netsh interface set interface %s enable' %(dev))
    else:
        print ("No Valid Input")

def setip(ip=None, mask=None, gateway=None, dns=None, dev=None, index_dns=2):
    # print "DNS =", dns
    #print "type(dns) 1 =", type(dns)
    # try:
    #     if ip.lower() == 'none' or ip == '' or ip == '#':
    #         ip = ''
    # except AttributeError:
    #     ip = ''
    # try:
    #     if mask.lower() == 'none' or mask == '' or mask == '#':
    #         mask = ''
    # except AttributeError:
    #     mask = ''
    # try:
    #     if gateway.lower() == 'none' or gateway == '' or gateway == '#':
    #         gateway = ''
    # except AttributeError:
    #     gateway = ''
    # try:
    #     if dns.lower() == 'none' or dns == '' or dns == '#':
    #         dns = ''
    # except AttributeError:
    #     dns = ''
    if ip == None:
        ip = ''
    if mask == None:
        mask = ''
    if gateway == None:
        gateway = ''
    if dns == None:
        dns = ''
    if dev == None:
        dev = ''
    if dev != '':
        if ip == ''and mask == '' and gateway == '' and dns == []:
            # if dns == []:
            #print "XXX"
            os.system("netsh interface ip show config {0}".format(dev))
        else:
            # print "YYY"
            if ip:
                # print "PLEASE INSERT IP ADDRESS !"
                # return 0
                if mask:
                    if gateway:
                        os.system("netsh interface ip set address {0} static {1} {2} {3}".format(
                    dev, ip, mask, gateway))        
                    # else:
                        #print "PLEASE INSERT GATEWAY !"
                        # return 0    
                # else:
                    #print "PLEASE INSERT NETMASK !"
                    # return 0
            # else:
            #     os.system("netsh interface ip set address {0} static {1} {2} {3}".format(
            #         dev, ip, mask, gateway))
            if dns:
                # print "ZZZ"
                #print "type(dns) =", type(dns)
                if isinstance(dns, list):
                    if len(dns) == 1:
                        #print "SSS 1"
                        os.system(
                            "netsh interface ip set dnsservers {0} static {1} primary".format(dev, dns[0]))
                    elif len(dns) == 1 and index_dns:
                        #print "SSS 2"
                        os.system(
                            "netsh interface ip add dnsservers {0} {1} index=".format(dev, str(index_dns)))
                    elif len(dns) > 1:
                        #print "SSS 3"
                        if dns[0] != '#':
                            #print "SSS 4"
                            os.system(
                                "netsh interface ip set dnsservers {0} static {1} primary".format(dev, dns[0]))
                        a = 2
                        # #print "index =", a
                        for i in dns[1:]:
                            # #print "i     =", i
                            # #print "dev   =", dev
                            if i != 'none' or i != '' or i != '#':
                                os.system(
                                    "netsh interface ip add dnsservers {0} {1} index={2}".format(dev, i, a))
                                a += 1
                else:
                    #print "WWW"
                    if dns != '':
                        #print "WWW 1"
                        os.system(
                            "netsh interface ip set dnsservers {0} static {1} primary".format(dev, dns))
                    else:
                        os.system("netsh interface ip show config {0}".format(dev))
            else:
                #print "HHH"
                os.system("netsh interface ip show config {0}".format(dev))
    else:
        # #print "PLEASE INSERT DEV NAME !"
        #print "\n"
        os.system("netsh interface ip show config")


def deldns(DNSIP, dev, all=None):
    if isinstance(DNSIP, list):
        for i in DNSIP:
            os.system(
                'netsh interface ip del dnsservers {0} {1}'.format(dev, i))
    else:
        os.system(
            'netsh interface ip del dnsservers {0} {1}'.format(dev, DNSIP))
    if all:
        os.system(
            'netsh interface ip del dnsservers {0} {1}'.format(dev, "all"))

def getInterfaceList():
    strData = os.popen('netsh interface ip show interfaces').readlines()
    # print "strData =", strData
    interface_list = []
    # #print "strData =", strData
    for i in strData:
        a = i.split("\n")
        b = a[0].split("  ")
        if b[-1] == 'Name' or b[-1] =='' or b[-1] ==' ' or b[-1] ==None or '---' in b[-1]:
            pass
        else:
            # #print "b =", b[-1].strip()
            interface_list.append(b[-1].strip().lower())
    return interface_list

def usage():

    import argparse
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter)
    # parser.add_argument('-f', '--dev', help='DEVICE NAME',
    #                     action='store', default='')
    parser.add_argument('-I', '--ip', help='IP ADDRESS',
                        action='store', default='')
    parser.add_argument('-m', '--netmask',
                        help='NETMASK ADDRESS', action='store', default='')
    parser.add_argument('-g', '--gateway', help='DNS ADDRESS',
                        action='store', default='')
    parser.add_argument('-d', '--dns', help='DNS ADDRESS',
                        action='store', nargs='*')
    parser.add_argument('-i', '--interface', help='Interface/DEVICE NAME', action='store')
    parser.add_argument('-x', '--index', help='Index DNS Server', action='store', type=int)
    parser.add_argument('-s', '--status', help = 'Get Status info Interface', action = 'store_true')
    parser.add_argument('-v', '--verbosity', help = 'Show more result', action = 'store_true')
    list_public_args = ['-I', '-m', '-g', '-d', '-i', '-x']
    
    # sub = parser.add_subparsers(
    #     title='DEV', help='DEVICE NAME FOR DIRECT SETUP', dest='DEV')

    # # args = parser.parse_args()
    # # #print "args =", args

    def main_usage(no_dev=False):
        if not no_dev:
            parser.add_argument('DEV', help='Interface/Device Name', action='store')
            args = parser.parse_args()
            setip(args.ip, args.netmask, args.gateway, args.dns, args.DEV)
        args = parser.parse_args()
        if args.status:
            getStatus(None, args.verbosity)
        #print "args main_usage:", args
        

    if len(sys.argv) == 1:
        # setip()
        parser.print_help()
        setip()
    else:
        # print "WWW"
        # print "len(sys.argv) =",len(sys.argv)
        LIFE = None
        list_interface = getInterfaceList()
        if sys.argv[1].lower() in list_interface:
            check_argv = False
            if len(sys.argv) == 3:
                #print "AAA"
                if args[2] == 'up' or args[2] == 'down' or args[2] == 'restart':
                    # setLife(args[2], args[1])
                    LIFE = args[2]
                
                for i in sys.argv:
                    if i in list_public_args:
                        check_argv = True
                if not check_argv:
                    parser.add_argument('DEV', help='Interface/Device Name', action='store')
                    if LIFE:
                        parser.add_argument('LIFE', help='Set Up/Down/Restart', action='store', default='None')    
                    parser.add_argument('IP', help='IP ADDRESS', action='store')
                    args = parser.parse_args()
                    setLife(args.LIFE, args.DEV)
                    if not args.LIFE == 'down':
                        setip(args.IP, dev=args.DEV)
                else:
                    main_usage()

            elif len(sys.argv) == 4:
                if args[2] == 'up' or args[2] == 'down' or args[2] == 'restart':
                    LIFE = args[2]
                
                for i in sys.argv:
                    if i in list_public_args:
                        check_argv = True
                if not check_argv:
                    parser.add_argument('DEV', help='Interface/Device Name', action='store')
                    if LIFE:
                        parser.add_argument('LIFE', help='Set Up/Down/Restart', action='store', default='None')    
                    parser.add_argument('IP', help='IP ADDRESS', action='store', default='None')
                    parser.add_argument('NETMASK', help='NETMASK ADDRESS', action='store', default='None')
                    args = parser.parse_args()
                    setLife(args.LIFE, args.DEV)
                    if not args.LIFE == 'down':
                        setip(args.IP, args.NETMASK, dev=args.DEV)
                else:
                    main_usage()
            elif len(sys.argv) == 5:
                # print "CCC"
                if args[2] == 'up' or args[2] == 'down' or args[2] == 'restart':
                    LIFE = args[2]
                for i in sys.argv:
                    if i in list_public_args:
                        check_argv = True
                if not check_argv:
                    parser.add_argument('DEV', help='Interface/Device Name', action='store')
                    if LIFE:
                        parser.add_argument('LIFE', help='Set Up/Down/Restart', action='store', default='None')    
                    parser.add_argument('IP', help='IP ADDRESS', action='store', default='None')
                    parser.add_argument('NETMASK', help='NETMASK ADDRESS', action='store', default='None')
                    parser.add_argument('GATEWAY', help='GATEWAY', action='store', default='None')
                    # if args.status:
                    #     getStatus(args.DEV)                    
                    args = parser.parse_args()
                    setLife(args.LIFE, args.DEV)
                    setip(args.IP, args.NETMASK, args.GATEWAY, dev=args.DEV)
                else:
                    main_usage()
            elif len(sys.argv) > 5:
                # print "DDD"
                if args[2] == 'up' or args[2] == 'down' or args[2] == 'restart':
                    LIFE = args[2]
                for i in sys.argv:
                    if i in list_public_args:
                        check_argv = True
                if not check_argv:
                    parser.add_argument('DEV', help='Interface/Device Name', action='store')
                    parser.add_argument('IP', help='IP ADDRESS', action='store', default='None')
                    parser.add_argument('NETMASK', help='NETMASK ADDRESS', action='store', default='None')
                    parser.add_argument('GATEWAY', help='GATEWAY ADDRESS', action='store', default='None')
                    parser.add_argument('DNS', help='DNS ADDRESS', action='store', nargs='*', default='None')
                    args = parser.parse_args()
                    # print "args =", args
                    # if args.status:
                    #     getStatus(args.DEV)   
                    setLife(args.LIFE, args.DEV)                 
                    setip(args.IP, args.NETMASK, args.GATEWAY, args.DNS, args.DEV)
                else:
                    main_usage()
                # if args.dns:
                #     setip(args.IP, args.NETMASK, args.GATEWAY, args.dns, args.DEV)
                # else: 
                #     setip(args.IP, args.NETMASK, args.GATEWAY, args.DNS, args.DEV)
            else:
                #print "FFF"
                main_usage()
                # parser.add_argument('DEV', help='Interface/Device Name', action='store')
                # args = parser.parse_args()
                # setip(args.ip, args.netmask, args.gateway, args.dns, args.DEV)
        else:
            args = parser.parse_args()
            if len(sys.argv) == 2:
                # print "ZZZ"
                main_usage(True)                
            else:
                # if args.status:
                #     getStatus(args.DEV)            
                setip(args.ip, args.netmask, args.gateway, args.dns, args.interface)


if __name__ == '__main__':
    usage()
    # getInterfaceList()
