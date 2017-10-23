import os
import sys
import configset
import optparse

class gain(object):
	def __init__(self):
		super(gain, self)
		self.conf = configset.get_config_file('conf.ini')
		self.path = configset.read_config('MP3GAIN', 'MASTER_PATH', self.conf)

	def check_path(self):
		if os.path.isfile(self.path):
			if str(str(self.path).lower()).endswith(".exe"):
				return True
			else:
				return False
		else:
			return False

	def mp3gain(self, path=None, analisys=None, gain=None):
		# print "GAIN =", gain
		if not self.check_path():
			raise SyntaxError('Please check your config file, ensure mp3gain file executable path !')
		if path == None:
			path = os.getcwd()
		if os.path.isdir(path):
			for root, dirs, files in os.walk(path):
				for i in files:
					i = os.path.join(root, i)
					# print "FILES =", i
					# print "is FILES ? =", os.path.isfile(i)
					# print "self.path =", self.path
					if str(str(i).lower()).endswith(".mp3"):
						if analisys:
							print "\n"
							os.system(self.path + ' /s s "' + str(i) + '"')
							print "-"*120
						else:
							print "\n"
							if gain:
								os.system(self.path + ' /g %s /t /s s "' %(gain) + str(i) + '"')
							else:
								os.system(self.path + ' /a /t /s s "' + str(i) + '"')
							print "-"*120
		elif os.path.isfile(path):
			if str(str(path).lower()).endswith(".mp3"):
				if analisys:
					print "\n"
					os.system(self.path + ' /s s "' + str(path) + '"')
					print "-"*120
				else:
					print "\n"
					if gain:
						os.system(self.path + ' /g %s /t /s s "' %(gain) + str(path) + '"')
					else:
						os.system(self.path + ' /a /t /s s "' + str(path) + '"')
					print "-"*120
		else:
			self.usage(True)

	def usage(self, print_help=None):
		print "\n"
		parser = optparse.OptionParser()
		parser.add_option('-g', '--gain', help="Integer gain", action="store")
		parser.add_option('-d', '--dir', help="Directory where is mp3 file", type=str, action="store")
		parser.add_option('-a', '--analisys', help="Don't gain just analisys", action="store_true")
		option, argv = parser.parse_args()
		if print_help:
			parser.print_help()
		if len(sys.argv) == 1:
			parser.print_help()
		else:
			self.mp3gain(option.dir, option.analisys, option.gain)

if __name__ == "__main__":
	c = gain()
	c.usage()

