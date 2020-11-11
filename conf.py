#!c:/SDK/Anaconda2/python.exe

from __future__ import print_function
import sys
import os
from configset import configset
from make_colors import make_colors
from pydebugger.debug import debug
import clipboard

def get(configfile, section=None, option=None, all=False):
	debug(ALL0 = all)
	debug(section = section)
	debug(option = option)
	debug(configfile = configfile)
	config = configset(configfile)
	d = None
	if section and option:
		d = config.get_config(section, option)
		debug(d = d)
	if d:
		clipboard.copy(d)
	if all:
		sections = config.sections()
		#print("sections =", sections)
		for i in sections:
			print(make_colors("[" + str(i) + "]", 'lw', 'bl'))
			options = config.options(i)
			for o in options:
				print(' ' * 4 + make_colors(str(o), 'b', 'ly') + "=" + make_colors(config.get(i, o), 'b', 'lg'))
	
	print ("\n")
	if d:
		print(make_colors("Config FOUND !, copy to clipboard !", 'lw', 'bl'))
		#clipboard.copy(d)
	else:
		if section and option:
			print(make_colors("Config Not FOUND !", 'lw', 'lr'))
		
	return d
	
def usage():
	import argparse
	print("\n")
	help = """FILE_CONFIG SECTION OPTION -a/--all
	
positional arguments:
  FILE        Config File Path
  SECTION     Section Name
  OPTION      Options Name
  
  if arguments not align, SECTION Must be the First !
"""
	SECTION = None
	OPTION = None
	ALL = False
	parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter, usage=help)
	parser.add_argument('-a', '--all', help='Print All Config', action='store_true')
	debug(LEN_ARGV = len(sys.argv))
	if len(sys.argv) <= 2:
		parser.print_help()
		sys.exit()
	if len(sys.argv) < 4:
		parser.add_argument("FILE", help='Config File Path', action='store')
	elif len(sys.argv) > 3:
		opts = sys.argv[1:]
		debug(opts = opts)
		for i in opts:
			if "-a" in opts:
				opts.remove('-a')
				ALL = True
			elif "-h" in opts:
				opts.remove('-h')
			elif '--all' in opts:
				ALL = True
				opts.remove('--all')
			elif '--help' in opts:
				opts.remove('--help')
		debug(opts = opts)
		for i in opts:
			debug(i = i)
			if os.path.exists(i) and os.path.isfile(i):
				debug(is_file = i)
				index = opts.index(i)
				opts.remove(i)
				opts.insert(index, "file")
				break
		debug(opts = opts)
		for i in opts:
			if i == "file":
				pass
			else:
				index_i = opts.index(i)
				opts.remove(opts[index_i])
				opts.insert(index_i, "section")
				break
		debug(opts = opts)
		for i in opts:
			if i == "file":
				parser.add_argument("FILE", help='Config File Path', action='store')
			elif i == "section":
				parser.add_argument('SECTION', help='Option Name', action='store')
			else:
				parser.add_argument('OPTION', help='Option Name', action='store')
		debug(opts = opts)
		args = parser.parse_args()
		
		SECTION = args.SECTION
		OPTION = args.OPTION
		debug(SECTION = args.SECTION)
		debug(OPTION = args.OPTION)
	args = parser.parse_args()
	debug(FILE = args.FILE)
	debug(ALL = args.all)
	if not args.all and ALL:
		args.all = True
	get(args.FILE, SECTION, OPTION, args.all)

if __name__ == '__main__':
	usage()
	