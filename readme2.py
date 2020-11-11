#!/usr/bin/python
#coding:utf-8

import traceback
import sys
import os
try:
	import cmdw
	WIDTH = "="*cmdw.getWidth()
except:
	print traceback.format_exc()
	WIDTH = "="*50

try:
	import misaka
except ImportError:
	print "Module 'misaka' NOT installed"
	sys.exit("Module 'misaka' NOT installed")
except:
	print traceback.format_exc()
	sys.exit(0)

class MD(object):
	def __init__(self, filemd=None):
		self.filemd = filemd

	def read(self, filemd):
		if self.filemd:
			filemd = self.filemd
		f = open(filemd, 'r')
		md = misaka.Markdown(f.read())
		print md.renderer
		f.close()
		return md.renderer

	def usage(self):
		print "\n"
		print " USAGE:", os.path.splitext(os.path.basename(__file__))[0], "FILE_README(*.md) FILE_README(*.md) ..."

if __name__ == '__main__':
	c = MD()
	if len(sys.argv) == 1:
		c.usage()
	elif len(sys.argv) == 2:
		c.read(sys.argv[1])
	elif len(sys.argv) > 2:
		for i in sys.argv[1:]:
			c.read(i)
			print WIDTH
	else:
		c.usage()
