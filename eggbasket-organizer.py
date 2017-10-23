import re
import os
import sys
import shutil
import traceback
import winshell
import termcolor
import colorama

filename = os.path.basename(__file__)

def organizer(path):
    excp = ['.gitignore','.git','.hg','.svn']
    ext_excp = ['.py','.txt']
    data = os.listdir(path)
    for i in data:
        #print os.path.abspath(i)
        if os.path.isfile(i):
            data_00 = re.split("-", i)
            if len(data_00) > 2:
                data_000 = data_00[0:len(data_00) - 1]
                data_01 =  "-".join(data_000)
            else:
                data_01 = data_00
            if isinstance(data_01, list):
                data_02 = data_01[0]
            else:
                data_02 = data_01
            if len(data_01) > 1:
                if os.path.isdir(data_02):
                    if data_02 not in excp:
                        #print "is dir         =", data_02
                        try:
                            if os.path.exists(os.path.join(data_02, i)):
                                os.remove(os.path.join(data_02, i))
                            shutil.move(i, data_02)
                            #print "i =", i
                            #print "data_02 =", data_02
                            #print "-" * 100
                        except:
                            traceback.format_exc_syslog_growl()
                else:
                    try:
                        os.makedirs(data_02)
                        pass
                    except:
                        traceback.format_exc_syslog_growl()
                    if data_02 not in excp:
                        #print "NOT is dir     =", data_02
                        try:
                            if os.path.exists(os.path.join(data_02, i)):
                                os.remove(os.path.join(data_02, i))
                            shutil.move(i, data_02)
                            #print "i 2 =", i
                            #print "data_02 2 =", data_02
                            #print "-" * 100
                        except:
                            traceback.format_exc_syslog_growl()
            else:
                pass
        else:
            pass

def checklen(path):
    dlen = len(os.listdir(path))
    return dlen

def colorit(data, message):
    colorama.init()
    severity = ['emergency', 'alert', 'critical', 'error', 'warn', 'notice', 'info', 'debug']
    if str(data).strip() in "emergency":
        return termcolor.colored(message, "white", "on_blue")
    elif str(data).strip() in "alert":
        return termcolor.colored(message, "yellow", "on_cyan")
    elif str(data).strip() in "critical":
        return termcolor.colored(message, "green", "on_magenta")
    elif str(data).strip() in "error":
        return termcolor.colored(message, "white", "on_red")
    elif str(data).strip() in "warning":
        return termcolor.colored(message, "white", "on_yellow")
    elif str(data).strip() in "notice":
        return termcolor.colored(message, "yellow", "on_cyan")
    elif str(data).strip() in "info":
        return termcolor.colored(message, "white", "on_grey")
    elif str(data).strip() in "debug":
        return termcolor.colored(message, "yellow", "on_white")
    else:
        return termcolor.colored(message, "green", "on_grey")

def cleanUp(path):
    excp = ['.zip', '.exe', '.tar', '.tar.gz', '.gz', '.bz2', '.rar', '.msi', '.whl', '.egg', '.asc', '.deb', '.rpm', '.tgz', '.pdf', '.inv', '.bunzip2', '.run', '.so', '.java', '.dll', '.md5', '.psd', '.sig']
    os.chdir(path)
    #print "path =", os.path.abspath(path)
    data = os.listdir(os.getcwdu())
    for i in data:
        try:
            q = str(os.path.basename(os.path.abspath(i))).lower()
        except UnicodeEncodeError:
            q = ''
        #print "q 1 =", q
        excp2 = ["pytube", "scripts", "masters", "inv", "web", "webpy", "web_py", "docs", "protobuf", "pygame", "pyaudio"]
        if str(q).lower() in excp2:
            #print "q 2 =", q
            pass
        else:
            if os.path.isdir(i):
                data1 = os.listdir(os.path.abspath(i))
                #print "data1 =", data1
                for x in data1:
                    data_02 = ''
                    if os.path.isfile(os.path.join(os.path.abspath(i), x)):
                        data_00 = re.split("-", x)
                        if len(data_00) > 2:
                            data_000 = data_00[0:len(data_00) - 1]
                            data_01 =  "-".join(data_000)
                        else:
                            data_01 = data_00
                        if isinstance(data_01, list):
                            data_02 = data_01[0]
                        else:
                            data_02 = data_01
                    if data_02 == os.path.basename(i):
                        pass
                    else:
                        if os.path.isfile(os.path.join(os.path.abspath(i), x)):
                            if str(os.path.splitext(os.path.join(os.path.abspath(i), x))[1]).lower() not in excp:
                                #print "x =", os.path.join(os.path.abspath(i), x)
                                print colorit(None, "DELETE FILE: " + os.path.join(os.path.abspath(i), x))
                                winshell.delete_file(os.path.join(os.path.abspath(i), x), no_confirm=True,  silent=True)
                        if os.path.isdir(os.path.join(os.path.abspath(i), x)):
                            print colorit('alert', "DELETE FOLDER: " + os.path.join(os.path.abspath(i), x))
                            winshell.delete_file(os.path.join(os.path.abspath(i), x), no_confirm=True,  silent=True)
                    if checklen(os.path.abspath(i)) == 0:
                        print colorit('error', "DELETE MASTER FOLDER: " + os.path.abspath(i))
                        winshell.delete_file(os.path.abspath(i), no_confirm=True,  silent=True)

def main(path):
    organizer(path)
    cleanUp(path)

def usage():
    usage = """eggbasket-organizer.py [options] PATH"""
    import optparse
    parser = optparse.OptionParser(usage=usage)
    parser.add_option('-m', '--manage', help="re-Structure Folder path", action="store_true")
    parser.add_option('-c', '--cleanup', help='delete folder/files which not needit', action='store_true')
    args, argv = parser.parse_args()
    if len(argv) > 0:
        if args.manage:
            organizer(argv[0])
            #print argv[0]
        elif  args.cleanup:
            cleanUp(argv[0])
            #print argv[0]
        else:
            print "\n"
            parser.print_help()
    else:
        print "\n"
        parser.print_help()	


if __name__ == "__main__":
    usage()