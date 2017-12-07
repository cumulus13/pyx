import os
import sys
import ConfigParser

cfg = ConfigParser.RawConfigParser(allow_no_value=True)
cfg.optionxform = str
hgrc = os.path.join(os.getcwd(), '.hg', 'hgrc')

HG_BIN = 'hg'
if HG_BIN == r'':
	HG_BIN = 'hg.exe'

def checkRemote():
	if os.path.isfile(hgrc):
		cfg.read(hgrc)
	try:
		data = cfg.get('paths', 'default-push')
	except ConfigParser.NoOptionError:
		try:
			data = cfg.get('paths', 'default')
		except ConfigParser.NoOptionError:
			q = raw_input('add hg remote origin (URL): ')
			if len(q) == 0:
				print "Please Add remote git url (origin) first !"
				sys.exit(0)
			else:
				#f = open(hgrc)
				try:
					cfg.set('paths', 'default-push', str(q))
				except ConfigParser.NoSectionError:
					cfg.add_section('paths')
					cfg.set('paths', 'default-push', str(q))
				cfg_data = open(hgrc, 'wb')
				cfg.write(cfg_data)
	else:
		os.system(HG_BIN + " push")

def commit():
	import datetime
	comment = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S:%f')
	tag = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d_%H-%M-%S-%f')
	if os.path.isfile(os.path.join(os.getcwd(), '.hgignore')):
		os.system(HG_BIN + " add .")
		os.system(HG_BIN + " tag \"" + str(tag) + '"')
		os.system(HG_BIN + " commit -m \"" + str(comment) + '"')
		checkRemote()
	else:
		f = open(os.path.join(os.getcwd(), '.hgignore'), 'w')
		f.write("*.pyc\n*.zip\n*.rar\n*.7z\n*.mp3\n*.wav\n")
		f.close()
		os.system(HG_BIN + " add .")
		os.system(HG_BIN + " tag \"" + str(tag) + '"')
		os.system(HG_BIN + " commit -m \"" + str(comment) + '"')
		checkRemote()


if __name__ == '__main__':
	commit()
	#checkRemote()