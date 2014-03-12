import sys
import os
import errno

usage = """ use : console big | small | super (Default normal)"""
file = r'd:\console\console.exe'
sprt = " "

def normal():
	try:
		os.execlp("d:\console\console.exe")

	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"


def small():
	try:
		#test = "d:\console\console_small.xml"
		#pypath = r'd:\console\console.exe'
		#os.spawnv("d:\console\console.exe", "d:\console\console_small.xml")
		#os.spawnv(os.P_NOWAIT, pypath, ('python','d:\console\console_small.xml'))
		opt = r'd:\console\console_small.xml'
		os.system('start ' + file + sprt + opt)

		
		#os.execlp("consolesmall.exe")
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"

def big():
	try:
		opt = r'd:\console\console_big.xml'
		#os.system('start ' + r'd:\console\console_big.xml' + " " + r'd:\console\console_big.xml')
		os.system('start ' + file + sprt + opt)
		#pypath = r'd:\console\console.exe'
		#os.spawnv(os.P_NOWAIT, pypath, ('python','d:\console\console_big.xml'))
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"

def super():	
	try:
		opt3 = r'd:\console\console_super.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
			
def startme(data):	
	#data = sys.argv[2]
	try:
		if (sys.argv <= 1):
			opt = r'd:\console\console_small.xml'
			os.system('start ' + file + sprt + opt + sprt + "'//k" + data + "'")
		elif (sys.argv <= 2):
			data002 = sys.argv[3]
			os.system('start ' + file + sprt + opt + sprt + "'//k" + data + data002 + "'")
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"


def chat():	
	try:
		opt3 = r'd:\console\console_kc.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
			
def spyx2():	
	try:
		opt3 = r'd:\console\console_spyx2.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"

			
def insecure():	
	try:
		opt3 = r'd:\console\console_nmap.xml -c """/k nmap"""'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
			
def tux():	
	try:
		opt3 = r'd:\console\console_tux.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
	

def blackid():	
	try:
		opt3 = r'd:\console\console_id.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
	

def super2():	
	try:
		opt3 = r'd:\console\console_super8.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
	
def center():	
	try:
		opt3 = r'd:\console\console_center.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
			
def winamp():	
	try:
		opt3 = r'd:\console\console_winamp.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
			
def center2():	
	try:
		opt3 = r'd:\console\console_center2.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"

def super3():	
	try:
		opt3 = r'd:\console\console_super_alpha.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
			
def qt():	
	try:
		opt3 = r'd:\console\console_qt.xml -c """/k d:\pyx\qtpath.bat"""'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
			
def gtk():	
	try:
		opt3 = r'd:\console\console_gtk.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
			
def gtk2():	
	try:
		opt3 = r'd:\console\console_gtk2.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
def gtk3():	
	try:
		opt3 = r'd:\console\console_gtk3.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
			
def gtk4():	
	try:
		opt3 = r'd:\console\console_gtk4.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
			
def gtk5():	
	try:
		opt3 = r'd:\console\console_gtk5.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
			
def mono():	
	try:
		opt3 = r'd:\console\console_mono.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
	
def moon():	
	try:
		opt3 = r'd:\console\console_moon.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
			
def tomcat():	
	try:
		opt3 = r'd:\console\console_tomcat.xml -c """/k cd /d d:\Tomcat\webapps"""'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
						
def python():	
	try:
		opt3 = r'd:\console\console_python.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
			
def pythonnet():	
	try:
		opt3 = r'd:\console\console_python4.xml -c """/k d:\pyx\python23.bat"""'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
			
def ironpython():	
	try:
		opt3 = r'd:\console\console_ironpython.xml -c """/k d:\pyx\ironpython.bat"""'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
def python2():	
	try:
		opt3 = r'd:\console\console_python2.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"

def python3():	
	try:
		opt3 = r'd:\console\console_python3.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
			
def runprog(datain):
	try:
		opt3 = r'd:\console\console_super_alpha.xml'
		
		os.system(file + sprt + opt3 + " -c '/k " + datain)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
			
def mini():	
	try:
		opt3 = r'd:\console\console_mini.xml -c """/k cd \"""'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
			
def ajax():	
	try:
		opt3 = r'd:\console\console_ajax.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"

def python4():	
	try:
		opt3 = r'd:\console\console_python4.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
			
			
def batik():	
	try:
		opt3 = r'd:\console\console_batik.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
			
			
def cisco():	
	try:
		opt3 = r'd:\console\console_cisco.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
			
def dynamips():	
	try:
		opt3 = r'd:\console\console_cisco.xml -c """/k d:\pyx\dynamips-start.bat"""'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
						
def css():	
	try:
		opt3 = r'd:\console\console_css.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
			
			
def java():	
	try:
		opt3 = r'd:\console\console_java.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
			
def java2():	
	try:
		opt3 = r'd:\console\console_java2.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"			
			
def jython():	
	try:
		opt3 = r'd:\console\console_jython.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
			
			
def klorofil():	
	try:
		opt3 = r'd:\console\console_klorofil.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
			
			
def netframework():	
	try:
		opt3 = r'd:\console\console_netframework.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
			
			
def nobug():	
	try:
		opt3 = r'd:\console\console_nobug.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
			
			
def php():	
	try:
		opt3 = r'd:\console\console_php.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
			
def cakephp():	
	try:
		opt3 = r'd:\console\console_cakephp.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"			
			
def cakephp2():	
	try:
		opt3 = r'd:\console\console_cakephp2.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"		
						
def python25():	
	try:
		opt3 = r'd:\console\console_python25.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
			
			
def python26():	
	try:
		opt3 = r'd:\console\console_python26.xml -c """/k d:\pyx\python26.bat"""'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
			
			
def rails():	
	try:
		opt3 = r'd:\console\console_rails.xml -c """/k d:\pyx\railspath.bat"""'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"

def flashrails():	
	try:
		opt3 = r'd:\console\console_flashrails.xml -c """/k D:\pyx\flashrails.bat"""'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"			
			
def ruby():	
	try:
		opt3 = r'd:\console\console_ruby.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
			
def ruby2():	
	try:
		opt3 = r'd:\console\console_ruby2.xml -c """/k d:\pyx\rubypath2.bat"""'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
			
def tcl():	
	try:
		opt3 = r'd:\console\console_tcl.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"

def tcl2():	
	try:
		opt3 = r'd:\console\console_tcl2.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
			

def tcl3():	
	try:
		opt3 = r'd:\console\console_tcl3.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
		

def tcl4():	
	try:
		opt3 = r'd:\console\console_tcl4.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"	
		

def tcl5():	
	try:
		opt3 = r'd:\console\console_tcl5.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"	
def vista():	
	try:
		opt3 = r'd:\console\console_vista.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
			
			
def wx():	
	try:
		opt3 = r'd:\console\console_wx.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
			
			
def wxperl():	
	try:
		opt3 = r'd:\console\console_wxperl.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
			
			
def wxperl2():	
	try:
		opt3 = r'd:\console\console_wxperl2.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
			
			
def wxpython():	
	try:
		opt3 = r'd:\console\console_wxpython.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
			
			
def wxruby():	
	try:
		opt3 = r'd:\console\console_wxruby.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
			
			
def wave():	
	try:
		opt3 = r'd:\console\console_wave.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"			
			
def x():	
	try:
		opt3 = r'd:\console\console_x.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
			
def codeigniter():	
	try:
		opt3 = r'd:\console\console_cig.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
			
def codeigniter2():	
	try:
		opt3 = r'd:\console\console_cig2.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
						
def jquery():	
	try:
		opt3 = r'd:\console\console_jquery.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
			
def jquery2():	
	try:
		opt3 = r'd:\console\console_jquery2.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"

			
def jquery3():	
	try:
		opt3 = r'd:\console\console_jquery3.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"

			
def jquery4():	
	try:
		opt3 = r'd:\console\console_jquery4.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
									
def tux2():	
	try:
		opt3 = r'd:\console\console_tux2.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
						
def tux3():	
	try:
		opt3 = r'd:\console\console_tux3.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"			
			
def mobil():	
	try:
		opt3 = r'd:\console\console_mobil.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
			
def cygwin():	
	try:
		opt3 = r'd:\console\console_cygwin.xml -c """/k c:\cygwin\Cygwin.bat"""'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
			
def cygwin2():	
	try:
		opt3 = r'd:\console\console_cygwin2.xml -c """/k c:\cygwin\Cygwin.bat"""'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"			
			
def pyqt4():	
	try:
		opt3 = r'd:\console\console_pyqt4.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
			
			
def netbean():	
	try:
		opt3 = r'd:\console\console_netbean.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
			
def editra():	
	try:
		opt3 = r'd:\console\console_editra.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
						
def perl():	
	try:
		opt3 = r'd:\console\console_perl.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
						
def syslog():	
	try:
		opt3 = r'd:\console\console_syslog.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
						
def android():	
	try:
		opt3 = r'd:\console\console_android.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
						
def linux():	
	try:
		opt3 = r'd:\console\console_linux.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
						
def ubuntu():	
	try:
		opt3 = r'd:\console\console_ubuntu.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
						
def editplus():	
	try:
		opt3 = r'd:\console\console_editplus.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
									
def spy():	
	try:
		opt3 = r'd:\console\console_spy.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
						
def note():	
	try:
		opt3 = r'd:\console\console_note.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
						
																								
def resin():	
	try:
		opt3 = r'd:\console\console_resin.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
			
def xampp():	
	try:
		opt3 = r'd:\console\console_xampp.xml'
		os.system('start ' + file + sprt + opt3)
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
									
def mysql():	
	try:
		namedata = os.path.split(sys.argv[0])
		usagemysql = """ use : """ + namedata[1] + """ mysql """ + """[username] """ + """[password]"""
		if (len(sys.argv) > 3):
			#opt3 = r'd:\console\console_mysql.xml -c """/k d:\xampp\mysql\bin\mysql.exe -u """' + str(sys.argv[2]) + """ -p""" + str(sys.argv[3])
			opt3 = r'd:\console\console_mysql.xml -c """/k d:\xampp\mysql\bin\mysql.exe -u %s -p%s"""' %(str(sys.argv[2]), str(sys.argv[3]))
			#print "sys.argv[2] = ", sys.argv[2]
			#print "sys.argv[3] = ", sys.argv[3]
			#print opt3
			os.system('start ' + file + sprt + opt3)
			
		else:
			os.system('cls')
			print "\n"
			print "\t" + usagemysql, "\n"
			#print "sys.argv[2] = ", sys.argv[2]
			
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"
			
def oracle():	
	try:
		namedata = os.path.split(sys.argv[0])
		usageoracle = """ use : """ + namedata[1] + """ oracle """ + """[username] """ + """[password]"""
		if (len(sys.argv) > 3):
			#opt3 = r'd:\console\console_mysql.xml -c """/k d:\xampp\mysql\bin\mysql.exe -u """' + str(sys.argv[2]) + """ -p""" + str(sys.argv[3])
			opt3 = r'd:\console\console_oracle.xml -c """/k i:\oraclexe\app\oracle\product\10.2.0\server\BIN\sqlplus.exe %s/%s"""' %(str(sys.argv[2]), str(sys.argv[3]))
			#print "sys.argv[2] = ", sys.argv[2]
			#print "sys.argv[3] = ", sys.argv[3]
			#print opt3
			os.system('start ' + file + sprt + opt3)
			
		else:
			os.system('cls')
			print "\n"
			print "\t" + usageoracle, "\n"
			#print "sys.argv[2] = ", sys.argv[2]
			
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"	
			
def oracle2():	
	try:
		namedata = os.path.split(sys.argv[0])
		usageoracle = """ use : """ + namedata[1] + """ oracle """ + """[username] """ + """[password]"""
		if (len(sys.argv) > 3):
			#opt3 = r'd:\console\console_mysql.xml -c """/k d:\xampp\mysql\bin\mysql.exe -u """' + str(sys.argv[2]) + """ -p""" + str(sys.argv[3])
			opt3 = r'd:\console\console_oracle2.xml -c """/k i:\oraclexe\app\oracle\product\10.2.0\server\BIN\sqlplus.exe %s/%s"""' %(str(sys.argv[2]), str(sys.argv[3]))
			#print "sys.argv[2] = ", sys.argv[2]
			#print "sys.argv[3] = ", sys.argv[3]
			#print opt3
			os.system('start ' + file + sprt + opt3)
			
		else:
			os.system('cls')
			print "\n"
			print "\t" + usageoracle, "\n"
			#print "sys.argv[2] = ", sys.argv[2]
			
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"			
def oracle3():	
	try:
		namedata = os.path.split(sys.argv[0])
		usageoracle = """ use : """ + namedata[1] + """ oracle """ + """[username] """ + """[password]"""
		if (len(sys.argv) > 3):
			#opt3 = r'd:\console\console_mysql.xml -c """/k d:\xampp\mysql\bin\mysql.exe -u """' + str(sys.argv[2]) + """ -p""" + str(sys.argv[3])
			opt3 = r'd:\console\console_oracle3.xml -c """/k i:\oraclexe\app\oracle\product\10.2.0\server\BIN\sqlplus.exe %s/%s"""' %(str(sys.argv[2]), str(sys.argv[3]))
			#print "sys.argv[2] = ", sys.argv[2]
			#print "sys.argv[3] = ", sys.argv[3]
			#print opt3
			os.system('start ' + file + sprt + opt3)
			
		else:
			os.system('cls')
			print "\n"
			print "\t" + usageoracle, "\n"
			#print "sys.argv[2] = ", sys.argv[2]
			
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"		
			
def oracle4():	
	try:
		namedata = os.path.split(sys.argv[0])
		usageoracle = """ use : """ + namedata[1] + """ oracle """ + """[username] """ + """[password]"""
		if (len(sys.argv) > 3):
			#opt3 = r'd:\console\console_mysql.xml -c """/k d:\xampp\mysql\bin\mysql.exe -u """' + str(sys.argv[2]) + """ -p""" + str(sys.argv[3])
			opt3 = r'd:\console\console_oracle4.xml -c """/k i:\oraclexe\app\oracle\product\10.2.0\server\BIN\sqlplus.exe %s/%s"""' %(str(sys.argv[2]), str(sys.argv[3]))
			#print "sys.argv[2] = ", sys.argv[2]
			#print "sys.argv[3] = ", sys.argv[3]
			#print opt3
			os.system('start ' + file + sprt + opt3)
			
		else:
			os.system('cls')
			print "\n"
			print "\t" + usageoracle, "\n"
			#print "sys.argv[2] = ", sys.argv[2]
			
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"		
			
def oracle5():	
	try:
		namedata = os.path.split(sys.argv[0])
		usageoracle = """ use : """ + namedata[1] + """ oracle """ + """[username] """ + """[password]"""
		if (len(sys.argv) > 3):
			#opt3 = r'd:\console\console_mysql.xml -c """/k d:\xampp\mysql\bin\mysql.exe -u """' + str(sys.argv[2]) + """ -p""" + str(sys.argv[3])
			opt3 = r'd:\console\console_oracle5.xml -c """/k i:\oraclexe\app\oracle\product\10.2.0\server\BIN\sqlplus.exe %s/%s"""' %(str(sys.argv[2]), str(sys.argv[3]))
			#print "sys.argv[2] = ", sys.argv[2]
			#print "sys.argv[3] = ", sys.argv[3]
			#print opt3
			os.system('start ' + file + sprt + opt3)
			
		else:
			os.system('cls')
			print "\n"
			print "\t" + usageoracle, "\n"
			#print "sys.argv[2] = ", sys.argv[2]
			
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n \t Program tidak dapat ditemukan ! \n"
		elif e.errno == errno.ENOEXEC:
			print "\n \t Program tidak dapat dieksekusi ! \n"
		else:
			print "\n \t Program tidak dapat berjalan di Win32 System ! \n"		
		
	
def main():
	try:
		if (len(sys.argv) < 1):
			normal()
		else:
			if (sys.argv[1] == "small"):
				small()
			elif (sys.argv[1] == "big"):
				big()
			elif (sys.argv[1] == "super"):
				super()
			elif (sys.argv[1] == "super8"):
				super2()
			elif (sys.argv[1] == "superalpha"):
				super3()
			elif (sys.argv[1] == "chat"):
				chat()
			elif (sys.argv[1] == "tux"):
				tux()
			elif (sys.argv[1] == "tux2"):
				tux2()
			elif (sys.argv[1] == "tux3"):
				tux3()
			elif (sys.argv[1] == "id"):
				blackid()
			elif (sys.argv[1] == "spyx2"):
				spyx2()
			elif (sys.argv[1] == "center"):
				center()
			elif (sys.argv[1] == "center2"):
				center2()
			elif (sys.argv[1] == "qt"):
				qt()
			elif (sys.argv[1] == "gtk"):
				gtk()
			elif (sys.argv[1] == "gtk2"):
				gtk2()
			elif (sys.argv[1] == "gtk3"):
				gtk3()
			elif (sys.argv[1] == "gtk4"):
				gtk4()
			elif (sys.argv[1] == "gtk5"):
				gtk5()
			elif (sys.argv[1] == "mono"):
				mono()
			elif (sys.argv[1] == "moon"):
				moon()
			elif (sys.argv[1] == "python"):
				python()
			elif (sys.argv[1] == "python2"):
				python2()
			elif (sys.argv[1] == "python3"):
				python3()
			elif (sys.argv[1] == "python4"):
				python4()
			elif (sys.argv[1] == "pyqt4"):
				pyqt4()
			elif (sys.argv[1] == "ajax"):
				ajax()
			elif (sys.argv[1] == "batik"):
				batik()
			elif (sys.argv[1] == "cisco"):
				cisco()
			elif (sys.argv[1] == "dynamips"):
				dynamips()
			elif (sys.argv[1] == "dynagen"):
				dynamips()
			elif (sys.argv[1] == "css"):
				css()
			elif (sys.argv[1] == "java"):
				java()
			elif (sys.argv[1] == "java2"):
				java2()
			elif (sys.argv[1] == "jython"):
				jython()
			elif (sys.argv[1] == "klorofil"):
				klorofil()
			elif (sys.argv[1] == "netframework"):
				netframework()
			elif (sys.argv[1] == "nobug"):
				nobug()
			elif (sys.argv[1] == "php"):
				php()
			elif (sys.argv[1] == "python25"):
				python25()
			elif (sys.argv[1] == "python26"):
				python26()
			elif (sys.argv[1] == "rails"):
				rails()
			elif (sys.argv[1] == "flashrails"):
				flashrails()
			elif (sys.argv[1] == "ruby"):
				ruby()
			elif (sys.argv[1] == "ruby2"):
				ruby2()
			elif (sys.argv[1] == "tcl"):
				tcl()
			elif (sys.argv[1] == "tcl2"):
				tcl2()
			elif (sys.argv[1] == "tcl3"):
				tcl3()
			elif (sys.argv[1] == "tcl4"):
				tcl4()
			elif (sys.argv[1] == "tcl5"):
				tcl5()
			elif (sys.argv[1] == "vista"):
				vista()
			elif (sys.argv[1] == "wx"):
				wx()
			elif (sys.argv[1] == "perl"):
				perl()
			elif (sys.argv[1] == "wxperl"):
				wxperl()
			elif (sys.argv[1] == "wxperl2"):
				wxperl2()
			elif (sys.argv[1] == "wxpython"):
				wxpython()
			elif (sys.argv[1] == "wxruby"):
				wxruby()
			elif (sys.argv[1] == "x"):
				x()
			elif (sys.argv[1] == "tux2"):
				tux2()
			elif (sys.argv[1] == "tux3"):
				tux3()
			elif (sys.argv[1] == "cygwin"):
				cygwin()
			elif (sys.argv[1] == "cygwin2"):
				cygwin2()
			elif (sys.argv[1] == "mysql"):
				mysql()
			elif (sys.argv[1] == "oracle"):
				oracle()
			elif (sys.argv[1] == "oracle2"):
				oracle2()
			elif (sys.argv[1] == "oracle3"):
				oracle3()
			elif (sys.argv[1] == "oracle4"):
				oracle4()
			elif (sys.argv[1] == "oracle5"):
				oracle5()
			elif (sys.argv[1] == "mobil"):
				mobil()
			elif (sys.argv[1] == "jquery"):
				jquery()
			elif (sys.argv[1] == "jquery2"):
				jquery2()
			elif (sys.argv[1] == "jquery3"):
				jquery3()
			elif (sys.argv[1] == "jquery4"):
				jquery4()
			elif (sys.argv[1] == "wave"):
				wave()
			elif (sys.argv[1] == "tomcat"):
				tomcat()
			elif (sys.argv[1] == "codeigniter"):
				codeigniter()
			elif (sys.argv[1] == "codeigniter2"):
				codeigniter2()
			elif (sys.argv[1] == "winamp"):
				winamp()
			elif (sys.argv[1] == "ironpython"):
				ironpython()
			elif (sys.argv[1] == "pythonnet"):
				pythonnet()
			elif (sys.argv[1] == "cakephp"):
				cakephp()
			elif (sys.argv[1] == "cakephp2"):
				cakephp2()
			elif (sys.argv[1] == "resin"):
				resin()
			elif (sys.argv[1] == "editra"):
				editra()
			elif (sys.argv[1] == "xampp"):
				xampp()
			elif (sys.argv[1] == "netbean"):
				netbean()
			elif (sys.argv[1] == "nmap"):
				insecure()
			elif (sys.argv[1] == "android"):
				android()
			elif (sys.argv[1] == "spy"):
				spy()
			elif (sys.argv[1] == "linux"):
				linux()
			elif (sys.argv[1] == "note"):
				note()
			elif (sys.argv[1] == "syslog"):
				syslog()
			elif (sys.argv[1] == "ubuntu"):
				ubuntu()
			elif (sys.argv[1] == "editplus"):
				editplus()
			elif (sys.argv[1] == "mini"):
				mini()
			elif (sys.argv[1] == "-r"):
				try:
					datain2 = sys.argv[2] + "'"
					runprog(datain2)
				except IndexError, e:
					print "\t\t Run Program invalid !\n"
					
			elif (sys.argv > 1):
				for i in range(3):
					startme(sys.argv[i])
			else:
				#os.system("cls")
				#print "\n"
				#print usage
				tcl4()
	except IndexError, e:
		#os.system("cls")
		#print str(e), "\n\n"
		#print "\n"
		#print usage
		normal()

if __name__ == '__main__':
	main()
