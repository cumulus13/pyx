import os
print "PID =", os.getpid()
import sys
import subprocess
import time
import math
import traceback
from progressbar import Bar, ETA, Percentage, ProgressBar, AdaptiveETA, AdaptiveTransferSpeed
import sendgrowl 
import PySnarl as snarl

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

def sendnotify(text="this is message", title="this is title", icon=None, event="Event"):
	if not icon:
		icon = r'F:\ICONS\Phuzion_Icon_Pack\PNG\Devices\Headphones2.png'
	try:
		mclass = sendgrowl.growl()
		appname = 'FolderPlayer'
		mclass.publish(appname, event, title, text, iconpath=icon)
	except:
		#print "ERROR:", traceback.format_exc()
		pass

def player(path):
	#print "path =", os.path.abspath(path)
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
				if i.endswith(".mp3"):
					listdir.append(os.path.join(root, i))
	#print listdir
	ext = None
	for i in listdir:
		coverart = None
		imgstring = None
		#print "coverart 0 =", coverart
		#print "listdir =", listdir
		from mutagen.mp3 import MP3
		from mutagen.id3 import ID3
		from mutagen.easyid3 import EasyID3
		x = MP3(i)
		#y = ID3(i)
		#z = EasyID3(i)
		#print "x =", x.keys()
		#print "y =", y
		#print "z =", z
		if len(x.keys()) > 0:
			length, tag, mp3tag, id3tag = getTag(i)
			#print "tag 0 =", tag
		else:
			length = x.info.length
			tag = None
			mp3tag = None
			id3tag = None

		if id3tag and id3tag.get(u'APIC:'):
			imgstring = id3tag.get(u'APIC:')
			#print imgstring.mime
			if 'jpeg' in imgstring.mime:
				ext = ".jpg"
			elif 'png' in imgstring.mime:
				ext = ".png"
		if ext and imgstring:
			with open(os.path.join(os.getenv('TMP'), os.path.splitext(os.path.basename(i))[0] + ext), 'wb') as imgdata:
				imgdata.write(imgstring.data)
				imgdata.close()
			coverart = os.path.join(os.getenv('TMP'), os.path.splitext(os.path.basename(i))[0] + ext)
			#print "coverart 1 =", coverart
			if not os.path.isfile(coverart):
				covertart = r'F:\ICONS\Phuzion_Icon_Pack\PNG\Devices\Headphones2.png'
		else:
			#print "not ext"
			covertart = r'F:\ICONS\Phuzion_Icon_Pack\PNG\Devices\Headphones2.png'
		#print "coverart 2 =", coverart
		#print "tag =", tag
		#print "tag.get('album')[0] =", tag.get('album')[0]
		#print "tag.get('albumartist')[0] =", tag.get('albumartist')[0]
		#print "mp3tag.get('COMM::eng') =", mp3tag.get('COMM::eng')
		if not mp3tag:
			comment = ''
		else:
			comment = mp3tag.get('COMM::eng')
		if not comment:
			comment = ''
		if not tag:
			albumartist = ''
			album = ''
		else:
			#if not tag:
				#artist = ''
				#albumartist = ''
				#album = ''
			if tag.get('artist'):
				artist = tag.get('artist')[0]
			if tag.get('albumartist'):
				albumartist = tag.get('albumartist')[0]
			else:
				albumartist = ''
			if tag.get('album'):
				album = tag.get('album')[0]
			else:
				album = ''
		if tag:
			msg = """
Album          : {0}
Artist            : {1}
Album Artist : {2}
Comment     : {3}

		""".format(unicode(album).encode('utf-8'), unicode(artist).encode('utf-8'), unicode(albumartist).encode('utf-8'), unicode(comment).encode('utf-8'))
			try:
				title = "{0}. {1}".format(tag.get('tracknumber')[0], tag.get('title')[0])
			except:
				title = "{0}. {1}".format(tag.get('tracknumber'), tag.get('title')[0])
		else:
			msg = 'No IDTag'
			title = os.path.basename(i)
		#print "tag x =", tag
		if not coverart:
			covertart = r'F:\ICONS\Phuzion_Icon_Pack\PNG\Devices\Headphones2.png'
		sendnotify(msg, title, coverart)
		#print "coverart =", coverart
		try:
			snarl.snShowMessage(title, msg, 20, coverart)
		except:
			pass
		if length > 0:
			pbar = ProgressBar(widgets=widgets, max_value= length)
			pbar.start()
		print "play %s ... [%s ~ %s]" %(os.path.basename(i), str(length), str(os.getpid()))
		a = subprocess.Popen(['madplay.exe', i])
		n = 1
		#m = 1
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
		
	
if __name__ == '__main__':
	player(sys.argv[1])
	#sendnotify('test', 'this is title')