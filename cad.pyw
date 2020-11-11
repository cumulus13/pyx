#!c:\SDK\Anaconda2\pythonw.exe
import sys
import module002a,os
import argparse
import win32gui, win32con
from make_colors import make_colors
import msvcrt

def usage(data = [r"c:\Program Files\CD Art Display\CAD.exe"], title="CD Art Display"):
	parser = argparse.ArgumentParser(formatter_class = argparse.RawTextHelpFormatter)
	parser.add_argument('-t', '--top', help='Show as always on top', action='store_true')
	parser.add_argument('-nt', '--notop', help='Show normal from always on top', action='store_true')
	parser.add_argument('-s', '--show', help='Show from minimize', action='store_true')
	parser.add_argument('--usage', help='Show Help', action='store_true')
	if len(sys.argv) == 1:
		#print_usage(parser)
		module002a.main(data)
		process = 'start cmd /c "c:\SDK\Anaconda2\python.exe {0} --usage"'.format(__file__)
		os.system(process)
	else:
		args = parser.parse_args()
		hdls = []
		def enums(hwnd, lParam):
			if win32gui.GetWindowText(hwnd) == title:
				hdls.append(hwnd)
		win32gui.EnumWindows(enums, None)
		#print("hdls =", hdls)
		rect = win32gui.GetWindowRect(hdls[0])
		
		if args.top:
			print("TOP")
			win32gui.SetWindowPos(hdls[0], win32con.HWND_TOPMOST, rect[0], rect[1], rect[2], rect[3], 0)
		elif args.notop:
			print("NORMAL")
			win32gui.SetWindowPos(hdls[0], win32con.HWND_NOTOPMOST, rect[0], rect[1], rect[2], rect[3], 0)
		elif args.show:
			pass
		elif args.usage:
			print_usage(parser)
		#else:
		#	print_usage()
		

def print_usage(parser, width=400, height=200, center=True, x=0, y=0,buffer_column = 1, buffer_row = 1,):
	HANDLE = win32gui.GetForegroundWindow()
	from dcmd import dcmd
	setting = dcmd.dcmd()
	setting.setBuffer(buffer_row, buffer_column)
	screensize = setting.getScreenSize()
	setting.setSize(width, height, x, y, center)
	#def changeFont(self, nfont=12, xfont=11, yfont=18, ffont=54, wfont=400, name="Lucida Console")
	setting.changeFont(yfont=13, name = "Consolas")
	setting.setAlwaysOnTop(width, height, x, y, center, handle = HANDLE)	
	
	parser.print_help()
	#print(make_colors("q|esc|x = quit|exit" , 'lw', 'lr', ['blink']))
	msvcrt.getch()
	
	
if __name__ == '__main__':
	usage()