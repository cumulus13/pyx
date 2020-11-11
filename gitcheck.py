from __future__ import print_function
import os
import sys
from git import Repo
import argparse
from make_colors import make_colors
import cmdw
import textwrap

class gitcheck(object):
	def __init__(self):
		super(gitcheck, self)

	def check_git_dirs(self, path):
		lists = []
		lists1 = []
		if not os.path.isdir(path):
			return False
		lists_temp = os.listdir(path)		
		for i in lists_temp:
			lists1.append(os.path.join(path, i))
		for i in lists1:
			if os.path.isdir(os.path.join(path, i, '.git')):
				lists.append(i)
		return lists

	def check_changes(self, path):
		lists = self.check_git_dirs(path)
		# print "lists =", lists
		lists_changes = []
		for i in lists:
			try:
				repo = Repo(i)
				if repo.is_dirty() or repo.untracked_files:
					lists_changes.append(i)
			except:
				pass
		return lists_changes

	def get_untrackers(self, repo):
		rp = Repo(repo)
		untrackers = rp.untracked_files
		return untrackers

	def set_untrackers(self, prefix, untrackers, width=None):
		if not width:
			width = cmdw.getWidth() - (len(prefix) + 5)
		initial_indent = prefix
		subsequent_indent = ' '*len(prefix)
		wrapper = textwrap.TextWrapper(initial_indent=initial_indent, width=width, subsequent_indent=subsequent_indent)
		return wrapper.fill(str(untrackers))

	def show_changes_dirs(self, path, show_untrakers=False):
		untrackers = ''
		lists_changes = self.check_changes(path)
		for i in lists_changes:
			if show_untrakers:
				untrackers = self.get_untrackers(i)
				if not untrackers:
					untrackers = ''
			if len(str(lists_changes.index(i) + 1)) == 1:
				if untrackers:
					untrackers = self.set_untrackers(prefix, untrackers)
				prefix = len("00" + str(lists_changes.index(i) + 1) + ". ") * ' '
				print("00" + str(lists_changes.index(i) + 1) + ". " + make_colors(os.path.dirname(i), 'lightmagenta') + make_colors("\\", 'lightyellow') + make_colors(os.path.basename(i), 'lightcyan'))
				if show_untrakers:
					print(make_colors(untrackers, 'lightred'))
			elif len(str(lists_changes.index(i) + 1)) == 2:
				if untrackers:
					untrackers = self.set_untrackers(prefix, untrackers)
				prefix = len("0" + str(lists_changes.index(i) + 1) + ". ") * ' '
				print("0" + str(lists_changes.index(i) + 1) + ". " + make_colors(os.path.dirname(i), 'lightmagenta') + make_colors("\\", 'lightyellow') + make_colors(os.path.basename(i), 'lightcyan'))
				if show_untrakers:
					print(make_colors(untrackers, 'lightred'))
			else:
				if untrackers:
					untrackers = self.set_untrackers(prefix, untrackers)
				prefix = len(str(lists_changes.index(i) + 1) + ". ") * ' '
				print(str(lists_changes.index(i) + 1) + ". " + make_colors(os.path.dirname(i), 'lightmagenta') + make_colors("\\", 'lightyellow') + make_colors(os.path.basename(i), 'lightcyan'))
				if show_untrakers:
					print(make_colors(untrackers, 'lightred'))

	def usage(self):
		parser = argparse.ArgumentParser(formatter_class= argparse.RawTextHelpFormatter)
		parser.add_argument('PATH', action='store', help='Path Containts (many) Git Repositories')
		parser.add_argument('-t', '--untrackers', action='store_true', help='Show untracker files')
		if len(sys.argv) == 1:
			parser.print_help()
			self.show_changes_dirs(os.getcwd())
		else:
			args = parser.parse_args()
			self.show_changes_dirs(args.PATH, args.untrackers)


if __name__ == '__main__':
	c = gitcheck()
	c.usage()
	# lists = c.check_changes(sys.argv[1])
	# if lists:
	# 	for i in lists:
	# 		print str(lists.index(i) + 1) + ". " + str(i)
