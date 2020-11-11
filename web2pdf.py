#!/usr/bin/env python2
from __future__ import print_function

import pdfkit
import argparse
import sys
from datetime import datetime
import os
from make_colors import make_colors
import clipboard
from pydebugger.debug import debug
if sys.version_info.major == 3:
	from urllib.parse import unquote, quote
else:
	from urllib import unquote, quote

def convert(url, output=None, saveto=os.getcwd()):
	if url == 'c':
		url = clipboard.paste()
	if output:
		if not os.path.splitext(output)[1].lower() == ".pdf":
			output = output + ".pdf"
	if url:
		if not output:
			output = os.path.split(url)[-1] + ".pdf"
	if not output:
		output = datetime.strftime(datetime.now(), '%Y%m%d_%H%M%S')
		output = str(output) + ".pdf"
	output = os.path.join(saveto, output)
	pdfkit.from_url(url, output)
	
def usage():
	parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
	parser.add_argument('URL', action='store', help='Url convert to, or just type "c" for get url from clipboard')
	parser.add_argument('-n', '--name', action='store', help='Save as Name')
	parser.add_argument('-p', '--path', action='store', help='Save to dir, default this dir', default=os.getcwd())
	if len(sys.argv) == 1:
		parser.print_help()
	else:
		args = parser.parse_args()
		if args.URL == 'c':
			args.URL = clipboard.paste()
		if 'https://www.google.com' in args.URL or 'http://www.google.com' in args.URL  or 'https://google.com' in args.URL or 'http://google.com' in args.URL:
			import guc
			debug(guc_file = guc.__file__)
			args.URL = guc.convert(args.URL)
		name = args.name
		if not name:
			import requests
			import time
			import re
			max_try = 10
			m = 1
			content = None
			while 1:
				try:
					content = requests.get(args.URL, timeout=4).content
					break
				except:
					if m == max_try:
						break
					else:
						m += 1
					time.sleep(1)
			title = None
			if content:
				title = re.findall("<title>(.*?)</title>", content, re.I|re.DOTALL)
			if title:
				title = title[0]
				import string
				pr = set(string.printable)
				title = str(filter(lambda x: x in pr, title))
				#print("title 1 =", title)
				title = unquote(title)
				#print("title 1 =", title)
				title = re.sub("/", " - ", title)
				title = re.sub("\?|:", "", title)
				#title = re.sub("\&", "", title)
				title = re.sub("&|#39;|;s", "", title)
				#print("title 2 =", title)
				name = title
				
		if not name:
			name =os.path.split(args.URL)[-1]
		if not name:
			name=os.path.split(os.path.dirname(args.URL))
			name=name[-1]
		print("name: ", name) 
		convert(args.URL, name, args.path)
	
if __name__ == '__main__':
	usage()
	#  if len(sys.argv) == 1:
		#  print(make_colors("USAGE:", 'lightwhite','lightred') + " " + make_colors(os.path.basename(__file__), 'lightred', 'lightyellow') + " " + make_colors("URL OUTPUT[.pdf] (default name is end of url name)", 'lightwhite', 'lightblue') + " " + make_colors("SAVE_DIR", "lightwhite", "lightmagenta"))
	#  else:
		#  if len(sys.argv) == 3:
			#  if os.path.isdir(sys.argv[2]):
				#  convert(sys.argv[1], saveto=sys.argv[2])
		#  else:
			#  convert(*sys.argv[1:])