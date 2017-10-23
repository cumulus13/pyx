import os
import sys
import configset
import argparse

class mp3diag(configset.usage):
	def __init__(self):
		super(mp3diag, self)
		self.conf = configset.get_config_file('conf.ini')
		self.exe = configset.read_config('MP3DIAG', 'EXE_PATH')

	def diag(self, path=None):
		os.chdir(os.path.dirname(self.exe))
		exe = os.path.basename(self.exe)
		if os.path.isfile(exe):
			os.system(exe + ' -l 4 -t 1 "' + path + '"')
		else:
			print "NO EXECUTABLE !"

	def usage(self):
		parser = argparse.ArgumentParser()
		parser.add_argument('PATH', help='Path where is mp3 file store', action='store')
		if len(sys.argv) == 1:
			parser.print_help()
		else:
			args = parser.parse_args()
			
			if args.PATH:
				self.diag(args.PATH)

if __name__ == '__main__':
	c = mp3diag()
	c.usage()
