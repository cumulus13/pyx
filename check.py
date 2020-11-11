from __future__ import print_function
import check_ansi
import sys
import argparse

parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('CHECKS', help='all of want to check', action='store', nargs='*')
if len(sys.argv) == 1:
	parser.print_help()
else:
	args = parser.parse_args()
	if 'ansi' in args.CHECKS:
		print("Is ANSI :", check_ansi.supports_color())
	else:
		parser.print_help()