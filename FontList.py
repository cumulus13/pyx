import win32gui
import ctypes
from ctypes import wintypes

class LOGFONT(ctypes.Structure): _fields_ = [
    ('lfHeight', wintypes.LONG),
    ('lfWidth', wintypes.LONG),
    ('lfEscapement', wintypes.LONG),
    ('lfOrientation', wintypes.LONG),
    ('lfWeight', wintypes.LONG),
    ('lfItalic', wintypes.BYTE),
    ('lfUnderline', wintypes.BYTE),
    ('lfStrikeOut', wintypes.BYTE),
    ('lfCharSet', wintypes.BYTE),
    ('lfOutPrecision', wintypes.BYTE),
    ('lfClipPrecision', wintypes.BYTE),
    ('lfQuality', wintypes.BYTE),
    ('lfPitchAndFamily', wintypes.BYTE),
    ('lfFaceName', ctypes.c_wchar*32)]

#we are not interested in NEWTEXTMETRIC parameter in FONTENUMPROC, use LPVOID instead
FONTENUMPROC = ctypes.WINFUNCTYPE(ctypes.c_int, 
    ctypes.POINTER(LOGFONT), wintypes.LPVOID, wintypes.DWORD, wintypes.LPARAM)

fontlist = []

def font_enum(logfont, textmetricex, fonttype, param):
    str = logfont.contents.lfFaceName;
    if (any(str in s for s in fontlist) == False):
        fontlist.append(str)
    return True

def callback(font, tm, fonttype, names):
    names.append(font.lfFaceName)
    return True

def get_list1():
	fontnames = []
	hdc = win32gui.GetDC(None)
	win32gui.EnumFontFamilies(hdc, None, callback, fontnames)
	print("\n".join(fontnames))
	win32gui.ReleaseDC(hdc, None)
	
def get_list2():
	hdc = ctypes.windll.user32.GetDC(None)
	ctypes.windll.gdi32.EnumFontFamiliesExW(hdc, None, FONTENUMPROC(font_enum), 0, 0)  
	ctypes.windll.user32.ReleaseDC(None, hdc)
	print("\n".join(fontlist))

get_list2()