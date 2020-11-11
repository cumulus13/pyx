#!c:/SDK/Anaconda2/python.exe
#encoding:utf-8

import os
import sys
from make_colors import make_colors
from debug import debug
import re
from getpass import getpass

class netuse(object):
	def __init__(self):
		super(netuse, self)
		self.username = None
		self.password = None

	def getList(self):
		lists = []
		list_01 = os.popen("NET USE").readlines()
		for i in list_01:
			if i == "\n":
				list_01.remove(i)
		# print "list_01 =", list_01[3:]
		debug(list_01=list_01)
		for i in list_01[3:]:
			x = re.sub("   |Microsoft Windows Network|The command completed successfully.|---|\n", "", i)
			if x == '':
				pass
			else:
				x = re.split(" ", x)
				# print "x =", x
				debug(x = x)
				lists.append(x)
		# print "LISTS =", lists
		debug(lists=lists)
		return lists

	def check(self):
		note1 = make_colors("delete|del|d, change|ch|c, skip|s|p|pass", "lightwhite", 'lightred')
		note2 = ['delete', 'del', 'd', 'change', 'ch', 'c', 'skip', 's', 'p', 'pass']
		lists = self.getList()
		for i in lists:
			for z in i:
				if z == '':
					i.remove(z)
			debug(i=i)
			debug(i_1=i[1])
			# debug(i_2=i[2][2:])
			if i[0].lower() == 'unavailable' or i[0].lower() == 'disconnected':
				for z in i:
					if z == '':
						i.remove(z)
				debug(i=i)
				print make_colors("re init:", 'lightwhite', "lightred"), make_colors(i[1], 'black', 'lightyellow'), make_colors(i[2], 'black', 'lightgreen'), note1
				# print make_colors(i[1], 'black', 'lightgreen') + " " + make_colors(i[2], 'black', 'lightyellow')
				if not self.username:
					self.username = raw_input("USERNAME: ")
				if self.username and not self.username in note2:
					if not self.password:
						self.password = getpass('PASSWORD: ')
					if self.password:
						os.system("NET USE %s %s %s /user:%s"%(i[1], i[2], str(self.password), str(self.username)))
				elif self.username == 'delete' or self.username == 'del' or self.username == 'd':
					os.system("NET USE %s /delete"%(i[1]))
				elif self.username == 'change' or self.username == 'ch' or self.username == 'c':
					debug(i=i)
					os.system("NET USE %s /delete"%(i[1]))
					drive = raw_input("DRIVE [%s]: "%(i[1]))
					path = raw_input("PATH [%s]: "%(i[2]))
					if not drive:
						drive = i[1]
					if not path:
						path = i[2]
					if not self.username:
						self.username = raw_input("USERNAME: ")
					if self.username:
						if not self.password:
							self.password = getpass('PASSWORD: ')
					if self.password:
						os.system("NET USE %s %s %s /user:%s"%(drive, path, self.password, self.username))
				elif self.username == 'skip' or self.username == 's' or self.username == 'p' or self.username == 'pass':
					pass
		os.system("NET USE")

if __name__ == '__main__':
	c = netuse()
	c.check()