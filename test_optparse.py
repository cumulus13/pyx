import optparse
import sys

parser = optparse.OptionParser()
parser.add_option('-t', '--test', nargs=2, help='just stest', action='store')

if len(sys.argv) ==1:
	parser.print_help()
else:
	args, options = parser.parse_args()
	print "args.test =", args.test[1]
