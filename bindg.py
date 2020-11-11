#!c:/SDK/Anaconda2/python.exe

__version__ = "0.1"
__test__ = "0.2"
__sdk__ = "all"
__build__ = "2.7"
__author__ = "licface"
__platform__ = 'all'
__url__ = "licface@yahoo.com"
__email__ = "licface@yahoo.com"

import argparse
import os
import sys
import re
import configset as config_set 
import requests
THIS_PATH = os.path.dirname(__file__)
configname = os.path.join(THIS_PATH, 'bindg.ini')
configset = config_set.configset(configname)
EXT = configset.read_config('DB', 'EXT')
if EXT == None:
	EXT = "dns"

class bind(object):
	def __init__(self):
		super(bind, self)

	def makedomain(self, host, ip, typedns='bind', serial='2015080401', refresh='10800', retry='3600', expire='777600', min_ttl='3600', A=None, NS=None, MX=None, ftpA=None, mailA=None, wwwCNAME='@', ttl='10800'):
		data = [ip, host, serial, refresh, retry, expire, min_ttl, A, NS, MX, ftpA, mailA, wwwCNAME, ttl]
		if typedns == 'bind' or typedns == 'bind9':
			template = """$TTL {13}
@		IN SOA	{0}. root.{1}. (
			  {2}   ; Serial number
			  {3}        ; Refresh
			  {4}         ; Retry
			  {5}       ; Expire
			  {6}       ) ; Minimum TTL
		A	{7}
		NS	{8}.
		MX	10 mail.{9}.
ftp		A	{10}
mail		A	{11}
www		CNAME	{12}
""".format(*data)
		elif typedns == 'sdnsp' or typedns == 'sdnsplus' or typedns == 'simple' or typedns == 'simple dns plus' or typedns == 'simplednsplus':
			template = """
		$TTL {13}
@		IN SOA	( {0}. ; Primary DNS server
			  root.{1}. ; Responsible person
			  {2}   ; Serial number
			  {3}        ; Refresh
			  {4}         ; Retry
			  {5}       ; Expire
			  {6}       ) ; Minimum TTL
		A	{7}
		NS	{8}.
		MX	10 mail.{9}.
ftp		A	{10}
mail		A	{11}
www		CNAME	{12}
""".format(*data)

		# print "template =", template
		# print '-'*94
		# print "DB-PATH =", os.path.join(os.path.join(configset.read_config4('DB', 'PATH', configname))[0], str(host) + '.' + EXT)
		# print '-'*94
		fi = open(os.path.join(configset.read_config('DB', 'PATH', configname), str(host) + '.' + EXT), 'w')
		fi.write("\n")
		fi.write(template)
		fi.close()

	def formatData(self, data):# format data from tuple to dict
		data_dict = {}
		for i in data:
			data_dict.update({i[0]:i[1]})
		return data_dict

	def makedomain_http(self, url='http://127.0.0.1:8053', host=None, ip=None, data=None, serial='2015080401', refresh='10800', retry='3600', expire='777600', min_ttl='3600', A=None, NS=None, MX=None, ftpA=None, mailA=None, wwwCNAME='@', username='', password='', ttl='10800'):
		'''
			data = [[host, str], [ip, str], [username, str], [password, str]]
		'''

		if ip == None:
			return False
		if host == None:
			return False
		if A == None:
			A = ip
		if NS == None:
			NS = ip
		if ftpA == None:
			ftpA = ip
		if mailA == None:
			mailA = ip
		if MX == None:
			MX = host

		datax = [ip, host, serial, refresh, retry, expire, min_ttl, A, NS, MX, ftpA, mailA, wwwCNAME, ttl]

		template = """
		$TTL {13}
@		IN SOA	( {0}. ; Primary DNS server
			  root.{1}. ; Responsible person
			  {2}   ; Serial number
			  {3}        ; Refresh
			  {4}         ; Retry
			  {5}       ; Expire
			  {6}       ) ; Minimum TTL
		A	{7}
		NS	{8}.
		MX	10 mail.{9}.
ftp		A	{10}
mail		A	{11}
www		CNAME	{12}
"""
		if data != None:
			fdata = open(data,'r')
			requests.post(url + '/updatezone', {'data':fdata}, auth=(username, password))
			return None
		
		data_dict = {'zone': host}
		data_dict.update({'data': template.format(*datax), 'username': username, 'password': password})
		requests.post(url + '/updatezone', data_dict, auth=(username, password))
		return None
	
	def checkdomain(self, host, host_replace = None, data_overwrite = None):
		fi = open(configset.read_config('DB', 'CONFIG_PATH', configname), 'r').readlines()
		fi2 = open(configset.read_config('DB', 'CONFIG_PATH', configname), 'r').read()
		#fi3 = open(os.path.join(os.getenv('TEMP'), "bindg_config.temp"), 'w') 
		#file "c:/Apps/bind9/etc/zones/docs.modpythonxxxxxxxxxx.net.dns";
		files_replace = os.path.join(configset.read_config('DB', 'PATH', configname), (str(host) + ".dns"))
		files_replace = str(files_replace).replace("\\", "/")
		cfg = configset.read_config('DB', 'CONFIG_PATH', configname)
		for i in fi:
			if "zone " in i:
				if host in i:
					print "Exist Domain for domain:", host
					line0 = fi.index(i)
					line1 = line0 + 10
					for l in range(line0, line0 + 10):
						if "}" in fi[l]:
							line1 = l
							break
	
					data = " ".join(fi[line0:line1+1])
					#print "data =", data
					data_file = data.split("file ")
					#print "data_file =", data_file
					for f in data_file:
						if "}" in f:
							f1 = re.split('\r|\n|"', f)
							#print "f1 =", f1
							for f2 in f1:
								if str(f2).strip() != '' and str(f2).strip() != ';' and str(f2).strip() != '};':
									#print "f2 =", f2
									if data_overwrite:
										#print "overwrite"
										self.domainoverwrite(host, host_replace, f2, files_replace, 
						                    cfg)
					return False, data
		return True, None
	
	def domainoverwrite(self, host, host_replace, files, files_replace, fileconfig):
		#print "host         ::", host
		#print "host_replace ::", host_replace
		#print "files        ::", files
		#print "files_replace::", files_replace
		#print "fileconfig   ::", fileconfig
		fi1 = open(fileconfig, 'r')
		fi11 = fi1.read()
		fi11 = re.sub(host, host_replace, fi11)
		fi11 = re.sub(files, files_replace, fi11)
		#fi11.replace(host, host_replace)
		#fi11.replace(files, files_replace)
		#print "fi1 =", fi1
		#print "-" * 220
		#import clipboard
		#clipboard.copy(fi11)
		fi2 = open(fileconfig, 'w')
		fi2.write(fi11)
		#print "file rewrite =", fi2.name
		fi2.close()

	def insertdomain(self, host, typehost='master', dbpath=None, configpath=None, overwrite = None):
		if self.checkdomain(host)[0]:
			if dbpath == None:
				dbpath = os.path.join(configset.read_config('DB', 'PATH', configname), str(host) + "." + EXT)
			else:
				dbpath = os.path.join(dbpath, str(host) + "." + EXT)
		
			template = """zone "%s" {
			type %s;
			file "%s";
	};"""%(host, typehost, dbpath)
			
			if configpath == None:
				fi = open(configset.read_config('DB', 'CONFIG_PATH', configname), 'a')
			else:
				fi = open(configpath, 'a')
			fi.write("\n")
			fi.write(template)
			fi.close()
		else:
			print "Domain is Exists ! (%s)" % (host)
			q = raw_input('Overwrite it ![y/n]:')
			if q.lower() == 'y':
				self.checkdomain(host, host, True)

	def control(self, host, ip, typehost='master', dbpath=None, configpath=None, typedns='bind', serial='2015080401', refresh='10800', retry='3600', expire='777600', min_ttl='3600', A=None, NS=None, MX=None, ftpA=None, mailA=None, wwwCNAME='@', ttl='10800', username='admin', password='', serverUrl='http://127.0.0.1:8053', data=None):
		print "TYPE DNS =", typedns
		if typedns == 'bind':
			print "write domain bind:%s" % (host)
			self.makedomain(host, ip, typedns, serial, refresh, retry, expire, min_ttl, A, NS, MX, ftpA, mailA, wwwCNAME, ttl)
			self.insertdomain(host, typehost, dbpath)
		elif typedns == 'sdnsp' or typedns == 'sdnsplus' or typedns == 'simple' or typedns == 'simple dns plus' or typedns == 'simplednsplus':
			print "write domain sdnsp:%s" % (host)
			self.makedomain_http(serverUrl, host, ip, data, serial, refresh, retry, expire, min_ttl, A, NS, MX, ftpA, mailA, wwwCNAME, username, password, ttl)
		else:
			self.usage(True)

	def usage(self, print_help=None):
		parser = argparse.ArgumentParser(formatter_class= argparse.RawTextHelpFormatter)
		parser.add_argument('-H', '--host', help='Host Domain Name, example: host:ip, example.com:192.168.1.0, example2.com, single host must use with -i or you can use ":" for separate', action='store', nargs = '*')
		parser.add_argument('-i', '--ip', help='IP Host Domain Name', action='store')
		parser.add_argument('-t', '--type', help='Type Host Domain Name [master, slave], default=master', default='master', action='store')
		parser.add_argument('-c', '--config', help='Config file name path, default=path of bind installer (Bind Only)', action='store')
		parser.add_argument('-z', '--zone-path', help='Zone Config path, default=path of bind installer (Bind Only)', action='store')
		parser.add_argument('-d', '--type-dns', help='Type Dns Server, default=bind option:pdnsp', default='bind', action='store')
		parser.add_argument('-s', '--serial', help='Serial Number (option)', action='store', default='2015080401')
		parser.add_argument('-R', '--refresh', help='Refresh Time Record (option)', action='store', default='10800')
		parser.add_argument('-r', '--retry', help='Retry Time from timeout (failover) (option)', action='store', default='3600')
		parser.add_argument('-e', '--expire', help='Expire Time for valid Dns Record (option)', action='store', default='777600')
		parser.add_argument('-l', '--min-ttl', help='Minimum TTL Time (option)', action='store', default='3600')
		parser.add_argument('-L', '--ttl', help='TTL Time (option)', action='store', default='10800')
		parser.add_argument('-w', '--www-cname', help='wwwCNAME Dns Record (option)', action='store', default='@')
		parser.add_argument('-A', '--ANAME', help='A Dns Record (option)', action='store')
		parser.add_argument('-NS', '--NSNAME', help='NS Dns Record (option)', action='store')
		parser.add_argument('-MX', '--MXNAME', help='MX Dns Record (option)', action='store')
		parser.add_argument('-f', '--ftpA', help='Ftp Dns Record (option)', action='store')
		parser.add_argument('-m', '--mailA', help='Mail Dns Record (option)', action='store')
		parser.add_argument('-u', '--username', help='Username for SimpleDNSPlus (option)', action='store')
		parser.add_argument('-p', '--password', help='Password for SimpleDNSPlus (option)', action='store')
		parser.add_argument('-U', '--url', help='Url for SimpleDNSPlus (option), example: http://127.0.0.1:8053', action='store')
		parser.add_argument('-D', '--data', help='File contain Dns Record for SimpleDNSPlus (option)', action='store')
		if len(sys.argv) == 1:
			parser.print_help()
		elif print_help:
			parser.print_help()
		else:
			args = parser.parse_args()
			if args.host:
				if isinstance(args.host, list):
					for i in args.host:
						if ":" in i:
							host, ip = str(i).split(":")
							if args.MXNAME == None:
								args.MXNAME = host
							if args.ANAME == None:
								args.ANAME = ip
							if args.NSNAME == None:
								args.NSNAME = ip
							if args.ftpA == None:
								args.ftpA = ip
							if args.mailA == None:
								args.mailA = ip							
							self.control(host, ip, args.type, args.zone_path, args.config, args.type_dns, args.serial, args.refresh, args.retry, args.expire, args.min_ttl, args.ANAME, args.NSNAME, args.MXNAME, args.ftpA, args.mailA, args.www_cname, args.ttl, args.username, args.password, args.url, args.data)
						else:
							if args.MXNAME == None:
								args.MXNAME = i
							if args.ANAME == None:
								args.ANAME = args.ip
							if args.NSNAME == None:
								args.NSNAME = args.ip
							if args.ftpA == None:
								args.ftpA = args.ip
							if args.mailA == None:
								args.mailA = args.ip							
							if args.ip:
								self.control(i, args.ip, args.type, args.zone_path, args.config, args.type_dns, args.serial, args.refresh, args.retry, args.expire, args.min_ttl, args.ANAME, args.NSNAME, args.MXNAME, args.ftpA, args.mailA, args.www_cname, args.ttl, args.username, args.password, args.url, args.data)
							else:
								print "PLEASE DEFINTION YOUR ADDRESS/IP HOST (001) !\n"
								parser.print_help()
				else:
					if args.MXNAME == None:
						args.MXNAME = args.host
					if args.ANAME == None:
						args.ANAME = args.ip
					if args.NSNAME == None:
						args.NSNAME = args.ip
					if args.ftpA == None:
						args.ftpA = args.ip
					if args.mailA == None:
						args.mailA = args.ip					
					if args.ip:
						self.control(args.host, args.ip, args.type, args.zone_path, args.config, args.type_dns, args.serial, args.refresh, args.retry, args.expire, args.min_ttl, args.ANAME, args.NSNAME, args.MXNAME, args.ftpA, args.mailA, args.www_cname, args.ttl, args.username, args.password, args.url, args.data)
					else:
						print "PLEASE DEFINTION YOUR ADDRESS/IP HOST (002) !\n"
						parser.print_help()
if __name__ == '__main__':
	c = bind()
	c.usage()
	#def checkdomain(self, host, host_replace = None, data_overwrite = None):
	#c.checkdomain(sys.argv[1], sys.argv[2], True)