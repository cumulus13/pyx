import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--test', nargs=2, help='just stest', action='store')

if len(sys.argv) ==1:
	parser.print_help()
else:
	args = parser.parse_args()
	print "args.test =", args.test[1]


