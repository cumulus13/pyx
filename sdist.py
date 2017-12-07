import os
import sys
import configini
import optparse

__version__ = "1.0"
__test__ = "1.0"
__build__ = "win32"
__platform__ = "windows"
__author__ = "licface"
__url__ = "licface@yahoo.com"
__email__ = "licface@yahoo.com"
__sdk__ = "2.7"

class redistribute:
    def __init__(self, parent=None):
        self.configname = '.pypirc'
        self.f = os.path.join(os.getenv('USERPROFILE'), self.configname)
        self.check_level = True
        self.r_rrr = ''
        self.repolist = self.getRepository('distutils', 'index-servers', self.f)
        self.repolist.remove('pypi')
        self.repolist.remove('licface')
        self.repolist.remove('pyshop2')
        self.repolist.remove('pyshop3')
        self.level = 4
    
    def getRepository(self, option, value, fileconfig):
        data = configini.read_config4(option, value, self.f)
        return data
    
    def checkFile(self, path, paths, repository):
        check_i = []
        if os.path.isdir(os.path.join(os.path.abspath(path), 'dist')):
            for r, d, f in os.walk(path):
                for i in f:
                    if ".zip" in i:
                        check_i.append(True)
        if len(check_i) > 0:
            return False
        else:
            if repository in self.repolist:
                adir = os.path.split(paths)[0]
                print adir
                os.chdir(adir)
                os.system("c:\SDK\Anaconda2\python.exe" + " " + "setup.py" + " " + "register -r %s sdist upload -r %s" %(str(repository), str(repository)))
            else:
                main(True)
    
    def checkUrl(self, url):
        import urllib2
        request = urllib2.Request(url)
        request.get_method = lambda : 'HEAD'
        try:
            response = urllib2.urlopen(request)
            return True
        except:
            return False
    
    def checkUrl2(self, url):
        import mechanize
        br = mechanize.Browser()
        br.set_handle_redirect(False)
        try:
            br.open_novisit(url)
            print 'OK'
        except:
            print 'KO'
    
    def walk(self, path, repository, level=4, checklevel=False, overwrite=None):
        for r, d, f in os.walk(path):
            for i in f:
                if i == "setup.py":
                    rr =  os.path.join(path, r, i)
                    rrr = str(rr).split("\\")
                    self.r_rrr = rrr
                    if level == None:
                        level = 4
                    else:
                        level = level
                        
                    if len(rrr) == level:
                        if overwrite:
                            print "\n"
                            adir = os.path.split(rr)[0]
                            print "current directory =", adir
                            print "\n"
                            os.chdir(adir)
                            if repository in self.repolist:
                                os.system("c:\SDK\Anaconda2\python.exe" + " " + "setup.py" + " " + "register -r %s sdist upload -r %s" %(str(repository), str(repository)))
                            else:
                                self.main(True)
                        else:
                            spath = os.path.join(path, r)
                            self.checkFile(spath, rr, repository)
                    else:
                        self.level = level
        if checklevel:
            self.checkLevel()
        
    def checkLevel(self, allow_print=False):
        if not self.level == len(self.r_rrr):
            print "Please insert correct level directory\n"
            print "Current Level directory is", len(self.r_rrr)
            print "Current Level directory is =", self.r_rrr
            self.main(True)
        elif allow_print:
            print "Please insert correct level directory\n"
            print "Number Current Level directory is", len(self.r_rrr)
            print "Current Level directory is =", self.r_rrr
            self.main(True)
    
    def walkAll(self, path, repository, level=4, overwrite=None):
        if isinstance(repository, list):
            for i in repository:
                if i == '' or i == ' ' or i == None:
                    pass
                else:
                    self.walk(path, i, level, False, overwrite)
            self.checkLevel()
        else:
            self.walk(path, repository, level, False, overwrite)
            self.checkLevel()
    
    def print_usage_repository(self):
        print "\n"
        print "Repository Avalaible: "
        for i in self.getRepository('distutils', 'index-servers', self.f):
            if i == '' or i == None or i == ' ':
                pass
            else:
                print "  -", i, "     ", "(%s)" % (self.getRepository(str(i), 'repository', self.f)[0])
        print "\n"
    
    def main(self, print_usage=False):
        print "\n"
        parser = optparse.OptionParser()
        parser.add_option("-d", "--directory", help="Root directory contain Repositories", action="store")
        parser.add_option("-r", "--repository", help="Repository Name from .pypirc", action="store")
        parser.add_option("-l", "--level", help="Level deep of directory", action="store", type=int)
        parser.add_option("-o", "--overwrite", help="Overwrite, Pass Checking File", action="store_true")
        parser.add_option("-a", "--all", help="Using All of Name's Repository", action="store_true")
        options, args = parser.parse_args()
        if print_usage:
            return parser.print_help()
        elif len(sys.argv) == 1:
            parser.print_help()
            self.print_usage_repository()            
        else:
            if not options.directory == None:
                if os.path.isdir(options.directory):
                    pass
                else:
                    options.directory = os.getcwd()
            else:
                options.directory = os.getcwd()
                
            if options.level == None:
                self.level = 4
                options.level = 4
            else:
                self.level = options.level                        
                        
            if options.all:
                self.walkAll(options.directory, self.repolist, options.level, options.overwrite)
            else:
                self.walk(options.directory, options.repository, options.level, True, options.overwrite)

if __name__ ==  "__main__":   
    c = redistribute()
    c.main()


