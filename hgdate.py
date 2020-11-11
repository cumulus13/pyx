#!c:/SDK/Anaconda2/python.exe
from __future__ import print_function
import traceback
import os
import sys
import re
import configparser
import sendgrowl 
from make_colors import make_colors
import argparse
from configset import configset
if sys.version_info.major == 3:
    import urllib.parse
else:
    class urllib:
        def parse(self):
            pass
    import urlparse
    urllib.parse = urlparse
import getpass
from pydebugger.debug import debug


hgrc = os.path.join(os.getcwd(), '.hg', 'hgrc')
configname = os.path.join(os.path.dirname(__file__), 'hgdate.ini')
CONFIG = configset(configname)
CONFIG1 = configset(hgrc)
HG_BIN = r'd:\TOOLS\pyx\thg.bat'
if HG_BIN == r'':
    HG_BIN = 'thg.exe'

def notify(app='HGDate', event='Commit', title='HgDate', message='Commit', host='', port=23053, icon='hgdate.png', timeout=10):
    if icon:
        icon = os.path.join(os.path.dirname(__file__), icon)
    if not os.path.isfile(icon):
        icon = None
    growl = sendgrowl.growl()
    if os.getenv('GROWL_SERVER'):
        growl_server = os.getenv('GROWL_SERVER').split(";")
        for i in growl_server:
            if ":" in i:
                host, port = str(i).split(":")
                host = host.strip()
                port = int(port)
                growl.publish(app, event, title, message, host, port, timeout, icon)
            else:
                host = str(i).strip()
                growl.publish(app, event, title, message, host, port, timeout, icon)
    else:
        if isinstance(host, list):
            for i in growl_server:
                if ":" in i:
                    host, port = str(i).split(":")
                    host = host.strip()
                    port = int(port)
                    growl.publish(app, event, title, message, host, port, timeout, icon)
                else:
                    host = str(i).strip()
                    growl.publish(app, event, title, message, host, port, timeout, icon)
        elif ";" in host:
            growl_server = str(host).split(";")
            for i in growl_server:
                if ":" in i:
                    host, port = str(i).split(":")
                    host = host.strip()
                    port = int(port)
                    growl.publish(app, event, title, message, host, port, timeout, icon)
                else:
                    host = str(i).strip()
                    growl.publish(app, event, title, message, host, port, timeout, icon)
        else:
            debug(host = host)
            debug(port = port)
            try:
                growl.publish(app, event, title, message, host, port, timeout, icon)
            except:
                print ("ERROR:", traceback.format_exc())
                print (make_colors("Can't Connect to Growl Server !", 'white', 'lightred'))
                pass

def remote_pack(remote, username = None, password = None):
    username_x = ''
    password_x = ''
    host = ''
    remote_parse = urllib.parse.urlparse(remote)
    scheme = remote_parse.scheme
    netloc = remote_parse.netloc
    path = remote_parse.path
    query = remote_parse.query
    if '@' in netloc:
        username_x, host = netloc.split('@')
        if ":" in username:
            username_x, password_x = username.split(":")
    if not host:
        host = netloc
    if not username:
        if username_x:
            username = username_x
    if not password:
        if password_x:
            password = password_x
    debug(username = username)
    debug(password = password)
    if username:
        if password:
            host = '%s:%s@%s' % (username, password, host)
        else:
            host = '%s@%s' % (username, host)
        if query:
            return scheme + '://' + host + path + '?' + query
        else:
            return scheme + '://' + host + path

def format_hg_remote(remote):
    
    global CONFIG
    username = ''
    password = ''
    host = ''
    port = ''
    if not remote:
        remote = ''
    
    if not urllib.parse.urlparse(remote).scheme in ['http', 'https', 'ssh']:
        return False

    if '@' in remote:
        debug(remote = remote)
        if ":" in remote:
            check_sep = re.findall(":", remote)
            debug(check_sep = check_sep)
            debug(len_check_sep = len(check_sep))
            if len(check_sep) == 2:
                if ":" in re.split('http://|https://|ssh://|@', remote)[1]:
                    username, password = re.split('http://|https://|ssh://|@', remote)[1].split(":")
                else:
                    username = re.split('http://|https://|ssh://|@', remote)[1]
                    #password = getpass.getpass('PASSWORD: ')
                host = re.split('http://|https://|ssh://|@', remote)[-1].split('/')[0]
                if ":" in host:
                    port = host.split(":")[1]
                debug(username = username)
                debug(password = password)
                debug(host = host)
            elif len(check_sep) == 3:
                username, password = re.split('http://|https://|ssh://|@', remote)[1].split(":")
                host = re.split('http://|https://|ssh://|@', remote)[-1].split('/')[0]
                if ":" in host:
                    port = host.split(":")[1]                
                debug(username = username)
                debug(password = password)
                debug(host = host)
            else:
                username = re.split('http://|https://|ssh://|@', remote)[1]
                host = re.split('http://|https://|ssh://|@', remote)[-1].split('/')[0]
                if ":" in host:
                    port = host.split(":")[1]
                debug(username = username)
                debug(password = password)
                debug(host = host)                
            #return False
    else:
        host = urllib.parse.urlparse(remote).netloc
        debug(host = host)
        if ":" in host:
            port = host.split(":")[1]        
        debug(host = host)
        #return False
    if 'bitbucket' in remote or 'github' in remote or 'kal' in remote:
        flag = host.split(".")[0]
        debug(flag = flag)
    else:
        flag = urllib.parse.urlparse(remote).netloc
        debug(flag = flag)
    debug(port = port)
    if ":" in flag:
        flag, port = str(flag).split(":")
        debug(flag = flag)
    debug(port = port)
    if port == '5000' or port == 5000:
        flag = 'kallithea'
        debug(flag = flag)
    debug(flag = flag)
    if CONFIG.read_config(flag, 'username'):
        username = CONFIG.read_config(flag, 'username')
    else:
        if not username:
            username = raw_input('[%s] USERNAME: ' % (flag))
    if CONFIG.read_config(flag, 'password'):
        password = CONFIG.read_config(flag, 'password')
    else:
        if not password:
            password = getpass.getpass('[%s] PASSWORD: ' % (flag))
    if not username and not password:
        return False
    remote = remote_pack(remote, username, password)
    debug(remote)
    return remote
    #else:
        #debug(remote)
        #return remote

def get_remotes(remote_name = 'default'):
    list_remotes = []
    
    data = CONFIG1.get_config('paths', remote_name)
        
    for i in CONFIG1.options('paths'):
        list_remotes.append({'name': i, 'url': CONFIG.get_config('paths', i)})					
    debug(list_remotes = list_remotes)
    return list_remotes

def checkRemote(remote_name='default', remote_url=None, push=True):
    
    remote_url = CONFIG1.get_config('paths', 'default-push')
    debug(remote_url = remote_url)
    if not remote_url:
        remote_url = CONFIG1.get_config('paths', 'default')
        debug(remote_url = remote_url)
    if push and remote_url:
        notify(event='push', message='PUSH repo to %s'%(remote_url))
        os.system(HG_BIN + " push")
        return True
    
    if not remote_url:
        remote_url = raw_input('add hg remote origin (URL): ')
        if len(remote_url) == 0:
            print ("Please Add remote git url (origin) first !")
            sys.exit(0)

        data = CONFIG1.get_config('paths', remote_name)
        if push and data:
            notify(event='push', message='PUSH repo to %s'%(data))
            os.system(HG_BIN + " push")

def commit(push = True):
    global HG_BIN
    import datetime
    comment = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S:%f')
    tag = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d_%H%M%S_%f')
    if os.path.isfile(os.path.join(os.getcwd(), '.hgignore')):
        notify(event='hgignore', message='.hgignore EXISTS')
        os.system(HG_BIN + " add .")
        notify(event='add_file', message='Add all of file in this repo')
        os.system(HG_BIN + " tag \"" + str(tag) + '"')
        notify(event='tag', message='make tag "%s"'%(str(tag)))
        os.system(HG_BIN + " commit -m \"" + str(comment) + '"')
        notify(event='commit', message='Commit Action')
        checkRemote(push = False)
    else:
        notify(event='hgignore', message='.hgignore NOT EXISTS !')
        f = open(os.path.join(os.getcwd(), '.hgignore'), 'w')
        f.write(".pyc\n.zip\n.rar\n.7z\n.mp3\n.wav\n.gitignore\n^.git/\ntraceback.log\n^build/\n^__pycache__/\n^dist/\n")
        f.close()
        os.system(HG_BIN + " add .")
        notify(event='add_file', message='Add all of file in this repo')
        os.system(HG_BIN + " tag \"" + str(tag) + '"')
        notify(event='tag', message='make tag "%s"'%(str(tag)))
        os.system(HG_BIN + " commit -m \"" + str(comment) + '"')
        notify(event='commit', message='Commit Action')
        checkRemote(push = False)
    remotes = get_remotes()
    debug(remotes = remotes)
    for i in remotes:
        if push:
            host = format_hg_remote(i.get('url'))
            notify(event='push', message='PUSH repo to %s'%(i.get('name')))
            os.system(HG_BIN + " push %s" % (host))

def push(remote_name = None):
    global HG_BIN
    remotes = get_remotes()
    debug(remotes = remotes)
    for i in remotes:
        if remote_name:
            if i.get('name') == remote_name:
                if push:
                    host = format_hg_remote(i.get('url'))
                    debug(host = host)
                    notify(event='push', message='PUSH repo to %s'%(i.get('name')))
                    os.system(HG_BIN + " push %s" % (host))
        else:
            if push:
                host = format_hg_remote(i.get('url'))
                debug(host = host)
                notify(event='push', message='PUSH repo to %s'%(i.get('name')))
                os.system(HG_BIN + " push %s" % (host))

def add_remote(remote_name, remote_url):
    
    if not os.path.isdir(os.path.join(os.getcwd(), '.hg')):
        print (make_colors("Not a Mercurial (HG) directory !", 'white', 'lightred'))
        sys.exit(0)
    else:
        CONFIG1.write_config('paths', remote_name, remote_url)

def remove_remote(remote_name):
    debug("remove_remote")
    
    if not os.path.isfile(hgrc):
        print (make_colors('No Config FOUND !', 'white', 'lightred'))
        return False

    try:
        if not CONFIG1.get_config('paths', remote_name):
            print (make_colors('NO remote name FOUND !', 'white', 'lightred'))
            sys.exit(0)
    except:
        print (make_colors('NO remote name FOUND !', 'white', 'lightred'))
        sys.exit(0)
    CONFIG1.write_config('paths', remote_name, '')
    
def list_remote():
    
    list_len = []
    if os.path.isfile(hgrc):
        CONFIG1.read(hgrc)
        names = CONFIG1.options('paths')
        for i in names:
            list_len.append(len(i))

        for i in names:
            if not CONFIG1.get('paths', i):
                pass
            else:
                print(make_colors(i, 'black', 'lightyellow'), (max(list_len) - len(i)) * ' ', ' ', make_colors(CONFIG1.get('paths', i), 'white', 'blue'))

def usage():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    subparser = parser.add_subparsers(title='ACTION', dest='ACTION')
    parser_remote = subparser.add_parser('remote', help='Remote actions, use: [-h|--help] for usage help')
    parser_list = subparser.add_parser('list', help='List Remote actions, use: [-h|--help] for usage help')
    parser_remote.add_argument('-a', '--add', action='store', help='add remote name and url, format: remote_name remote_url', nargs=2)
    parser_remote.add_argument('-r', '--remove', action='store', help='delete remote name and url')
    parser_remote.add_argument('-u', '--update', action='store', help='update remote name and url, format: remote_name remote_url', nargs=2)
    parser_remote.add_argument('-U', '--url', action='store', help='url remote to add')
    parser_remote.add_argument('-v', '--list', action='store_true', help='list all remote')
    print (make_colors("HG (Mercurial) Command commit ,tag and push based on Datetime (Timestamp) support manipulation of remote name and url", 'lightblue'))
    if len(sys.argv) == 1:
        commit()
    elif len(sys.argv) == 2:
        if sys.argv[1] == '-p' or sys.argv[1] == '--push':
            push()
        else:
            parser.print_help()
    elif len(sys.argv) == 3 and sys.argv[1] == '-p' or sys.argv[1] == '--push':
        if sys.argv[1] == '-p' or sys.argv[1] == '--push':
            push(sys.argv[2])
        else:
            parser.print_help()
    else:
        args = parser.parse_args()
        if args.ACTION == 'remote':
            if args.add:
                if len(args.add) == 2:
                    remote_name, remote_url = args.add
                if args.url:
                    remote_url = args.url
                    remote_name = args.add[0]
                if remote_name:
                    if remote_url:
                        add_remote(remote_name, remote_url)
                    else:
                        print (make_colors('No URL given !', 'white', 'lightred'))
                        sys.exit(0)
                else:
                    print (make_colors('No NAME given !', 'white', 'lightred'))
                    sys.exit(0)
            elif args.list:
                list_remote()
            elif args.remove:
                remove_remote(args.remove)
            elif args.update:
                remove_remote(args.update[0])
                if len(args.update) == 2:
                    remote_name, remote_url = args.update
                if args.url:
                    remote_url = args.url
                    remote_name = args.update[0]
                if remote_name:
                    if remote_url:
                        add_remote(remote_name, remote_url)
                    else:
                        print (make_colors('No URL given !', 'white', 'lightred'))
                        sys.exit(0)
                else:
                    print (make_colors('No NAME given !', 'white', 'lightred'))
                    sys.exit(0)
            else:
                parser.print_help()
        elif args.ACTION == 'list':
            list_remote()
        else:
            parser.print_help()

if __name__ == '__main__':
    PID = os.getpid()
    print ("PID:", PID)
    # commit()
    usage()
    #checkRemote()