import win32gui

def findme(hwnd, extra):
	a = win32gui.FindWindow('notepad2', extra)
	print "a =", a

def callback(hwnd, extra):
    rect = win32gui.GetWindowRect(hwnd)
    #rect1 = win32gui.GetClientRect(hwnd)
    #print "rect1 =", rect1
    x = rect[0]
    y = rect[1]
    w = rect[2] - x
    h = rect[3] - y
    #print "Window %s:" % win32gui.GetWindowText(hwnd)
    #print "\tLocation: (%d, %d)" % (x, y)
    #print "\t    Size: (%d, %d)" % (w, h)
    if 'scite' in str(win32gui.GetWindowText(hwnd)).lower():
		print "Window =", win32gui.GetWindowText(hwnd)
		win32gui.UpdateLayeredWindow(hwnd, None, (100, 100), None, None, None, 0, (0, 0,255,0), 0)

def main():
    win32gui.EnumWindows(callback, None)
    #win32gui.EnumWindows(findme, 'notepad2')

if __name__ == '__main__':
    main()