#coding: utf8

import win32gui
import sys
import os

# def RaiseWindowNamed(nameRe):
#     import win32gui
#     # start by getting a list of all the windows:
#     cb = lambda x,y: y.append(x)
#     wins = []
#     win32gui.EnumWindows(cb,wins)

#     # now check to see if any match our regexp:
#     tgtWin = -1
#     for win in wins:
#         txt = win32gui.GetWindowText(win)
#         if nameRe.match(txt):
#             tgtWin=win
#             break

#     if tgtWin>=0:
#         win32gui.SetForegroundWindow(tgtWin)


# def WinRaise(HWND):
# 	import win32gui
# 	import win32con
# 	win32gui.ShowWindow(HWND, win32con.SW_RESTORE)
# 	win32gui.SetWindowPos(HWND,win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)  
# 	win32gui.SetWindowPos(HWND,win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)  
# 	win32gui.SetWindowPos(HWND,win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_SHOWWINDOW + win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)

# def AutoWinRaise(title_name):
#     # print "title_name =", title_name
#     # print "type(title_name) =", type(title_name)
#     from pywinauto.findwindows    import find_window
#     from pywinauto.win32functions import SetForegroundWindow
#     SetForegroundWindow(find_window(title=title_name))

# def list_windows(query=None):

#     import ctypes
    
#     EnumWindows = ctypes.windll.user32.EnumWindows
#     EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
#     GetWindowText = ctypes.windll.user32.GetWindowTextW
#     GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
#     IsWindowVisible = ctypes.windll.user32.IsWindowVisible
    
#     titles = []
#     def foreach_window(hwnd, lParam):
#         if IsWindowVisible(hwnd):
#             length = GetWindowTextLength(hwnd)
#             buff = ctypes.create_unicode_buffer(length + 1)
#             GetWindowText(hwnd, buff, length + 1)
#             titles.append(buff.value)
#         return True
#     EnumWindows(EnumWindowsProc(foreach_window), 0)
#     b = []
#     a=1
#     for i in titles:
#     	if i == '':
#     		pass
#     	else:
#     		if query != None and str(query).lower() in str(i).encode('utf-8').lower() and os.path.basename(__file__).lower() not in str(i).encode('utf-8').lower():
#     			print str(a).encode('utf-8') + ".", str(i).encode('utf-8')
#     			b.append(str(i).encode('utf-8'))
#     			a +=1
#     		else:
#     			if query == None:
#     				print str(a).encode('utf-8') + ".", str(i).encode('utf-8')
#     				a +=1
#     return b

def window_enum_handler(hwnd, resultList):
    if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) != '':
        resultList.append((hwnd, win32gui.GetWindowText(hwnd)))

def get_app_list(handles=[]):
    mlst=[]
    win32gui.EnumWindows(window_enum_handler, handles)
    for handle in handles:
        mlst.append(handle)
    return mlst

def Raise(HWND):
	return win32gui.SetForegroundWindow(int(HWND))

def usage():
	appwindows = get_app_list()
	if len(sys.argv) == 1:
		print "Usage:", os.path.basename(__file__), "windows_title_name [-l]\n"
		print "       -l, --list   List Active Windows"
	else:
		ver = False
		b = []
		a=1
		if "-l" in sys.argv[1:]:
			for i in appwindows:
				print str(a) + ".", str(i[1]).decode('iso-8859-1').encode('utf-8')
				a +=1
			print "0 = all"
			q = raw_input('Select Number: ')
			if str(q).isdigit():
				if q == '0':
					for e in appwindows:
						Raise(e[0])
					sys.exit(0)
				else:
					if int(q) < len(appwindows) + 1:
						Raise(appwindows[int(q)-1][0])
						sys.exit(0)
			else:
				sys.exit(0)

		else:
			for i in appwindows:
				if i == '':
					pass
				else:
					if sys.argv[1] in str(i[1]).decode('iso-8859-1').encode('utf-8').lower():
						# if sys.argv[0] not in str(i[1]).decode('iso-8859-1').encode('utf-8').lower():
						b.append(i)
		b = b[1:]
		# print "b =", b
		# print "len(b) =", len(b)
		if len(b) > 1: 
			b = b[1:]
			n = 1
			for c in b:
				print str(n) + ".", str(c[1]).decode('iso-8859-1').encode('utf-8').lower() 
				n += 1
			# print "len(sys.argv[1:] =", len(sys.argv[1:])
			if len(sys.argv[1:]) > 1 and str(sys.argv[2]).isdigit():
				q = sys.argv[2]
			else:
				print "0 = all"
				q = raw_input('Select Number: ')
			# print "len(b) =", len(b)
			while str(q).isdigit():
				if q == '0':
					for d in b:
						Raise(d[0])
					break
				else:
					if int(q) < len(b) + 1:
						Raise(b[int(q)- 1][0])
						break
					else:
						print "0 = all"
						q = raw_input('Select Number: ')
						# print "sys.argv[1:]      =", sys.argv[1:]
						# print "len(sys.argv[1:]) =", len(sys.argv[1:])
						# if len(sys.argv[1:]) > 1:
						# 	# if "-l" in sys.argv[1:]:
						# 	# 	sys.argv.remove('-l')
						# 	for a in sys.argv:
						# 		if a in appwindows:
						# 			ver = True
						# 	if ver:
						# 		print "BBBB"
						# # if query != None:
						# # 	# print "ZZZZ"
						# # 	if str(query).lower() in str(i[1]).decode('iso-8859-1').encode('utf-8').lower():
						# # 		# print "AAAA"
						# # 		# if os.path.basename(__file__).lower() not in str(i[1]).decode('iso-8859-1').encode('utf-8').lower():
						# # 		print "BBBB"
						# 			# print str(a) + ".", str(i[1]).decode('iso-8859-1').encode('utf-8')
						# 			# b.append(str(i))
						# 			# a +=1
						# else:
						# 	print "XXXX"
						# 	print str(a) + ".", str(i[1]).decode('iso-8859-1').encode('utf-8')
						# 	a +=1

			# print "b =", b
		else:
			# print "b =", b[0][0]
			Raise(int(b[0][0]))


def test(query):
	AutoWinRaise(query)
			
if __name__ == '__main__':
    usage()