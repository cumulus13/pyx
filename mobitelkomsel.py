import requests
import bs4
import re
import time
import sys
import argparse
import platform

__version__ 	= "1.1"
__build__   	= "2.7"
__test__    	= "0.6"
__author__  	= "licface"
__email__   	= "licface@yahoo.com"
__platform__ 	= "any"

class mobi(object):
	def __init__(self, simple = None):
		super(mobi, self)
		self.simple = simple
		try:
			self.url = requests.get('http://mobi.telkomsel.com/profil/profileinternet/profileinternet')
		except:
			print "Absolute Error Exception Failed Connection with url !"
			sys.exit(0)
		if platform.system() == 'Linux':
			self.soup = bs4.BeautifulSoup(self.url.text, "lxml")
		else:
			self.soup = bs4.BeautifulSoup(self.url.text)
			
	def getNumber(self):
		#soup = bs4.BeautifulSoup(self.url.text)
		a = self.soup.find_all('span', 'usermsidn')
		b = re.split("<|>", str(a[0]))[-3]
		return b

	def telkomsel(self, simple = None, timeout = 30):
		if simple == None:
			simple = self.simple

		number = self.getNumber()
		if self.url.ok:
			#soup = bs4.BeautifulSoup(self.url.text)
			a1 = []
			a2 = []
			for i in self.soup.find_all('table'):
				a = str(i.text).split("\n")
				for j in a:
					if str(j).strip() != '':
						a2.append(str(j).strip())
				a1.append(a2)
				a2 = []
		else:
			self.url.close()
			return False
		
		if len(a1) > 0:
			for i in range(len(a1)):
				if i != len(a1) - 1:
					if a1[i][1:] == a1[i+1]:
						if simple:
							print number, "|",a1[i][1+1] 
						else:
							print "\n"
							print "Number",(' '*(34 - len("number"))), "=", number
							print a1[i][0],":"
							print "\t",a1[i][1],(' '*(26 - len(a1[i][1]))), "=", a1[i][1+1]
							print "\t",a1[i][3],(' '*(26 - len(a1[i][3]))), "=", a1[i][3+1]
							print "*"*64
			return True
		else:
			return False
		
	def getStatus(self, simple = None, timeout = None):
		if timeout == None:
			timeout == 30
		return self.telkomsel(simple, timeout)

def run(simple = None, timeout = 50):
	c = mobi()
	i = 0
	sys.stdout.write("connecting ...")
	while True:
		if c.getStatus(simple, timeout):
			break
		else:
			self.url.close()
			i += 1
			sys.stdout.write(".")
		if i == 50:
			print "error"
			break
		else:
			time.sleep(1)
				
def usage():
	c = mobi()
	parser = argparse.ArgumentParser()
	parser.add_argument('-s', '--simple', help = 'show simple view', action = 'store_true')
	parser.add_argument('-t', '--timeout', help = 'timeout time', action = 'store')
	if len(sys.argv) > 1:
		args = parser.parse_args()
		run(args.simple, args.timeout)
	else:
		parser.print_help()
		print "\n"
		run()
		
if __name__ == '__main__':
	usage()
	# c = mobi()
	# if c != False:
	# 	c.usage()
	# else:
	# 	print "Can't connect to server !"