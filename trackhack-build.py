import os
import sys

def generate(path):
	data = os.popen("dir /s /b " + path).readlines()
	for i in data:
		d, n = str(i).split("\n")
		if os.path.basename(d) == "setup.py":
			os.chdir(os.path.dirname(d))
			os.system("c:\Python27\python.exe" + " setup.py build -c mingw32")
			os.system("c:\Python27\python.exe" + " setup.py bdist_wininst --skip-build")
			os.system("c:\Python27\python.exe" + " setup.py bdist_wininst --skip-build --target-version 2.7")
			os.system("c:\Python27\python.exe" + " setup.py sdist register -r djangopypi upload -r djangopypi")
			os.system("c:\Python27\python.exe" + " setup.py sdist register -r chishop upload -r chishop")
			os.system("copy /y dist\* d:\PYTHON_MODULES\trachacks")
			#print os.path.dirname(d)

if __name__ == "__main__":
	generate(sys.argv[1])