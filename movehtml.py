import sys
import os
import shutil
import argparse
import diffmov

def usage():
	parser = argparse.ArgumentParser()
	parser.add_argument('-q', '--quit', help='Overwrite all action', action='store_true')
	parser.add_argument('-v', '--verbosity', help='Print detail running process', action	='store_true')
	parser.add_argument('-o', '--Overwrite', help='Other name option for "-q" or "--quit"', action='store_true')
	parser.add_argument('SRC', help='Source directory', action='store')
	parser.add_argument('DST', help='Destination directory', action='store')
	# if len(sys.argv) == 2:
	# 	movehtml(sys.argv[1], None)
	# elif len(sys.argv) == 3:
	# 	movehtml(sys.argv[1], sys.argv[2])
	# print "len(sys.argv) =", len(sys.argv)
	if len(sys.argv) > 1:
		if sys.argv[1] == '-q':
			movehtml(quit=True)
		else:
			args = parser.parse_args()
			movehtml(args.SRC, args.DST)
	else:
		print "\n"
		# print "\t Usage:", os.path.basename(__file__), ".|(source directory) (destination directory)|HTML"
		parser.print_help()
		print "\n"
		print "\t if you continue, this will make a directory 'HTML' in current directory"
		print "\t and automatic find file *htm* and move to it"
		q = raw_input("\t Do you want to continue ? [y/n]: ")
		if str(q).lower() == 'y':
			movehtml()

def movehtml(src=None, dest=None, quit=None, verbosity=None):
	if not dest == None and os.path.isdir(dest):
		if not str(dest).endswith("HTML"):
			os.makedirs(os.path.join(dest, 'HTML'))
			dest = os.path.join(dest, 'HTML')
		if not src == None and  os.path.isdir(src):
			listdir = os.listdir(src)
		else:
			src = os.getcwd()
			listdir = os.listdir(src)
	else:
		if not src == None and  os.path.isdir(src):
			listdir = os.listdir(src)
		else:
			src = os.getcwd()
			listdir = os.listdir(src)

		if os.path.isdir(os.path.join(os.getcwd(), 'HTML')):
			dest = os.path.join(os.getcwd(), 'HTML')
		else:
			os.makedirs(os.path.join(os.getcwd(), 'HTML'))
			dest = os.path.join(os.getcwd(), 'HTML')
				
	for i in listdir:
		if i.endswith('htm') or i.endswith('html'):
			if os.path.isfile(os.path.join(dest, i)):
				if quit:
					os.remove(os.path.join(dest, i))
					shutil.move(os.path.join(src, i), dest)
				else:
					pass
			else:
				shutil.move(os.path.join(src, i), dest)
		elif i.endswith('_files'):
			if os.path.isdir(os.path.join(dest, i)):
				if quit:
					shutil.rmtree(os.path.join(dest, i))
					shutil.move(os.path.join(src, i), dest)
				else:
					pass
			else:
				shutil.move(os.path.join(src, i), dest)

if __name__ == '__main__':
	# if len(sys.argv) == 2:
	# 	movehtml(sys.argv[1], None)
	# elif len(sys.argv) == 3:
	# 	movehtml(sys.argv[1], sys.argv[2])
	# else:
	# 	print "\n"
	# 	print "\t Usage:", os.path.basename(__file__), ".|(source directory) (destination directory)|HTML"
	# 	print "\n"
	# 	print "\t if you continue, this will make a directory 'HTML' in current directory"
	# 	print "\t and automatic find file *htm* and move to it"
	# 	q = raw_input("\t Do you want to continue ? [y/n]: ")
	# 	if str(q).lower() == 'y':
	# 		movehtml()
	usage()

