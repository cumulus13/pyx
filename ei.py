import os
import sys
import configset

_cfg = r'c:\Anaconda\Lib\distutils\distutils.cfg'
_ei = r'c:\Anaconda\Scripts\easy_install.exe'
#_ei = r''

def easy_install(package, file_ini='distutils.cfg', easy_install_exe='easy_install.exe', index_url = '', find_links = '', debug=None):
    if os.path.exists(file_ini):
        cfg = file_ini
    if os.path.isfile(os.path.join(os.path.dirname(__file__), file_ini)):
        cfg = os.path.join(os.path.dirname(__file__), file_ini)
    if os.path.isfile(os.path.join(os.getcwd(), file_ini)):
        cfg = os.path.join(os.getcwd(), file_ini)                
    try:
        if not os.path.isfile(cfg):
            cfg = _cfg
    except:
        cfg = _cfg
        
    if not os.path.isfile(cfg):
        return False
    
    if os.path.exists(easy_install_exe):
        ei = easy_install_exe
    if os.path.isfile(os.path.join(os.path.dirname(__file__), easy_install_exe)):
        ei = os.path.join(os.path.dirname(__file__), easy_install_exe)    
    if os.path.isfile(os.path.join(os.getcwd(), easy_install_exe)):
        ei = os.path.join(os.getcwd(), easy_install_exe)        
    try:
        if not os.path.isfile(ei):
            ei = _ei
    except:
        ei = _ei
        
    if not os.path.isfile(ei):
        return False
        
    if index_url == '':
        index_url  = configset.read_config('easy_install', 'index_url', cfg)
    
    if find_links == '':
        find_links = configset.read_config2('easy_install', 'find-links', cfg)
    if isinstance(find_links, str):
        find_links = [find_links]
    if debug:
        print "cfg" + (20 - len("cfg"))*' ' + '=', cfg
        print "easy_install" + (20 - len("easy_install"))*' ' + '=', ei
        print "index_url" + (20 - len("index_url"))*' ' + '=', index_url
        print "find-links" + (20 - len("find-links"))*' ' + '=', find_links
    
    str_ei = '{0} -i {1} -f {2} {3}'
    d = 1
    while True:
        if d != 0:
            if len(index_url) > 0:
                if len(find_links) > 0:
                    for i in find_links:
                        d = os.system(str_ei.format(ei, index_url, i, package))
            else:
                print "NO INDEX_URL !"
                break
        else:
            break
def usage():
    import argparse
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('PACKAGE', help='package name to install', action='store')
    parser.add_argument('-i', '--index-url', help='Index url', action='store', default='')
    parser.add_argument('-f', '--find-links', help='Find links url', action='store', nargs='*', default='')
    parser.add_argument('-c', '--ini-file', help='Custom file ini (config)', action='store', default='distutils.cfg')
    parser.add_argument('-e', '--easy-install', help='Custom easy_install executable', action='store', default='easy_install.exe')
    parser.add_argument('-d', '--debug', help='Debug process', action='store_true')
    if len(sys.argv) == 1:
        parser.print_help()
    else:        
        args = parser.parse_args()
        easy_install(args.PACKAGE, args.ini_file, args.easy_install, args.index_url, args.find_links, args.debug)
        
if __name__ == '__main__':
    usage()
        