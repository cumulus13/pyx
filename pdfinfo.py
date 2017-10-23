#!/usr/bin/python

import pyPdf
from pdfminer.pdfparser import PDFParser as pdfparser
from pdfminer.pdfdocument import PDFDocument as pdfdoc
import argparse
import sys
import clipboard
import os
import shutil

class with_pdfminer(object):
	def __init__(self):
		super(with_pdfminer, self)

	def getInfo(self, pdf_file):
		fp = open(pdf_file, 'rb')
		parser = pdfparser(fp)
		doc = pdfdoc(parser)
		fp.close()
		return doc.info

class with_pypdf(object):
	def __init__(self):
		super(with_pypdf, self)

	def getInfo(self, pdf_file):
		fp = open(pdf_file, 'rb')
		pdfparser = pyPdf.PdfFileReader(fp)
		doc = pdfparser.getDocumentInfo()
		fp.close()
		return doc

def formatOut(data, ftype, clipboard):
	if isinstance(data, dict):
		if ftype == 'raw':
			return data
		elif ftype == 'str':
			for i in data.keys():
				print i, " "*(18 - len(i)), "=", data.get(i)
		elif ftype == 'comma':
			for i in data.keys():
				sys.stdout.write(str(i) + ":", data.get(i), ", ")
		elif ftype == 'dot':
			for i in data.keys():
				sys.stdout.write(str(i) + ":", data.get(i), ". ")
		else:
			print "Not implement"
			print "\n"
			print usage()
		if clipboard:
			clipboard.copy(data)

def rename(name, file, quite=None):
	new_name = str(name + os.path.splitext(file)[1])
	new_name = os.path.join(os.path.dirname(file), new_name)
	print "\n"
	print "Rename %s --> \"%s\"\n"%(os.path.abspath(file), new_name)
	if quite:
		if os.path.isfile(new_name):
			os.remove(new_name)
		os.rename(file, new_name)
	else:
		q = raw_input("rename it ? (y/n): ")
		if str(q).lower() == 'y':
			if os.path.isfile(new_name):
				q1 = raw_input("File exits, overwrite it ? (y/n): ")
				if str(q1).lower() == 'y':
					os.remove(new_name)
			os.rename(file, new_name)
			# shutil.move(os.path.abspath(file), new_name)
		else:
			pass

def usage():
	def copyformatUsage():
		data = """
	raw   = return raw string format of copy, it can be dict or list or tuple
	str   = return return string format of copy with space separator
	comma = return return string format of copy with space comma separator
	dot   = return return string format of copy with space comma dot separator
		"""
		return data

	parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
	parser.add_argument('FILE_PDF', help='pdf file', action='store')
	parser.add_argument('-c', '--clipboard', help='Copy info to clipboard', action='store_true')
	parser.add_argument_group('COPY FORMAT', copyformatUsage())
	parser.add_argument('-f', '--copy-format', help='Format copy clipboard' , action='store', default="str")
	parser.add_argument('-b', '--both', help='Show all' , action='store_true')
	parser.add_argument('-q', '--quite', help='No Questions Answer' , action='store_true')
	if len(sys.argv) > 1:
		args = parser.parse_args()
		c1 = with_pdfminer()
		i1 = c1.getInfo(args.FILE_PDF)
		c2 = with_pypdf()
		try:
			i2 = c2.getInfo(args.FILE_PDF)
		except:
			i2 = i1

		if len(i1) > len(i2):
			if args.copy_format:
				formatOut(i1, args.copy_format, args.clipboard)
			if "/Title" in i1.keys():
				rename(i1.get("/Title"), args.FILE_PDF, args.quite)
		elif len(i2) > len(i1):
			if args.copy_format:
				formatOut(i2, args.copy_format, args.clipboard)
			if "/Title" in i2.keys():
				rename(i2.get("/Title"), args.FILE_PDF, args.quite)
		else:
			if args.copy_format:
				formatOut(i2[0], args.copy_format, args.clipboard)
			if "/Title" in i2[0].keys():
				rename(i2[0].get("/Title"), args.FILE_PDF, args.quite)
			
		if args.both:
			formatOut(i1, args.copy_format, args.clipboard)
			print "-"* 150
			formatOut(i2, args.copy_format, args.clipboard)

	else:
		parser.print_help()


if __name__ == '__main__':
	usage()