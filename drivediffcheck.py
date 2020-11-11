#!c:/SDK/Anaconda2/python.exe
from __future__ import print_function
from make_colors import make_colors
from pydebugger.debug import debug
from clint.textui import progress
import sys, os

def check(path1, path2):
	d = 2
	if not os.path.isdir(path1):
		print(make_colors('PATH1 is not Directory !', 'white','red'))
	if not os.path.isdir(path2):
		print(make_colors('PATH2 is not Directory !', 'white','red'))
	for i in range(1, len(path2)):
		if len(path2) / i == 100:
			d = i
			break
	list_path1 = os.listdir(path1)
	list_path2 = os.listdir(path2)
	bar = progress.Bar(expected_size=100, label="start checking ")
	#bar1 = progress.Bar(expected_size=100, label="start checking ")
	n = 1
	for i in list_path1:
		label = make_colors('checking', 'black','green') + " " + make_colors(str(i), 'green') + " "
		bar.label = label
		bar.show(50)
		#print(label)
		matched = False
		for x in list_path2:
			#if str(os.path.basename(i)) in str(os.path.abspath(x)) or str(os.path.basename(i)) == str(os.path.basename(x)):
			if str(os.path.basename(i)) == str(os.path.basename(x)):
				bar.show(100)
				n = 1
				label = make_colors(make_colors('[MATCHED]', 'red','white')) + ": " + make_colors(str(i), 'yellow') + " "
				bar.label = label
				print(label)
				matched = True
				break
			if n == 100:
				n = 1
			else:
				bar.show(n)
			n += 1
		if not matched:
			bar.show(100)
			n = 1
			label = make_colors(make_colors('[NO MATCHED]', 'white','red')) + ": " + make_colors(str(i), 'cyan') + " "
			bar.label = label
			print(label)
		bar.show(100)
		n = 1
		
	label = make_colors(make_colors('[FINISHED]', 'red','yellow')) + " "
	bar.label = label
	bar.show(100)
				
def usage():
	if len(sys.argv) == 3:
		check(sys.argv[1], sys.argv[2])
	else:
		help_str = make_colors('USAGE:', 'blue') + " " + make_colors(os.path.basename(__file__), 'magenta') + " " + make_colors('PATH1 PATH2', 'green')
		print(help_str)
		
def test():
	for i in range(1, 200):
		if 200 / i == 100:
			print("i =", i)
			break
	print("TEST")
if __name__ == '__main__':
	usage()
	#test()