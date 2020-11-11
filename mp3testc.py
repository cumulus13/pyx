from __future__ import print_function
import os, sys
process = 'd:\\TOOLS\\exe\\mp3test.exe {0} "{1}"'
path = None
args = []
if len(sys.argv) > 1:
	for i in sys.argv[1:]:
		print("i =", i)
		if os.path.isdir(i):
			path = i
		else:
			args.append(i)
		
if not path:
	path = os.getcwd()

if args:
	os.system(process.format(" ".join(args), path))
else:
	os.system(process.format(" -rq ", path))

