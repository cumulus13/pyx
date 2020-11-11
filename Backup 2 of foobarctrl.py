import os
import sys
MODULE_PATH = r'd:\PROJECTS\ctrfoobar2000'

if not os.path.exists(MODULE_PATH):
	print "INVALID MODULE_PATH !"
else:
	sys.path.insert(0, MODULE_PATH)
	import control
	ctrl = control.control()
	ctrl.usage()