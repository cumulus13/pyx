#  import requests
#  import clipboard
#  import urllib.parse
#  import sys
#  BASE = 'https://render-tron.appspot.com/screenshot/'
#  url = sys.argv[1]
#  if url == 'c':
	#  url = clipboard.paste()
#  url = urllib.parse.quote_plus(url)
#  print("url =", url)
#  path = sys.argv[2]
#  response = requests.get(BASE + url, stream=True)
#  print("code =", response.status_code)
#  if response.status_code == 200: 
	#  with open(path, 'wb') as file:
		#  for chunk in response:
			#  file.write(chunk)
#  print(path)

import requests
import clipboard
import urllib.parse
import sys

BASE = 'https://mini.s-shot.ru/1024x0/JPEG/1024/Z100/?'
url = sys.argv[1]
if url == 'c':
	url = clipboard.paste()
url = urllib.parse.quote_plus(url)
print("url =", url)
path = sys.argv[2]
response = requests.get(BASE + url, stream=True)
if response.status_code == 200:
	with open(path, 'wb') as file:
		for chunk in response:
			file.write(chunk)