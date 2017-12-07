import win32gui
import win32api
import sys
import argparse

__version__ = "1.0"
__test__ = "0.1"
__sdk__ = "2.7"
__platform__ = "nt"
__url__ = "licface@yahoo.com"
__description__ = "Move this or other windows to Point X/Y and Size Specificed"
__email__ = "licface@yahoo.com"
__testsdk__ = "windows"

class moving:
	def __init__(self, parent=None):
		self.width = None
		self.height = None
		self.x = None
		self.y = None
		self.title = None
		self.size = []
		self.datatitle = []
		#mytitle = win32api.GetConsoleTitle()

	def listTitle(self, hwnd, LParam):
		if win32gui.IsWindowVisible(hwnd):
			title = win32gui.GetWindowText(hwnd)
			if len(str(title).strip()) == 0 or title == '' or title == ' ':
				pass
			else:
				self.datatitle.append(title)

	def convert_listTitle(self):
		win32gui.EnumWindows(self.listTitle, None)
		return self.datatitle

	def listWindow(self):
		"""
		if win32gui.IsWindowVisible(hwnd):
			title = win32gui.GetWindowText(hwnd)
			if len(str(title).strip()) == 0 or title == '' or title == ' ':
				pass
			else:
				print "-", title
		"""

		self.convert_listTitle()
		for i in range(0, len(self.datatitle)):
			print str(i + 1) + ". " + self.datatitle[i]

	def getsize(self, hwnd, LParam):
		rect = win32gui.GetWindowRect(hwnd)
		x = rect[0]
		y = rect[1]
		w = rect[2] - x 
		h = rect[3] - y
		if win32gui.IsWindowVisible(hwnd):
			if self.title == None:
				mytitle = win32api.GetConsoleTitle()
				if mytitle in win32gui.GetWindowText(hwnd):
					self.size = [x, y, w, h]
			else:
				if self.title in win32gui.GetWindowText(hwnd):
					self.size = [x, y, w, h]

	def fixsize(self):
		win32gui.EnumWindows(self.getsize, None)

	def moveme(self, hwnd, LParam):
		if win32gui.IsWindowVisible(hwnd):
			if self.title == None:
				mytitle = win32api.GetConsoleTitle()
				if mytitle in win32gui.GetWindowText(hwnd):
					rect = win32gui.GetWindowRect(hwnd)
					self.rect = rect
					if self.x == None:
						self.x = rect[0]
					if self.y == None:
						self.y = rect[1]
					if self.width == None:
						self.width = rect[2] - rect[0]
					if self.height == None:
						self.height = rect[3] - rect[1]
					win32gui.MoveWindow(hwnd, self.x, self.y, self.width, self.height, True)
			else:
				if self.title in win32gui.GetWindowText(hwnd):
					rect = win32gui.GetWindowRect(hwnd)
					self.rect = rect
					if self.x == None:
						self.x = rect[0]
					if self.y == None:
						self.y = rect[1]
					if self.width == None:
						self.width = rect[2] - rect[0]
					if self.height == None:
						self.height = rect[3] - rect[1]
					win32gui.MoveWindow(hwnd, self.x, self.y, self.width, self.height, True)

	def usage(self):
		parser = argparse.ArgumentParser(prog="pymove")
		parser.add_argument('X', help="Position X", action="store", type=int)
		parser.add_argument('Y', help="Position Y", action="store", type=int)
		parser.add_argument('-w', '--width', help="Width Window Set", type=int, action="store")
		parser.add_argument('-t', '--height', help="Height Window Set", type=int, action="store")
		parser.add_argument('-l', '--list', help="List Visible Window Name/Title", action="store_true")
		parser.add_argument('-n', '--name', help="Name/Title of Window to move", action="store", type=str)
		parser.add_argument('-z', '--getsize', help="Get Size Of Window", action="store_true")

		parser2 = argparse.ArgumentParser(prog="pymove")
		parser2.add_argument('-w', '--width', help="Width Window Set", type=int, action="store")
		parser2.add_argument('-t', '--height', help="Height Window Set", type=int, action="store")
		parser2.add_argument('-l', '--list', help="List Visible Window Name/Title", action="store_true")
		parser2.add_argument('-n', '--name', help="Number/Name/Title of Window to move", action="store", type=str)
		parser2.add_argument('-z', '--getsize', help="Get Size Of Window", action="store_true")

		if len(sys.argv) > 1:
			if sys.argv[1] == '-l' or sys.argv[1] == '-w' or sys.argv[1] == '-t' or sys.argv[1] == '--list' or sys.argv[1] == '--width' or sys.argv[1] == '--height' or sys.argv[1] == '-z' or sys.argv[1] == '--getsize':
				args2 = parser2.parse_args()
				try:
					int(args2.name)
					self.convert_listTitle()
					self.title = self.datatitle[int(args2.name) - 1]
				except:
					self.title = args2.name
				if args2.list:
					#win32gui.EnumWindows(self.listWindow, None)			
					self.listWindow()
				if args2.getsize:
					#if args2.name:
					self.fixsize()
					if self.title == None:
						self.title = win32api.GetConsoleTitle()
					print "Window Name:", self.title
					print "Width      :", (self.size[2] / 10) + 55
					print "Height     :", (self.size[3] / 10) - 14
					print "X          :", self.size[0]
					print "Y          :", self.size[1]

				if args2.width:
					if args2.height:
						self.width = (args2.width * 10) - 55
						self.height = (args2.height * 10) + 155
						self.x = None
						self.y = None
						win32gui.EnumWindows(self.moveme, None)
					else:
						print "\n"
						parser.print_help()
				if args2.height:
					if args2.width:
						self.width = (args2.width * 10) - 55
						self.height = (args2.height * 10) + 155
						self.x = None
						self.y = None
						win32gui.EnumWindows(self.moveme, None)
					else:
						print "\n"
						parser.print_help()
			else:
				args = parser.parse_args()
				self.convert_listTitle()
				if args.name:
					try:
						int(args.name)
						self.convert_listTitle()
						self.title = self.datatitle[int(args.name) - 1]
					except:
						self.title = args.name
				if args.getsize:
					#if args.name:
					self.fixsize()
					if self.title == None:
						self.title = win32api.GetConsoleTitle()
					print "Window Name:", self.title
					print "Width      :", (self.size[2] / 10) + 55
					print "Height     :", (self.size[3] / 10) - 14
					print "X          :", self.size[0]
					print "Y          :", self.size[1]
				if isinstance(int(args.X), int):
					if isinstance(int(args.Y), int):
						self.fixsize()
						self.x = args.X
						self.y = args.Y
						if not self.width == None:	
							self.width = (args.width * 10) - 55
						else:
							self.width = self.size[2]
						if not self.height == None:
							self.height = (args.height * 10) + 24
						else:
							self.hight = self.size[3]
						self.title = args.name
						win32gui.EnumWindows(self.moveme, None)
					else:
						print "\n"
						parser.print_help()
				else:
					print "\n"
					parser.print_help()
		else:
			print "\n"
			parser.print_help()

		
if __name__ == "__main__":
	c = moving()
	c.usage()