import vping
import re
import sys
import os
import optparse
import configset
import traceback
import getpass
import thread


class reuse(object):

    def __init__(self):
        super(reuse, self)
        self.configname = configset.get_config_file('reuse.ini')

    def makeconfig(self, list_path, list_vpath, list_host, username, password, list_complete=None):
        '''
           len of list_path, list_vpath, list_host, username, password must same
           username and password = None or string

           list_complete = 'path:vpath:host:username:password', if password or username = None, it must = '' not None
        '''
        if list_complete == None:
            configset.write_config2('PATH', 'name', self.configname, list_path)
            configset.write_config2(
                'PATH', 'vpath', self.configname, list_vpath)
            configset.write_config2('PATH', 'host', self.configname, list_host)
            configset.write_config2(
                'PATH', 'username', self.configname, username)
            configset.write_config2(
                'PATH', 'password', self.configname, password)
        else:
            if isinstance(list_complete, list):
                list_path = []
                list_vpath = []
                list_host = []
                list_username = []
                list_password = []
                for i in list_complete:
                    name, vpath, host, username, password = i.split(":")
                    list_path.append(name)
                    list_vpath.append(vpath)
                    list_host.append(host)
                    list_username.append(username)
                    list_password.append(password)
                list_path = ",".join(list_path)
                list_vpath = ",".join(list_vpath)
                list_host = ",".join(list_host)
                list_username = ",".join(list_username)
                list_password = ",".join(list_password)

                configset.write_config2(
                    'PATH', 'name', self.configname, list_path)
                configset.write_config2(
                    'PATH', 'vpath', self.configname, list_vpath)
                configset.write_config2(
                    'PATH', 'host', self.configname, list_host)
                configset.write_config2(
                    'PATH', 'username', self.configname, username)
                configset.write_config2(
                    'PATH', 'password', self.configname, password)
            else:
                name, vpath, host, username, password = i.split(":")
                configset.write_config2('PATH', 'name', self.configname, name)
                configset.write_config2(
                    'PATH', 'vpath', self.configname, vpath)
                configset.write_config2('PATH', 'host', self.configname, host)
                configset.write_config2(
                    'PATH', 'username', self.configname, username)
                configset.write_config2(
                    'PATH', 'password', self.configname, password)

    def getconfig(self):
        path = ''
        vpath = ''
        host = ''
        username = ''
        password = ''
        data_dict = {}
        if os.path.exists(self.configname):
            try:
                data_list = configset.read_config2(
                    'PATH', 'name', self.configname)
            except:
                self.setconfig()
                return {}
            # print "data_list =", data_list
            if data_list != []:
                for i in data_list:
                    a = i
                    i = str(i).strip()
                    i = str(i).split(":")
                    if len(i) == 5:
                        path, vpath, host, username, password = i
                        path = path.strip()
                        vpath = vpath.strip()
                        host = host.strip()
                        username = username.strip()
                        password = password.strip()
                        data_dict.update({data_list.index(a): {
                            'path': path, 'vpath': vpath, 'host': host, 'username': username, 'password': password}})
                    elif len(i) == 4:
                        path, vpath, host, username = i
                        path = path.strip()
                        vpath = vpath.strip()
                        host = host.strip()
                        username = username.strip()
                        password = password.strip()
                        data_dict.update({data_list.index(a): {
                            'path': path, 'vpath': vpath, 'host': host, 'username': username, 'password': password}})
                    elif len(i) == 3:
                        path, vpath, host = i
                        path = path.strip()
                        vpath = vpath.strip()
                        host = host.strip()
                        username = username.strip()
                        password = password.strip()
                        data_dict.update({data_list.index(a): {
                            'path': path, 'vpath': vpath, 'host': host, 'username': username, 'password': password}})
                    else:
                        print "WARNING: Can't parse data {0}".format(":".join(i))
        return data_dict

    def setconfig(self, path=None, vpath=None, host=None, username='', password=''):
        if ":" in path:
            path = path[0:path.index(":")]
        if os.path.exists(self.configname):
            try:
                data_list = configset.read_config2(
                    'PATH', 'name', self.configname)
                if path != None:
                    data_add = "{0}:{1}:{2}:{3}:{4}".format(
                        path, vpath, host, username, password)
                    if data_add not in data_list:
                        data_list.append(data_add)

                data = "\n".join(data_list)
                configset.write_config2('PATH', 'name', self.configname, data)
                return data_list
            except:
                print traceback.format_exc()
                # configset.write_config2('PATH', 'name', self.configname)
                return []

    def delconfig(self, path=None, vpath=None, host=None, username='', password=''):
        if os.path.exists(self.configname):
            try:
                data_list = configset.read_config2(
                    'PATH', 'name', self.configname)
                if path != None:
                    data_del = "{0}:{1}:{2}:{3}:{4}".format(
                        path, vpath, host, username, password)
                    try:
                        data_list.remove(data_del)
                    except:
                        pass
            except:
                print traceback.format_exc()

    def checkUserPassword(self, username, password, host, verbosity=False):
        # print "USERNAME =", username
        # print "PASSWORD =", password
        if verbosity:
            print "checkUserPassword --> GET CONFIG"
        data_config = self.getconfig()
        data_config_temp = []
        for i in data_config:
            # print "data_config.get(i).get('username') =", data_config.get(i).get('username')
            # print "data_config.get(i).get('password') =", data_config.get(i).get('password')
            # print "data_config.get(i).get('host')     =", data_config.get(i).get('host')
            # print "-" * 220
            if username.strip() == data_config.get(i).get('username'):
                if password.strip() == data_config.get(i).get('password'):
                    if host.strip() == data_config.get(i).get('host'):
                        # print "ADA"
                        data_config_temp.append(data_config.get(i))
        if len(data_config_temp) > 1:
            # print "data_config_temp =", data_config_temp[:1]
            return False
        else:
            return True

    def reuse(self, name='', vpath='', host='', username='', password='', verbosity=False):
        # if save_cred:
        #     save_cred = 'YES'
        # else:
        #     save_cred = ''
        if verbosity:
            verbosity = ""
        else:
            verbosity = " > NUL"

        path = name
        if ":" in name:
            name = name[0:name.index(":")]
            path = name
        data_use = self.getconfig()
        # check = False
        if name != '':
            for i in data_use:
                # if data_use.get(i).get('host') == host and
                # data_use.get(i).get('password') != '':
                if data_use.get(i).get('path') == path and data_use.get(i).get('vpath') == vpath and data_use.get(i).get('host') == host:
                    q0 = raw_input(
                        'Path with %s and Host with %s is EXISTS !, replace/overwrite it [y/n] ?: ' % (path, vpath))
                    path, vpath, host, username, password = data_use.get(i).get('path'), data_use.get(i).get(
                        'vpath'), data_use.get(i).get('host'), data_use.get(i).get('username'), data_use.get(i).get('password')

                    if q0 == 'y':
                        self.delconfig(path, vpath, host,
                                       username, password)
                        self.setconfig(name, vpath, host, username, '')
                else:
                    self.setconfig(name, vpath, host, username, '')
                # check = True
                    # break

            # if not check:
                if password == '' and username == '':
                    q1 = raw_input('Please enter username:')
                    q2 = getpass.getpass('Please enter password:')
                    self.setconfig(name, vpath, host, q1, q2)
                elif password == '' and username != '':
                    q2 = getpass.getpass('Please enter password:')
                    self.setconfig(name, vpath, host, username, q2)

        data_use = self.getconfig()
        for x in data_use:
            name = data_use.get(x).get('path')
            vpath = data_use.get(x).get('vpath')
            host = data_use.get(x).get('host')
            username = data_use.get(x).get('username')
            password = data_use.get(x).get('password')
            # print "x =", data_use.get(x)
            ip = re.findall(
                r"\b(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\b", str(host))
            # print "ip =",ip
            # print "ip 1    =", ip
            if len(ip) > 0:
                checkip = vping.vping(ip[0], 3)
                # print "ip 2    =", ip
                # print "checkip =", checkip
            else:
                return False
            if not ":" in name:
                name = name[0] + ":"
            if checkip:
                # print "delete %s"%name
                print "checkip =", checkip

                try:
                    print "DELETE PATH:", str(name)
                    ndel = os.system(
                        "NET USE {0} /DELETE {1}".format(name, verbosity))
                except:
                    pass
                if ndel == 1:
                    if verbosity != "":
                        print "ERROR: DELETING Path={0}, vpath={1}, host={2}, username={3}, password={4}".format(name, vpath, host, username, password)
                # net use Y: \\192.168.1.5\www blackid /user:licface
                # if username:
                #     print "AAA"
                #     if password:
                #         print "BBB"
                #         os.system(
                #             "net use {0} \\\\{1}\{2} {3} /user:{4} {5}".format(name, host, vpath, password, username, verbosity))
                #     else:
                #         print "CCC"
                #         os.system(
                #             "net use {0} \\\\{1}\{2} /user:{3} {4}".format(name, host, vpath, username, verbosity))
                # else:
                #     print "DDD"
                #     os.system("net use {0} \\\\{1}\{2} {3}".format(
                #         name, host, vpath, verbosity))
                # print "Name        =", name
                # print "Host        =", host
                # print "Vpath       =", vpath
                # print "Password    =", password
                # print "Username    =", username
                # print "Verbosity   =", verbosity
                # print "-" * 220
                if self.checkUserPassword(username, password, host):
                    # print "AAA"
                    os.system("net use {0} \\\\{1}\{2} {3} /user:{4} {5}".format(
                    name, host, vpath, password, username, verbosity))
                else:
                    # print "BBB"
                    os.system("net use {0} \\\\{1}\{2} {3}".format(
                    name, host, vpath, verbosity))

    def delete(self, name):
        change = False
        if name == 'all':
            data_use = self.getconfig()
            for x in data_use:
                name = data_use.get(x).get('path')
                if not ":" in name:
                    name = name[0] + ":"
                try:
                    print "DELETE PATH:", str(name)
                    ndel = os.system(
                        "NET USE {0} /DELETE > NUL".format(name))
                except:
                    pass
        if not name[-1] == ":":
            name = name + ":"
        data = configset.read_config2('PATH', 'name', self.configname)
        for i in data:
            if i[0:2].lower() == name.lower():
                data.remove(data[data.index(i)])
                change = True
                try:
                    print "DELETE PATH:", str(name)
                    ndel = os.system(
                        "NET USE {0} /DELETE > NUL".format(name))
                except:
                    pass
        if change:
            data = "\n".join(data)
            configset.write_config2('PATH', 'name', self.configname, data)

    def view(self):
        data = configset.read_config2('PATH', 'name', self.configname)
        print "==================================================================================="
        print "Name ||            Vpath             ||        Host/IP         ||      Username        "
        print "==================================================================================="
        # for i in data:
        #     r = str(i).split(":")
        #     if len(r) == 4:
        #         print r[0] + "   ||" + ((28 - len(r[1])) / 2) * " " + r[1] + ((28 - len(r[1]) / 2) * " " + "||" + ((22 - len(r[2])) / 2) * " " + r[2] + ((22 - len(r[2])) / 2) * ' ' + "||" + ((22 - len(r[3])) / 2) * " " + r[3] + ((22 - len(r[3])) / 2) * " "
        #     elif len(r) == 3:
        # print r[0] + "   ||" + ((28 - len(r[1])) / 2) * " " + r[1] + ((28 -
        # len(r[1]) / 2) * " " + "||" + ((22 - len(r[2])) / 2) * " " + r[2] +
        # ((22 - len(r[2])) / 2) * ' ' + "||"

        # data = ['K:C:192.168.1.3:myusername:mypassword', 'M:N:192.168.3.2:root:toor']
        for i in data:
            r = str(i).split(":")
            # print "r        =", r
            # print "len(r)   =", len(r)
            # print "-"*220
            len1 = ((28 - len(r[1])) / 2)
            len2 = ((22 - len(r[2])) / 2)
            if not (len1 % 2) == 0:
                len1 = ((28 - len(r[1]) + 1) / 2)
            if not (len2 % 2) == 0:
                len2 = ((22 - len(r[2]) + 1) / 2)
            if len(r) >= 4:
                len3 = ((22 - len(r[3])) / 2)
                if not (len3 % 2) == 0:
                    len3 = ((21 - len(r[3]) + 1) / 2)
                print " " + r[0] + "   ||" + len1 * " " + r[1] + len1 * " " + " ||" + len2 * " " + r[2] + len2 * ' ' + " ||" + len3 * " " + r[3] + len3 * " "
            elif len(r) == 3:
                print " " + r[0] + "   ||" + len1 * " " + r[1] + len1 * " " + " ||" + len2 * " " + r[2] + len2 * ' ' + " ||"

    def usage(self):
        import argparse
        parser = argparse.ArgumentParser(
            formatter_class=argparse.RawTextHelpFormatter)
        parser.add_argument(
            '-n', '--name', help='Name or Drive will use', action='store')
        parser.add_argument(
            '-p', '--vpath', help='Path name of virtual host path', action='store')
        parser.add_argument(
            '-H', '--host', help='Host or Ip Address name', action='store')
        parser.add_argument('-U', '--username',
                            help='Username access host', action='store', default='')
        parser.add_argument('-P', '--password',
                            help='Password access host', action='store', default='')
        parser.add_argument(
            '-d', '--delete', help='Delete Path Name', action='store')
        parser.add_argument(
            '-V', '--view', help='View list of Path', action='store_true')
        parser.add_argument(
            '-v', '--verbosity', help='Show Process logs', action='store_true')

        if len(sys.argv) == 1:
            self.reuse()
            # thread.start_new(self.reuse, ())
            parser.print_help()
        elif len(sys.argv) == 2:
            if sys.argv[1] == '-v':
                self.reuse(verbosity=True)
            else:
                self.reuse()
            # thread.start_new(self.reuse, ())
            parser.print_help()
        else:
            args = parser.parse_args()
            if args.name:
                if not ":" == args.name[-1]:
                    args.name = args.name + ":"
            if args.delete:
                if args.delete == 'all':
                    self.delete('all')
                elif args.name:
                    self.delete(args.name)
                else:
                    self.delete(args.delete)
            elif args.view:
                self.view()
            else:
                self.reuse(args.name, args.vpath, args.host,
                           args.username, args.password, args.verbosity)


if __name__ == '__main__':
    c = reuse()
    c.usage()
    # c.checkUserPassword('root', ' blackid', '192.168.100.3')
    # c.delete('t')
    # for i in c.getconfig():
    # print i,"=",c.getconfig().get(i)
    # c.setconfig('A','AAA','192.168.1.100','hacker','blackid')
    # print "-"*220
    # for x in c.getconfig():
    # print x,"=",c.getconfig().get(x)
