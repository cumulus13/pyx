import sys
import os
import argparse
from storjtorrent import StorjTorrent as sj
import clipboard as clip

class torrent(object):
	def __init__(self, file_torrent=None):
		super(torrent, self)
		self.file_torrent = file_torrent

	def torrent2magnet(self, file_torrent=None, clipboard=None):
		if file_torrent == None:
			if self.file_torrent == None:
				return WindowsError('File torrent NOT FOUND !')
			else:
				file_torrent = self.file_torrent
		#magnet:?xt=urn:btih:DD4A1198009E19DA1819B4EBA758CD1F3729F7D5&dn=radiohead+thom+yorke+atoms+for+peace+discography+pablo+honey+the+bends+ok+computer+kid+a+amnesiac+hail+to+the+thief+the+eraser+in+rainbows+the+king+of+limbs+amok+tomorrow+s+modern+boxes&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80%2Fannounce&tr=udp%3A%2F%2Fopen.demonii.com%3A1337
		if str(sj.get_hash([], file_torrent)):
			if clipboard:
				clip.copy("magnet:?xt=urn:btih:" + str(sj.get_hash([], file_torrent)))
			return "magnet:?xt=urn:btih:" + str(sj.get_hash([], file_torrent))
		else:
			return False

	def usage(self):
		parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
		parser.add_argument('FILE', help='File torrrent', action='store')
		parser.add_argument('-c', '--clipboard', help='Copy to clipboard', action='store_true')
		if len(sys.argv) == 1:
			parser.print_help()
		else:
			args = parser.parse_args()
			a = self.torrent2magnet(args.FILE, args.clipboard)
			if a:
				print a
			else:
				print "Torrent file is corrupt !"

if __name__ == '__main__':
	c = torrent()
	c.usage()
