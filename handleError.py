import syslog
import traceback
import sys
import  textwrap

#def getError(facility,severity,host,port,msg):
class handleError:
	def __init__(self, name=''):
		self.name =  name
	
	def getError(self):
		try:
			#sys.argv[1]
			pass
		except:
			#er = traceback.format_exc()
			#print traceback.format_exc()
			#print "-" * 120
			#er =  sys.exc_info()
			etype, value, tb = sys.exc_info()
			#print "er =", tb
			TYPE = str(traceback.format_exception_only(etype, tb)[0]).split(":")[0].strip()
			#print traceback.format_exception(etype, value, tb)
			#print traceback.extract_tb(tb)[0]
			ERROR = str(traceback.format_exception_only(etype, value)[0]).split(":")[1].strip()
			DETAIL_1 =  traceback.format_tb(tb)[0].strip()
			DETAIL_2 =  textwrap.wrap(traceback.format_tb(tb)[0].strip(), 300)[0]
			print "TYPE   =", TYPE
			print "ERROR  =", ERROR
			if type_detail == "raw":
				print "DETAIL =", DETAIL_1
			else:
				print "DETAIL =", DETAIL_2
			
class mtest(handleError):
	def getError(self):
		print sys.argv[1]


he = mtest('rere')
he.getError()