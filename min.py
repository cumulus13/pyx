import win32gui
import win32con
from make_colors import make_colors
import sys
if sys.version_info.major == 3:
	raw_input = input
	
TITLE = ''
ALL = []
HANDLE = win32gui.GetForegroundWindow()
def enumHandler(hwnd, lParam):
	if win32gui.IsWindowVisible(hwnd):
		if TITLE.lower() in win32gui.GetWindowText(hwnd).lower():
			title = win32gui.GetWindowText(hwnd)
			ALL.append([hwnd, title.lower()])
			
def show(title):
	global TITLE
	global ALL
	global HANDLE
	name = None
	TITLE = title
	handle = None
	win32gui.EnumWindows(enumHandler, None)
	this_title = win32gui.GetWindowText(HANDLE).lower()
	#print("this_title =", this_title)
	#print("ALL =", ALL)
	for i in ALL:
		if this_title in i[1]:
			ALL.remove(i)
	#print("ALL =", ALL)
	if len(ALL) > 1:
		n = 1
		for i in ALL:
			print(make_colors(str(n), 'lc') + ". " + make_colors(i[1], 'lw', 'bl'))
			n += 1
		q = raw_input(make_colors("Select number to show: ", 'lw', 'lr'))
		if q and int(q) <= len(ALL):
			handle = ALL[int(q) - 1][0]
			name = ALL[int(q) - 1][1]
	else:
		if len(ALL) == 1:
			handle = ALL[0][0]
			name = ALL[0][1]
		else:
			print(make_colors("Not Found !", 'lw', 'lr', ['blink']))
	if handle:
		#print("handle =", handle)
		print(make_colors("Minimize ", 'lw', 'bl') + make_colors(name, 'lw', 'lr') + " ....")
		win32gui.ShowWindow(handle, win32con.SW_MINIMIZE)
	
if len(sys.argv) > 1:
	show(sys.argv[1])