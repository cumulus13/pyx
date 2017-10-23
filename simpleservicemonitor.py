import argparse
import sys
import os
import ConfigParser
import traceback
import collection

class MultiOrderedDict(ordereddict):
	def __setitem__

def test_config():
	config = ConfigParser.ConfigParser()
	config.optionxform=str
	try:
		config.read('config.ini')
		return config
	except:
		print traceback.format_exc()
