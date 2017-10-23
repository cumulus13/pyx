import os
import sys
import diffmov
from pysvn import *
import urlparse

SVN_PATH = r'c:\Apps\svn-win32-1.8.5\bin\svn.exe'
filename = os.path.basename(sys.argv[0])

def svndownload(url, name=None):
	if '.googlecode.com' in urlparse.urlparse(url).netloc:
		fname_1 = str(urlparse.urlparse(url).netloc).split('.googlecode.com')
		fname = fname_1[0]
	else:
		fname = os.path.basename(url)
		if fname == '':
			fname = url
	print "Repository From Name   :", fname
	if name == None:
		name = fname
		print "Repository Name        :", name
	else:
		print "Repository Name        :", name
	print "Repository url         :", url
	os.chdir(r'd:\PROJECT_DOWNLOADs\svn')
	if os.path.isdir(os.path.join(r'd:\PROJECT_DOWNLOADs\svn', name)):
		listdir = os.listdir(os.path.join(r'd:\PROJECT_DOWNLOADs\svn', name))
		repo =  Client(os.path.join(r'd:\PROJECT_DOWNLOADs\svn', name))
		remotes_url = repo.root_url_from_path(r'd:\PROJECT_DOWNLOADs\svn', name)
		print "FOUND: Remotes Url   :",  remotes_url
		q1 = raw_input("Repository is Exists !, Do you want to overwrite/re-clone it ? (y[es]/n[o]/r[ename]): ")
		if not '.svn' in listdir:
			print "FOUND: Bare Repository !"
			q2 = raw_input("Do you want to continue ?(y[es]/n[o])")
			if q2.strip() == 'y' or q2.strip() == 'yes':
				pass
			elif q2.strip() == 'n' or q2.strip() == 'no':
				os._exit(0)
		if str(q1).strip() == 'y' or str(q1).strip() == 'yes':
			main = diffmov.DifficultRemove()
			main.Remove(os.path.join(r'd:\PROJECT_DOWNLOADs\svn', name))
		elif str(q1).strip() == 'n' or str(q1).strip() == 'no':
			return None
		elif str(q1).strip() == 'r' or str(q1).strip() == 'rename':
			q2 =  raw_input("Please insert new name local repo: ")
			name =  q2
			print "\n"
		else:
			return None		
		
	if name == None:
		os.system(SVN_PATH + " checkout " + url)
	else:
		os.system(SVN_PATH + " checkout " + url + " " + name)


if __name__ == "__main__":
	try:
		if len(sys.argv) > 1:
			if len(sys.argv) == 3:
				svndownload(sys.argv[1], sys.argv[2])
			else:
				svndownload(sys.argv[1])
		else:
			print "\n"
			print "Usage:", filename, " [url/link pf svn] [name_of_destination_repo (default basename of url)]" 
	except:
		pass