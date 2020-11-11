#!c:/SDK/Anaconda2/python.exe
import sys
import os
import argparse
from make_colors import make_colors
from pydebugger.debug import debug
import clipboard

def usage():
	app = r"c:\Apps\monolith\monolith.exe"
	parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
	parser.add_argument('URLS', action='store', help='Any Url, can be multiply', nargs='*') 
	parser.add_argument('-p', '--output-dirs', action='store', help='Save output to dir')
	parser.add_argument('-n', '--output-name', action='store', help='Save as to name')
	if len(sys.argv) == 1:
		parser.print_help()
	else:
		args = parser.parse_args()
		if args.URLS == ['c']:
			args.URLS = [clipboard.paste()]
		
		for i in args.URLS:
			if 'google.com' in i:
				import guc
				i = guc.convert(i)
			if args.output_name:
				name = args.output_name
			else:
				name = os.path.split(i)[-1]
			debug(name = name)
			if not name:
				name = os.path.split(i)[-2]
				debug(name = name)
			if not os.path.splitext(name) == '.html' or not os.path.splitext(name) == '.htm':
				name = name + ".html"
				debug(name = name)
			if not len(name) > 5:
				debug(i = i)
				name = os.path.basename(i)
				debug(name = name)
				if "/" == name[:-1]:
					name = name[:-1]
				name = os.path.join(args.output_dirs, name)
				debug(name = name)
					
			if args.output_dirs:
				if args.output_dirs[-1] == ":":
					args.output_dirs = args.output_dirs + "\\"
				
				name = os.path.join(args.output_dirs, os.path.basename(name))
			print(make_colors("Save as:", 'lw','bl') + make_colors(name, 'b','ly'))
			os.system(app + " " + i + " -o " + name)
		
if __name__ == '__main__':
	usage()