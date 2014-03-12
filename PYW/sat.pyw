#!/usr/bin/env python
# SAT (Simple scAnning Tool)
# http://sat.berlios.de/
# Copyright (C) 2003-2006 azurIt (azurit@pobox.sk, azurIt@IRCnet)
#
# LICENSE:
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
################################################################################
import select, telnetlib, threading, socket, re, signal, Queue, urllib, sha
import smtplib
from string import join
from random import randint
from fnmatch import translate
from sys import exit, argv, stdout
from thread import error as ThreadError
from sys import version as PythonVersion
from time import strftime, time, sleep, localtime

sat_version = "1.3dev"

def my_open(name, mode):
	try:
		file_obj = open(name, mode)
	except IOError, error:
		return error
	else:
		return file_obj

def test_ipv4(ip):
	ip = ip.replace(".", " ").split()
	if len(ip) != 4:
		return 0
	try:
		for i in xrange(4):
			ip[i] = int(ip[i])
			if ip[i] < 0 or ip[i] > 255:
				return 0
	except ValueError:
		return 0
	return 1

def conv_ipv6(ip):
	length = len(ip.replace(":", " ").split())
	if length < 8 and "::" in ip:
		ip = ip.replace("::", ":0"*(8-length)+":")
		if ip[0] == ":":
			ip = ip[1:]
	return ip

def test_ipv6(ip):
	ip = conv_ipv6(ip).replace(":", " ").split()
	if len(ip) != 8:
		return 0
	try:
		for i in xrange(8):
			ip[i] = int(ip[i], 16)
			if ip[i] < 0 or ip[i] > 65535:
				return 0
	except ValueError:
		return 0
	return 1

def sig_hand(signum, frame):
	sat.die = 2

# this is here for signals on Windows compatibility
# (it seems that Win takes sleep() as an I/O operation)
def my_sleep(secs):
	try:
		sleep(secs)
	except IOError:
		pass

class sat:
	def __init__(self):
		# default settings
		self.ports = "23"
		self.use_conn_timeout = 1
		self.connect_timeout = 10
		self.receive_timeout_tcp = 10
		self.receive_timeout_udp = 5
		self.log_recv_timeout = 0
		self.send_data = 1
		self.wait_data = 0.5
		self.data = "Can u suck my dick \n?\nhelp\n\n\n\r\n\r\n\r"
		self.case_sensitive = 1
		self.notify_all = 0
		self.notify_found = 1
		self.log_found = 1
		self.read_data = 15
		self.max_threads = 100
		self.log_file = "sat.log"
		self.error_file = "sat.error"
		self.restore_file = "sat.restore"
		self.rules_debug = 0
		self.log_rules_debug = 1
		self.search_unknown = 0
		self.notify_unknown = 0
		self.log_unknown = 1
		self.scan_type = "i"
		self.scan_proto = "TCP"
		self.scan_proto_ver = "4"
		self.smtp_enable = 0
		self.smtp_tls_enable = 0
		self.smtp_auth_enable = 0
		self.smtp_auth_login = "sender"
		self.smtp_auth_password = "password"
		self.smtp_host = "localhost"
		self.smtp_port = "25"
		self.smtp_sender = "sender@domain"
		self.smtp_receiver = "receiver@domain"
		self.smtp_subject = "SAT log"
		self.quiet_mode = 0
		# default rule
		self.srules = [["Default rule (everything): This means that no srules file was loaded", 1, [1, "*"]]]
		self.config_file = "sat.conf"
		self.srules_file = "sat.srules"
		# other vars (do not change)
		self.all = 0
		self.found = 0
		self.unknown = 0
		self.error = 0
		self.conn_tim = 0
		self.recv_tim = 0
		self.cnt_thrds = 0
		self.die = 0
		self.queue_end = 0
		self.srules_version = 0
		self.upd_srules_host = "http://sat.berlios.de/update_srules.txt"
		self.supported_proto = ["TCP", "UDP"]
		self.supported_proto_ver = ["4", "6"]

	# this will execute the config file and check the settings there
	def exec_config(self, cfile):
		error_msg = ""
		try:
			execfile(cfile)
		except IOError, error:
			if error[0] == 2:
				self.print_message("CONFIG FILE WARNING - No such file, useing the default settings")
			else:
				error_msg = "CONFIG FILE ERROR - %s" % error[1]
		if error_msg == "":
			if type(self.receive_timeout_tcp) not in [int, long, float] or self.receive_timeout_tcp < 0:
				error_msg = "CONFIG ERROR - Variable 'self.receive_timeout_tcp': TCP receive timeout must be a non-negative number"
			elif type(self.receive_timeout_udp) not in [int, long, float] or self.receive_timeout_udp < 0:
				error_msg = "CONFIG ERROR - Variable 'self.receive_timeout_udp': UDP receive timeout must be a non-negative number"
			elif type(self.connect_timeout) not in [int, long, float] or self.connect_timeout < 0:
				error_msg = "CONFIG ERROR - Variable 'self.connect_timeout': connect timeout must be a non-negative number"
			elif type(self.wait_data) not in [int, long, float] or self.wait_data < 0:
				error_msg = "CONFIG ERROR - Variable 'self.wait_data': must be a non-negative number"
			elif type(self.read_data) not in [int, long] or self.read_data < 0:
				error_msg = "CONFIG ERROR - Variable 'self.read_data': must be a non-negative number"
			elif type(self.max_threads) not in [int, long]:
				error_msg = "CONFIG ERROR - Variable 'self.max_threads': must be a number"
			elif self.max_threads < 2:
				error_msg = "CONFIG ERROR - Variable 'self.max_threads': must be at least 2"
			elif self.ports == "":
				error_msg = "CONFIG ERROR - Variable 'self.ports': no ports specified"
			elif self.scan_proto.upper() not in self.supported_proto:
				error_msg = "CONFIG ERROR - Variable 'self.scan_proto': unsupported protocol"
			elif self.scan_proto_ver not in self.supported_proto_ver:
				error_msg = "CONFIG ERROR - Variable 'self.scan_proto_ver': unsupported protocol version"
		if error_msg != "":
			self.print_message(error_msg)
			self.log_error(error_msg)
			exit()

	def exec_db(self, dbfile):
		# executing the srules file
		try:
			execfile(dbfile)
		except IOError, error:
			if error[0] == 2:
				self.print_message("SRULES FILE WARNING - No such file, useing the default rule")
			else:
				error_msg = "SRULES FILE ERROR - %s" % error[1]
				self.print_message(error_msg)
				self.log_error(error_msg)
				exit()
		except:
			error_msg = "SRULES FILE ERROR - File is corrupted"
			self.print_message(error_msg)
			self.log_error(error_msg)
			exit()
		# checking the rules
		else:
			self.print_message("checking the rules.. ", 2)
			if type(self.srules) != list:
				error_msg = "SRULES ERROR - Invalid rules file format detected"
				self.print_message(error_msg)
				self.log_error(error_msg)
				exit()
			for item in self.srules:
				if len(item) < 3 or type(item) != list:
					error_msg = "SRULES ERROR - Invalid rule detected (%s. rule: %s)" % (self.srules.index(item), item)
					self.print_message(error_msg)
					self.log_error(error_msg)
					exit()
				for i in item[2:]:
					if len(i) < 2 or type(i) != list:
						error_msg = "SRULES ERROR - Invalid rule detected (%s. rule: %s)" % (self.srules.index(item), item)
						self.print_message(error_msg)
						self.log_error(error_msg)
						exit()
			self.print_message("done")
		self.print_message("removeing disabled rules and compiling the patterns.. ", 2)
		srules2 = []
		for rule in self.srules:
			if self.search_unknown or rule[1]:
				for subrule in rule[2:]:
					if not self.search_unknown and not subrule[0]:
						rule.remove(subrule)
					else:
						subrule2 = translate(subrule[1])
						if self.case_sensitive:
							rule[rule.index(subrule)] = [subrule[0], re.compile(subrule2, re.DOTALL)]
						else:
							rule[rule.index(subrule)] = [subrule[0], re.compile(subrule2, re.DOTALL | re.IGNORECASE)]
				if len(rule) > 2:
					srules2.append(rule)
			if self.die:
				exit()
		self.srules = srules2
		self.print_message("done")

	def log_message(self, message):
		self.lock_log_file.acquire()
		self.log_fd.write(message)
		try:
			self.log_fd.flush()
		except IOError, error:
			self.print_message("RESULT FILE WARNING - %s" % error)
		self.lock_log_file.release()

	def log_error(self, message):
		self.lock_error_file.acquire()
		self.error_fd.write("%s : %s\n" % (strftime("%d.%m.%Y %H:%M:%S"), message))
		try:
			self.error_fd.flush()
		except IOError, error:
			self.print_message("ERROR FILE WARNING - %s" % error)
		self.lock_error_file.release()

	def print_message(self, message, type=1):
		if not self.quiet_mode:
			if type == 1:
				print message
			elif type == 2:
				stdout.write(message)
				stdout.flush()

	def start_scan(self):
		if "-c" in argv:
			if len(argv) > argv.index("-c"):
				self.config_file = argv[argv.index("-c")+1]
		self.exec_config(self.config_file)
		self.cmdline()
		self.print_message("::   SAT (Simple scAnning Tool)   ::")
		self.print_message("::          version %s%s::" % (sat_version, (14-len(sat_version))*" "))
		self.print_message("::     http://sat.berlios.de/     ::")
		self.print_message(":: Copyright (C) 2003-2006 azurIt ::")
		self.print_message(":: azurit@pobox.sk, azurIt@IRCnet ::")
		self.exec_db(self.srules_file)
		if self.use_conn_timeout:
			socket.setdefaulttimeout(self.connect_timeout)
		self.lock_log_file = threading.Lock()
		self.lock_error_file = threading.Lock()
		self.lock_cnt_thrds = threading.Lock()
		self.lock_all = threading.Lock()
		self.lock_found = threading.Lock()
		self.lock_unknown = threading.Lock()
		self.lock_error = threading.Lock()
		self.lock_conn_tim = threading.Lock()
		self.lock_recv_tim = threading.Lock()
		self.log_fd = my_open(self.log_file, "a")
		self.error_fd = my_open(self.error_file, "a")
		if type(self.log_fd) != file:
			self.print_message("RESULT FILE WARNING - Logging disabled: %s" % self.log_fd)
			self.log_recv_timeout = 0
			self.log_found = 0
			self.log_unknown = 0
			self.log_rules_debug = 0
		if self.scan_proto == "TCP":
			self.try_connect = self.try_connect_tcp
		elif self.scan_proto == "UDP":
			self.try_connect = self.try_connect_udp
		self.data_queue = Queue.Queue(0)
		self.targets_queue = Queue.Queue(1000)
		self.print_message("starting threads.. ", 2)
		try:
			thrd = threading.Thread(target=self.get_from_queue)
			thrd.start()
			self.cnt_thrds += 1
			for i in xrange(self.max_threads-1):
				thrd = threading.Thread(target=self.try_connect)
				thrd.start()
				self.cnt_thrds += 1
		except ThreadError, error:
			if self.cnt_thrds < 2:
				error_msg = "THREADS ERROR - At least 2 threads must be started (%s)" % error
				self.print_message(error_msg)
				self.log_error(error_msg)
				exit()
			else:
				self.print_message("THREADS WARNING - Only %s thread(s) started (%s)" % (self.cnt_thrds, error))
		else:
			self.print_message("done")
		self.start_time = time()
		# 45 x '='
		self.log_message("=============================================\nscan started at %s\n" % strftime("%H:%M:%S %d.%m.%Y", localtime(self.start_time)))
		self.print_message("scan started at %s" % strftime("%H:%M:%S %d.%m.%Y", localtime(self.start_time)))
		self.print_message("scanning %s ports" % self.scan_proto)
		if self.scan_type == "t":
			self.log_message("  using target file: %s\n  using port range : %s\n  scan type        : %s version %s\n  ----\n" % (self.cmd_args[0], self.cmd_options.port_range, self.scan_proto, self.scan_proto_ver))
			for target in self.targets:
				self.start_connecting(target)
		elif self.scan_type == "i":
			self.log_message("  using IP range  : %s\n  using port range: %s\n  scan type       : %s version %s\n  ----\n" % (self.cmd_args[0], self.cmd_options.port_range, self.scan_proto, self.scan_proto_ver))
			if self.scan_proto_ver == "4":
				for ipset in self.targets:
					if "-" in ipset:
						start_ip = ipset.replace("-", " ", 1).split()[0].replace(".", " ", 3).split()
						end_ip = ipset.replace("-", " ", 1).split()[1].replace(".", " ", 3).split()
						for i in xrange(4):
							start_ip[i] = int(start_ip[i])
							end_ip[i] = int(end_ip[i])
						# this is ugly but very fast
						for start_ip[0] in xrange(start_ip[0], 256):
							for start_ip[1] in xrange(start_ip[1], 256):
								for start_ip[2] in xrange(start_ip[2], 256):
									for start_ip[3] in xrange(start_ip[3], 256):
										if self.die != 2:
											self.start_connecting("%s.%s.%s.%s" % (start_ip[0], start_ip[1], start_ip[2], start_ip[3]))
										else:
											start_ip = end_ip
										if start_ip[0] == end_ip[0] and start_ip[1] == end_ip[1] and start_ip[2] == end_ip[2] and start_ip[3] == end_ip[3]:
											break
									if start_ip[0] == end_ip[0] and start_ip[1] == end_ip[1] and start_ip[2] == end_ip[2]:
										break
									start_ip[3] = 0
								if start_ip[0] == end_ip[0] and start_ip[1] == end_ip[1]:
									break
								start_ip[2] = 0
							if start_ip[0] == end_ip[0]:
								break
							start_ip[1] = 0
					else:
						self.start_connecting(ipset)
			elif self.scan_proto_ver == "6":
				for ipset in self.targets:
					if "-" in ipset:
						start_ip = conv_ipv6(ipset.replace("-", " ", 1).split()[0]).replace(":", " ", 8).split()
						end_ip = conv_ipv6(ipset.replace("-", " ", 1).split()[1]).replace(":", " ", 8).split()
						for i in xrange(8):
							start_ip[i] = int(start_ip[i], 16)
							end_ip[i] = int(end_ip[i], 16)
						# this is ugly but very fast
						for start_ip[0] in xrange(start_ip[0], 65536):
							for start_ip[1] in xrange(start_ip[1], 65536):
								for start_ip[2] in xrange(start_ip[2], 65536):
									for start_ip[3] in xrange(start_ip[3], 65536):
										for start_ip[4] in xrange(start_ip[4], 65536):
											for start_ip[5] in xrange(start_ip[5], 65536):
												for start_ip[6] in xrange(start_ip[6], 65536):
													for start_ip[7] in xrange(start_ip[7], 65536):
														if self.die != 2:
															self.start_connecting("%s:%s:%s:%s:%s:%s:%s:%s" % (hex(start_ip[0])[2:], hex(start_ip[1])[2:], hex(start_ip[2])[2:], hex(start_ip[3])[2:], hex(start_ip[4])[2:], hex(start_ip[5])[2:], hex(start_ip[6])[2:], hex(start_ip[7])[2:]))
														else:
															start_ip = end_ip
														if start_ip[0] == end_ip[0] and start_ip[1] == end_ip[1] and start_ip[2] == end_ip[2] and start_ip[3] == end_ip[3] and start_ip[4] == end_ip[4] and start_ip[5] == end_ip[5] and start_ip[6] == end_ip[6] and start_ip[7] == end_ip[7]:
															break
													if start_ip[0] == end_ip[0] and start_ip[1] == end_ip[1] and start_ip[2] == end_ip[2] and start_ip[3] == end_ip[3] and start_ip[4] == end_ip[4] and start_ip[5] == end_ip[5] and start_ip[6] == end_ip[6]:
														break
													start_ip[7] = 0
												if start_ip[0] == end_ip[0] and start_ip[1] == end_ip[1] and start_ip[2] == end_ip[2] and start_ip[3] == end_ip[3] and start_ip[4] == end_ip[4] and start_ip[5] == end_ip[5]:
													break
												start_ip[6] = 0
											if start_ip[0] == end_ip[0] and start_ip[1] == end_ip[1] and start_ip[2] == end_ip[2] and start_ip[3] == end_ip[3] and start_ip[4] == end_ip[4]:
												break
											start_ip[5] = 0
										if start_ip[0] == end_ip[0] and start_ip[1] == end_ip[1] and start_ip[2] == end_ip[2] and start_ip[3] == end_ip[3]:
											break
										start_ip[4] = 0
									if start_ip[0] == end_ip[0] and start_ip[1] == end_ip[1] and start_ip[2] == end_ip[2]:
										break
									start_ip[3] = 0
								if start_ip[0] == end_ip[0] and start_ip[1] == end_ip[1]:
									break
								start_ip[2] = 0
							if start_ip[0] == end_ip[0]:
								break
							start_ip[1] = 0
					else:
						self.start_connecting(ipset)
		elif self.scan_type == "n":
			self.log_message("  using target file: %s\n  nmap grepable output format\n  scan type        : %s version %s\n  ----\n" % (self.cmd_args[0], self.scan_proto, self.scan_proto_ver))
			for target in self.targets:
				self.ports = target[1]
				self.start_connecting(target[0])
		if not self.die:
			self.die = 1
		self.print_message("waiting for all threads to complete.. ", 2)
		while self.cnt_thrds != 1:
			my_sleep(1)
		self.print_message("done")
		self.queue_end = 1
		self.print_message("empting queue.. ", 2)
		while self.cnt_thrds != 0:
			my_sleep(1)
		self.print_message("done")
		if self.die == 2:
			try:
				file_obj = my_open(self.restore_file, "w")
				if type(file_obj) != file:
					self.print_message("RESTORE FILE WARNING - %s" % file_obj)
				else:
					file_obj.write("%s\n%s\n%s\n%s\n%s\n%s\n" % (self.scan_type, self.cmd_args[0], self.target, self.cmd_options.port_range, self.scan_proto, self.scan_proto_ver))
					try:
						file_obj.close()
					except IOError, error:
						self.print_message("RESTORE FILE WARNING - %s" % error)
			except AttributeError:
				exit()
		self.log_message("  ----\n  scan time             : %0.4f s\n" % (time()-self.start_time))
		self.log_message("  average time          : %0.4f s for host/IP:port\n" % ((time()-self.start_time)/self.all))
		self.log_message("  --\n  scaned [host/IP:port]s: %s\n  found                 : %s\n" % (self.all, self.found))
		if self.search_unknown:
			self.log_message("  unknown               : %s\n" % self.unknown)
		self.log_message("  error                 : %s\n" % self.error)
		self.log_message("  connect timeout       : %s\n" % self.conn_tim)
		self.log_message("  receive timeout       : %s\n" % self.recv_tim)
		if self.die == 2:
			self.log_message("scan aborted at %s\n" % strftime("%H:%M:%S %d.%m.%Y"))
		else:
			self.log_message("scan completed at %s\n" % strftime("%H:%M:%S %d.%m.%Y"))
		self.log_fd.close()
		if self.smtp_enable:
			self.send_log()
		self.error_fd.close()
		self.print_message("----")
		self.print_message("scan time             : %0.4f s" % (time()-self.start_time))
		self.print_message("average time          : %0.4f s for host/IP:port" % ((time()-self.start_time)/self.all))
		self.print_message("--")
		self.print_message("scaned [host/IP:port]s: %s" % self.all)
		self.print_message("found                 : %s" % self.found)
		if self.search_unknown:
			self.print_message("unknown               : %s" % self.unknown)
		self.print_message("error                 : %s" % self.error)
		self.print_message("connect timeout       : %s" % self.conn_tim)
		self.print_message("receive timeout       : %s" % self.recv_tim)
		self.print_message("----")
		if self.die == 2:
			self.print_message("scan aborted at %s" % strftime("%H:%M:%S %d.%m.%Y"))
		else:
			self.print_message("scan completed at %s" % strftime("%H:%M:%S %d.%m.%Y"))

	def start_connecting(self, target):
		for portset in self.ports:
			if "-" in portset:
				for port in xrange(int(portset.replace("-", " ", 1).split()[0]), int(portset.replace("-", " ", 1).split()[1])+1):
					while self.die != 2:
						try:
							self.targets_queue.put_nowait([target, port])
						except Queue.Full:
							my_sleep(1)
						else:
							break
					if self.die == 2:
						break
			else:
				while self.die != 2:
					try:
						self.targets_queue.put_nowait([target, portset])
					except Queue.Full:
						my_sleep(1)
					else:
						break
			if self.die == 2:
				break

	def try_connect_tcp(self, target="", port=""):
		while self.die != 2:
			try:
				target = self.targets_queue.get_nowait()
				port = target[1]
				target = target[0]
			except Queue.Empty:
				if self.die == 1:
					break
				else:
					my_sleep(0.1)
			else:
				self.lock_all.acquire()
				self.all += 1
				self.target = target
				self.lock_all.release()
				again = 1
				while again:
					again = 0
					try:
						if self.notify_all:
							self.print_message("TRYING      : %s:%s.." % (target, port))
						sck = telnetlib.Telnet(str(target), port)
					except socket.timeout:
						if self.notify_all:
							self.print_message("TIMED OUT   : %s:%s - Connect timeout" % (target, port))
						self.lock_conn_tim.acquire()
						self.conn_tim += 1
						self.lock_conn_tim.release()
					except socket.error, error:
						# 10050 - Network is down
						# 10051 - Network is unreachable
						if error[0] == 10050 or error[0] == 10051:
							again = 1
						else:
							self.lock_error.acquire()
							self.error += 1
							self.lock_error.release()
						if self.notify_all:
							self.print_message("ERROR       : %s:%s - %s" % (target, port, error))
					except socket.gaierror, error:
						if self.notify_all:
							self.print_message("ERROR       : %s:%s - %s" % (target, port, error[1]))
						self.lock_error.acquire()
						self.error += 1
						self.lock_error.release()
					else:
						if self.notify_all:
							self.print_message("CONNECTED TO: %s:%s" % (target, port))
						try:
							if self.send_data:
								my_sleep(self.wait_data)
								sck.get_socket().send(self.data)
							rd, wr, ex = select.select([sck.fileno()], [], [], self.receive_timeout_tcp)
							if rd:
								data = sck.read_some()
								for i in xrange(self.read_data):
									rd, wr, ex = select.select([sck.fileno()], [], [], 0.1)
									if rd:
										try:
											data = str(data)+str(sck.get_socket().recv(100))
										except socket.error:
											pass
								self.data_queue.put([target, port, data])
							else:
								if self.notify_all:
									self.print_message("TIMED OUT   : %s:%s - receive timeout" % (target, port))
								if self.log_recv_timeout:
									self.log_message("  %s:%s = receive timeout\n" % (target, port))
								self.lock_recv_tim.acquire()
								self.recv_tim += 1
								self.lock_recv_tim.release()
						except select.error, error:
							if self.notify_all:
								self.print_message("ERROR       : %s:%s - %s" % (target, port, error[1]))
							self.lock_error.acquire()
							self.error += 1
							self.lock_error.release()
						except socket.error, error:
							if self.notify_all:
								self.print_message("ERROR       : %s:%s - %s" % (target, port, error))
							self.lock_error.acquire()
							self.error += 1
							self.lock_error.release()
						sck.close()
		self.lock_cnt_thrds.acquire()
		self.cnt_thrds -= 1
		self.lock_cnt_thrds.release()

	def try_connect_udp(self, target="", port=""):
		while self.die != 2:
			try:
				target = self.targets_queue.get_nowait()
				port = target[1]
				target = target[0]
			except Queue.Empty:
				if self.die == 1:
					break
				else:
					my_sleep(0.1)
			else:
				self.lock_all.acquire()
				self.all += 1
				self.target = target
				self.lock_all.release()
				again = 1
				while again:
					again = 0
					try:
						if self.notify_all:
							self.print_message("TRYING      : %s:%s.." % (target, port))
						sck = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
					except socket.error, error:
						# 10050 - Network is down
						# 10051 - Network is unreachable
						if error[0] == 10050 or error[0] == 10051:
							again = 1
						else:
							self.lock_error.acquire()
							self.error += 1
							self.lock_error.release()
						if self.notify_all:
							self.print_message("ERROR       : %s:%s - %s" % (target, port, error))
					except socket.gaierror, error:
						if self.notify_all:
							self.print_message("ERROR       : %s:%s - %s" % (target, port, error[1]))
						self.lock_error.acquire()
						self.error += 1
						self.lock_error.release()
					else:
						if self.notify_all:
							self.print_message("DATA SENT TO: %s:%s" % (target, port))
						try:
							if self.send_data:
								my_sleep(self.wait_data)
								sck.sendto(self.data, (target, int(port)))
							rd, wr, ex = select.select([sck.fileno()], [], [], self.receive_timeout_udp)
							if rd:
								data = sck.recvfrom(1000)[0]
								for i in xrange(self.read_data):
									rd, wr, ex = select.select([sck.fileno()], [], [], 0.1)
									if rd:
										try:
											data = str(data)+str(sck.recvfrom(100)[0])
										except socket.error:
											pass
								self.data_queue.put([target, port, data])
							else:
								if self.notify_all:
									self.print_message("TIMED OUT   : %s:%s - receive timeout" % (target, port))
								if self.log_recv_timeout:
									self.log_message("  %s:%s = receive timeout\n" % (target, port))
								self.lock_recv_tim.acquire()
								self.recv_tim += 1
								self.lock_recv_tim.release()
						except select.error, error:
							if self.notify_all:
								self.print_message("ERROR       : %s:%s - %s" % (target, port, error[1]))
							self.lock_error.acquire()
							self.error += 1
							self.lock_error.release()
						except socket.error, error:
							if self.notify_all:
								self.print_message("ERROR       : %s:%s - %s" % (target, port, error))
							self.lock_error.acquire()
							self.error += 1
							self.lock_error.release()
						sck.close()
		self.lock_cnt_thrds.acquire()
		self.cnt_thrds -= 1
		self.lock_cnt_thrds.release()

	def get_from_queue(self):
		while not (self.queue_end and self.data_queue.empty()):
				if not self.data_queue.empty():
					item = self.data_queue.get()
					self.match_rule(item[0], item[1], item[2])
				else:
					my_sleep(1)
		self.lock_cnt_thrds.acquire()
		self.cnt_thrds -= 1
		self.lock_cnt_thrds.release()

	def match_rule(self, target, port, data):
		if self.rules_debug:
			self.print_message("DEBUG       : %s:%s - %s" % (target, port, [data]))
			if self.log_rules_debug:
				self.log_message("  %s:%s = %s\n" % (target, port, [data]))
		found = ""
		for rule in self.srules:
			for subrule in rule[2:]:
				if subrule[1].match(data) is not None:
					found = str(found)+str(rule[0])+" | "
					break
		if found != "":
			self.lock_found.acquire()
			self.found += 1
			self.lock_found.release()
			if self.notify_all or self.notify_found:
				self.print_message("FOUND       : %s:%s (%s)" % (target, port, found[0:-3]))
			if self.log_found:
				self.log_message("  %s:%s = %s\n" % (target, port, found[0:-3]))
		elif self.search_unknown:
			self.lock_unknown.acquire()
			self.unknown += 1
			self.lock_unknown.release()
			if self.notify_unknown:
				self.print_message("UNKNOWN     : %s:%s (%s)" % (target, port, [data]))
			if self.log_unknown:
				self.log_message("  %s:%s = unknown - %s\n" % (target, port, [data]))

	def send_log(self):
		log_fd = my_open(self.log_file, "r")
		if type(log_fd) != file:
			error_msg = "SMTP LOG FILE ERROR - %s" % log_fd
			self.print_message(error_msg)
			self.log_error(error_msg)
			return 0
		msg = "From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n" % (self.smtp_sender, self.smtp_receiver, self.smtp_subject)
		msg = msg + log_fd.read()
		log_fd.close()
		try:
			smpt_srv = smtplib.SMTP(self.smtp_host, self.smtp_port)
			if self.smtp_tls_enable:
				smpt_srv.starttls()
				smpt_srv.ehlo()
			if self.smtp_auth_enable:
				try:
					smpt_srv.login(self.smtp_auth_login, self.smtp_auth_password)
				except smtplib.SMTPException, error:
					error_msg = "SMTP ERROR - %s" % error
					self.print_message(error_msg)
					self.log_error(error_msg)
					smpt_srv.quit()
					return 0
				except smtplib.SMTPAuthenticationError, error:
					error_msg = "SMTP ERROR - %s" % error
					self.print_message(error_msg)
					self.log_error(error_msg)
					smpt_srv.quit()
					return 0
			try:
				smpt_srv.sendmail(self.smtp_sender, self.smtp_receiver, msg)
			except smtplib.SMTPRecipientsRefused, error:
				error_msg = "SMTP ERROR - %s" % error
				self.print_message(error_msg)
				self.log_error(error_msg)
			except smtplib.SMTPSenderRefused, error:
				error_msg = "SMTP ERROR - %s" % error
				self.print_message(error_msg)
				self.log_error(error_msg)
			except smtplib.SMTPDataError, error:
				error_msg = "SMTP ERROR - %s" % error
				self.print_message(error_msg)
				self.log_error(error_msg)
			smpt_srv.quit()
		except smtplib.SMTPHeloError, error:
			error_msg = "SMTP ERROR - %s" % error
			self.print_message(error_msg)
			self.log_error(error_msg)
		except socket.error, error:
			error_msg = "SMTP ERROR - %s" % error
			self.print_message(error_msg)
			self.log_error(error_msg)
		return 1

	def update_srules(self, proxy={}):
		try:
			execfile(self.srules_file)
		except IOError, error:
			# file not found
			if error[0] == 2:
				pass
			else:
				error_msg = "SRULES FILE ERROR - %s" % error[1]
				self.print_message(error_msg)
				self.log_error(error_msg)
				return 0
		except:
			pass
		self.print_message("checking for updates.. ", 2)
		try:
			url_obj = urllib.urlopen(self.upd_srules_host, proxies=proxy)
		except IOError, error:
			error_msg = "SRULES UPDATE ERROR - %s" % error
			self.print_message(error_msg)
			self.log_error(error_msg)
			return 0
		data = url_obj.read()
		url_obj.close()
		if "HTTP 407 Proxy Authentication Required" in data:
			error_msg = "SRULES UPDATE ERROR - Proxy authentication required but not supported"
			self.print_message(error_msg)
			self.log_error(error_msg)
			return 0
		data = data.splitlines()
		for i in data:
			data[data.index(i)] = i.replace("\n", "").replace("\r", "")
		if len(data) < 3:
			error_msg = "SRULES UPDATE ERROR - Info file on home server is corrupted"
			self.print_message(error_msg)
			self.log_error(error_msg)
			return 0
		try:
			data[0] = int(data[0])
		except ValueError:
			error_msg = "SRULES UPDATE ERROR - Info file on home server is corrupted"
			self.print_message(error_msg)
			self.log_error(error_msg)
			return 0
		if self.srules_version < data[0]:
			self.print_message("update available!")
			for mirror in data[2:]:
				self.print_message("downloading file.. ", 2)
				try:
					url_obj = urllib.urlopen(mirror, proxies=proxy)
				except IOError, error:
					self.print_message("SRULES UPDATE/MIRROR WARNING - %s" % error)
				else:
					srules_data = url_obj.read()
					url_obj.close()
					if sha.new(srules_data).hexdigest() != data[1]:
						self.print_message("downloaded file is corrupted!")
					else:
						file_obj = open(self.srules_file, "w")
						file_obj.write(srules_data)
						file_obj.close()
						self.print_message("update successful!")
						return 1
			error_msg = "SRULES UPDATE ERROR - Update failed"
			self.print_message(error_msg)
			self.log_error(error_msg)
			return 0
		else:
			self.print_message("update NOT available")
			return 0

	def cmd_check_targets(self, cmd_parser, targets):
		if self.scan_type == "i":
			targets = targets.split(",")
			if targets == ["R"] or len(targets) != 1 or "-" in targets[0]:
				for ipset in targets:
					if "-" in ipset:
						if ipset == "R-R":
							if self.scan_proto_ver == "4":
								ip1_1 = randint(0, 255)
								ip2_1 = randint(0, 255)
								ip3_1 = randint(0, 255)
								# this is not a mistake
								ip4_1 = randint(0, 254)
								ip1_2 = randint(ip1_1, 255)
								if ip1_2 == ip1_1:
									ip2_2 = randint(ip2_1, 255)
									if ip2_2 == ip2_1:
										ip3_2 = randint(ip3_1, 255)
										if ip3_2 == ip3_1:
											ip4_2 = randint(ip4_1+1, 255)
										else:
											ip4_2 = randint(0, 255)
									else:
										ip3_2 = randint(0, 255)
										ip4_2 = randint(0, 255)
								else:
									ip2_2 = randint(0, 255)
									ip3_2 = randint(0, 255)
									ip4_2 = randint(0, 255)
								targets[targets.index(ipset)] = "%s.%s.%s.%s-%s.%s.%s.%s" % (ip1_1, ip2_1, ip3_1, ip4_1, ip1_2, ip2_2, ip3_2, ip4_2)
							elif self.scan_proto_ver == "6":
								ip1_1 = randint(0, 65535)
								ip2_1 = randint(0, 65535)
								ip3_1 = randint(0, 65535)
								ip4_1 = randint(0, 65535)
								ip5_1 = randint(0, 65535)
								ip6_1 = randint(0, 65535)
								ip7_1 = randint(0, 65535)
								# this is not a mistake
								ip8_1 = randint(0, 65534)
								ip1_2 = randint(ip1_1, 65535)
								if ip1_2 == ip1_1:
									ip2_2 = randint(ip2_1, 65535)
									if ip2_2 == ip2_1:
										ip3_2 = randint(ip3_1, 65535)
										if ip3_2 == ip3_1:
											ip4_2 = randint(ip4_1, 65535)
											if ip4_2 == ip4_1:
												ip5_2 = randint(ip5_1, 65535)
												if ip5_2 == ip5_1:
													ip6_2 = randint(ip6_1, 65535)
													if ip6_2 == ip6_1:
														ip7_2 = randint(ip7_1, 65535)
														if ip7_2 == ip7_1:
															ip8_2 = randint(ip8_1+1, 65535)
														else:
															ip8_2 = randint(0, 65535)
													else:
														ip7_2 = randint(0, 65535)
														ip8_2 = randint(0, 65535)
												else:
													ip6_2 = randint(0, 65535)
													ip7_2 = randint(0, 65535)
													ip8_2 = randint(0, 65535)
											else:
												ip5_2 = randint(0, 65535)
												ip6_2 = randint(0, 65535)
												ip7_2 = randint(0, 65535)
												ip8_2 = randint(0, 65535)
										else:
											ip4_2 = randint(0, 65535)
											ip5_2 = randint(0, 65535)
											ip6_2 = randint(0, 65535)
											ip7_2 = randint(0, 65535)
											ip8_2 = randint(0, 65535)
									else:
										ip3_2 = randint(0, 65535)
										ip4_2 = randint(0, 65535)
										ip5_2 = randint(0, 65535)
										ip6_2 = randint(0, 65535)
										ip7_2 = randint(0, 65535)
										ip8_2 = randint(0, 65535)
								else:
									ip2_2 = randint(0, 65535)
									ip3_2 = randint(0, 65535)
									ip4_2 = randint(0, 65535)
									ip5_2 = randint(0, 65535)
									ip6_2 = randint(0, 65535)
									ip7_2 = randint(0, 65535)
									ip8_2 = randint(0, 65535)
								targets[targets.index(ipset)] = "%s:%s:%s:%s:%s:%s:%s:%s-%s:%s:%s:%s:%s:%s:%s:%s" % (hex(ip1_1)[2:], hex(ip2_1)[2:], hex(ip3_1)[2:], hex(ip4_1)[2:], hex(ip5_1)[2:], hex(ip6_1)[2:], hex(ip7_1)[2:], hex(ip8_1)[2:], hex(ip1_2)[2:], hex(ip2_2)[2:], hex(ip3_2)[2:], hex(ip4_2)[2:], hex(ip5_2)[2:], hex(ip6_2)[2:], hex(ip7_2)[2:], hex(ip8_2)[2:])
						else:
							iprange = ipset.split("-")
							if len(iprange) != 2:
								cmd_parser.error("invalid argument")
							if self.scan_proto_ver == "4":
								if not (test_ipv4(iprange[0]) and test_ipv4(iprange[1])):
									cmd_parser.error("invalid argument")
								iprange[0] = iprange[0].split(".")
								iprange[1] = iprange[1].split(".")
								for i in xrange(4):
									iprange[0][i] = int(iprange[0][i])
									iprange[1][i] = int(iprange[1][i])
								start_ip = iprange[0][0] * 256**3 + iprange[0][1] * 256**2 + iprange[0][2] * 256 + iprange[0][3]
								end_ip = iprange[1][0] * 256**3 + iprange[1][1] * 256**2 + iprange[1][2] * 256 + iprange[1][3]
							elif self.scan_proto_ver == "6":
								if not (test_ipv6(iprange[0]) and test_ipv6(iprange[1])):
									cmd_parser.error("invalid argument")
								iprange[0] = conv_ipv6(iprange[0]).split(":")
								iprange[1] = conv_ipv6(iprange[1]).split(":")
								for i in xrange(8):
									iprange[0][i] = int(iprange[0][i], 16)
									iprange[1][i] = int(iprange[1][i], 16)
								start_ip = iprange[0][0] * 65536**7 + iprange[0][1] * 65536**6 + iprange[0][2] * 65536**5 + iprange[0][3] * 65536**4 + iprange[0][4] * 65536**3 + iprange[0][5] * 65536**2 + iprange[0][6] * 65536 + iprange[0][7]
								end_ip = iprange[1][0] * 65536**7 + iprange[1][1] * 65536**6 + iprange[1][2] * 65536**5 + iprange[1][3] * 65536**4 + iprange[1][4] * 65536**3 + iprange[1][5] * 65536**2 + iprange[1][6] * 65536 + iprange[1][7]
							if start_ip > end_ip:
								cmd_parser.error("invalid argument")
					else:
						if ipset == "R":
							if self.scan_proto_ver == "4":
								targets[targets.index(ipset)] = "%s.%s.%s.%s" % (randint(0, 255), randint(0, 255), randint(0, 255), randint(0, 255))
							elif self.scan_proto_ver == "6":
								targets[targets.index(ipset)] = "%s:%s:%s:%s:%s:%s:%s:%s" % (hex(randint(0, 65535))[2:], hex(randint(0, 65535))[2:], hex(randint(0, 65535))[2:], hex(randint(0, 65535))[2:], hex(randint(0, 65535))[2:], hex(randint(0, 65535))[2:], hex(randint(0, 65535))[2:], hex(randint(0, 65535))[2:])
			# this will remove duplicated ipsets
			self.targets = list(set(targets))
			if not self.cmd_options.restore_scan:
				self.cmd_args[0] = join(self.targets, ",")
		elif self.scan_type == "t":
			file_obj = my_open(targets, "r")
			if type(file_obj) != file:
				cmd_parser.error(file_obj)
			targets = file_obj.readlines()
			file_obj.close()
			self.targets = []
			for i in xrange(len(targets)):
				if targets[i][0] != "#":
					targets[i] = targets[i].replace("\r", "").replace("\n", "")
					if targets[i] != "":
						self.targets.append(targets[i])
			if self.targets == []:
				cmd_parser.error("no targets loaded")
		elif self.scan_type == "n":
			file_obj = my_open(targets, "r")
			if type(file_obj) != file:
				cmd_parser.error(file_obj)
			targets = file_obj.readlines()
			file_obj.close()
			self.targets = []
			for i in xrange(len(targets)):
				if targets[i][0] != "#":
					targets[i] = targets[i].replace("\r", "").replace("\n", "").replace("\t", " ")
					if targets[i] != "":
						if targets[i].split()[3] == "Ports:":
							targets[i] = [targets[i].split()[1], targets[i].split()[4:]]
							ports = []
							for j in xrange(len(targets[i][1])):
								if len(targets[i][1][j].split("/")) > 1:
									if targets[i][1][j].split("/")[1].lower() == "open":
										ports.append(targets[i][1][j].split("/")[0])
							if ports != []:
								self.targets.append([targets[i][0], ports])
						else:
							self.targets.append([targets[i].split()[1], [self.ports]])
			if self.targets == []:
				cmd_parser.error("no targets loaded")

	def cmd_check_ports(self, cmd_parser, ports):
		self.ports = ports.split(",")
		for portset in self.ports:
			try:
				if "-" in portset:
					if portset == "R-R":
						port1 = randint(0, 65535)
						self.ports[self.ports.index(portset)] = "%s-%s" % (port1, randint(port1+1, 65535))
					else:
						if int(portset.split("-")[0]) < 0 or int(portset.split("-")[0]) > 65535:
							cmd_parser.error("port must be a number between 0 and 65535")
						if int(portset.split("-")[1]) < 0 or int(portset.split("-")[1]) > 65535:
							cmd_parser.error("port must be a number between 0 and 65535")
						if int(portset.split("-")[0]) > int(portset.split("-")[1]):
							cmd_parser.error("invalid port range")
				else:
					if portset == "R":
						self.ports[self.ports.index(portset)] = str(randint(0, 65535))
					else:
						if int(portset) < 0 or int(portset) > 65535:
							cmd_parser.error("port must be a number between 0 and 65535")
			except ValueError:
				cmd_parser.error("invalid port range")
		# this will remove duplicated ports
		self.ports = list(set(self.ports))
		self.cmd_options.port_range = join(self.ports, ",")

	def cmdline(self):
		from optparse import OptionParser, SUPPRESS_HELP
		cmd_parser = OptionParser(version="SAT %s" % sat_version, usage="""\
		 %prog [options] <file_name/ip_range>
		 %prog -r [-f <file>]
		 %prog -u [-o <host:port>]
		 %prog -h""")
		cmd_parser.remove_option("--help")
		cmd_parser.remove_option("--version")
		cmd_parser.add_option("-i", action="store_const", const="i", dest="scan_type", default=self.scan_type, help="scan ip range, example: 10.1.1.1-10.1.1.2,10.1.2.2 [default]")
		cmd_parser.add_option("-t", action="store_const", const="t", dest="scan_type", help="scan targets from file")
		cmd_parser.add_option("-n", action="store_const", const="n", dest="scan_type", help="scan targets from file with nmap grepable output format (nmap switch '-oG')")
		cmd_parser.add_option("-p", action="store", type="string", dest="port_range", default=self.ports, metavar="<port_range>", help="port range to scan, example: 1-1024,3333,4000-5000 [default %default]")
		cmd_parser.add_option("-T", action="store_const", const="TCP", dest="scan_proto", default=self.scan_proto, help="scan TCP ports rather then UDP [default]")
		cmd_parser.add_option("-U", action="store_const", const="UDP", dest="scan_proto", help="scan UDP ports rather then TCP")
		cmd_parser.add_option("-4", action="store_const", const="4", dest="scan_proto_ver", default=self.scan_proto_ver, help="scan via IPv4 rather than IPv6 [default]")
		cmd_parser.add_option("-6", action="store_const", const="6", dest="scan_proto_ver", help="scan via IPv6 rather than IPv4")
		cmd_parser.add_option("-H", action="store", type="int", dest="max_threads", default=self.max_threads, metavar="<number>", help="maximum number of threads [default %default]")
		cmd_parser.add_option("-O", action="store", type="string", dest="log_file", default=self.log_file, metavar="<file_name>", help="set the output file name [default %default]")
		cmd_parser.add_option("-q", action="store_const", const=1, dest="quiet_mode", default=self.quiet_mode, help="quiet mode")
		cmd_parser.add_option("-V", action="store_const", const=1, dest="notify_all", default=self.notify_all, help="verbose scan mode")
		# ak sa zmeni prepinac, treba ho upravit aj hore
		cmd_parser.add_option("-c", action="store", type="string", dest="config_file", default=self.config_file, metavar="<file>", help="specify the config file [default %default]")
		cmd_parser.add_option("-l", action="store", type="string", dest="srules_file", default=self.srules_file, metavar="<file>", help="specify the srules file [default %default]")
		cmd_parser.add_option("-r", action="store_true", dest="restore_scan", help="restore aborted scan")
		cmd_parser.add_option("-f", action="store", type="string", dest="restore_file", default=self.restore_file, metavar="<file>", help="specify the restore file [default %default]")
		cmd_parser.add_option("-u", action="store_true", dest="update_srules", help="update srules file from the net")
		cmd_parser.add_option("-o", action="store", type="string", dest="updater_proxy", metavar="<host:port>", help="set the HTTP/FTP proxy for updater")
		# users doesn't need to know about this switch so it's hidden, help for it is here:
		# -d <level>  rules debug mode, level can be 1 or 2
		cmd_parser.add_option("-d", action="store", dest="srules_debug", choices=["1", "2"], metavar="<level>", help=SUPPRESS_HELP)
		cmd_parser.add_option("-v", action="version", help="show program's version number and exit")
		cmd_parser.add_option("-h", action="help", help="show this help message and exit")
		(self.cmd_options, self.cmd_args) = cmd_parser.parse_args()
		if self.cmd_options.scan_proto_ver == "6" and not socket.has_ipv6:
			cmd_parser.error("there is no IPv6 support on this mahine or Python is not compiled to support it")
		if len(self.cmd_args) != 1:
			if self.cmd_options.restore_scan:
				file_obj = my_open(self.cmd_options.restore_file, "r")
				if type(file_obj) != file:
					cmd_parser.error(file_obj)
				lines = file_obj.readlines()
				file_obj.close()
				if len(lines) < 6:
					cmd_parser.error("restore file is corrupted")
				for i in xrange(len(lines)):
					lines[i] = lines[i].replace("\n", "").replace("\r", "")
				self.scan_type = lines[0]
				if self.scan_type == "i":
					self.scan_proto = lines[4]
					self.scan_proto_ver = lines[5]
					self.cmd_check_targets(cmd_parser, lines[1])
					self.cmd_args.append(lines[1])
					if self.scan_proto not in self.supported_proto:
						cmd_parser.error("unsupported protocol (maybe corrupted restore file?)")
					if self.scan_proto_ver == "4":
						if not test_ipv4(lines[2]):
							cmd_parser.error("restore file is corrupted")
						while self.targets != []:
							if "-" in self.targets[0]:
								iprange = self.targets[0].split("-")
								iprange[0] = iprange[0].split(".")
								iprange[1] = iprange[1].split(".")
								target = lines[2].split(".")
								for i in xrange(4):
									iprange[0][i] = int(iprange[0][i])
									iprange[1][i] = int(iprange[1][i])
									target[i] = int(target[i])
								start_ip = iprange[0][0] * 256**3 + iprange[0][1] * 256**2 + iprange[0][2] * 256 + iprange[0][3]
								end_ip = iprange[1][0] * 256**3 + iprange[1][1] * 256**2 + iprange[1][2] * 256 + iprange[1][3]
								target = target[0] * 256**3 + target[1] * 256**2 + target[2] * 256 + target[3]
								if target >= start_ip and target <= end_ip:
									self.targets[0] = "%s-%s" % (lines[2], self.targets[0].split("-")[1])
									break
								self.targets.pop(0)
							else:
								if self.targets[0] == lines[2]:
									break
								self.targets.pop(0)
					elif self.scan_proto_ver == "6":
						if not test_ipv6(lines[2]):
							cmd_parser.error("restore file is corrupted")
						while self.targets != []:
							if "-" in self.targets[0]:
								iprange = self.targets[0].split("-")
								iprange[0] = conv_ipv6(iprange[0]).split(":")
								iprange[1] = conv_ipv6(iprange[1]).split(":")
								target = lines[2].split(":")
								for i in xrange(8):
									iprange[0][i] = int(iprange[0][i], 16)
									iprange[1][i] = int(iprange[1][i], 16)
									target[i] = int(target[i], 16)
								start_ip = iprange[0][0] * 65536**7 + iprange[0][1] * 65536**6 + iprange[0][2] * 65536**5 + iprange[0][3] * 65536**4 + iprange[0][4] * 65536**3 + iprange[0][5] * 65536**2 + iprange[0][6] * 65536 + iprange[0][7]
								end_ip = iprange[1][0] * 65536**7 + iprange[1][1] * 65536**6 + iprange[1][2] * 65536**5 + iprange[1][3] * 65536**4 + iprange[1][4] * 65536**3 + iprange[1][5] * 65536**2 + iprange[1][6] * 65536 + iprange[1][7]
								target = target[0] * 65536**7 + target[1] * 65536**6 + target[2] * 65536**5 + target[3] * 65536**4 + target[4] * 65536**3 + target[5] * 65536**2 + target[6] * 65536 + target[7]
								if target >= start_ip and target <= end_ip:
									self.targets[0] = "%s-%s" % (lines[2], self.targets[0].split("-")[1])
									break
								self.targets.pop(0)
							else:
								if self.targets[0] == lines[2]:
									break
								self.targets.pop(0)
					else:
						cmd_parser.error("unsupported protocol version (maybe corrupted restore file?)")
					if self.targets == []:
						cmd_parser.error("no targets loaded")
				elif self.scan_type == "t":
					self.cmd_check_targets(cmd_parser, lines[1])
					self.cmd_args.append(lines[1])
					while self.targets != []:
						if self.targets[0] != lines[2]:
							self.targets.pop(0)
						else:
							break
					if self.targets == []:
						cmd_parser.error("no targets loaded")
				elif self.scan_type == "n":
					self.cmd_check_targets(cmd_parser, lines[1])
					self.cmd_args.append(lines[1])
					while self.targets != []:
						if self.targets[0][0] != lines[2]:
							self.targets.pop(0)
						else:
							break
					if self.targets == []:
						cmd_parser.error("no targets loaded")
				else:
					cmd_parser.error("unknown scan type (maybe corrupted restore file?)")
				self.cmd_check_ports(cmd_parser, lines[3])
			elif self.cmd_options.update_srules:
				if self.cmd_options.updater_proxy:
					try:
						self.update_srules(proxy={"http": "http://%s" % self.cmd_options.updater_proxy, "ftp": "ftp://%s" % self.cmd_options.updater_proxy})
					except TypeError:
						cmd_parser.error("invalid proxy")
				else:
					self.update_srules()
				exit()
			else:
				cmd_parser.error("incorrect number of arguments")
		else:
			self.scan_type = self.cmd_options.scan_type
			self.scan_proto = self.cmd_options.scan_proto
			self.scan_proto_ver = self.cmd_options.scan_proto_ver
			self.cmd_check_targets(cmd_parser, self.cmd_args[0])
			if self.cmd_options.port_range:
				self.cmd_check_ports(cmd_parser, self.cmd_options.port_range)
		self.quiet_mode = self.cmd_options.quiet_mode
		self.max_threads = self.cmd_options.max_threads
		if self.max_threads < 2:
			cmd_parser.error("maximum threads must be at least 2")
		self.srules_file = self.cmd_options.srules_file
		if self.cmd_options.srules_debug == "1":
			self.rules_debug = 1
			self.log_rules_debug = 0
		elif self.cmd_options.srules_debug == "2":
			self.rules_debug = 1
			self.log_rules_debug = 1
		self.notify_all = self.cmd_options.notify_all
		self.log_file = self.cmd_options.log_file

if __name__ == "__main__":
	# do not remove this check, it will REALLY doesn't work :)
	if int(PythonVersion.replace(".", "")[:2]) < 23:
		print "PYTHON VERSION ERROR - Only Python versions 2.3 and up are supported"
		exit()
	elif int(PythonVersion.replace(".", "")[:2]) < 24:
		from sets import Set as set
	signal.signal(signal.SIGINT, sig_hand)
	signal.signal(signal.SIGTERM, sig_hand)
	sat = sat()
	sat.start_scan()
