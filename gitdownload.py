import os
import sys
import diffmov
from git import * 

GIT_PATH = r'c:\Git\bin\git.exe'
filename = os.path.basename(sys.argv[0])

def gitdownload(url, name=None):
	fname = os.path.basename(url)
	print "Repository From Name   :", fname
	if name == None:
		name = fname
		print "Repository Name        :", name
	else:
		print "Repository Name        :", name
	print "Repository url         :", url
	os.chdir(r'd:\PROJECT_DOWNLOADs\git')
	if os.path.isdir(os.path.join(r'd:\PROJECT_DOWNLOADs\git', name)):
		repo =  Repo(os.path.join(r'd:\PROJECT_DOWNLOADs\git', name), odbt=GitCmdObjectDB)
		origin = repo.remotes.origin
		remotes_url = origin.url
		print "FOUND: Remotes Url   :",  remotes_url
		q1 = raw_input("Repository is Exists !, Do you want to overwrite/re-clone it ? (y[es]/n[o]/r[ename]): ")
		if repo.bare:
			print "FOUND: Bare Repository !"
		if str(q1).strip() == 'y' or str(q1).strip() == 'yes':
			main = diffmov.DifficultRemove()
			main.Remove(os.path.join(r'd:\PROJECT_DOWNLOADs\git', name))
		elif str(q1).strip() == 'n' or str(q1).strip() == 'no':
			return None
		elif str(q1).strip() == 'r' or str(q1).strip() == 'rename':
			q2 =  raw_input("Please insert new name local repo: ")
			name =  q2
			print "\n"
		else:
			return None		
		
	if name == None:
		os.system(GIT_PATH + " clone " + url)
	else:
		os.system(GIT_PATH + " clone " + url + " " + name)


if __name__ == "__main__":
	try:
		if len(sys.argv) > 1:
			if len(sys.argv) == 3:
				gitdownload(sys.argv[1], sys.argv[2])
			else:
				gitdownload(sys.argv[1])
		else:
			print "\n"
			print "Usage:", filename, " [url/link pf git] [name_of_destination_repo (default basename of url)]" 
	except:
		pass