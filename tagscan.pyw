import os
import sys
import subprocess

def update():
	import requests as req
	from bs4 import BeautifulSoup as bs
	import easygui
	a = req.get('https://www.xdlab.ru/en/download.htm')
	content = a.content
	b = bs(content, 'lxml')
	all_p = b.find('div', {'class':'seven columns'}).find_all('p')
	all_dl = {}
	n = 1
	msg = ""
	for i in all_p[:2]:
		link = i.find('a')
		all_dl.update({
			n : {
					'name': link.text,
					'link': 'https://www.xdlab.ru' + link.get('href')
				}
			}
		)
		msg += "{0}. {1}\n".format(str(n), link.text)
		n += 1
	print('all_dl =', all_dl)
	q = easygui.enterbox(msg)
	if q and int(q) <= len(list(all_dl.keys())):
		print("LINK =", all_dl.get(int(q)).get('link'))
	
data = [r"c:\Program Files (x86)\TagScanner\Tagscan.exe"]
if not os.path.isfile(data[0]):
	data = [r"c:\Program Files\TagScanner\Tagscan.exe"]
	if not os.path.isfile(data[0]):
		data = [r"c:\Program Files\TagScanner\Tagscan.exe"]
# else:
if len(sys.argv) > 1:
	if sys.argv[1] == '-h' or '-h' in sys.argv:
		# print "USAGE:", os.path.basename(__file__) + " " + "FILE|DIRS (can multiply)"
		import easygui
		USAGE = "USAGE:", os.path.basename(__file__) + " " + "FILE|DIRS (can multiply)"
		image = r'f:\ICONS\FatCow_Icons32x32\clipboard_empty.png'
		choices = ["Close"]
		reply = easygui.codebox(msg='Tagscan Usage', title='Tagscan Usage', text=USAGE)
	elif sys.argv[1] == '-u' or sys.argv[1] == '-U':
		update()
	else:
		for i in sys.argv[1:]:
			if os.path.isfile(i):
				subprocess.Popen([data[0], os.path.abspath(os.path.dirname(i))])
			elif os.path.isdir(i):
				subprocess.Popen([data[0],os.path.abspath(i)])
	
else:
	subprocess.Popen([data[0], os.getcwd()])
	