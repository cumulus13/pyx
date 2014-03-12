import os
import sys
import traceback

filename = os.path.split(sys.argv[0])[1]
usage = "\t Use : " + filename + " [name of vhost] [directory vhost]\n\n\t Exp : " + filename + " example.com \"c:\www\example.com\"\n\n\t By  : licface"
usage2 = "\t Use : " + filename + " [name of vhost] [directory vhost] [directoryindex]\n\n\t Exp : " + filename + " example.com \"c:\www\example.com\" Index.html\n\n\t By  : licface"

try:
	data_dir = str(sys.argv[2]).replace("\\", "/") + "/"
	data = """
<VirtualHost *:80>
  ServerName %s
  DocumentRoot "%s"
  CustomLog logs/%s-custom.log common
  ErrorLog logs/%s-error.log
  ServerAlias www.%s
  ServerAdmin root@%s
</VirtualHost>""" %(sys.argv[1],data_dir,sys.argv[1],sys.argv[1],sys.argv[1],sys.argv[1])
	
	data_test = open(r"D:\xampp\apache\conf\extra\httpd-vhosts.conf").read()
	#print data_test
	#print "-"*80
	if "www." in sys.argv[1]:
		print "\t Can't add with suffix \"www.\", please remove it ! "
		print usage
	else:
		if sys.argv[1] in data_test:
			print "\n"
			print "\t vhost has been added ! \n"
		else:
			if len(sys.argv) > 3:
				try:
					dataA = """
<VirtualHost *:80>
   ServerName %s
   DocumentRoot "%s"
   CustomLog logs/%s-custom.log common
   ErrorLog logs/%s-error.log
   ServerAlias www.%s
   ServerAdmin root@%s
   DirectoryIndex %s
</VirtualHost>""" %(sys.argv[1],data_dir,sys.argv[1],sys.argv[1],sys.argv[1],sys.argv[1],sys.argv[3])
					file = open(r"D:\xampp\apache\conf\extra\httpd-vhosts.conf","a")
					file.write("\n")
					file.write(dataA)
					file.close()
					
				except:
					print "\n"
					data_e = traceback.format_exc()
					print "Programming Develop b :"
					print "\t " + str(data_e)
					print "-"*80
					print usage2
			else:
				file = open(r"D:\xampp\apache\conf\extra\httpd-vhosts.conf","a")
				file.write("\n")
				file.write(data)
				file.close()
				#file2 = open(r"D:\xampp\apache\conf\extra\httpd-vhosts.conf", "r")
				#print file2.read()
				#file2.close()
except:
	print "\n"
	#data_e = traceback.format_exc()
	#print "ERROR : "
	#print "\t " + str(data_e)
	#print "-"*80
	print usage