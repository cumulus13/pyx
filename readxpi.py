import zipfile
import re
import os
import datetime
import traceback

__version__ = "0.1"
__test__ = "0.1"
__build__ = "2.7"
__platform__ = "win"
__depedency__ = "list tree of directory, use only for windows"
__link__ = "licface@yahoo.com"
__email__ = "licface@yahoo.com"
__site__ = "licface@yahoo.com"

class readxpi(object):
	def __init__(self, filezip=None, path=None, verbosity=None):
		self.filezip = filezip
		self.path = path

	def read_install_rdf(self, filezip=None):
		if filezip == None:
			filezip == self.filezip
		if filezip == None:
			return SystemError('Please Definition filezip name ')
		try:
			a = zipfile.ZipFile(filezip)
			installrdf = ''
			for i in a.namelist():
				if i in "install.rdf":
					installrdf = a.read(i)
			#print "installrdf =",installrdf
			b = re.split("\n|\r|\t", installrdf)
			data_info = {}
			data_info_name = []
			for i in b:
				c = str(i).strip()
				#print "C =", c
				if c == '':
					pass
				else:
					if "em:name" in c:
						name = re.split("<|>|em:name|/em:name|=|\"", c)
						name_pre = []
						for x in name:
							if x != '':
								name_pre.append(x)
						#print "name =", name_pre[0]
						data_info_name.append(name_pre[0])
					if "em:version" in c:
						version = re.split("<|>|em:version|/em:version|=|\"", c)
						version_pre = []
						for y in version:
							if y != '':
								version_pre.append(y)
						version = version_pre
						data_info.update({'version':version_pre[0]})
						#print "version =", version_pre[0]
			data_info.update({'name':data_info_name[0]})
			if data_info.get('version') != None:
				pass
			else:
				version = datetime.datetime.strftime(datetime.datetime.fromtimestamp(os.stat(filezip)[-1]), '%H%M%S-%d%m%Y')
				data_info.update({'version':version})
			#print "data_info =",data_info
			#print "data_info_name =",data_info_name
			return data_info
		except zipfile.BadZipfile:
			return None

	def rename_xpi(self, path=None, verbosity=None):
		#print "type file =", os.path.isfile(path)
		#print "type dir =", os.path.isdir(path)
		if path == None:
			if self.path == None:
				raise SyntaxError("Please definition path of xpi files")
			else:
				path = self.path
		if os.path.isdir(path):
			listdir = os.popen("dir /s /b \"" + path + "\"\*.xpi").readlines()
			listfile = []
			for i in listdir:
				a = str(i).split("\n")[0]
				listfile.append(a)
				#print "listfile =", listfile
			for i in listfile:
				name_a, ext_a = os.path.splitext(i)
				#print "-"*100
				#print "i =", i
				#print "self.read_install_rdf(i) =", self.read_install_rdf(i)
				if verbosity:
					print "rename file:",str(i)
				try:
					name = self.read_install_rdf(i).get('name')
					version = self.read_install_rdf(i).get('version')
					os.rename(i, os.path.join(os.path.dirname(i),name + "-" + version + ext_a))
					if verbosity:
						print "rename file:",str(i), "to:", os.path.join(os.path.dirname(i),name + "-" + version + ext_a, " [DONES]")
				except WindowsError:
					os.remove(i)
				except:
					traceback.format_exc_syslog_growl()
				#print "file =", i
				#print "name 0 =", name
				#print "version 0 =", version
				sys.stdout.write(".")
			sys.stdout.write("... DONE !")
		elif os.path.isfile(path):
			a = str(path).split("\n")[0]
			#print "a =", a
			name_a, ext_a = os.path.splitext(a)
			try:
				name = self.read_install_rdf(a).get('name')
				version = self.read_install_rdf(a).get('version')
				os.rename(a, os.path.join(os.path.dirname(a),name + "-" + version + ext_a))
				#print "XXX =", os.path.join(os.path.dirname(a),name + "-" + version + ext_a)
			except WindowsError:
				os.remove(i)
			except:
				traceback.format_exc_syslog_growl()

			#print "file =",path
			#print "name 1 =", name
			#print "version 1 =", version
		else:
			print "just relax ! \n"

if __name__ == "__main__":
	import sys
	c = readxpi()
	#c.read_install_rdf(sys.argv[1])
	if "-v" in sys.argv:
		c.rename_xpi(sys.argv[1], verbosity=True)
	else:
		c.rename_xpi(sys.argv[1])