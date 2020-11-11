#/usr/bin/env python3
from __future__ import print_function
import sys
from github import Github
from make_colors import make_colors
import os

def auth(token='f8e5b4d71566c10e9ae1780853b453e97f9862ee'):
	return Github(token).get_user()

def clone(repo):
	r = None
	try:
		r = auth().get_repo(repo)
	except:
		print(make_colors("No Repo {} Found !".format(repo), 'lw', 'lr'))
		sys.exit()
	if r:
		clone_url = r.clone_url
		os.system("git clone " + clone_url)


if __name__ == '__main__':
	if 'clone' in sys.argv[1:]:
		clone(sys.argv[2])
	else:
		print("Usage: gh clone REPO_NAME")
