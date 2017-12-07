import os
import sys

for root, dirs, files in os.walk(os.getcwd()):
	for i in files:
		if str(os.path.join(root, i)).endswith(".flac"):
			a = os.path.join(root, i)
			b = os.path.splitext(a)[0]
			c = os.path.join(os.path.abspath(sys.argv[1]), b + ".mp3")
			os.chdir(r"c:\Program Files\OJOsoft\OJOsoft Audio Converter")
			print "convert file:", os.path.join(root, i)
			os.system('convert.exe -i "{0}" -ab 320k -ac 2 -ar 48000 -acodec libmp3lame -vn -y "{1}"'.format(a, c)) 
			