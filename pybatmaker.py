#!c:\sdk\Anaconda2\python.exe
import os
import sys

# data = '@echo off\n"{0}" "{1}" %*'
ROOT_PATH = r'd:\TOOLS\pyx'
PYTHON_PATH = r"c:\sdk\Anaconda2\python.exe"
def maker(exe_path, python_path=None, root_path=None, filename=None):
	global ROOT_PATH
	global PYTHON_PATH
	if root_path:
		ROOT_PATH = root_path
	#if PYTHON_PATH and os.path.isfile(PYTHON_PATH):
		#python_path = PYTHON_PATH
	if not python_path:
		python_path = PYTHON_PATH
	if not python_path:
		env = os.getenv('PATH').split(";")
		for i in env:
			try:
				listdir = os.listdir(i)
			except:
				listdir = os.popen('dir /b "%s"'%(i)).readlines()
			for a in listdir:
				# print "os.path.split(a)[-1].split =", os.path.split(a)[-1].split("\n")[0]
				if os.path.split(a)[-1].split("\n")[0] == 'python.exe':
					# print "a =",a
					python_path = os.path.join(i, os.path.basename(os.path.split(a)[-1].split("\n")[0]))
					# print "python_path =",python_path
	if not python_path:
		python_path = raw_input('PYTHON BIN/EXE PATH: ')
	# print "PYTHON BIN =", python_path
	# print "EXE_PATH   =", exe_path
	data = '@echo off\nSET me1=%%CD%%\nCD /d "%s"\n"%s" "%s" %%*\nCD /d "%%me1%%"\nSET me1='%(os.path.dirname(os.path.abspath(exe_path)), python_path, os.path.abspath(exe_path))
	print "DATA =", data
	if not filename:
		filename = os.path.splitext(os.path.basename(exe_path))[0] + ".bat"
	f = open(os.path.join(ROOT_PATH, filename), 'wb')
	f.write(data)
	f.close()

def main():
	import argparse
	parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
	parser.add_argument('SCRIPT_PATH', help='Python Script Full Path')
	parser.add_argument('-p', '--python-path', action='store', help='Alternative Python bin/exe Path')
	parser.add_argument('-r', '--root-path', action='store', help='Where is script can save')
	parser.add_argument('-f', '--filename', action='store', help='Alternative file output name')
	if len(sys.argv) == 1:
		parser.print_help()
	else:
		args = parser.parse_args()
		maker(args.SCRIPT_PATH, args.python_path, args.root_path, args.filename)

if __name__ == '__main__':
	main()