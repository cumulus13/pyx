#!/usr/bin/env python2

import argparse
import os
import sys
from make_colors import make_colors

SAVE_PATH = r"Y:\PYTHON_MODULES"

def download_source_py2(packages):
	CMD = "pip download -i https://pypi.python.org/simple -d {}2 --no-binary=:all: \"{}\"".format(SAVE_PATH, packages)
	packages = make_colors(packages, 'lr', 'lw')
	print(make_colors("Download Source for Python 2 [", 'lw', 'bl') + packages + make_colors("]", 'lw', 'bl') + " ...")
	os.system(CMD)

def download_source_py3(packages):
	CMD = "pip3 download -i https://pypi.python.org/simple -d {}2 --no-binary=:all: \"{}\"".format(SAVE_PATH, packages)
	packages = make_colors(packages, 'lr', 'lw')
	print(make_colors("Download Source for Python 3 [", 'lw', 'bl') + packages + make_colors("]", 'lw', 'bl') + " ...")
	os.system(CMD)

def download_binary_py2(packages):
	CMD = "pip download -i https://pypi.python.org/simple -d {} --only-binary=:all: \"{}\"".format(SAVE_PATH, packages)
	packages = make_colors(packages, 'lr', 'lw')
	print(make_colors("Download Binary for Python 2 [", 'lw', 'bl') + packages + make_colors("]", 'lw', 'bl') + " ...")
	os.system(CMD)

def download_binary_py3(packages):
	CMD = "pip3 download -i https://pypi.python.org/simple -d {} --only-binary=:all: \"{}\"".format(SAVE_PATH, packages)
	packages = make_colors(packages, 'lr', 'lw')
	print(make_colors("Download Binary for Python 3 [", 'lw', 'bl') + packages + make_colors("]", 'lw', 'bl') + " ...")
	os.system(CMD)

def download_all(packages):
	packages_str = make_colors(packages, 'lr', 'lw')
	print(make_colors("Download Source and Binary for All [{0}] ...".format(packages_str), 'lw', 'lr'))
	download_binary_py3(packages)
	download_binary_py2(packages)
	download_source_py3(packages)
	download_source_py2(packages)

def usage():
	parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
	parser.add_argument('-2', '--py2', action='store_true', help='Download Binary and Source for python 2 only')
	parser.add_argument('-2b', '--py2b', action='store_true', help='Download Binary for python 2 only')
	parser.add_argument('-2s', '--py2s', action='store_true', help='Download Source for python 2 only')
	parser.add_argument('-3', '--py3', action='store_true', help='Download Binary and Source for python 3 only')
	parser.add_argument('-3b', '--py3b', action='store_true', help='Download Binary for python 3 only')
	parser.add_argument('-3s', '--py3s', action='store_true', help='Download Source for python 3 only')
	parser.add_argument('-a', '--all', action='store_true', help='Download all Source and Binary for all')
	parser.add_argument('PACKAGES', action='store', help='Package/Module Name', nargs='*')
	if len(sys.argv) == 1:
		parser.print_help()
	else:
		PARSER = False
		ALL = ['--py3s', '-a', '--py2b', '-3b', '-3s', '-h', '--py2', '-2s', '--py2s', '-3', '-2', '--py3b', '--py3', '--help', '-2b', '--all']
		for i in sys.argv[1:]:
			if i in ALL:
				PARSER = True
		if PARSER:
			args = parser.parse_args()
			# print("dir(args) =", dir(args))
			# print("dir(parser) =", dir(parser))
			# print(parser._option_string_actions.keys())
			# sys.exit()
			packages = " ".join(args.PACKAGES)
			if args.all:
				download_all(packages)
			else:
				if args.py2:
					download_binary_py2(packages)
					download_source_py2(packages)
				elif args.py2b:
					download_binary_py2(packages)
				elif args.py2s:
					download_source_py2(packages)

				if args.py3:
					download_binary_py3(packages)
					download_source_py3(packages)
				elif args.py3b:
					download_binary_py3(packages)
				elif args.py3s:
					download_source_py3(packages)
		else:
			packages = " ".join(sys.argv[1:])
			download_all(packages)


if __name__ == '__main__':
	usage()

