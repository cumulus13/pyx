import shutil
import sys
import os
import distutils.core

__version__ = "1.0"
__filename__ = os.path.basename(sys.argv[0])
__help__ = """ \n\tUse : """ + __filename__ + """ [FROM]  [TO] """

#function for copy directory tree (recursive)
def copydir(scr,dst):
	distutils.dir_util.copy_tree(scr,dst)

def copydir2(scr,dst):
	d_scr = str(scr).replace("\\","/")
	d_dst = str(dst).replace("\\","/")
	shutil.copytree(d_scr,d_dst)

def copydir3(scr,dst):
	import errno
	try:
		shutil.copytree(src, dst)
	except OSError as exc: # python >2.5
		if exc.errno == errno.ENOTDIR:
			shutil.copy(src, dst)
		else: raise

def copysearchdir(scr,dst):
	# First, create a list and populate it with the files
	# you want to find (1 file per row in myfiles.txt)
	files_to_find = []
	with open('myfiles.txt') as fh:
	    for row in fh:
	        files_to_find.append(row.strip)

	# Then we recursively traverse through each folder
	# and match each file against our list of files to find.
	for root, dirs, files in os.walk(scr):
	    for _file in files:
	        if _file in files_to_find:
	            # If we find it, notify us about it and copy it it to C:\NewPath\
	            print 'Found file in: ' + str(root)
	            shutil.copy(os.path.abspath(root + '/' + _file), dst)

#function for copy file to anything
def copyfile(scr,dst):
	shutil.copy2(scr,dst)
#print len(sys.argv)

#function for process copy
def process():
	if len(sys.argv) > 2:
		print os.path.isdir(sys.argv[1])
		print os.path.isdir(sys.argv[2])
		print "dir_dst = ", os.path.abspath(sys.argv[2])
		print "dst = ", os.path.join(os.path.abspath(sys.argv[2]),os.path.basename(sys.argv[1]))
		try:
			if os.path.isdir(sys.argv[1]) and os.path.isdir(sys.argv[2]) == False:
				if os.path.dirname(sys.argv[1]) in sys.argv[2]:
					copydir(sys.argv[1],sys.argv[2])
				else:
					os.mkdir(os.path.join(sys.argv[2],os.path.basename(sys.argv[1])))
					dst = os.path.join(sys.argv[2],os.path.basename(sys.argv[1]))
					copydir(sys.argv[1],dst)
			elif os.path.isdir(sys.argv[1]) and os.path.isdir(sys.argv[2]):
				if os.path.dirname(sys.argv[1]) in sys.argv[2]:
					_to = os.path.join(os.path.abspath(sys.argv[2]),os.path.basename(sys.argv[1]))
					if os.path.isdir(_to) == False:
						os.mkdir(os.path.join(os.path.abspath(sys.argv[2]),os.path.basename(sys.argv[1])))
						copydir(os.path.abspath(sys.argv[1]),_to)
					else:
						copydir(os.path.abspath(sys.argv[1]),sys.argv[2])
				else:
					os.mkdir(os.path.abspath(sys.argv[2],os.path.basename(sys.argv[1])))
					dst = os.path.join(sys.argv[2],os.path.basename(sys.argv[1]))
					copydir(sys.argv[1],dst)
			else:
				if os.path.isfile(sys.argv[1]) and os.path.isfile(sys.argv[2]):
					copyfile(sys.argv[1],sys.argv[2])
				elif os.path.isfile(sys.argv[1]) and os.path.isdir(sys.argv[2]):
					copyfile(sys.argv[1],sys.argv[2])
				elif os.path.isdir(sys.argv[1]) and os.path.isfile(sys.argv[2]):
					copyfile(sys.argv[1],sys.argv[2])
				else:
					print "3"
					print __help__

		except:
			import traceback
			if len(sys.argv) > 2:
				if sys.argv[-1] == '-v':
					print "\n\tError: ",traceback.format_exc()
				else:
					print __help__
	else:
		print __help__


if __name__ == "__main__":
	process()
