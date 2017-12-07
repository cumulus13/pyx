import os
import sys
import optparse
import git
import datetime

GIT_PATH = r'c:\Apps\git\bin\git.exe'

class gitv(object):
	def __init__(self):
		super(gitv, self)

	def getnow(self):
		return datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S:%f')

	# def gitmain(self, path=None, gitsrv=None, name=None, username=None, password=None):
	# 	if path == None:
	# 		if os.path.exists(os.path.join(os.getcwd(), '.git')):
	# 			print "GIT REPO::", os.getcwd()
	# 			os.chdir(os.getcwd())
	# 		else:
	# 			return None
	# 	else:
	# 		if os.path.exists(os.path.join(path, '.git')):
	# 			print "GIT REPO::", path
	# 			os.chdir(path)
	# 		else:
	# 			return None
	# 		# os.chdir(path)

	# 	# print "gtisrv =", gitsrv

	# 	if gitsrv == None:
	# 		if username != None and Password != None:
	# 			gitsrv = '%s:%s@http://gitmain.net/git/' %(str(username), str(password))
	# 		else:
	# 			gitsrv = 'http://root:blackid@gitmain.net/git/'
	# 	else:
	# 		if username != None and Password != None:
	# 			gitsrv = '%s:%s@%s' %(str(username), str(password), str(gitsrv))
	# 		else:
	# 			gitsrv = 'http://root:blackid@%s/'%(gitsrv)


	# 	if name==None:	
	# 		os.system(GIT_PATH + ' push ' + gitsrv + os.path.basename(os.getcwd()) + ' master')
	# 		os.system(GIT_PATH + ' push ' + gitsrv + os.path.basename(os.getcwd()) + ' master --tag')
	# 	else:
	# 		os.system(GIT_PATH + ' push ' + gitsrv + name + ' master')
	# 		os.system(GIT_PATH + ' push ' + gitsrv + name + ' master --tag')

	# def gitmainMulti(self, path=None, gitsrv=None, name=None, username=None, password=None):
	# 	if path != None and "*" in path:
	# 		path = os.path.dirname(path)
	# 		if path == '':
	# 			path = os.getcwd()
	# 		path_1 = os.listdir(path)
	# 		path_2 = []
	# 		for i in path_1:
	# 			path_2.append(os.path.join(path, i))
	# 		for a in path_2:
	# 			if os.path.isdir(a):
	# 				self.gitmain(a, gitsrv, name, username, password)
	# 	else:
	# 		self.gitmain(path, gitsrv, name, username, password)

	# def getStatus(self, path):
	# 	list_changed = []
	# 	repo = git.repo(path)
	# 	commit = repo.head.commit
	# 	result = commit.diff(None)
	# 	for i in result:
	# 		list_changed.append(i.b_path)
	# 	return list_changed

	# def getUntracked(self, path):
	# 	repo = git.repo(path)
	# 	return repo.untracked_files
	
	def getCommitVersion(self):
		import traceback
		os.chdir(os.getcwd())
		sys.path.insert(0, os.getcwd())
		if os.path.isfile(os.path.join(os.getcwd(), '__init__.py')):
			try:
				import __init__
				version = "version: " + str(__init__.__version__) + "; test: " + str(__init__.__test__)
				tag = "v" + str(__init__.__version__) + "(t" + str(__init__.__test__) + ")"
				return version, tag
			except:
				try:
					import __init__
					version = "version: " + str(__init__.__VERSION__) + "; test: " + str(__init__.__TEST__)
					tag = "v" + str(__init__.__VERSION__) + "(t" + str(__init__.__TEST__) + ")"
					return version, tag
				except:
					print "NOT IMPLEMENT YET !"

	def commit(self):
		msg = self.getCommitVersion()
		os.system(GIT_PATH + ' commit -a -m \"' + msg[0] + '"')

	def tag(self):
		msg = self.getCommitVersion()
		os.system(GIT_PATH + ' tag  \"' + msg[1] + '"')

c = gitv()

def usage():
	# parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
	# parser = optparse.OptionParser()
	# parser.add_option('-p', '--path', help='(Optional) Path Git Workbeach, default is this directory', action='store')
	# parser.add_option('-u', '--name', help='(Optional) name of Git Workbeach, default is this directory name', action='store')
	# parser.add_option('-l', '--url', help='(Optional) Url of Git Server, default is "http://gitmain.net/git/[Git Workbeach]', action='store')
	# parser.add_option('-U', '--username', help='Username connect to git server',action='store')
	# parser.add_option('-P', '--password', help='Password connect to git server',action='store')
	# if len(sys.argv) > 1:
	# 	args, options = parser.parse_args()
	# 	if len(options) > 0:
	# 		if os.path.isdir(options[0]):
	# 			c.gitmainMulti(options[0])
	# 		elif "*" in options[0]:
	# 			c.gitmainMulti(options[0], args.url, args.name, args.username, args.password)
	# 	else:
	# 		c.gitmainMulti(args.path, args.url, args.name, args.username, args.password)
	# else:
	# 	parser.print_help()
	c.commit()
	c.tag()
	# print c.getCommitVersion()

if __name__ == '__main__':
	usage()
	# print c.getnow()