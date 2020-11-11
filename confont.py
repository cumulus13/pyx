import ctypes

LF_FACESIZE = 32
STD_OUTPUT_HANDLE = -11

class COORD(ctypes.Structure):
    _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

class CONSOLE_FONT_INFOEX(ctypes.Structure):
    _fields_ = [("cbSize", ctypes.c_ulong),
             ("nFont", ctypes.c_ulong),
             ("dwFontSize", COORD),
             ("FontFamily", ctypes.c_uint),
             ("FontWeight", ctypes.c_uint),
             ("FaceName", ctypes.c_wchar * LF_FACESIZE)]

def main(size=12, font_type=None):
	font = CONSOLE_FONT_INFOEX()
	font.cbSize = ctypes.sizeof(CONSOLE_FONT_INFOEX)
	font.nFont = 12
	font.dwFontSize.X = 11
	font.dwFontSize.Y = int(size)
	font.FontFamily = 54
	font.FontWeight = 400
	if font_type:
		font.FaceName = font_type
	else:
		font.FaceName = "Lucida Console"

	handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
	ctypes.windll.kernel32.SetCurrentConsoleFontEx(
	handle, ctypes.c_long(False), ctypes.pointer(font))

if __name__ == '__main__':
	import sys
	if len(sys.argv) == 2:
		main(sys.argv[1])
	elif len(sys.argv) == 3:
		main(sys.argv[1], sys.argv[2])