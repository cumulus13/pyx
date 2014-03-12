import os
import sys
import traceback

__version__ = "1.0"
__test__ = "0.1"
__author__ = "LICFACE"
__url__ = "licface@yahoo.com"
__email__ = "licface@yahoo.com"
__target__ = "all"
__build__ = "2.7"
__error__ = traceback.format_exc()
__help__ = "   Use: " + os.path.splitext(os.path.basename(__file__))[0] + " [me|to [Name Of Search Of Window]] [WIDTH] [HEIGHT]"

pdata = os.popen("cmdow.exe /t").readlines()
#print pdata
def resizeme():
	for i in range(0,len(pdata)):
		j = str(pdata[i]).split("\n")
		#print j[0]
		#print os.path.splitext(__file__)[0]
		#if str(os.path.splitext(__file__)[0]) in j[0]:
		if " - resize" in j[0]:
			#print j[0]
			x = str(str(j[0]).split(" 1 ")[0]).strip()
			#print x
			#y = str(x).split(" 1 ")
			#print y
			if "," in sys.argv[2]:
				q = str(sys.argv[2]).split(",")
				width = int(str(q[0]).strip()) * 10
				height = int(str(q[1]).strip()) * 10
			else:
				width = int(str(sys.argv[2]).strip()) * 10
				height = int(str(sys.argv[3]).strip()) * 10
			#print "Width = ", width
			#print "Height = ", height
			os.system("cmdow.exe " + str(x) + " /siz " + str(width) + " " + str(height))
		else:
			pass
			
def topme():
	for i in range(0,len(pdata)):
		j = str(pdata[i]).split("\n")
		#print j[0]
		#print os.path.splitext(__file__)[0]
		#if str(os.path.splitext(__file__)[0]) in j[0]:
		if " - resize" in j[0]:
			#print j[0]
			x = str(str(j[0]).split(" 1 ")[0]).strip()
			#print x
			#y = str(x).split(" 1 ")
			#print y
			width = int(sys.argv[1]) * 10
			height = int(sys.argv[2]) * 10
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
		if " - resize" in j[0]:
			#print j[0]
			x = str(str(j[0]).split(" 1 ")[0]).strip()
			#print x
			#y = str(x).split(" 1 ")
			#print y
			width = int(sys.argv[1]) * 10
			height = int(sys.argv[2]) * 10
			#print "Width = ", width
			#print "Height = ", height
			os.system("cmdow.exe " + str(x) + " /not ")
		else:
			pass
	
def resizeto(window):
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
	
def _resizeto(window):
	#print "windows = ", window
	#print len(resizeto(window)[0])
	#print resizeto(window)[0]
	#print resizeto(window)[0].keys()[1]
	#print "-"*120
	x2 = dict()
	if len(resizeto(window)[0]) > 1:
		for h in range(0,len(resizeto(window)[0].keys())):
			g = resizeto(window)[0].keys()[h]
			print str(h) + ". " + (resizeto(window)[0]).get(g)[1]
			x = (detectto(window)[0]).get(g)[0]
			x2.update({h+1:x})
			if "," in sys.argv[3]:
				q = str(sys.argv[3]).split(",")
				width = int(str(q[0]).strip()) * 10
				height = int(str(q[1]).strip()) * 10
			else:
				width = int(str(sys.argv[3]).strip()) * 10
				height = int(str(sys.argv[4]).strip()) * 10
			
		ex = raw_input(" No Window: ")
		if ex != '':
			os.system("cmdow.exe " + str(x2.get(int(ex))) + " /siz " + str(width) + " " + str(height))
		else:
			pass
			
	else:
		#pass
		#print resizeto(window)[0]
		if "," in sys.argv[3]:
				q = str(sys.argv[3]).split(",")
				width = int(str(q[0]).strip()) * 10
				height = int(str(q[1]).strip()) * 10
		else:
			width = int(str(sys.argv[3]).strip()) * 10
			height = int(str(sys.argv[4]).strip()) * 10
		x2 = dict()
		for i in resizeto(window)[0]:
			print str(i) + ". \"" +  (resizeto(window)[0]).get(i)[1] + "\""
			x2.update({i:(resizeto(window)[0]).get(i)[0]})
		print "\n"
		ex = raw_input(" No Window: ")
		if ex != '':
			os.system("cmdow.exe " + str(x2.get(int(ex))) + " /siz " + str(width) + " " + str(height))
		else:
			pass
		
def main():
	if len(sys.argv) > 1:
		if sys.argv[1] == "me":
			resizeme()
		elif sys.argv[1] == "to":
			_resizeto(sys.argv[2])
        elif sys.argv[1] == "-h" or sys.argv[1] == "-help" or sys.argv[1] == "--help" or sys.argv[1] == "help" or sys.argv[1] == "--h":
            print "\n"
            print __help__
	else:
		resizeme()
			
if __name__ == "__main__":
	main()
	#_resizeto(sys.argv[1])
	#resizeto(sys.argv[1])