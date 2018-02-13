#-*- coding: UTF-8 -*-
#coding:utf-8
__version__ = '2.0'
DEBUG = False
import glob
import tracert
import os
pid = os.getpid()
print "PID =", pid
import sys
fse = sys.getfilesystemencoding()
import subprocess
import time
import math
import traceback
from progressbar import Bar, ETA, Percentage, ProgressBar, AdaptiveETA, AdaptiveTransferSpeed
import sendgrowl 
import PySnarl as snarl
from make_colors import make_colors
import datetime
import configset
configset.set_config_name('folderplay.ini')
if configset.read_config('PLAYER', 'PLAYER0'):
	PLAYER0 = configset.read_config('PLAYER', 'PLAYER0')
else:
	PLAYER0 = r'c:\Apps\fmedia\fmedia.exe'
if configset.read_config('PLAYER', 'PLAYER1'):
	PLAYER1 = configset.read_config('PLAYER', 'PLAYER1')
else:
	PLAYER1 = r'c:\EXE\madplay.exe'
if configset.read_config('PLAYER', 'PLAYER2'):
	PLAYER2 = configset.read_config('PLAYER', 'PLAYER2')
else:
	PLAYER2 = r'c:\EXE\playwav.exe'
IS_PLAYER = ''

widgets = [
    Percentage(),
            ' ', Bar(),
            ' ', ETA(),
            ' ', AdaptiveETA(),
            ' ', AdaptiveTransferSpeed(),
]

def getTag(music_file):
	from mutagen.mp3 import MP3
	from mutagen.id3 import ID3
	from mutagen.easyid3 import EasyID3
	a = MP3(music_file)
	#print "aaaaaaaaa =", a
	b = EasyID3(music_file)
	c = ID3(music_file)
	#~ for i in a:
		#~ if i == 'APIC:':
			#~ pass
		#~ else:
			#~ print i, "=", a.get(i)

	return a.info.length, b, a, c

def getCover(music_file, imgstring = ''):
	from mutagen.mp3 import MP3
	x = MP3(music_file)

	if len(x.keys()) > 0:
		length, tag, mp3tag, id3tag = getTag(music_file)
		#print "tag 0 =", tag
	else:
		length = x.info.length
		tag = None
		mp3tag = None
		id3tag = None
	if imgstring:
		ext = ".jpg"
		with open(os.path.join(os.getenv('TMP'), os.path.splitext(os.path.basename(music_file))[0] + ext), 'wb') as imgdata:
			imgdata.write(imgstring.data)
			imgdata.close()
			coverart = os.path.join(os.getenv('TMP'), os.path.splitext(os.path.basename(music_file))[0] + ext)
			return coverart
	else:
		if id3tag and id3tag.get(u'APIC:'):
			imgstring = id3tag.get(u'APIC:')
			#print imgstring.mime
			if 'jpeg' in imgstring.mime:
				ext = ".jpg"
			elif 'png' in imgstring.mime:
				ext = ".png"
		if ext and imgstring:
			with open(os.path.join(os.getenv('TMP'), os.path.splitext(os.path.basename(music_file))[0] + ext), 'wb') as imgdata:
				imgdata.write(imgstring.data)
				imgdata.close()
			coverart = os.path.join(os.getenv('TMP'), os.path.splitext(os.path.basename(music_file))[0] + ext)
			return coverart
	return False

def get_tag(music_file, print_tag = False, debug = False):
	from tinytag import TinyTag
	coverart = ''
	imgstring = ''
	ext = '.jpg'
	try:
		tag = TinyTag.get(unicode(music_file).decode('UTF-8'), image= True)
		file_music = music_file
		#tag = TinyTag.get(glob.glob(music_file)[0], image= True)
		#file_music = [unicode(x, fse) for x in glob.glob(music_file)][0]
		#tag = TinyTag.get(glob.glob(file_music)[0], image= True)
		#imgstring = tag.get_image()
		coverart = getCover(file_music)
		if not coverart:
			imgstring = tag.get_image()
	
			if imgstring:
				with open(os.path.join(os.getenv('TMP'), os.path.splitext(os.path.basename(file_music))[0] + ext), 'wb') as imgdata:
					imgdata.write(imgstring.data)
					imgdata.close()
				coverart = os.path.join(os.getenv('TMP'), os.path.splitext(os.path.basename(file_music))[0] + ext)
				#print "coverart 1 =", coverart
				if not os.path.isfile(coverart):
					coverart = r'F:\ICONS\Phuzion_Icon_Pack\PNG\Devices\Headphones2.png'
			else:
				#print "not ext"
				coverart = r'F:\ICONS\Phuzion_Icon_Pack\PNG\Devices\Headphones2.png'
		if print_tag:
			print "\n"
			print "Title        :", unicode(str(tag.track)).encode('UTF-8') + "/" + unicode(tag.disc).encode('UTF-8') + "/" + unicode(tag.disc_total).encode('UTF-8') + ". " + unicode(tag.title).encode('UTF-8')         									   # title of the song
			print "Artist       :", unicode(tag.artist).encode('UTF-8')        # artist name as string
			print "Album        :", unicode(tag.album).encode('UTF-8')         # album as string
			print "Album Artist :", unicode(tag.albumartist).encode('UTF-8')   # album artist as string
			print "Disc         :", unicode(tag.disc).encode('UTF-8')          # disc number
			print "Total Disc   :", unicode(tag.disc_total).encode('UTF-8')    # the total number of discs
			print "Genre        :", unicode(tag.genre).encode('UTF-8')         # genre as string
			#print "Duration     :", unicode(tag.duration).encode('UTF-8')      # duration of the song in seconds
			print "Duration     :", str(datetime.timedelta(seconds = float(tag.duration)))      # duration of the song in seconds
			print "Audio Offset :", unicode(tag.audio_offset).encode('UTF-8')  # number of bytes before audio data begins
			print "Bitrate      :", unicode(tag.bitrate).encode('UTF-8')       # bitrate in kBits/s
			print "Filesize     :", unicode(tag.filesize).encode('UTF-8')      # file size in bytes
			print "Sample Rate  :", unicode(tag.samplerate).encode('UTF-8')    # samples per second
			print "Track        :", unicode(tag.track).encode('UTF-8')         # track number as string
			print "Track Total  :", unicode(tag.track_total).encode('UTF-8')   # total number of tracks as string
			print "Year         :", unicode(tag.year).encode('UTF-8')          # year or data as string
			print "Pid          :", str(pid)
		return tag, coverart
	except:
		if debug:
			traceback.format_exc()
		return False, False

def playing(i, print_error = True):
	if os.path.isfile(PLAYER0):
		a = subprocess.Popen([PLAYER0, i])
		IS_PLAYER = os.path.basename(os.path.splitext(PLAYER0)[0])
		return a
	else:
		if print_error:
			print make_colors("PLAYER NOT FOUND:", 'white', 'red', attrs= ['blink']) + make_colors('PLEASE INSTALL ', 'lightyellow', color_type= 'colorama') + make_colors("fmedia", 'lightcyan', color_type= 'colorama') + ' or ' + make_colors("madplay ", 'lightgreen', color_type= 'colorama') + make_colors('FIRST !', 'lightyellow', color_type= 'colorama')
		return False

def playing2(i, print_error = True):
	if os.path.isfile(PLAYER1):
		a = subprocess.Popen([PLAYER1, i])
		IS_PLAYER = os.path.basename(os.path.splitext(PLAYER1)[0])
		return a
	else:
		if print_error:
			print make_colors("PLAYER NOT FOUND:", 'white', 'red', attrs= ['blink']) + make_colors('PLEASE INSTALL ', 'lightyellow', color_type= 'colorama') + make_colors("fmedia", 'lightcyan', color_type= 'colorama') + ' or ' + make_colors("madplay ", 'lightgreen', color_type= 'colorama') + make_colors('FIRST !', 'lightyellow', color_type= 'colorama')
		return False

def playing3(i, print_error = True):
	if os.path.isfile(PLAYER2):
		a = subprocess.Popen([PLAYER2, i])
		IS_PLAYER = os.path.basename(os.path.splitext(PLAYER2)[0])
		return a
	else:
		if print_error:
			print make_colors("PLAYER NOT FOUND:", 'white', 'red', attrs= ['blink']) + make_colors('PLEASE INSTALL ', 'lightyellow', color_type= 'colorama') + make_colors("fmedia", 'lightcyan', color_type= 'colorama') + ' or ' + make_colors("madplay ", 'lightgreen', color_type= 'colorama') + make_colors('FIRST !', 'lightyellow', color_type= 'colorama')
		return False

def sendnotify(text="this is message", title="this is title", icon=None, event="Event", debug = False):
	if not icon:
		icon = r'F:\ICONS\Phuzion_Icon_Pack\PNG\Devices\Headphones2.png'
	try:
		mclass = sendgrowl.growl()
		appname = 'FolderPlayer'
		if configset.read_config4('GROWL', 'HOST'):
			#print "configset.read_config4('GROWL', 'HOST') =", configset.read_config4('GROWL', 'HOST')
			for i in configset.read_config4('GROWL', 'HOST'):
				if ":" in i:
					host, port = str(i).split(":")
					port = int(port)
				else:
					host = i
					port = 25053
				if debug:
					print "host :", host
					print "port :", port
				mclass.publish(appname, event, title, text, iconpath=icon, host = host, port = port)
		else:
			mclass.publish(appname, event, title, text, iconpath=icon)
	except:
		#print "ERROR:", traceback.format_exc()
		pass

def player(path, debug = False):
	#print "path =", os.path.abspath(path)
	IS_PLAYER = ''
	coverart = ''
	if os.path.isfile(os.path.join(path, 'cover.jpg')):
		coverart = os.path.join(path, 'cover.jpg')
	elif os.path.isfile(os.path.join(path, 'Cover.jpg')):
		coverart = os.path.join(path, 'Cover.jpg')
	elif os.path.isfile(os.path.join(path, 'cover.jpg')):
		coverart = os.path.join(path, 'Cover03.jpg')
	else:
		coverart = None
	listdir = []
	for root, dirs, files in os.walk(os.path.abspath(path)):
		if len(files) > 0:
			for i in files:
				if os.path.splitext(i)[1].strip() == '.mp3':
					listdir.append(os.path.join(root, i))
				if os.path.splitext(i)[1].strip() == '.wav':
					listdir.append(os.path.join(root, i))
				if os.path.splitext(i)[1].strip() == '.m4a':
					listdir.append(os.path.join(root, i))
				if os.path.splitext(i)[1].strip() == '.mp4':
					listdir.append(os.path.join(root, i))				
				#if i.endswith(".mp3") or i.endswith(".m4a") or i.endswith(".wav"):
					#listdir.append(os.path.join(root, i))
	for i in listdir:
		tags, coverart1 = get_tag(i, True, debug = debug)
		#print "tags =", tags
		if tags:
			if os.path.splitext(i)[1] == '.mp3':
				length, tag, mp3tag, id3tag = getTag(i)
				coverart = getCover(i)
				#duration = str(datetime.timedelta(seconds = float(length)))
			else:
				coverart = getCover(i, coverart1)
			length = int(tags.duration)
			if os.path.splitext(i)[1] == '.mp3':
				if not mp3tag:
					comment = ''
				else:
					comment = mp3tag.get('COMM::eng')
			else:
				comment = ''
			duration = str(datetime.timedelta(seconds = float(tags.duration)))
			if tags:
				#print "send Notify"
				msg = """
	Album           : {0}
	Artist            : {1}
	Album Artist  : {2}
	Disc              : {3}/{4}
	Genre           : {5}
	Duration       : {6}
	Bitrate          : {7}
	Year              : {8}
	Comment      : {9}""".format(unicode(tags.album).encode('UTF-8'), unicode(tags.artist).encode('UTF-8'), unicode(tags.albumartist).encode('UTF-8'), unicode(tags.disc).encode('UTF-8'), unicode(tags.disc_total).encode('UTF-8'), unicode(tags.genre).encode('UTF-8'), unicode(duration).encode('UTF-8'), unicode(tags.bitrate).encode('UTF-8'), unicode(tags.year).encode('UTF-8'), unicode(comment).encode('UTF-8'))
				#format(unicode(album).encode('UTF-8'), unicode(artist).encode('UTF-8'), unicode(albumartist).encode('UTF-8'), unicode(comment).encode('UTF-8'))
				try:
					title = "{0}/{1}/{2}/{3}. {4}".format(tags.track, tags.track_total, tags.disc, tags.disc_total, unicode(tags.title).encode('UTF-8'))
				except:
					try:
						title = "{0}. {1}".format(tag.get('tracknumber')[0], tag.get('title')[0])
					except:
						title = "{0}. {1}".format(tag.get('tracknumber'), tag.get('title')[0])
			else:
				msg = 'No IDTag'
				title = os.path.basename(i)
			#print "tag x =", tag
			if not coverart:
				coverart = r'F:\ICONS\Phuzion_Icon_Pack\PNG\Devices\Headphones2.png'
			sendnotify(msg, title, coverart, debug = debug)
			#print "coverart =", coverart
			try:
				snarl.snShowMessage(title, msg, 20, coverart)
			except:
				pass
			if length > 0:
				pbar = ProgressBar(widgets=widgets, max_value= length)
				pbar.start()
			print "play %s ... [%s ~ %s]" %(os.path.basename(i), str(length), str(os.getpid()))
		if os.path.isfile(PLAYER0):
			a = subprocess.Popen([PLAYER0, i])
			IS_PLAYER = os.path.basename(os.path.splitext(PLAYER0)[0])
		else:
			if os.path.splitext(i)[1].strip() == '.mp3':
				if os.path.isfile(PLAYER1):
					a = subprocess.Popen([PLAYER1, i])
					IS_PLAYER = os.path.basename(os.path.splitext(PLAYER1)[0])
				else:
					a = playing2(i)
					if a == False:
						sys.exit(0)
			if os.path.splitext(i)[1].strip() == '.m4a' or os.path.splitext(i)[1].strip() == '.mp4':
				a = playing(i)
				if a == False:
					sys.exit(0)
			if os.path.splitext(i)[1].strip() == '.wav':
				a = playing2(i)
				if a == False:
					sys.exit(0)			
		n = 1
		if not IS_PLAYER.lower() == 'fmedia' or not 'fmedia' in IS_PLAYER.lower():
			try:
				while 1:
					if a.poll() == 0:
						pbar.finish()
						break
					else:
						time.sleep(1)
						if length > 0:
							if n > length:
								pbar.finish()
								break
							else:
								pbar.update(n)
								n += 1
								#m +=1
								#if m == 20:
								#	sendnotify(msg, title, coverart, 'Play Monitoring')
								#	snarl.snShowMessage(title, msg, 20, coverart)
								#	m = 1
			except KeyboardInterrupt:
				pbar.finish()

			except:
				#print "error =", traceback.format_exc()
				sys.exit(0)
		else:
			try:
				while 1:
					if a.poll() == 0:
						break
					else:
						time.sleep(1)
			except KeyboardInterrupt:
				os.kill(a.pid, a.pid)
			except:
				sys.exit(0)			


if __name__ == '__main__':
	#player(sys.argv[1])
	import argparse
	parse = argparse.ArgumentParser(formatter_class= argparse.RawTextHelpFormatter, version= __version__)
	parse.add_argument("PATH", help = 'Folder Play to', action = 'store')
	parse.add_argument('-d', '--debug', help = 'Debug process running (logger)', action = 'store_true')
	if len(sys.argv) == 1:
		parse.print_help()
	else:
		args = parse.parse_args()
		if args.debug:
			configset.DEBUG.DEBUG = True
		player(args.PATH, debug = args.debug)
	#sendnotify('test', 'this is title')