import os
import sys
import configset
import argparse

class mp3val(configset.usage):
	def __init__(self):
		super(mp3val, self)
		self.conf = configset.get_config_file('conf.ini')
		self.exe = configset.read_config('MP3VAL', 'EXE_PATH')

	def mp3(self, path=None):
		if path == None:
			path = os.getcwd()

		for root, dirs, files in os.walk(path):
			for i in files:
				if str(i).endswith('.mp3'):
					mp3_file = os.path.join(root, i)
					#print "mp3_file =", mp3_file
					os.system(self.exe + ' -f -nb "' + mp3_file + '"')


	def usage(self):
		parser = argparse.ArgumentParser()
		parser.add_argument('PATH', help='Path where is mp3 file store', action='store')
		if len(sys.argv) == 1:
			parser.print_help()
		else:
			args = parser.parse_args()
			
			if args.PATH:
				self.mp3(args.PATH)

if __name__ == '__main__':
	c = mp3val()
	c.usage()
