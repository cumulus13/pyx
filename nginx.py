import os
import sys
import time


def getlist():
    ps = os.popen('tasklist').readlines()
    ps_list = []
    for i in ps:
        if ".exe" in i:
            a = str(i).split(".exe")
            b = a[0] + ".exe"
            # print b
            # print "-"*96
        # if str(i).endswith('.exe'):
            ps_list.append(b)
    return ps_list


def start():
    print 'SERVICE: nginx START'
    os.system('sc start nginx > e:\\temp\NULL')
    if 'nginx.exe' in getlist():
        print 'SERVICE: nginx RUNNING'


def stop():
    print 'SERVICE: nginx STOP'
    os.system('sc stop nginx > e:\\temp\NULL')
    dlist = getlist()
    while True:
        if 'nginx.exe' in dlist:
            os.system('px -k nginx.exe > e:\\temp\NULL')
            dlist = getlist()
        else:
            print 'SERVICE: nginx STOPPED'
            break


def restart():
    stop()
    time.sleep(3)
    start()


def status():
    if 'nginx.exe' in getlist():
        print "\n"
        print "ACTIVE"
    else:
        print "\n"
        print "NOT ACTIVE"


def print_usage():
    print "\n"
    print "USAGE:", os.path.splitext(os.path.basename(__file__))[0], "[start|stop|restart|status]"


def usage():
    if len(sys.argv) > 1:
        for i in sys.argv:
            if i == 'start':
                # print "PRE START"
                start()
            elif i == 'stop':
                # print "PRE STOP"
                stop()
            elif i == 'restart':
                # print "PRE RE-START"
                restart()
            elif i == 'status':
                status()
            elif i == '-h' or i == '--help':
                print_usage()
            else:
                pass
    else:
        print_usage()

if __name__ == '__main__':
    usage()
