import os
import sys
import optparse
import re

class setdns(object):
	def __init__(self):
		super(setdns, self)

	def showdns(self, device, verbosity):
		print "\n"
		dns_list = []
		if verbosity == 1:
			verbose = ' '
		else:
			verbose = '  > NUL'
		data = os.popen('netsh interface ip show dnsservers %s' %(device)).readlines()
		data_1 = []
		for i in data:
			if str(i).strip() != '':
				data_1.append(str(i).split('\n')[0].strip())
		for i in data_1:
			ip = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", i)
			if len(ip) > 0:
				dns_list.append(ip[0])

		if len(dns_list) > 1:
			print "Primary : ", dns_list[0]
		for i in range(1, len(dns_list)):
			print "        : ", dns_list[i]

	def getDevice(self):
		p = os.popen('netsh interface show interface').readlines()
		p1 = []
		p2 = []
		for i in p:
			if str(i).strip() == '\n' or str(i).strip() == '':
				pass
			else:
				p1.append(i)
		for i in p1:
			if "Enabled" in i or "Disabled" in i:
				a = str(i).split(" ")[-1]
				b = str(a).split("\n")[0]
				p2.append(str(b).lower())
		return p2

	def setdns(self, dns, device, index=None, verbosity=None, quite=None, start=None):
		if verbosity == 1:
			verbose = ' '
		else:
			verbose = '  > NUL'
		# print "len(dns)  =", len(dns)
		# print "type(dns) =", type(dns)
		# print "dns       =", dns
		if isinstance(dns, list):
			if len(dns) == 1:
				if index:
					if index == 0:
						os.system('netsh interface ip del dnsservers %s %s %s' %(device, dns[0], verbose))
						os.system('netsh interface ip set dnsservers %s static %s primary %s' %(device, str(dns[0]), verbose))
					else:
						os.system('netsh interface ip del dnsservers %s %s %s' %(device, dns[0], verbose))
						os.system('netsh interface ip add dnsservers %s index=%s %s' %(device, str(index[0]), verbose))	
				else:
					os.system('netsh interface ip del dnsservers %s %s %s' %(device, "all", verbose))
					os.system('netsh interface ip set dnsservers %s static %s primary %s' %(device, str(dns[0]), verbose))
			elif len(dns) > 1:
				if index:
					if len(dns) == len(index):
						for i in dns:
							os.system('netsh interface ip del dnsservers %s %s %s' %(device, "all", verbose))
							if index[dns.index(i)] == 1 or index[dns.index(i)] == 0:
								os.system('netsh interface ip set dnsservers %s static %s primary %s' %(device, str(i), verbose))
							else:
								os.system('netsh interface ip add dnsservers %s %s index=%s %s' %(device, str(i), str(index[dns.index(i)]), verbose))
					else:
						print "WARNINGS: Your len index not same with len dns"
						if index:
							if index == 0:
								os.system('netsh interface ip del dnsservers %s %s %s' %(device, dns[0], verbose))
								os.system('netsh interface ip set dnsservers %s static %s primary %s' %(device, str(dns[0]), verbose))
							else:
								os.system('netsh interface ip del dnsservers %s %s %s' %(device, "all", verbose))
								os.system('netsh interface ip add dnsservers %s index=%s %s' %(device, str(index[0]), verbose))	
				else:
					if quite == False:
						q = raw_input("Do you want to continue ?: ")
						if str(q).lower() == 'y':
							if int(start) == 0:
								os.system('netsh interface ip del dnsservers %s %s %s' %(device, "all", verbose))
								os.system('netsh interface ip set dnsservers %s static %s primary %s' %(device, str(dns[0]), verbose))
								for i in range(1, len(dns)):
									os.system('netsh interface ip del dnsservers %s %s %s' %(device, str(dns[i]), verbose))
									os.system('netsh interface ip add dnsservers %s %s index=%s %s' %(device, str(dns[i]), str(i+1), verbose))
							else:			
								for i in range(1, len(dns)):
									os.system('netsh interface ip del dnsservers %s %s %s' %(device, str(dns[i]), verbose))
									os.system('netsh interface ip add dnsservers %s %s index=%s %s' %(device, str(dns[i]), str(i+1), verbose))
					else:
						if int(start) == 0:
							os.system('netsh interface ip del dnsservers %s %s %s' %(device, "all", verbose))
							os.system('netsh interface ip set dnsservers %s static %s primary %s' %(device, str(dns[0]), verbose))
							for i in range(1, len(dns)):
								os.system('netsh interface ip del dnsservers %s %s %s' %(device, str(dns[i]), verbose))
								os.system('netsh interface ip add dnsservers %s %s index=%s %s' %(device, str(dns[i]), str(i+1), verbose))
						else:	
							for i in range(1, len(dns)):
								os.system('netsh interface ip del dnsservers %s %s %s' %(device, str(dns[i]), verbose))
								os.system('netsh interface ip add dnsservers %s %s index=%s %s' %(device, str(dns[i]), str(i+1), verbose))
			else:
				WindowsError('Please Definition your dns ip !')

	def usage(self):
		usage = "setdns [-N]|[dns1 dns2 dns3] [-D]|[wi-fi] [Options]"
		parser = optparse.OptionParser(usage=usage)
		parser.add_option('-N', '--dns', help='Alias Dns Ip', nargs='*', action='store')				
		parser.add_option('-D', '--device', help='Alias Device/NIC', action='store')
		parser.add_option('-d', '--delete', help='Delete DNS Server', action='store_true')
		parser.add_option('-i', '--index', help='Index DNS Server', action='store', nargs="*")
		parser.add_option('-q', '--quite', help='No Question', action='store_true')
		parser.add_option('-v', '--verbosity', help='Verbosity', action='count')
		parser.add_option('-s', '--start', help='Start Index', action='store', default=1)
		parser.add_option('-S', '--show', help='Show all dns server on device', action='store_true')
		options, args = parser.parse_args()
		# print "options =", options
		# print "args    =", args
		# print "getDevice =", self.getDevice()
		# print "len(sys.argv) =", len(sys.argv)
		if len(sys.argv) > 1:
			ip_data = []
			device_data = []
			if len(args) > 0:
				for i in args:
					ip = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", i)
					if len(ip) > 0:
						ip_data.append(ip[0])
					if i in self.getDevice():
						device_data.append(i)

			if options.delete:
				if options.dns:
					for i in options.dns:
						os.system('netsh interface ip del dnsservers %s %s > NUL' %(options.device, str(i)))
				else:
					if ip_data > 0:
						if options.device:
							for i in ip_data:
								os.system('netsh interface ip del dnsservers %s %s > NUL' %(options.device, str(i)))		
						else:
							if device_data > 0:
								for i in ip_data:
									os.system('netsh interface ip del dnsservers %s %s > NUL' %(device_data[0], str(i)))			
			elif options.show:
				if options.device:
					self.showdns(options.device, options.verbosity)
				else:
					for i in args:
						if i in self.getDevice():
							self.showdns(i, options.verbosity)		 
			else:
				error_report = []
				check = {'ip':False, 'device': False}
				if len(args) > 0:
					for i in args:
						if len(ip_data) > 0:
							check.update({'ip':True})
							if len(device_data) > 0:
								check.update({'ip':True, 'device':True})
							else:
								error_report.append("No len one of device name")
					error_report = list(set(error_report))
					for i in error_report:
						print i
				else:
					self.setdns(options.dns, options.device, options.index, options.verbosity, options.quite, options.start)

				if check.get('ip') and check.get('device'):
					self.setdns(ip_data, device_data[0], options.index, options.verbosity, options.quite, options.start)
		else:
			parser.print_help()

if __name__ == '__main__':
	c = setdns()
	c.usage()
	# c.getDevice()
