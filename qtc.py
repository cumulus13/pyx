import os
import sys

def usage():
	import argparse
	parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter)
	parser.add_argument('VERSION', help='Please definition version of Qt (4/5)', action='store')
	if len(sys.argv) == 1:
		parser.print_help()
	else:
		args = parser.parse_args()
		if args.VERSION:
			if args.VERSION == '4':
				os.environ.update({'PATH': r'C:\Qt\4.8.6\bin;c:\mingw32\4.9.2\bin;%SystemRoot%\System32'})
				os.environ.update({'QTDIR': r'C:\Qt\4.8.6'})
				os.environ.update({'QMAKESPEC': 'win32-g++-4.6'})
			elif args.VERSION == '5':
				os.environ.update({'PATH': r'C:\Qt\Qt5.5.0\5.5\mingw492_32\bin;C:\Qt\Qt5.5.0\Tools\mingw492_32\bin;'})
			else:
				parser.print_help()

		os.system('qmake -project')
		os.system('qmake')
		os.system('mingw32-make')

		if args.VERSION == '4':
			for root, dirs, files in os.walk(os.path.join(os.getcwd(), 'debug')):
				if len(files) > 0:
					for i in files:
						if i.endswith('.exe'):
							os.system(os.path.join(root,i))
		elif args.VERSION == '5':
			for root, dirs, files in os.walk(os.path.join(os.getcwd(), 'release')):
				if len(files) > 0:
					for i in files:
						if i.endswith('.exe'):
							os.system(os.path.join(root,i))

if __name__ == '__main__':
	usage()
