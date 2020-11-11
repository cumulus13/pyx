import sys
import os
import chardet

if len(sys.argv) > 1:
	if os.path.isfile(sys.argv[1]):
		f = open(sys.argv[1]).read()
		the_encoding = chardet.detect(f)['encoding']
		print the_encoding