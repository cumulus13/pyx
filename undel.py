import winshell
import os

def undelete():
	r = winshell.recycle_bin()
	delete_data = {}
	x = 1
	z = 1
	for i in r.enumerate():
		try:
			t = i.getatime().Format('%Y%m%d%H%M%S')
		except:
			t = x
			x += 1
		n = i.name()
		delete_data.update({t:n})
	a = delete_data.keys()
	b = sorted(a, reverse=True)
	for i in b:
		print str(z) + ".", delete_data.get(i)
		z += 1
	q = raw_input('Select Number: ')
	q1 = []
	if "," in q:
		q = q.split(",")
		for i in q:
			q1.append(i.strip())
		for i in q1:
			try:
				print "UNDELETE:", r.undelete(delete_data.get(b[int(i) - 1])), "[SUCCESS]"	
			except:
				print "UNDELETE:", r.undelete(delete_data.get(b[int(i) - 1])), "[ERROR]"	
	else:
		try:
			print "UNDELETE:", r.undelete(delete_data.get(b[int(q) - 1])), "[SUCCESS]"
		except:
			print "UNDELETE:", r.undelete(delete_data.get(b[int(i) - 1])), "[ERROR]"	
	
	
if __name__ == '__main__':
	undelete()