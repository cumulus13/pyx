# based on http://dzone.com/snippets/set-windows-desktop-wallpaper
import win32api
import win32con
import win32gui
import ctypes
import sys
#----------------------------------------------------------------------


def setWallpaper(path):
    key = win32api.RegOpenKeyEx(
        win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(key, "WallpaperStyle", 1, win32con.REG_SZ, "0")
    win32api.RegSetValueEx(key, "FillWallpaper", 1, win32con.REG_SZ, "0")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, path, 1 + 2)

# if __name__ == "__main__":
#     path = r'C:\Users\Public\Pictures\Sample Pictures\Jellyfish.jpg'
#     setWallpaper(path)


def setWallpaperWithCtypes(path):
    # This code is based on the following two links
    # http://mail.python.org/pipermail/python-win32/2005-January/002893.html
    # http://code.activestate.com/recipes/435877-change-the-wallpaper-under-windows/
    cs = ctypes.c_buffer(path)
    ok = ctypes.windll.user32.SystemParametersInfoA(
        win32con.SPI_SETDESKWALLPAPER, 0, cs, 0)


def usage():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'PATH', help='Path file of image wallpaper', action='store')
    if len(sys.argv) == 1:
        parser.print_help()
    else:
        args = parser.parse_args()
        try:
            setWallpaper(args.PATH)
        except:
            setWallpaperWithCtypes(args.PATH)

if __name__ == "__main__":
    usage()
