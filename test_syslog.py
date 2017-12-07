#!/user/bin/python
# -*- encoding: iso-8859-1 -*-

import sys
import os
import argparse
from datetime import datetime
import termcolor
DEBUG = False
FACILITY = [
    'Kern   : 0',
    'User   : 8',
    'Mail   : 16',
    'Daemon : 24',
    'Auth   : 32',
    'Syslog : 40',
    'Lpr    : 48',
    'News   : 56',
    'UUCP   : 64',
    'Cron   : 72',
    'Local0 : 128', 
    'Local1 : 136',
    'Local2 : 144', 
    'Local3 : 152', 
    'Local4 : 160', 
    'Local5 : 168', 
    'Local6 : 176', 
    'Local7 : 184', 
]

def makeList(alist, ncols, vertically=True, file=None):
	from distutils.version import StrictVersion  # pep 386
	import prettytable as ptt  # pip install prettytable
	import sys
	assert StrictVersion(ptt.__version__) >= StrictVersion(
        '0.7')  # for PrettyTable.vrules property
	L = alist
	nrows = - ((-len(L)) // ncols)
	ncols = - ((-len(L)) // nrows)
	t = ptt.PrettyTable([str(x) for x in range(ncols)])
	t.header = False
	t.align = 'l'
	t.hrules = ptt.NONE
	t.vrules = ptt.NONE
	r = nrows if vertically else ncols
	chunks = [L[i:i + r] for i in range(0, len(L), r)]
	chunks[-1].extend('' for i in range(r - len(chunks[-1])))
	if vertically:
		chunks = zip(*chunks)
	for c in chunks:
		t.add_row(c)
	print termcolor.colored(t, 'green')

def usage(print_help = False):
	global DEBUG
	parse = argparse.ArgumentParser(formatter_class= argparse.RawTextHelpFormatter)
	parse.add_argument('SEVERITY', action = 'store', help = 'Severity Number', type = int)
	parse.add_argument('FACILITY', action = 'store', help = 'Facility Number', type = int)
	parse.add_argument('HOST', action = 'store', help = 'Host or IpAddress, example: 192.168.1.2 or 192.168.1.2:519', nargs = '*')
	parse.add_argument('-p', '--port', action = 'store', help = 'Port Number (default: 514), if given then host with example: "192.168.1.2:519" and other all of it will change to host:port which port is given it so it change to "192.168.1.2:[port]"', type = int, nargs = '*')
	parse.add_argument('-m', '--message', action = 'store', help = 'Message to sent (default: "test message"', type = str, default = "test message")
	parse.add_argument('-d', '--date', action = 'store', help = 'Date and time to sent, format example: "%s", default is date and time this day' % (datetime.strftime(datetime.now(), "%b %d %H:%M:%S")), default = datetime.strftime(datetime.now(), "%b %d %H:%M:%S"))
	parse.add_argument('-t', '--tag', action = 'store', help = 'Tag name, default:"TEST"', default = 'TEST')
	parse.add_argument('-i', '--pid', action = 'store', help = 'PID Number, default this pid process')
	parse.add_argument('-v', '--debug', action = 'store_true')
	parse.add_argument('-l', '--list-facility', action = 'store_true')
	if len(sys.argv) == 1:
		parse.print_help()
	elif print_help:
		parse.print_help()
	else:
		args = parse.parse_args()
		if args.debug:
			DEBUG = args.debug
			print "ARGS:", args
		if args.list_facility:
			makeList(FACILITY, 4)
		else:
			makeList(FACILITY, 4)
			main(args.SEVERITY, args.FACILITY, args.message, args.HOST, args.port, args.tag, args.date, args.pid, args.debug)
		
def sender(logger, severity, facility, message, host, port, tag, timestamp, pid, debug):
	if DEBUG:
		print "=" * 200
		print "DEBUG             :", DEBUG
		print "SEVERITY          :", severity
		print "FACILITY          :", facility
		print "MESSAGE           :", message
		print "HOST              :", host
		print "PORT              :", port
		print "TAG               :", tag
		print "DATETIME          :", timestamp
		print "PID               :", pid
		print "debug             :", debug
		print "+" * 200
	import netsyslog
	if isinstance(port, list) and len(port) > 0:
		if len(port) == 1:
			logger.PORT = int(port)
		else:
			for p in port:
				logger.PORT = int(p)
				logger.add_host(host)
				pri = netsyslog.PriPart(int(facility), int(severity))
				header = netsyslog.HeaderPart(timestamp, host)
				message = netsyslog.MsgPart(str(tag), str(message), pid)
				packet = netsyslog.Packet(pri, header, message)
				logger.send_packet(packet)
	else:
		logger.PORT = int(port)
		logger.add_host(host)
		pri = netsyslog.PriPart(int(facility), int(severity))
		header = netsyslog.HeaderPart(timestamp, host)
		message = netsyslog.MsgPart(str(tag), str(message), pid)
		packet = netsyslog.Packet(pri, header, message)
		logger.send_packet(packet)
	if debug:
		print "PACKET:", repr(packet)	

def main(severity, facility, message, host, port = [], tag = 'TEST', timestamp = None, pid = None, debug = False):
	if DEBUG:
		print "DEBUG             :", DEBUG
		print "SEVERITY          :", severity
		print "FACILITY          :", facility
		print "MESSAGE           :", message
		print "HOST              :", host
		print "PORT              :", port
		print "TAG               :", tag
		print "DATETIME          :", timestamp
		print "PID               :", pid
		print "debug             :", debug
	if not port:
		port = [514]
	if not timestamp:
		timestamp = datetime.strftime(datetime.now(), "%b %d %H:%M:%S")
	if not pid:
		pid = str(os.getpid())
		
	def use_netsyslog(severity, facility, message, host, port, tag, timestamp, pid, debug):
		#makeList(FACILITY, 4)
		if not int(severity) == 0:
			severity = abs(int(severity))
		if not facility == 0:
			facility = abs(int(facility))
		import netsyslog
		if not str(severity).isdigit():
			usage(True)
			sys.exit(0)
			
		if not str(facility).isdigit():
			usage(True)
			sys.exit(0)
		if not len(message) >= 4:
			usage(True)
			sys.exit(0)
		logger = netsyslog.Logger()
		if isinstance(host, list):
			for i in host:
				if ":" in i:
					host, port = str(i).strip().split(":")
					port = int(port)
					logger.remove_host('*')
					sender(logger, severity, facility, message, host, port, tag, timestamp, pid, debug)
				else:
					for i in host:
						logger.remove_host('*')
						sender(logger, severity, facility, message, i, port, tag, timestamp, pid, debug)
						
		else:
			sender(logger, severity, facility, message, host, port, tag, timestamp, pid, debug)
	
	def use_syslog(severity, facility, message, host, port, tag, timestamp, pid, debug):
		import syslog
		list_facility = []
		for i in syslog.FACILITY:
			list_facility.append(str(i) + ": " + str(syslog.FACILITY.get(i)))
		if facility == 8:facility = 1
		elif facility == 16:facility = 2
		elif facility == 24:facility = 3
		elif facility == 32:facility = 4
		elif facility == 40:facility = 5
		elif facility == 48:facility = 6
		elif facility == 56:facility = 7
		elif facility == 64:facility = 8
		elif facility == 72:facility = 9
		elif facility == 128:facility = 16
		elif facility == 136:facility = 17
		elif facility == 144:facility = 18
		elif facility == 152:facility = 19
		elif facility == 160:facility = 20
		elif facility == 168:facility = 21
		elif facility == 176:facility = 22
		elif facility == 184:facility = 23
		#makeList(list_facility, 5)
		facility = int(facility)
		severity = int(severity)
		if isinstance(host, list) and len(host) > 1:
			for i in host:
				if ":" in i:
					host, port = str(i).strip().split(":")
					port = int(port)
					if isinstance(port, list) and len(port) > 1:
						for p in port:
							syslog.syslog(str(message), int(severity), int(facility), str(host), int(p))
					else:
						syslog.syslog(str(message), int(severity), int(facility), str(host), int(port))
				else:
					if isinstance(port, list) and len(port) > 1:
						for p in port:
							syslog.syslog(str(message), int(severity), int(facility), str(host[0]), int(p))
					else:
						syslog.syslog(str(message), int(severity), int(facility), str(host[0]), int(port))
		else:
			if isinstance(port, list) and len(port) > 1:
				for p in port:
					syslog.syslog(str(message), int(severity), int(facility), str(host[0]), int(p))
			else:
				syslog.syslog(str(message), int(severity), int(facility), str(host[0]), int(port))
	try:
		use_netsyslog(severity, facility, message, host, port, tag, timestamp, pid, debug)
	except:
		import traceback
		traceback.format_exc()
		use_syslog(severity, facility, message, host, port, tag, timestamp, pid, debug)
if __name__ == '__main__':
	usage()
