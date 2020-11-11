#!/usr/bin/python
#!encoding: utf-8

import os
import sys
import optparse
import re
from debug import debug
from make_colors import make_colors

class gem(object):
    def __init__(self, url=None, path=None):
        super(gem, self)
        self.url = url
        self.path = path

    # def download(self, gems, url="http://127.0.0.1:50000", path=None, source='https://rubygems.org/', version=None):
    def download(self, gems_name, source='https://rubygems.org/', upload_to_geminbox=False, geminabox_server='127.0.0.1', geminabox_port='5000', version=None):
    	debug(print_function_parameters=True)
        print "downloading gem:", gems_name, "..."
        
        if version:
            g = os.popen("gem fetch %s -v '%s'--source %s" %(gems_name, version, source)).readlines()
        else:
            g = os.popen('gem fetch %s --source %s' %(gems_name, source)).readlines()
        debug(g=g)
        if len(g) > 0:
            d1 = re.split(" |\n", g[0])
          	debug(d1=d1)
          	if upload_to_geminbox:
	            if d1:
	                # print "PASS geminabox"
	                h = os.popen('gem inabox %s' %(str(d1) + ".gem -o")).readlines()
	                # print "H =", h
	                print h[0]
        else:
            print "No Gem name: %s" %(gems)

    def multidownload(self, gems_names, source='https://rubygems.org/', upload_to_geminbox=False, geminabox_server='127.0.0.1', geminabox_port='5000', version=None):
        if isinstance(gems, list):
            for i in gems_names:
                self.download(i, source, upload_to_geminbox, geminabox_server, geminabox_port, version)

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
