import sys
import module002a,os
if len(sys.argv) == 1:
	data = [r"c:\Program Files\CD Art Display\CAD.exe"]
	module002a.main(data)
else:
	import win32gui, win32con
	hdls = []
	def enums(hwnd, lParam):
		if win32gui.GetWindowText(hwnd) == "CD Art Display":
			hdls.append(hwnd)
	win32gui.EnumWindows(enums, None)
	#print("hdls =", hdls)
	rect = win32gui.GetWindowRect(hdls[0])
		
	if sys.argv[1] == 'top' or sys.argv[1] == 't':
		print("TOP")
		win32gui.SetWindowPos(hdls[0], win32con.HWND_TOPMOST, rect[0], rect[1], rect[2], rect[3], 0)
	elif sys.argv[1] == 'notop' or sys.argv[1] == 'nt':
		print("NORMAL")
		win32gui.SetWindowPos(hdls[0], win32con.HWND_NOTOPMOST, rect[0], rect[1], rect[2], rect[3], 0)
		
