import os
import sys


class keymaker(object):

    def __init__(self, host='', openssl_app='', openssl_path=''):
        super(keymaker, self)
        self.host = host
        self.OPENSSL_APP = openssl_app
        if self.OPENSSL_APP == '' or self.OPENSSL_APP == None:
            self.OPENSSL_APP = r'c:\Apps\Apache2416\bin\openssl.exe'
        self.OPENSSL_PATH = openssl_path
        if self.OPENSSL_PATH == '' or self.OPENSSL_PATH == None:
            self.OPENSSL_PATH = os.getcwd()

    def get_key(self, bits, pem, C, ST, L, O, OU, CN, emailaddr, output_password='', challengePassword=''):
        """
            get inserted key for SSL key config return variabel key string
    
        [req]
            default_bits           =
            default_keyfile        = .pem
            distinguished_name     =
            attributes             =
            prompt                 =
            output_password        =
    
        [req_distinguished_name]
            C                      =
            ST                     =
            L                      =
            O                      =
            OU                     =
            CN                     =
            emailAddress           =
    
        [req_attributes]
            challengePassword      =
        """
        key = """
    [req]
    default_bits           = %d
    default_keyfile        = %s.pem
    distinguished_name     = req_distinguished_name
    attributes             = req_attributes
    prompt                 = no
    output_password        = %s
    
    [req_distinguished_name]
    C                      = %s
    ST                     = %s
    L                      = %s
    O                      = %s
    OU                     = %s
    CN                     = %s
    emailAddress           = %s
    
    [req_attributes]
    challengePassword      = %s
            """ % (bits, pem, output_password, C, ST, L, O, OU, CN, emailaddr, challengePassword)
        return key
    
    def make_key_config(self, bits, pem, OU, CN, emailaddr, C='XX', ST='WestLand', L='NeveLand', O='LICFACE', output_password='', challengePassword=''):
        """
        make_key_config(self, bits, pem, OU, CN, emailaddr, C='XX', ST='WestLand',
                        L='NeveLand', O='LICFACE', output_password='', challengePassword='')
    
        data = self.get_key(bits, pem, C, ST, L, O, OU, CN,
                            emailaddr, output_password, challengePassword)
    
            path = os.path.join(os.getenv('TEMP'), CN + "_temp.key")
            f = open(path, "w")
            f.write(data)
            f.close()
            return path
        """
        data = self.get_key(bits, pem, C, ST, L, O, OU, CN,
                            emailaddr, output_password, challengePassword)
        path = os.path.join(os.getenv('TEMP'), CN + "_temp.key")
        f = open(path, "w")
        f.write(data)
        f.close()
        return path

    def get_OU(self, host):
        d3 = ''
        if 'www.' in host:
            d1 = str(host).split('www')  # ['www', 'xxx.com']
            if len(d1) > 1:
                if "." in d1[1]:
                    d2 = str(d1[1]).split(".")  # ['xxx', 'com']
                    if len(d2[-1]) == 2 or len(d2[-1]) == 3:
                        for i in range(0, len(d2) - 1):
                            d3 = d3 + d2[i]
                    else:
                        for i in range(0, len(d2)):
                            d3 = d3 + d2[i]
                else:
                    return d1[1]
            else:
                return False
        else:
            if "." in host:
                d2 = str(host).split('.')  # ['xxx', 'com']
                if len(d2[-1]) == 2 or len(d2[-1]) == 3:
                    for i in range(0, len(d2) - 1):
                        d3 = d3 + d2[i]
                else:
                    for i in range(0, len(d2)):
                        d3 = d3 + d2[i]  # print "d3 =", d3
            else:
                return host
        return d3

    def get_email(self, host, mailaccount):
        d3 = ''
        if 'www.' in host:
            d1 = str(host).split('www') #['www', 'xxx.com']
            if len(d1) > 1:
                d3 = str(mailaccount) + '@' + d1[1]
            else:
                return False
        else:
            d3 = str(mailaccount) + '@' + host
        return d3

    def create_pem(self, key, crt=None):
        path = os.path.join(os.getenv('TEMP'), "nopassword.key")
        os.system("openssl rsa -in " + key + " -out " + path)
        pem = open(os.path.join(self.OPENSSL_PATH, self.host + ".pem"), 'wb')
        read_key = open(path, 'r').read()
        if crt == None or crt == '':
            crt = os.path.join(self.OPENSSL_PATH, self.host + ".crt")
        read_crt = open(crt, 'r').read()
        pem.write(read_key + read_crt)
        pem.close()
        return os.path.join(self.OPENSSL_PATH, self.host + ".pem")

    def maker(self, host, quiet = None):
        self.host = host
        path = self.OPENSSL_PATH
        if os.path.isfile(os.path.join(str(self.OPENSSL_PATH), self.host + ".crt")):
            print "\n"
            if quiet:
                confr = 'y'
            else:
                confr = raw_input(" File EXIST: (" + str(os.path.join(str(path),self.host + ".crt")) + "), Do you want to Overwrite file (y/n) ?: ")
                print "\n"
            if confr == 'y' or confr == "Y":
                DOU = self.get_OU(self.host)
                DMail = self.get_email(self.host, 'root')
                if DOU != False:
                    OU = self.get_OU(self.host)
                else:
                    raise SyntaxWarning('Error making key (OU) ....')
                if DMail != False:
                    Mail = self.get_email(self.host, 'root')
                else:
                    raise SyntaxWarning('Error making key (Mail) ....')
                cfgkey = self.make_key_config(2048, self.host, OU, self.host, Mail)
                os.system("{0} req -x509 -nodes -days 365 -newkey rsa:2048 -keyout {1}.key -out {2}.crt -config {3}".format(self.OPENSSL_APP, os.path.join(str(path), self.host), os.path.join(str(path), self.host), cfgkey))
                self.create_pem(os.path.join(str(path), self.host) + ".key", os.path.join(str(path), self.host) + ".crt")
                return True
            elif confr == 'n' or confr == 'N':
                pass
            else:
                print "\n"
                print " You Not select y/n (SKIPPED)!"
                return False
        else:
            DOU = self.get_OU(self.host)
            DMail = self.get_email(self.host, 'root')
            if DOU != False:
                OU = self.get_OU(self.host)
            else:
                raise SyntaxWarning('Error making key (OU) ....')
            if DMail != False:
                Mail = self.get_email(self.host, 'root')
            else:
                raise SyntaxWarning('Error making key (Mail) ....')
            cfgkey = self.make_key_config(2048, self.host, OU, self.host, Mail)
            os.system("{0} req -x509 -nodes -days 365 -newkey rsa:2048 -keyout {1}.key -out {2}.crt -config {3}".format(self.OPENSSL_APP, os.path.join(str(path), self.host), os.path.join(str(path), self.host), cfgkey))
            # os.system("openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout d:\WWW\SSLCertificateKeyFile\\" + self.host + ".key -out " + str(path) + self.host + ".crt")
            self.create_pem(os.path.join(str(path), self.host) + ".key", os.path.join(str(path), self.host) + ".crt")
            return True

    def usage(self):
        import argparse
        parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter)
        parser.add_argument('HOST', help='Hostname', action='store')
        parser.add_argument('-p', '--path', help='Path to store', action='store')
        parser.add_argument('-q', '--quite', help = 'Overwrite/No Question', action = 'store_true')
        if len(sys.argv) == 1:
            parser.print_help()
        else:
            args = parser.parse_args()
            self.host = args.HOST
            if args.path:
                self.OPENSSL_PATH = args.path
            self.maker(args.HOST, args.quite)

if __name__ == '__main__':
    c = keymaker()
    c.usage()