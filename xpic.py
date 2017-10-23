import os
import sys
import optparse
import zipfile
import re
import shutil
import traceback

class xpi(object):
	def __init__(self, filename=None):
		super(xpi, self)
		self.filename = self.getfile(filename)
		


	def getInfo(self, filename=None, verbosity=None):
		if verbosity:
			print "try to getinfo: %s" %(str(filename))
		if filename == None:
			if self.filename == None:
				return WindowsError('No input filename')
			else:
				filename = self.filename

		z = zipfile.ZipFile(filename)
		if 'install.rdf' in z.namelist():
			rdf = z.read('install.rdf')
			rdf1 = []
			for i in rdf.split("\n"):
				if str(i).strip() != '':
					rdf1.append(str(i).strip())
			# print "RDF 1 =", rdf1
			info = {'name':'', 'version':''}
			for i in rdf1:
				if ":name" in i:
					# print "NAME 1 =", i
					# print "re.split('<|>', i) =",re.split('<|>', i)
					pre_name = re.split('<|>', i)
					if len(pre_name) > 1:
						name = pre_name[2]
						
					elif len(pre_name) == 1:
						name = re.split('"|=', pre_name[0])
						# print "NAME 2 ", name
						name = name[2]
					info.update({'name':name})
				if ":version" in i:
					# print "VERSION 1 =", i
					if "<" in i:
						version = re.split('<|>', i)[2]
					else:
						version = re.split('"|=', i)[-2]
						# print "VERSION 2 =", version
					# print "VERSION 2 =", version
					info.update({'version':version})
			# print "INFO =", info
			z.close()
			return info.get('name'), info.get('version')
		else:
			return SyntaxError('Non install.rdf !')

	def getfile(self, filename):
		filex = os.path.abspath(filename)
		return filex

	def delfile(self, filename):
		try:
			return os.unlink(filename)
		except:
			return os.remove(filename)
		finally:
			return os.system("DEL %s > NUL"%(filename))

	def rename(self, filename=None, move=None, verbosity=None, overwrite=None):
		if verbosity:
			print "try to rename: %s" %(str(filename))
		temp = os.getenv('TEMP')		
		if filename == None:
			filename = self.filename

		name = self.getInfo(filename, verbosity)[0]
		version = self.getInfo(filename, verbosity)[1]
		name = "{0} v{1}".format(name, version)
		# print "NAME =", name
		dirname = os.path.dirname(filename)
		namefile = os.path.basename(filename)
		ext = os.path.splitext(filename)[1]
		destname = os.path.join(dirname, name + ext)

		if verbosity:
			print "rename {0} --> {1}".format(self.getInfo(filename)[0], destname)
		if os.path.exists(destname):
			if overwrite:
				print "OVERWRITE!"
				self.delfile(destname)
				try:
					shutil.copyfile(filename, destname)
					# os.unlink(filename)
					self.delfile(filename)
					# os.rename(filename, destname)
				except:
					print "ERROR 001:"
					print traceback.format_exc()
			else:
				shutil.copyfile(self.getInfo(filename)[0], destname)
				try:
					sys.exit(self.delfile(self.getInfo(filename)[0]))
				except:
					pass
		else:
			try:
				shutil.copyfile(filename, destname)
				# os.unlink(filename)
				self.delfile(filename)
				# os.rename(filename, destname)
				# os.unlink(filename)
			except:
				print "ERROR 002:"
				print traceback.format_exc()
		if move:
			if verbosity:
				print "move {0} --> {1}".format(self.getInfo(filename)[0], move)
			if overwrite:
				print "OVERWRITE 2!"
				if os.path.exists(os.path.join(move, os.path.basename(destname))):
					print "exists !"
					self.delfile(os.path.join(move, os.path.basename(destname)))
					self.move(destname, move)
			else:
				self.move(destname, move)

	def multirename(self, path, move=None, verbosity=None, overwrite=None):
		files_list = []
		for root, dirs, files in os.walk(path):
			for i in files:
				if i.endswith(".xpi"):
					files_list.append(os.path.join(root, i))
		if len(files_list) > 0:
			for i in files_list:
				if verbosity:
					print "FILE:", str(i)
				self.rename(i, move, verbosity, overwrite)

	def multirename2(self, path, move=None, verbosity=None, overwrite=None):
		files_list = []
		files = os.listdir(path)
		for i in files:
			if i.endswith(".xpi"):
				files_list.append(os.path.join(path, i))
		# print "files_list =", files_list
		if len(files_list) > 0:
			for i in files_list:
				if verbosity:
					print "FILE:", str(i)
				self.rename(i, move, verbosity, overwrite)

	def move(self, src, dst):
		shutil.move(src, dst)

	def usage(self):
		usage = "xpic.py [path|*] [options]"
		parser = optparse.OptionParser(usage=usage)
		parser.add_option('-m','--move', help='rename it and move to in folder', action='store', dest="DIRS")
		parser.add_option('-v', '--verbosity', help='print verbosity info', action='count')
		parser.add_option('-r', '--recursive', help='rename with sub directory', action='store_true')
		parser.add_option('-o', '--overwrite', help='Overwrite', action='store_true')
		if len(sys.argv) == 1:
			parser.print_help()
		else:
			options, args = parser.parse_args()
			# print "OPTIONS =", options
			# print "ARGS =", args
			# print "len(args) =",len(args)
			if len(args) == 1:
				if '*' == args[0]:
					# print "AAA"
					if options.recursive:
						self.multirename(os.getcwd(), options.DIRS, options.verbosity, options.overwrite)	
					else:
						# print "AAA 1"
						self.multirename2(os.getcwd(), options.DIRS, options.verbosity, options.overwrite)
				elif "*" in args[0]:
					# print "BBB"
					if options.recursive:
						self.multirename(os.path.basename(args[0]), options.DIRS, options.verbosity, options.overwrite)
					else:
						self.multirename2(os.path.basename(args[0]), options.DIRS, options.verbosity, options.overwrite)
				else:
					self.rename(os.path.abspath(args[0]), options.DIRS, options.verbosity, options.overwrite)
			else:
				for i in args:
					if '*' == i:
						if options.recursive:
							self.multirename(os.path.basename(i), options.DIRS, options.verbosity, options.overwrite)
						else:
							self.multirename2(os.path.basename(i), options.DIRS, options.overwrite)
					elif "*" in args[0]:
						if options.recursive:
							self.multirename(os.getcwd(), options.DIRS, options.verbosity, options.overwrite)
						else:
							self.multirename2(os.getcwd(), options.DIRS, options.verbosity, options.overwrite)
					else:
						self.rename(os.path.abspath(i), options.DIRS, options.verbosity, options.overwrite)

if __name__ == '__main__':
	c = xpi(sys.argv[1])
	c.usage()
	# print c.getInfo(sys.argv[1])
	# c.rename(overwrite=True)