import os
import sys
import re
from debug import debug

class installer(object):
	def __init__(self):
		super(installer, self)

	def getList(self):
		name = ''
		l1 = os.popen('REG QUERY "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"').readlines()
		l2 = os.popen('REG QUERY "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"').readlines()
		for i in l1:
			if i == "\n":
				l1.remove(i)
		debug(l1=l1)
		for i in l2:
			if i == "\n":
				l2.remove(i)
		debug(l2=l2)
		m1 = {}
		m2 = {}
		n1 = 1
		n2 = 1
		for i in l1:
			debug(i=i)
			a = i.split("\n")[0]
			debug(a=a)
			a = os.path.basename(a)
			name = a
			debug(a=a)
			b = os.popen('REG QUERY "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\%s"'%(a)).readlines()
			debug(b=b)
			for j in b:
				if j == "\n":
					b.remove(j)
			debug(b=b)
			for j in b:
				j = j.split("\n")[0]
				debug(j=j)

				c = re.split("REG_SZ|REG_EXPAND_SZ|REG_DWORD|", j)
				debug(c = c)
				if len(c)> 1:
					if not m1.get(n1):
						m1.update({
							n1: {
								c[0].strip():c[1].strip(), 'name': name
							}
						})
					else:
						m1.get(n1).update(
							{
								c[0].strip():c[1].strip(), 'name': name
						})
			n1 +=1

		for i in l2:
			debug(i=i)
			a = i.split("\n")[0]
			debug(a=a)
			a = os.path.basename(a)
			name = a
			debug(a=a)
			b = os.popen('REG QUERY "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\%s"'%(a)).readlines()
			debug(b=b)
			for j in b:
				if j == "\n":
					b.remove(j)
			debug(b=b)
			for j in b:
				j = j.split("\n")[0]
				debug(j=j)

				c = re.split("REG_SZ|REG_EXPAND_SZ|REG_DWORD|", j)
				debug(c = c)
				if len(c)> 1:
					if not m2.get(n2):
						m2.update({
							n2: {
								c[0].strip():c[1].strip(), 'name': name
							}
						})
					else:
						m2.get(n2).update(
							{
								c[0].strip():c[1].strip(), 'name': name
						})
			n2 +=1

		# print "m1 =", m1
		# print "m2 =", m2
		return m1, m2

	def hide(self, name):
		os.system('REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\%s" /v SystemComponent /t REG_DWORD /d 1 /f'%(name))

	def delete(self. name):
		os.system('REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\%s" /v SystemComponent /t REG_DWORD /d 1 /f'%(name))

	def search(self, name):
		n = 1
		found = {}


	def navigator(self, data=None):
		if not data:
			l1,l2 = self.getList()
		else:
			l1,l2 = data
		n = 1
		for i in l1:
			if l1.get(i).get("DisplayName"):
				print n, ".", l1.get(i).get("DisplayName")
			else:
				print n, ".", l1.get(i)
			n+=1
		qnote = "[D]elete[N] | [H]ide[N] | [S]earch[Q], (N = Number of List, Q = Search Query/Text): "


if __name__ == '__main__':
	c = installer()
	# c.getList()
	c.navigator()