#!/usr/bin/python

import os
import sys
import optparse
import re

class gem(object):
    def __init__(self, url=None, path=None):
        super(gem, self)
        self.url = url
        self.path = path

    def download(self, gems, url="http://127.0.0.1:50000", path=None, source='https://rubygems.org/', version=None):
        if url==None:
            url="http://127.0.0.1:50000"
        print "downloading gem:", gems, "..."
        # if path == None:
        # 	if self.path != None:
        # 		path = self.path
        # 	else:
        # 		return SyntaxError('Path Not Definition !')
        # if self.url != None:
        # 	url = self.url
        if version:
            g = os.popen("gem fetch %s -v '%s'--source %s" %(gems, version, source)).readlines()
        else:
            g = os.popen('gem fetch %s --source %s' %(gems, source)).readlines()
        # print "G =", g
        # d = ['Downloaded ruby-growl-4.1\n']
        # print g[0]
        if len(g) > 0:
            d1 = re.split(" |\n", g[0])
            # print "d1 =", d1[1]
            if d1:
                # print "PASS geminabox"
                h = os.popen('gem inabox %s' %(str(d1) + ".gem -o")).readlines()
                # print "H =", h
                print h[0]
        else:
            print "No Gem name: %s" %(gems)

    def multidownload(self, gems, path, source, repo = None, version=None):
        if isinstance(gems, list):
            for i in gems:
                if repo:
                    if isinstance(repo, list):
                        for r in repo:
                            self.download(i, r, path, source, version)
                    else:
                        self.download(i, repo, path, source, version)                    
                else:
                    self.download(i, path=path, source=source, version=version)

    def cb(self, option, opt_str, value, parser):
        args=[]
        for arg in parser.rargs:
            if arg[0] != "-":
                args.append(arg)
            else:
                del parser.rargs[:len(args)]
                break
        if getattr(parser.values, option.dest):
            args.extend(getattr(parser.values, option.dest))
        setattr(parser.values, option.dest, args)

    def usage(self):
        def vararg_callback(option, opt_str, value, parser):
            value = []
            for arg in parser.rargs:
                # stop on --foo like options
                if arg[:2] == "--" and len(arg) > 2:
                    break
                # stop on -a (ignore the floats issue)
                if arg[:1] == "-" and len(arg) > 1:
                    break
                value.append(arg)
            del parser.rargs[:len(value)]
            setattr(parser.values, option.dest, value)        

        def arg_list(option, opt_str, value, parser):
            args = set()
            for arg in parser.rargs:
                if arg[0] == '-':
                    break
                args.add(arg)
                parser.rargs.pop(0)
            setattr(parser.values, option.dest, args)

        usage = "gemd gem1 gem2 gem3 [path_to_save_its or -p]"
        parser = optparse.OptionParser(usage=usage)
        parser.add_option('-p', '--path', help='Path download to, default configuration', action='store')
        parser.add_option('-s', '--source', help='Source gem server default="http://rubygems.org/"', action='store', default="http://rubygems.org/")
        parser.add_option('-r', '--repo', help='Repository geminabox url', action='callback', callback= vararg_callback, dest = 'repo', default = 'http://127.0.0.1:50000')
        parser.add_option('-v', '--version', help='Version of Gems', action='store')
        options, args = parser.parse_args()
        print "options =", options
        print "args =", args
        print "args.repo =",options.repo        
        if len(sys.argv) == 1:
            parser.print_help()
        else:
            if len(args) > 0:
                if os.path.isdir(args[-1]):
                    if options.path:
                        path = options.path
                    else:
                        path = args[-1]
                    args = args[:-1]
                else:
                    path = options.path
                if path == None or path == '':
                    path = os.getcwd()
                os.chdir(path)			
                self.multidownload(args, path, options.source, options.repo, options.version)

            # print "options =", options
            # print "args    =", args


if __name__ == '__main__':
    c = gem()
    # c.download(sys.argv[1])
    c.usage()
