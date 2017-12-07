import os
import sys
import argparse
import shutil

class backup(object):
	def __init__(self, filename=None, oname=None):
		super(backup, self)
		self.filename = filename
		self.oname = oname

	def bck(self, filename=None, oname=None):
		if filename == None:
			if self.filename == None:
				WindowsError("No Input Filename !!!")
			else:
				filename = self.filename
		
		if oname == None:
			if self.oname == None:
				WindowsError("Optional Name Error !!!")
			else:
				oname = self.oname
		filename_path = os.path.abspath(filename)
		filename_ext  = os.path.splitext(filename_path)[1]
		filename_name = os.path.splitext(filename_path)[0]
		filename_dir  = os.path.dirname(filename_path)
		dest_name     = os.path.join(filename_dir, "{0}_bck{1}")

		if oname:
			new = dest_name.format(os.path.basename(oname), filename_ext)
			shutil.copyfile(filename_path, new)
		else:
			new = dest_name.format(os.path.basename(filename_name), filename_ext)
			shutil.copyfile(filename_path, new)

	def usage(self):
		parser = argparse.ArgumentParser()
		parser.add_argument('-n' , '--name', help='Optional Name', action='store')
		parser.add_argument('FILE', help='Filename path', action='store')
		if len(sys.argv) == 1:
			print "\n"
			parser.print_help()
		else:
			args = parser.parse_args()
			self.bck(args.FILE, args.name)

if __name__ == '__main__':
	c = backup()
	c.usage()