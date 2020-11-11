from make_colors import make_colors
import argparse
import sys
import os

def colored(message, foreground='white', background='black'):
	# print "message 0 =", message
	if 'error' in str(message).lower():
		foreground='white'
		background='lightred'
	elif 'warning' in str(message).lower():
		foreground='black'
		background='lightyellow'
	elif 'notice' in str(message).lower():
		foreground='black'
		background='lightcyan'
	elif 'alert' in str(message).lower():
		foreground='black'
		background='lightgreen'
	elif 'emergency' in str(message).lower():
		foreground='white'
		background='lightmagenta'
	elif 'debug' in str(message).lower():
		foreground='white'
		background='lightblue'
	# print "foreground =", foreground
	# print "background =", background
	# data = make_colors(message, foreground, background)
	# return data
	# print "data =", data
	return make_colors(message, foreground, background)

def usage():
	parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
	parser.add_argument('MESSAGE', action='store', help='Message coloring to')
	parser.add_argument('-f', '--foreground', action='store', help='Foreground Color, default:white', default='white')
	parser.add_argument('-b', '--background', action='store', help='Background Color, default:black', default='black')

	if len(sys.argv) == 2:
		# print "message =", sys.argv[1]
		print colored(sys.argv[1])
	else:
		args = parser.parse_args()
		data = colored(args.MESSAGE, args.foreground, args.background)
		# print "data usage =", data

if __name__ == '__main__':
	# usage()
	# unbuffered_stdin = os.fdopen(sys.stdin.fileno(), 'rb', buffering=0)
	# colored(unbuffered_stdin)
	# print colored(sys.stdin.readlines())
	# newin = os.fdopen(sys.stdin.fileno(), 'r', 100)
	# colored(newin)
	# colored(sys.stdin.fileno())
	for line in sys.stdin.readlines():
	    print colored(line.split("\n")[0])