import module003
import sys

data = "IQService"
data_config = r"c:\Program Files\Fastream IQ Proxy Server Engine\IQ.ini"
try:
	if (sys.argv[1] == "config"):
		module003.set(data_config)
	else:
		module003.main(data)
except IndexError, e:
	print "\n\n"
	print "\t", e
