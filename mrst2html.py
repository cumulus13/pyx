
#!C:\Python27\python.exe
# EASY-INSTALL-SCRIPT: 'docutils==0.11','rst2html.py'
import pkg_resources
import os
import sys

def multi_rst2html():
	data = os.popen("dir /b *.rst").readlines()
	for i in data:
		x = os.path.abspath(i)
		sys.argv = x
		__requires__ = 'docutils==0.11'
		pkg_resources.run_script('docutils==0.11', 'rst2html.py')
		
if __name__ == "__main__":
	multi_rst2html()

