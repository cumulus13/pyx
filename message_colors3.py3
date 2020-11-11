from make_colors import make_colors
import argparse
import sys
import os

def colored(message, foreground='white', background='black'):
	if 'error' in str(message).lower():
		foreground='white'
		background='lighred'
	elif 'warning' in str(message).lower():
		foreground='black'
		background='lighyellow'
	elif 'notice' in str(message).lower():
		foreground='black'
		background='lighcyan'
	elif 'alert' in str(message).lower():
		foreground='black'
		background='lighgreen'
	elif 'emergency' in str(message).lower():
		foreground='white'
		background='lighmagenta'
	elif 'debug' in str(message).lower():
		foreground='white'
		background='lighblue'

	return make_colors(message, foreground, background)

def usage():
	parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
	parser.add_argument('MESSAGE', action='store', help='Message coloring to')
	parser.add_argument('-f', '--foreground', action='store', help='Foreground Color, default:white', default='white')
	parser.add_argument('-b', '--background', action='store', help='Background Color, default:black', default='black')

	if len(sys.argv) == 2:
		colored(sys.argv[1])
	else:
		args = parser.parse_args()
		colored(args.MESSAGE, args.foreground, args.background)

if __name__ == '__main__':
	# usage()
	# unbuffered_stdin = os.fdopen(sys.stdin.fileno(), 'rb', buffering=0)
	# colored(unbuffered_stdin)
	# colored(sys.stdin.readline())
	# newin = os.fdopen(sys.stdin.fileno(), 'r', 100)
	# colored(newin)
	colored(sys.stdin)