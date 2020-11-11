import os
import sys
from make_colors import make_colors

path = os.getcwd()
if len(sys.argv) == 2:
	path = sys.argv[1]
scanned = os.listdir(path)
for i in scanned:
	if os.path.isdir(os.path.join(path, i, 'trailers')):
		if os.path.isfile(os.path.join(path, i, 'trailers', 'trailer.mp4')):
			print(make_colors(os.path.abspath(i), 'lightcyan') + " " + make_colors("[TRAILED]", 'lightred', 'lightwhite'))
		else:
			scanned_1 = os.listdir(os.path.join(path, i, 'trailers'))
			if len(scanned_1) > 0:
				if os.path.splitext(scanned_1[0])[1].lower() == ".mp4":
					print(make_colors(os.path.abspath(i), 'lightgreen') + " " + make_colors("[TRAILED With Other Files]", 'lightwhite', 'blue'))
				else:
					for i in scanned_1:
						print(make_colors(i, 'black', 'lightyellow'))
			else:
				print(make_colors(os.path.abspath(i), 'lightblue') + " " + make_colors("[DIR ONLY]", 'lightwhite', 'lightred'))
	else:
		print(make_colors(os.path.abspath(i), 'lightwhite'))
