
import time
import ctypes
import ctypes.wintypes
import sys

SEE_MASK_NOCLOSEPROCESS = 0x00000040
SEE_MASK_INVOKEIDLIST = 0x0000000C

class SHELLEXECUTEINFO(ctypes.Structure):
    _fields_ = (
        ("cbSize",ctypes.wintypes.DWORD),
        ("fMask",ctypes.c_ulong),
        ("hwnd",ctypes.wintypes.HANDLE),
        ("lpVerb",ctypes.c_char_p),
        ("lpFile",ctypes.c_char_p),
        ("lpParameters",ctypes.c_char_p),
        ("lpDirectory",ctypes.c_char_p),
        ("nShow",ctypes.c_int),
        ("hInstApp",ctypes.wintypes.HINSTANCE),
        ("lpIDList",ctypes.c_void_p),
        ("lpClass",ctypes.c_char_p),
        ("hKeyClass",ctypes.wintypes.HKEY),
        ("dwHotKey",ctypes.wintypes.DWORD),
        ("hIconOrMonitor",ctypes.wintypes.HANDLE),
        ("hProcess",ctypes.wintypes.HANDLE),
    )

ShellExecuteEx = ctypes.windll.shell32.ShellExecuteEx
ShellExecuteEx.restype = ctypes.wintypes.BOOL

sei = SHELLEXECUTEINFO()
sei.cbSize = ctypes.sizeof(sei)
sei.fMask = SEE_MASK_NOCLOSEPROCESS | SEE_MASK_INVOKEIDLIST
sei.lpVerb = bytes("Properties".encode('utf-8'))
sei.lpFile = bytes(sys.argv[1].encode('utf-8'))
sei.nShow = 1
if __name__ == '__main__':
    if len(sys.argv) == 2:
        sleeper = 5
    elif len(sys.argv) > 2:
        sleeper = int(sys.argv[2])
        m = ShellExecuteEx(ctypes.byref(sei))
        #print("m =",sei.hwnd.__bool__)
        #print("dir(m) =", dir(sei.hwnd.__bool__))
        time.sleep(sleeper)
        #print("m =",sei.hwnd.__bool__)