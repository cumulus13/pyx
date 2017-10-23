import os
import sys

def rcopy(src, dest):
	destdir = os.path.basename(src)
	finaldest = os.path.join(os.path.abspath(dest), destdir)
	if not os.path.isdir(finaldest):
		os.makedirs(finaldest)
	print "SRC       =", src
	print "DST       =", finaldest
	if len(sys.argv) > 3:
		args = " ".join(sys.argv[3:])
		print "args =", args
		os.system('ROBOCOPY "{0}" "{1}" /mir /zb {2}'.format(src, finaldest, args))
	else:
		os.system('ROBOCOPY "{0}" "{1}" /mir /zb'.format(src, finaldest))

if __name__ == '__main__':
	rcopy(sys.argv[1], sys.argv[2])
