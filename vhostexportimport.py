import os
import sys
import addhost

def export(path):
	c = addhost.simplednshostadd('192.168.10.2', 'blackid')
	data = os.listdir(path)
	for i in data:
		a = str(i).split(".conf")
		#print "a = ", a
		if a[0] == ".git":
			pass
		else:
			print "add %s" %(a[0])
			c.add(a[0], 8053, '192.168.10.2', '192.168.10.2', '192.168.10.2', '192.168.10.2', '192.168.10.2', '192.168.10.2', '127.0.0.1', 'blackid', 'root@'+str(a[0]))


if __name__ == "__main__":
	export(os.path.abspath(sys.argv[1]))