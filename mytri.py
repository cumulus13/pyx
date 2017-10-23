#!/usr/bin/python

import requests
from bs4 import BeautifulSoup as bs

class mytri(object):
	def __init__(self):
		super(mytri,self)
		self.masterURL = 'http://internet.tri.co.id'

	def getUrl(self):
		a = requests.post(self.masterURL)
		# print "status =", a.status_code
		return unicode(a.text).encode('utf-8')

	def getUrlCheck(self):
		a = False
		while 1:
			if a == False:
				try:
					a = self.getUrl()
				except:
					sys.stdout.write(".")
					a = False
			else:
				break
		print "\n"
		return a


	def getSisa(self, text):
		a = bs(text)
		b = a.find('div', {'class':'proListImgCon'})
		c = b.find_next('img', {'class':'proListImg'})
		# print "b =", b
		# print "-"*100
		# print "c =", c
		# print "type(c) =", type(c)
		# print "dir(c) =", dir(c)
		# print "+" * 100
		# d = c.findNext('img', {'class':'proListImg'})
		# print "SISA:", c.getText()
		# print "SISA:", c.get_text()
		print "SISA:", c.get('title')

if __name__ == '__main__':
	import warnings
	with warnings.catch_warnings():
		warnings.filterwarnings("ignore")

		c = mytri()
		import sys
		sys.stdout.write("Loading .")
		text = c.getUrlCheck()
		c.getSisa(text)