import os
import sys
import traceback

__version__ = "0.1"
__test__ = "0.1"
__author__ = "LICFACE"
__url__ = "licface@yahoo.com"
__email__ = "licface@yahoo.com"
__target__ = "all"
__build__ = "2.7"
__error__ = traceback.format_exc()
__usage__ = "Usage: " + str(__file__) + " PID [show|hide|top|nor]"

pdata = os.popen("cmdow.exe /t").readlines()

def topme():
	for i in range(0,len(pdata)):
		j = str(pdata[i]).split("\n")
		#print j[0]
		#print os.path.splitext(__file__)[0]
		#if str(os.path.splitext(__file__)[0]) in j[0]:
		if " - v" in j[0]:
			#print j[0]
			x = str(str(j[0]).split(" 1 ")[0]).strip()
			#print x
			#y = str(x).split(" 1 ")
			#print y
			#width = int(sys.argv[1]) * 10
			#height = int(sys.argv[2]) * 10
			#print "Width = ", width
			#print "Height = ", height
			os.system("cmdow.exe " + str(x) + " /top ")
		else:
			pass
	
def winme():
	for i in range(0,len(pdata)):
		j = str(pdata[i]).split("\n")
		#print j[0]
		#print os.path.splitext(__file__)[0]
		#if str(os.path.splitext(__file__)[0]) in j[0]:
		if " - v" in j[0]:
			#print j[0]
			x = str(str(j[0]).split(" 1 ")[0]).strip()
			#print x
			#y = str(x).split(" 1 ")
			#print y
			#width = int(sys.argv[1]) * 10
			#height = int(sys.argv[2]) * 10
			#print "Width = ", width
			#print "Height = ", height
			os.system("cmdow.exe " + str(x) + " /not ")
			os.system("cmdow.exe " + str(x) + " /not ")
		else:
			pass
			
def detectto(window):
	d = dict()
	e = []
	for i in range(1,len(pdata)):
		j = str(pdata[i]).split("\n")
		j2 = str(j[0]).split("Vis")
		j3 = str(j2[0]).split(" 1 ")
		name = str(j3[0]).strip()
		#print j2[1]
		if str(window) in j2[1]:
			#print j2[1]
			if "- resize" in j2[1]:
				#print j2[1]
				pass
			else:
				#print i
				#print j2[1]
				name2 = str(j3[0]).strip()
				d.update({i:[name2,j2[1]]})
				e.append(j2[1])
	#print "d = ",d
	#print "e = ",e
	return [d,e]
			
def winto(window):
	#print "windows = ", window
	#print len(detectto(window)[0])
	#print detectto(window)[0]
	#print detectto(window)[0].keys()[1]
	#print "-"*120
	
	if len(detectto(window)[0]) > 1:
		for h in range(0,len(detectto(window)[0].keys())):
			g = detectto(window)[0].keys()[h]
			if " to " in (detectto(window)[0]).get(g)[1]:
				pass
			else:
				print str(h) + ". " + (detectto(window)[0]).get(g)[1]
				x = (detectto(window)[0]).get(g)[0]
				print "\n"
				ex = raw_input("No Window: ")
				os.system("cmdow.exe " + str(x) + " /not ")
				
def topto(window):
	#print "windows = ", window
	#print len(detectto(window)[0])
	#print detectto(window)[0]
	#print detectto(window)[0].keys()[1]
	#print "-"*120
	
	if len(detectto(window)[0]) > 1:
		for h in range(0,len(detectto(window)[0].keys())):
			g = detectto(window)[0].keys()[h]
			if " to " in (detectto(window)[0]).get(g)[1]:
				pass
			else:
				print str(h) + ". " + (detectto(window)[0]).get(g)[1]
				x = (detectto(window)[0]).get(g)[0]
				print "\n"
				ex = raw_input("No Window: ")
				os.system("cmdow.exe " + str(x) + " /top ")
				
def closeto(window):
	#print "windows = ", window
	#print len(detectto(window)[0])
	#print detectto(window)[0]
	#print detectto(window)[0].keys()[1]
	#print "-"*120
	
	if len(detectto(window)[0]) > 1:
		x2 = dict()
		for h in range(0,len(detectto(window)[0].keys())):
			g = detectto(window)[0].keys()[h]
			if " to " in (detectto(window)[0]).get(g)[1]:
				pass
			else:
				print str(h + 1) + ". " + (detectto(window)[0]).get(g)[1]
				x = (detectto(window)[0]).get(g)[0]
				x2.update({h+1:x})
				#print x
				#print "\n"
		#print x2
		ex = raw_input("No Window: ")
		os.system("cmdow.exe " + str(x2.get(int(ex))) + " /CLS ")
			

pdata = os.popen("cmdow /t").readlines()
ps = dict()
name = dict()
for i in range(1,len(pdata)):
		j = str(pdata[i]).split("\n")
		j2 = str(j[0]).split("Vis")
		#print "J = ",j
		j3 = str(j2[-1]).split(" ")
		#print j3
		z = []
		for x in range(1,len(j3)):
				#print dir(z)
				if str(j3[x]).strip() == '':
						pass
				else:
						z.append(j3[x])
		#print z
		for r in xrange(0,len(z)):
			k = str(j[0]).split("Res")
			#print "K = ",k
			L = str(k[0]).split(' 1 ')
			#print "L = ",L
			m = str(L[-1]).strip()
			#print "M = ",m
			n = str(L[0]).strip()
			#print "N = ",n
			ps.update({m:n})
#print ps
show = "/vis"
hide = "/hid"
top = "/top"
nor = "/not"
if sys.argv[-1] == "show":
	os.system("cmdow " + ps.get(str(sys.argv[1])) + " /vis")
elif sys.argv[-1] == "hide":
	os.system("cmdow " + ps.get(str(sys.argv[1])) + " /hid")
elif sys.argv[-1] == "top":
	if len(sys.argv) > 3:
		os.system("cmdow " + ps.get(str(sys.argv[1])) + " /top")
	else:
		topme()
elif sys.argv[-1] == "nor":
	if len(sys.argv) > 3:
		os.system("cmdow " + ps.get(str(sys.argv[1])) + " /not")
	else:
		winme()
elif sys.argv[2] == "to":
	#print "WEK WEK"
	if sys.argv[1] == "top":
		topto(sys.argv[3])
	elif sys.argv[1] == "nor":
		winto(sys.argv[3])
	elif sys.argv[1] == "close":
		closeto(sys.argv[3])
	elif sys.argv[1] == "exit":
		closeto(sys.argv[3])
	elif sys.argv[1] == "x":
		closeto(sys.argv[3])
	else:
		print __usage__
else:
	print "\n"
	print 
	print __usage__
