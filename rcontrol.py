#!/usr/bin/python

import optparse
import sys
import re
import getpass
import vping

__version__ = "0.1"
__test__ = "0.8"
__author__ = "LICFACE"
__url__ = "www.licface.tk"
__email__ = "licface13@gmail.com"
__sdk__ = "2.7"
__platform__ = "All"
__requirement__ = "pyping, requests"

"""
	use option -h for manual help, Thank's
"""

class control:
	def __init__(self, parent=None):
		self.master_url = "http://192.168.43.1"
		self.username = "admin"
		self.password = None
		self.max_time = 100

	def getVersion(self):
		return __version__ + "." + __test__

	def connect(self, url="/goform/contorl", master_url=None, username=None, password=None):
		import requests
		if not master_url == None:
			self.master_url = master_url
		if not username == None:
			self.username = username
		if not password == None:
			self.password = password
		r = requests.get(self.master_url + url, auth=(self.username, self.password))
		return r.status_code

	def disconnect(self, url="/goform/contorl_dis", master_url=None, username=None, password=None):
		import requests
		if not master_url == None:
			self.master_url = master_url
		if not username == None:
			self.username = username
		if not password == None:
			self.password = password
		r = requests.get(self.master_url + url, auth=(self.username, self.password))
		return r.status_code

	def get_datauser(self, i):
		excp = ['-c','--connect','-d','--disconnect','-u','--username','-p','--password','-m','--master-url']
		try:
			check_username = re.split(" |<|>|'", str(type(sys.argv[sys.argv.index(i) + 1])))[-3]
			if check_username == 'str':
				if sys.argv[sys.argv.index(i) + 1] not in excp:
					self.username = sys.argv[sys.argv.index(i) + 1]
				else:
					if self.username == None or str(self.username).strip() == '':
						self.username = getpass.getpass("Username: ")
			else:
				if self.username == None or str(self.username).strip() == '':
					self.username = getpass.getpass("Username: ")
		except:
			if self.username == None or str(self.username).strip() == '':
				self.username = getpass.getpass("Username: ")
		return self.username

	def get_datapassword(self, i):
		excp = ['-c','--connect','-d','--disconnect','-u','--username','-p','--password','-m','--master-url']
		try:
			check_password = re.split(" |<|>|'", str(type(sys.argv[sys.argv.index(i) + 1])))[-3]
			if check_password == 'str':
				if sys.argv[sys.argv.index(i) + 1] not in excp:
					self.password = sys.argv[sys.argv.index(i) + 1]
				else:
					if self.password == None or str(self.password).strip() == '':
						self.password= getpass.getpass("Password: ")
			else:
				if self.password == None or str(self.password).strip() == '':
					self.password= getpass.getpass("Password: ")
		except:
			if self.password == None or str(self.password).strip() == '':
				self.password = getpass.getpass("Password: ")
		return self.password

	def usage(self):
		parser = optparse.OptionParser()
		parser.add_option("-c", "--connect", help="Connect 3/4 G Router", action="store_true")
		parser.add_option("-d", "--disconnect", help="Disconnect 3/4 G Router", action="store_true")
		parser.add_option("-r", "--reconnect", help="Re-Connect 3/4 G Router", action="store_true")
		parser.add_option("-u", "--username", help="Username for connection", action="store", default='admin')
		parser.add_option("-p", "--password", help="Password for connection", action="store")
		parser.add_option("-m", "--master-url", help="IPAddress/Hostname of Router", action="store")
		parser.add_option('-R', "--retry", help='Retry time for connecting from disconnect [Re-Connect]', action='store', default=10)
		parser.add_option('-v', '--version', help='-v = version | -vv = verbosity', action='count')
		options, args = parser.parse_args(sys.argv)

		if options.version == 1:
			print "version:", self.getVersion()

		def connect():
			max_time = 0
			if options.disconnect:
				pass
			if options.password:
				check_conn = self.connect(master_url=options.master_url, username=options.username, password=options.password)
				username = options.username
				password = options.password
			else:
				username = getpass.getpass("Username: ")
				if username == None or username == '':
					username == 'admin'
				password = getpass.getpass("Password: ")
				self.username = username
				self.password = password
				if password != '' or password != None:
					check_conn = self.connect(master_url=options.master_url, username=username, password=password)
				else:
					check_conn = self.connect(master_url=options.master_url, username=self.username, password=self.password)
			if check_conn > '203':
				if self.password == None:
					username = getpass.getpass("Username: ")
					if username == None or username == '':
						username == 'admin'
					password = getpass.getpass("Password: ")
				check_conn = self.connect(master_url=options.master_url, username=username, password=password)
				if check_conn > '203':
					print "Incorrect USERNAME or PASSWORD [connecting]"
					if platform.uname()[0] == 'Windows':
						return IOError("Incorrect USERNAME or PASSWORD")

			sys.stdout.write("connecting ")
			while vping.vping("8.8.8.8", count=1) == False:
				max_time = max_time + 1
				retry = int(options.retry)
				if max_time == 10:
					retry = retry + 1
				sys.stdout.write(".")
				if max_time == 100:
					sys.stdout.write(" Maybe ERROR, you took so long time - Please ensure your internet connecting | ")
					break
				elif max_time == retry or max_time == (2*retry):
					self.connect(master_url=options.master_url, username=username, password=password)

			sys.stdout.write(" DONE")
			sys.stdout.write(" \n")

		def disconnect():
			max_time = 0
			if options.connect:
				pass
			if options.password:
				# print "USERNAME =", options.username
				# print "PASSWORD =", options.password
				check_conn = self.disconnect(master_url=options.master_url, username=options.username, password=options.password)
				username = options.username
				password = options.password
				# print "CHECK CON =", check_conn
			else:
				username = getpass.getpass("Username: ")
				if username == None or username == '':
					username == 'admin'
				password = getpass.getpass("Password: ")
				self.username = username
				self.password = password
				if password != '' or password != None:
					check_conn = self.disconnect(master_url=options.master_url, username=username, password=password)
				else:
					check_conn = self.disconnect(master_url=options.master_url, username=self.username, password=self.password)
			if check_conn > '203':
				if self.password == None:
					username = getpass.getpass("Username: ")
					if username == None or username == '':
						username == 'admin'
					password = getpass.getpass("Password: ")
				check_conn = self.disconnect(master_url=options.master_url, username=username, password=password)
				print "check_conn =", check_conn
				if check_conn  > '203':
					print "Incorrect USERNAME or PASSWORD [disconnecting]"
					return IOError("Incorrect USERNAME or PASSWORD")
			sys.stdout.write("disconnecting ")
			while vping.vping("8.8.8.8", count=1) == True:
				sys.stdout.write(".")
				if max_time == 100:
					break
			sys.stdout.write(" DONE")
			sys.stdout.write(" \n")

		# for i in sys.argv:
		# 	if "-u" in i:
		# 		username = self.get_datauser(i)
		# 	elif "-p" in i:
		# 		password = self.get_datapassword(i)

		if len(sys.argv) > 1:
			if options.connect:
				connect()

			if options.disconnect:
				disconnect()
			
			if options.reconnect:
				disconnect()
				connect()
		else:
			parser.print_help()

def test_usage():
	try:
		parser = optparse.OptionParser()
		parser.add_option("-c", "--connect", help="Connect 3/4 G Router", action="store_true")
		parser.add_option("-d", "--disconnect", help="Disconnect 3/4 G Router", action="store_true")
		parser.add_option("-u", "--username", help="Username for connection", action="store_true")
		parser.add_option("-p", "--password", help="Password for connection", action="store_true")
		parser.add_option("-m", "--master-url", help="IPAddress/Hostname of Router", action="store")
		options, args = parser.parse_args(sys.argv)
		excp = ['-c','--connect','-d','--disconnect','-u','--username','-p','--password','-m','--master-url']
		for i in sys.argv:
			if "-u" in i:
				print True
				check_username = re.split(" |<|>|'", str(type(sys.argv[sys.argv.index(i) + 1])))[-3]
				if check_username == 'str':
					if sys.argv[sys.argv.index(i) + 1] not in excp:
						print "Username =", sys.argv[sys.argv.index(i) + 1]

		print "args 0 =", args
		print "options 0 =", options
		if len(sys.argv) > 1:
			if options.connect:
				print "connecting ...."
				print "args =", args
				print "options =", options
			if options.disconnect:
				print "disconnecting ...."
				print "args =", args
				print "options =", options
		else:
			parser.print_help()
	except:
		import traceback
		print traceback.format_exc()

if __name__ == "__main__":
	c = control()
	c.usage()
	#test_usage()
	#print ping.vping("8.8.8.8", count=1)
