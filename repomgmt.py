import os
import sys
import shutil
import argparse
import traceback
import re
import socket
import datetime
import sendgrow

__version__ = "1.0"
__sdk__ = "2.7"
__build__ = "2.7"
__platform__ = "all"
__author__ = "licface"
__email__ = "licface@yahoo.com"
__test__ = "0.1"

FACILITY = {
    'kern': 0, 'user': 1, 'mail': 2, 'daemon': 3,
    'auth': 4, 'syslog': 5, 'lpr': 6, 'news': 7,
    'uucp': 8, 'cron': 9, 'authpriv': 10, 'ftp': 11,
    'local0': 16, 'local1': 17, 'local2': 18, 'local3': 19,
    'local4': 20, 'local5': 21, 'local6': 22, 'local7': 23,
}

LEVEL = {
    'emerg': 0, 'alert':1, 'crit': 2, 'err': 3,
    'warning': 4, 'notice': 5, 'info': 6, 'debug': 7
}

def syslog(message, level=LEVEL['notice'], facility=FACILITY['daemon'],
           host='localhost', port=514):

    """
	Send syslog UDP packet to given host and port.
	"""

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = '<%d>%s' % (level + facility*8, message)
    sock.sendto(data, (host, port))
    sock.close()


class error:
    def __init__(self, data, severity, facility):
        self.data = data
        self.severity = severity
        self.facility = facility

    def error_growl(self, host=None, port=None, passwd=None, appname=None, title=None, event=None, msg=None, icon=None, timeout=None):
        if msg == None:
            msg = self.data
        if host == None:
            host = '127.0.0.1'
        if port == None:
            port = 23053
        if passwd == None:
            passwd = 'blackid'
        if appname == None:
            appname = 'Repository Management'
        if title == None:
            title = 'Repository Management'
        if event == None:
            event = 'Repository Management'
        if icon == None:
            icon = os.path.join(os.path.join(os.path.dirname(__file__), 'icons'), 'repomgmt.png')
        
        c_growl = sendgrow.growl()
        c_growl.publish(appname, event, title, str(msg), host, port, timeout, icon, icon)

    def error_syslog(self, port=514, host='127.0.0.1', data=None, severity=None, facility=None):
        if severity == None:
            severity = self.severity
        if facility == None:
            facility = self.facility
        if data == None:
            data = self.data        
        syslog(str(data), severity, facility, host, port)    

    def error_file(self, data=None):
        if data == None:
            data = self.data        
        logfile(data)
        
    def log_to_all(self, data=None, facility=None, severity=None):
        if severity == None:
            severity = self.severity
        if facility == None:
            facility = self.facility
        if data == None:
            data = self.data          
        self.error_growl(msg=data)
        self.error_syslog(520, data=data)
        self.error_file(data)

def logfile(data, filelog='repomgmt_traceback.log'):
    timex = datetime.datetime.isoformat(datetime.datetime.now())
    try:
        if os.path.isfile(os.path.join(os.path.dirname(__file__), filelog)):
            f = open(os.path.join(os.path.dirname(__file__), filelog), 'a')
            f.write(str(timex) + " - " + str(data) + "\n")
            f.close()
        else:
            f = open(os.path.join(os.path.dirname(__file__), filelog), 'w')
            f.write(str(timex) + " - " + str(data) + "\n")
            f.close()
    except:
        error(str(__file__) + "ERROR: " + str(er),3,1)
        error.log_to_all()

def checkdir(path):
    data = re.split("\\\\", path)
    d = ['hg', 'git', 'svn']
    for i in d:
        if data[2] == i:
            return False
        else:
            return True
        
def check_dstall(path, dtype):
    a = ['hg', 'git', 'svn']
    for i in a:
        if not os.path.isdir(os.path.join(os.path.abspath(path), i)):
            os.mkdir(os.path.join(os.path.abspath(path), i))
    return os.path.join(os.path.abspath(path), dtype)

def analisys(path, dst_hg=None, dst_git=None, dst_svn=None, verbosity=None, logtofile=None, logtofilename=None, logtosyslog=None, logtosysloghost=None, logtosyslogport=None, logtosyslogfacility=None, logtosyslogseverity=None, logtosyslogmsg=None, logtogrowl=None, logtogrowlhost=None, logtogrowlport=None, logtogrowlpass=None, logtogrowlappname=None, logtogrowltitle=None, logtogrowlevent=None, logtogrowlmsg=None, logtogrowlicon=None, logtogrowltimeout=None, logtoall=None, printerror=None, dstall=None):
    if logtosyslogport == None:
        logtosyslogport = 520
    if logtogrowlport == None:
        logtogrowlport = 23053
    try:   
        for root, dirs, files in os.walk(path):
            #print "root =", root
            #print "dirs =", dirs
            if dst_hg == None:
                if os.path.isdir(os.path.join(os.path.abspath(path), 'hg')):
                    pass
                else:
                    os.makedirs(os.path.join(os.path.abspath(path), 'hg'))
                if not dstall == None:
                    dst_hg = check_dstall(dstall, 'hg')
                else:
                    dst_hg = os.path.join(os.path.abspath(path), 'hg')
            if dst_git == None:
                if os.path.isdir(os.path.join(os.path.abspath(path), 'git')):
                    pass
                else:            
                    os.makedirs(os.path.join(os.path.abspath(path), 'git'))
                if not dstall == None:
                    dst_git = check_dstall(dstall, 'git')
                else:
                    dst_git = os.path.join(os.path.abspath(path), 'git')
            if dst_svn == None:
                if os.path.isdir(os.path.join(os.path.abspath(path), 'svn')):
                    pass
                else:            
                    os.makedirs(os.path.join(os.path.abspath(path), 'svn'))
                if not dstall == None:
                    dst_svn = check_dstall(dstall, 'svn')
                else:
                    dst_svn = os.path.join(os.path.abspath(path), 'svn')            
            hg = os.path.join(os.path.abspath(root), '.hg')
            #print "hg =", hg
            git = os.path.join(os.path.abspath(root), '.git')
            #print "git =", git
            svn = os.path.join(os.path.abspath(root), '.svn')
            logs = error('', 6, 0)
            if os.path.isdir(hg):
                if verbosity > 0:
                    msg = "MOVE HG Dir : '%s' --> '%s'" % (str(os.path.abspath(os.path.dirname(hg))), str(dst_hg))
                    if logtosyslogmsg == None:
                        logtosyslogmsg = msg
                    if logtogrowlmsg == None:
                        logtogrowlmsg = msg
                    if logtoall:
                        logs.log_to_all(msg)
                    elif logtofile:
                        if not logtofilename == None:
                            logfile(msg, logtofilename)
                        else:
                            logs.error_file(msg)
                    elif logtosyslog:
                        logs.error_syslog(logtosyslogport, logtosysloghost, msg, logtosyslogseverity, logtosyslogfacility)
                    elif logtogrowl:
                        logs.error_growl(logtogrowlhost, logtogrowlport, logtogrowlpass, logtogrowlappname, logtogrowltitle, logtogrowlevent, logtogrowlmsg, logtogrowlicon, logtogrowlicon)
                    
                    print msg 
                try:
                    if checkdir(hg) == True:
                        shutil.move(os.path.dirname(hg), dst_hg)
                except:
                    if verbosity == 2:
                        import traceback
                        msg = "Error:", traceback.format_exc()
                        if logtosyslogmsg == None:
                            logtosyslogmsg = msg
                        if logtogrowlmsg == None:
                            logtogrowlmsg = msg                        
                        if logtoall:
                            logs.log_to_all(msg)
                        elif logtofile:
                            if not logtofilename == None:
                                logfile(msg, logtofilename)
                            else:
                                logs.error_file(msg)
                        elif logtosyslog:
                            logs.error_syslog(logtosyslogport, logtosysloghost, msg, logtosyslogseverity, logtosyslogfacility)
                        elif logtogrowl:
                            logs.error_growl(logtogrowlhost, logtogrowlport, logtogrowlpass, logtogrowlappname, logtogrowltitle, logtogrowlevent, logtogrowlmsg, logtogrowlicon, logtogrowlicon)
                        if printerror:
                            print msg                                             
                        
            elif os.path.isdir(git):
                #print "git =", git
                if verbosity > 0:
                    msg = "MOVE GIT Dir: '%s' --> '%s'" % (str(os.path.abspath(os.path.dirname(git))), str(dst_git))
                    if logtosyslogmsg == None:
                        logtosyslogmsg = msg
                    if logtogrowlmsg == None:
                        logtogrowlmsg = msg                    
                    if logtoall:
                        logs.log_to_all(msg)
                    elif logtofile:
                        if not logtofilename == None:
                            logfile(msg, logtofilename)
                        else:
                            logs.error_file(msg)
                    elif logtosyslog:
                        logs.error_syslog(logtosyslogport, logtosysloghost, msg, logtosyslogseverity, logtosyslogfacility)
                    elif logtogrowl:
                        logs.error_growl(logtogrowlhost, logtogrowlport, logtogrowlpass, logtogrowlappname, logtogrowltitle, logtogrowlevent, logtogrowlmsg, logtogrowlicon, logtogrowlicon)
                    print msg                     
                try:
                    if checkdir(git) == True:
                        shutil.move(os.path.dirname(git), dst_git)
                except:
                    if verbosity == 2:
                        import traceback
                        msg = "Error:", traceback.format_exc()
                        if logtosyslogmsg == None:
                            logtosyslogmsg = msg
                        if logtogrowlmsg == None:
                            logtogrowlmsg = msg                        
                        if logtoall:
                            logs.log_to_all(msg)
                        elif logtofile:
                            if not logtofilename == None:
                                logfile(msg, logtofilename)
                            else:
                                logs.error_file(msg)
                        elif logtosyslog:
                            logs.error_syslog(logtosyslogport, logtosysloghost, msg, logtosyslogseverity, logtosyslogfacility)
                        elif logtogrowl:
                            logs.error_growl(logtogrowlhost, logtogrowlport, logtogrowlpass, logtogrowlappname, logtogrowltitle, logtogrowlevent, logtogrowlmsg, logtogrowlicon, logtogrowlicon)
                        if printerror:
                            print msg  
            elif os.path.isdir(svn):
                #print "git =", git
                if verbosity > 0:
                    msg = "MOVE SVN Dir: '%s' --> '%s'" % (str(os.path.abspath(os.path.dirname(svn))), str(dst_svn))
                    if logtosyslogmsg == None:
                        logtosyslogmsg = msg
                    if logtogrowlmsg == None:
                        logtogrowlmsg = msg                    
                    if logtoall:
                        logs.log_to_all(msg)
                    elif logtofile:
                        if not logtofilename == None:
                            logfile(msg, logtofilename)
                        else:
                            logs.error_file(msg)
                    elif logtosyslog:
                        logs.error_syslog(logtosyslogport, logtosysloghost, msg, logtosyslogseverity, logtosyslogfacility)
                    elif logtogrowl:
                        logs.error_growl(logtogrowlhost, logtogrowlport, logtogrowlpass, logtogrowlappname, logtogrowltitle, logtogrowlevent, logtogrowlmsg, logtogrowlicon, logtogrowlicon)
                    print msg                        
                try:
                    if checkdir(svn) == True:
                        shutil.move(os.path.dirname(svn), dst_svn)
                except:
                    if verbosity == 2:
                        import traceback
                        msg = "Error:", traceback.format_exc()
                        if logtosyslogmsg == None:
                            logtosyslogmsg = msg
                        if logtogrowlmsg == None:
                            logtogrowlmsg = msg                        
                        if logtoall:
                            logs.log_to_all(msg)
                        elif logtofile:
                            if not logtofilename == None:
                                logfile(msg, logtofilename)
                            else:
                                logs.error_file(msg)
                        elif logtosyslog:
                            logs.error_syslog(logtosyslogport, logtosysloghost, msg, logtosyslogseverity, logtosyslogfacility)
                        elif logtogrowl:
                            logs.error_growl(logtogrowlhost, logtogrowlport, logtogrowlpass, logtogrowlappname, logtogrowltitle, logtogrowlevent, logtogrowlmsg, logtogrowlicon, logtogrowlicon)
                        if printerror:
                            print msg             
            else:
                pass
    except KeyboardInterrupt:
        try:
            sys.exit()
        except:
            pass
    except:
        import traceback
        if printerror:
            print "Error: ", traceback.format_exc()

def usage():
    parser = argparse.ArgumentParser()
    parser.add_argument('PATH', help='Root directory contains of hg or git repository folder', action='store')
    parser.add_argument('-hg', '--hgdir', help='Destination of hg directory, default is "hg", and make dir automatic if not exists')
    parser.add_argument('-git', '--gitdir', help='Destination of git directory, default is "git", and make dir automatic if not exists')
    parser.add_argument('-svn', '--svndir', help='Destination of svn directory, default is "svn", and make dir automatic if not exists')
    parser.add_argument('-dst', '--dst-all', help='Destination All of type repository', action='store')
    parser.add_argument('-l', '--log', help='Log to', action="store_true")
    parser.add_argument('-la', '--log-toall', help='Log to All (File, Syslog, Growl)', action="store_true")
    parser.add_argument('-lf', '--logfile', help='Log Error/Warning log to file, default filename is "traceback.log"', action="store_true")
    parser.add_argument('-lfname', '--logfilename', help='Filename of Log to file', action='store')
    parser.add_argument('-lg', '--loggrowl', help='Log Error/Warning log to growl', action='store_true')
    parser.add_argument('-lg-host', '--loggrowl-host', help='Hostname of Log to growl, default="localhost"', action='store')
    parser.add_argument('-lg-port', '--loggrowl-port', help='Port of Log to growl, default:23053', action='store')
    parser.add_argument('-lg-pass', '--loggrowl-password', help='Password of Log to growl if needed', action='store')
    parser.add_argument('-lg-app', '--loggrowl-app', help='App name of Log to growl, default: "repomgmt"', action='store')
    parser.add_argument('-lg-event', '--loggrowl-event', help='Eventname of Log to growl, default: "Error: "', action='store')
    parser.add_argument('-lg-title', '--loggrowl-title', help='Hostname of Log to growl, default: "Repository Management"', action='store')
    parser.add_argument('-lg-text', '--loggrowl-text', help='Message of Log to growl, default is error log', action='store')
    parser.add_argument('-lg-timeout', '--loggrowl-timeout', help='Timeout of Log to growl, default: 10 seconds', action='store')
    parser.add_argument('-lg-icon', '--loggrowl-icon', help='Icon path of Log to growl', action='store')
    parser.add_argument('-ls', '--logsyslog', help='Log Error/Warning log to syslog', action='store_true')
    parser.add_argument('-ls-host', '--logsyslog-host', help='Hostname of log to syslog', action='store')
    parser.add_argument('-ls-port', '--logsyslog-port', help='Port of log to syslog', action='store')
    parser.add_argument('-ls-sev', '--logsyslog-severity', help='Severity of log to syslog', action='store')
    parser.add_argument('-ls-fac', '--logsyslog-facility', help='Facility of log to syslog', action='store')
    parser.add_argument('-ls-msg', '--logsyslog-message', help='Message of log to syslog, default is error message', action='store')
    parser.add_argument('-pe', '--print-error', help='Print Error Message', action='store_true')
    parser.add_argument('-v', '--verbosity', help='print/show process running', action='count')
    if len(sys.argv) < 2:
        parser.print_help()
    else:
        args = parser.parse_args()
        if args.PATH:
            if args.log:
                analisys(os.path.relpath(args.PATH), args.hgdir, args.gitdir, args.svndir, args.verbosity, args.logfile, args.logfilename, args.logsyslog, args.logsyslog_host, args.logsyslog_port, args.logsyslog_facility, args.logsyslog_severity, args.logsyslog_message, args.loggrowl, args.loggrowl_host, args.loggrowl_port, args.loggrowl_password, args.loggrowl_app, args.loggrowl_title, args.loggrowl_event, args.loggrowl_text, args.loggrowl_icon, args.loggrowl_timeout, args.log_toall, args.print_error, args.dst_all)
            else:
                analisys(os.path.relpath(args.PATH), args.hgdir, args.gitdir, args.svndir, args.verbosity, printerror=args.print_error)
        else:
            parser.print_help()

if __name__ == '__main__':
    usage()


