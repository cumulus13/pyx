#!c:/SDK/Anaconda2/python.exe
import os
import sys
import argparse

ROOT_PATH = r'd:\TOOLS\pyx'

def maker(path, root_path=None):
	if not root_path:
		root_path = ROOT_PATH
	file_name = os.path.basename(path)
	#print "file_name =", file_name
	file_name, file_ext = os.path.splitext(file_name)
	#print "file_name =", file_name
	file_create = open(os.path.join(root_path, file_name) + ".bat", 'wb')
	#print "file_create =", file_create
	string_create = """@echo off\n"%s" %%*"""%(os.path.abspath(path))
	file_create.write(string_create)
	file_create.close()


def usage():
	import argparse
	parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
	parser.add_argument('FILE', action='store', help='Original File, it can be multiply separated by space', nargs='*')
	parser.add_argument('-p', '--path', action='store', help='Option to save bat file, default is "{0}"'.format(ROOT_PATH))
	if len(sys.argv) == 1:
		parser.print_help()
	else:
		args = parser.parse_args()
		for i in args.FILE:
			maker(i, args.path)
	
if __name__ == '__main__':
	usage()