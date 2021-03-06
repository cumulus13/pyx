#!c:/SDK/Anaconda2/python.exe

import os
import sys
import argparse
import clipboard

GIT_PATH = r'x:\SCM\Git\bin\git.exe'
if not os.path.isfile(GIT_PATH):	
	GIT_PATH = 'git'
REPO_PATH = r"D:\PROJECTS"

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
		#print "gitsrv =", gitsrv
		#print "name =", name
		if name==None:				
			os.system(GIT_PATH + ' clone ' + gitsrv)
		else:
			os.system(GIT_PATH + ' clone ' + gitsrv + ' ' + name)

c = gitp()

def usage():
	global REPO_PATH
	parser = argparse.ArgumentParser(formatter_class = argparse.RawTextHelpFormatter)
	parser.add_argument('URL', help = 'URL clone to', action = 'store')
	parser.add_argument('-p', '--path', help='(Optional) Path Git Workbeach, default is this directory', action='store')
	parser.add_argument('-n', '--name', help='(Optional) name of Git Workbeach, default is this directory name', action='store')
	#parser.add_argument('-l', '--url', help='(Optional) Url of Git Server', action='store')
	parser.add_argument('-U', '--username', help='Username connect to git server',action='store')
	parser.add_argument('-P', '--password', help='Password connect to git server',action='store')
	if len(sys.argv) > 1:
		args = parser.parse_args()
		if args.URL == 'c':
			args.URL = clipboard.paste()
		#print "ARGS =", args
		#print "args.path =", args.path
		#print "OPTION =", options
		#if len(options) > 0:
			#if options[0].startswith('http') or options[0].startswith('https'):
				#c.gitmain(None, options[0], args.name, args.username, args.password)
		#else:	
			# args = parser.parse_args()
		# this = os.getcwd()
		# if args.path:
		# 	if not REPO_PATH:
		# 		REPO_PATH = os.getcwd()
		# 	os.chdir(REPO_PATH)
		c.gitmain(args.path, args.URL, args.name, args.username, args.password)
		# os.chdir(this)
	else:
		parser.print_help()

if __name__ == '__main__':
	usage()