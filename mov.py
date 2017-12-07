import sys
# import time
import os
# import shutil
# from progressbar import AnimatedMarker, Bar, BouncingBar, Counter, ETA, \
#                         FileTransferSpeed, FormatLabel, Percentage, \
#                         ProgressBar, ReverseBar, RotatingMarker, \
#                         SimpleProgress, Timer

# def progress():
#     widgets = [Bar('>'), ' ', ETA(), ' ', ReverseBar('<')]
#     pbar = ProgressBar(widgets=widgets, maxval=10000000).start()
#     for i in range(1000000):
#         # do something
#         pbar.update(10*i+1)
#     pbar.finish()

# if sys.argv[1] == '-c':
# 	progress()
	# q = raw_input(" exit now (y/n)")
	# if q == 'y':
	# 	os.system('exit')
	# elif q == 'n':
	# 	print "not exit"
	# else:
	# 	print "not exit"
# if sys.argv[1] == '-s':
	# os.system('start cmd /k "mode 80,8 & python ycp.py -c & mo & echo exit ? & PAUSE & exit"')
os.system('start cmd /k "mode 100,35 & mo BL=3000 & cls & python c:\pyx\mva.py ' + " ".join(sys.argv[1:]) + ' & PAUSE & EXIT')