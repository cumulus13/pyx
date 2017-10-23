#!/usr/bin/python

import os
import sys
import optparse

GIT_PATH = r'c:\Apps\git\bin\git.exe'
REPO_PATH = r"f:\PROJECTS\REPOSITORY"

class gitp(object):
	def __init__(self):
		super(gitp, self)

	def gitmain(self, path=None, gitsrv=None, name=None, username=None, password=None):
		if path == None:
			os.chdir(REPO_PATH)
		else:
			os.chdir(path)

		if username != None and Password != None:
			gitsrv = '%s:%s@%s' %(str(username), str(password), str(gitsrv))
		
		if name==None:				
			os.system(GIT_PATH + ' clone ' + gitsrv)
		else:
			os.system(GIT_PATH + ' clone ' + gitsrv + ' ' + name)

c = gitp()

def usage():
	parser = optparse.OptionParser()
	parser.add_option('-p', '--path', help='(Optional) Path Git Workbeach, default is this directory', action='store')
	parser.add_option('-u', '--name', help='(Optional) name of Git Workbeach, default is this directory name', action='store')
	parser.add_option('-l', '--url', help='(Optional) Url of Git Server', action='store')
	parser.add_option('-U', '--username', help='Username connect to git server',action='store')
	parser.add_option('-P', '--password', help='Password connect to git server',action='store')
	if len(sys.argv) > 1:
		(args, options) = parser.parse_args()
		# print "ARGS =", args
		# print "OPTION =", options
		if len(options) > 0:
			if options[0].startswith('http') or options[0].startswith('https'):
				c.gitmain(None, options[0], args.name, args.username, args.password)
		else:	
			# args = parser.parse_args()
			c.gitmain(args.path, args.url, args.name, args.username, args.password)
	else:
		parser.print_help()

if __name__ == '__main__':
	usage()