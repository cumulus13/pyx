import os
import sys
import diffmov
import hgapi

HG_PATH = r'C:\Progra~1\Mercurial\hg.exe'
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
	os.chdir(r'd:\PROJECT_DOWNLOADs\hg')
	if os.path.isdir(os.path.join(r'd:\PROJECT_DOWNLOADs\hg', name)):
		listdir = os.listdir(os.path.join(r'd:\PROJECT_DOWNLOADs\svn', name))
		repo =  hginit.Repo(os.path.join(r'd:\PROJECT_DOWNLOADs\hg', name))
		try:
			conf = repo.read_config()['paths']
			remotes_url = str(conf['default'])
		except:
			remotes_url = ''
		print "FOUND: Remotes Url   :",  remotes_url
		q1 = raw_input("Repository is Exists !, Do you want to overwrite/re-clone it ? (y[es]/n[o]/r[ename]): ")
		if repo.bare:
			print "FOUND: Bare Repository !"
			q2 = raw_input("Do you want to continue ?(y[es]/n[o])")
			if q2.strip() == 'y' or q2.strip() == 'yes':
				pass
			elif q2.strip() == 'n' or q2.strip() == 'no':
				os._exit(0)			
		if str(q1).strip() == 'y' or str(q1).strip() == 'yes':
			main = diffmov.DifficultRemove()
			main.Remove(os.path.join(r'd:\PROJECT_DOWNLOADs\hg', name))
		elif str(q1).strip() == 'n' or str(q1).strip() == 'no':
			return None
		elif str(q1).strip() == 'r' or str(q1).strip() == 'rename':
			q2 =  raw_input("Please insert new name local repo: ")
			name =  q2
			print "\n"
		else:
			return None		
		
	if name == None:
		os.system(HG_PATH + " clone " + url)
	else:
		os.system(HG_PATH + " clone " + url + " " + name)


if __name__ == "__main__":
	try:
		if len(sys.argv) > 1:
			if len(sys.argv) == 3:
				gitdownload(sys.argv[1], sys.argv[2])
			else:
				gitdownload(sys.argv[1])
		else:
			print "\n"
			print "Usage:", filename, " [url/link pf hg] [name_of_destination_repo (default basename of url)]" 
	except:
		pass