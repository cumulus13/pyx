#import ceksvc
#import  win32service

#svc = win32service.ChangeServiceConfig(

#import sys
#sys.stdout.write("HELLO")
#import os
#import termcolor
#import subprocess
#proc = subprocess.Popen(["git"], stdout=subprocess.PIPE, shell=True)
#(out, err) = proc.communicate()
#print proc.poll()
#print "program output:", termcolor.colored(out, 'red')

#try:
	#print sys.argv[1]
#except:
#	import traceback
#	traceback.format_exc()

#  import termcolor
#termcolor.cprint('test', 'white', 'on_red')

#  myDict = {1: {"name" : "test.exe","cmd" : "text test","exe" : r"c:\program\text.exe","mem" : 234234L},2: {"name" : "test2.exe","cmd" : "text test 2","exe" : r"c:\program\text2.exe","mem" : 345345L},3: {"name" : "test3.exe","cmd" : "text test 3","exe" : r"c:\program\text3.exe","mem" : 65675656L},4: {"name" : "test4.exe","cmd" : "text test 4","exe" : r"c:\program\text4.exe","mem" : 12312332L},5: {"name" : "test5.exe","cmd" : "text test 5","exe" : r"c:\program\text5.exe","mem" : 78789789L},}

#  dicts = myDict.items()
#  dicts.sort(key=lambda (k,d): (d['mem']), reverse=False)
#  print dicts
#dicts = [{k: v} for (k,v) in myDict.items()]
#dicts.sort(key=lambda d: (d.values()[0]['mem'], d.values()[0]['name'],))
#dicts = myDict.items()
#print "dicts 0 =", myDict.keys().keys()
#dicts.sort(key=lambda (k,d): (d['mem']))

#print "dicts =", dicts
#Output for doing:
#import pprint
#pprint.pprint(dicts)

#import traceback
#import sys
#import easygui

#try:
	#print sys.argv[1]
#except:
	#easygui.codebox('Traceback Error', 'Traceback', traceback.format_exc())
	
	
#class kallithea(object):
	#def __init__(self, host = '192.168.1.2:5000', api = None, debug = False, **kwargs):
		#self.host = host
		#self.debug = debug
		#self.URL = 'http://%s/_admin/api' % host
		#if not api:
			#self.API = 'a4585aadb592539a63f9937ae4e203669163536d'
		#else:
			#self.API = api
		#if kwargs:
			#for i in kwargs:
				#setattr(self, i, kwargs.get(i))
	
	#def setURL(self):
		#return self.URL
	
	#@setURL
	#def setHost(self, host, port = 5000):
		#self.host = host + ":" + str(port)
		#return self.host
	
#c = kallithea()
#print c.setHost('192.168.100.22')


#import inspect
#import debug

#class TESTX(object):
	#def __index__(self):
		#super(TEST, self)
		
	#def test1(self, data = "testdata"):
		#debug.debug(data = data, debug = True)
	
	#def test2(self, data = "data"):
		#print "stacks =", inspect.stack()
		#for name, datax in inspect.getmembers(self, inspect.isclass):
			#print "name  :", name
			#print "datax :", repr(datax)
			#print "+" * 200
			#if name == 'im_class':
				#print "dir(datax) =", dir(repr(datax))
				#print "-" * 200
				#print 'name : %s' % name
				#print 'data : %s' % repr(datax)
				#print "=" * 200
			
			#elif name == '__class__':
				#print "dir(datax) =", dir(repr(datax))
				#print "-" * 200
				#print 'name : %s' % name
				#print 'data : %s' % repr(datax).split('__main__.', 1)[1][:-2]
				#print "=" * 200
			
		

#c = TESTX()
#c.test1()

#import vping
#import re
#import sys
#sys.path.append(r'f:\PROJECTS\REPOSITORY\mp3link_django\mp3link\mp3link')
#import settings
# #print "settings.CHECK_HOSTS =", settings.CHECK_HOSTS

#class ping():
	#def __init__(self, host = [], timeout = 2, count = 4):
		#self.host = host
		#if not self.host:
			#self.host = settings.CHECK_HOSTS
		#self.timeout = timeout
		#self.count = count
		#for i in self.host:
			# #print "host =", i
			#self.ping = self.pinging(i)
			#attr_host1 = re.sub('http:|https:|www.|/', '', i)
			#if len(attr_host1.split(".")) == 4:
				#attr_host = "ip_" + re.sub("\.", "_", attr_host1)
			#else:
				#attr_host = re.sub("\.", "_", attr_host1)
			#setattr(self, attr_host, self.ping)
		
	#def pinging(self, host):
		#return vping.vping(host, self.timeout, self.count)
	
#url = 'http://www.google.com', 'www.yahoo.com'
# #print ping().ping
#print "ping(url).google_com =", ping().google_com
#print "ping(url).192_168_1_2 =", ping().ip_192_168_1_2



def test(data):
	def aaa():
		print "data on aaa =", data
	return aaa()
	
test("SUPERMAN").aaa()