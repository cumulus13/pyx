
from __future__ import print_function
"""
#linux only
import os

def get_mount_point(pathname):
    "Get the mount point of the filesystem containing pathname"
    pathname= os.path.normcase(os.path.realpath(pathname))
    parent_device= path_device= os.stat(pathname).st_dev
    while parent_device == path_device:
        mount_point= pathname
        pathname= os.path.dirname(pathname)
        if pathname == mount_point: break
        parent_device= os.stat(pathname).st_dev
    return mount_point

def get_mounted_device(pathname):
    "Get the device mounted at pathname"
    # uses "/proc/mounts"
    pathname= os.path.normcase(pathname) # might be unnecessary here
    try:
        with open("/proc/mounts", "r") as ifp:
            for line in ifp:
                fields= line.rstrip('\n').split()
                # note that line above assumes that
                # no mount points contain whitespace
                if fields[1] == pathname:
                    return fields[0]
    except EnvironmentError:
        pass
    return None # explicit

def get_fs_freespace(pathname):
    "Get the free space of the filesystem containing pathname"
    stat= os.statvfs(pathname)
    # use f_bfree for superuser, or f_bavail if filesystem
    # has reserved space for superuser
    return stat.f_bfree*stat.f_bsize

#drive = r'\\servername\c$'
print get_mount_point("/data")
print get_mounted_device("/home")
print get_fs_freespace("/mnt/hdd1")

"""
try:
    import win32com.client as com
except:
    pass
import string
import traceback
import sys
import os
import win32file
import pywintypes
import argparse
PYTHON_VER = sys.version_info.major

def TotalSize(drive, show_in_bites=None, verbose=None):
    """ Return the TotalSize of a shared drive [GB]"""
    try:
        fso = com.Dispatch("Scripting.FileSystemObject")
        drv = fso.GetDrive(drive)
        if show_in_bites == None:
            return drv.TotalSize
        else:
            return drv.TotalSize / 2**30

    except:
        if verbose == None:
            return 0
        else:
            print ("Error: ", traceback.format_exc())


def FreeSpace(drive, show_in_bites=None, verbose=None):
    """ Return the FreeSape of a shared drive [GB]"""
    try:
        fso = com.Dispatch("Scripting.FileSystemObject")
        drv = fso.GetDrive(drive)
        if show_in_bites == None:
            return drv.FreeSpace
        else:
            return drv.FreeSpace / 2**30
    except:
        if verbose == None:
            return 0
        else:
            print ("Error: ", traceback.format_exc())


def sizeof_fmt(num):
    for x in [' bytes', ' KB', ' MB', ' GB', ' TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def sizeof_fmt2(num):
    """
        for actual with minus size
    """
    for x in [' bytes', ' KB', ' MB', ' GB']:
        if num < 1024.0 and num > -1024.0:
            return "%3.1f%s" % (num, x)
        num /= 1024.0
    return "%3.1f%s" % (num, ' TB')


def sizeof_fmt3(num):
    from math import log
    unit_list = zip(['bytes', 'kB', 'MB', 'GB', 'TB', 'PB'],
                    [0, 0, 1, 2, 2, 2])

    """Human friendly file size"""
    if num > 1:
        exponent = min(int(log(num, 1024)), len(unit_list) - 1)
        quotient = float(num) / 1024**exponent
        unit, num_decimals = unit_list[exponent]
        format_string = '{:.%sf} {}' % (num_decimals)
        return format_string.format(quotient, unit)
    if num == 0:
        return '0 bytes'
    if num == 1:
        return '1 byte'


# def sizeof_fmt3A(num):
#     from math import log
#     unit_list = zip(['bytes', 'kB', 'MB', 'GB', 'TB', 'PB'],
#                     [0, 0, 1, 2, 2, 2])

#     """Human friendly file size"""
#     if num > 1:
#         exponent = min(int(log(num, 1024)), len(unit_list) - 1)
#         quotient = float(num) / 1024**exponent
#         # unit, num_decimals = unit_list[exponent]
#         # format_string = '{:.%sf} {}' % (num_decimals)
#         # return format_string.format(quotient, unit)
#         return float(num)
#     if num == 0:
#         return '0 bytes'
#     if num == 1:
#         return '1 byte'


def sizeof_fmt4(num):
    """Human friendly file size"""
    from math import log
    if num > 1:
        exponent = int(log(num, 1024))
        quotient = num / 1024**exponent
        unit, num_decimals = unit_list[exponent]
        format_string = '{:.%sf} {}' % (num_decimals)
        return format_string.format(quotient, unit)
    if num == 0:
        return '0 bytes'
    if num == 1:
        return '1 byte'

#drive = r'D:'
# print 'TotalSize of %s = %d GB' % (drive, TotalSize(drive))
# print 'FreeSpace on %s = %d GB' % (drive, FreeSpace(drive))


def human_size(size_bytes):
    """
    format a size in bytes into a 'human' file size, e.g. bytes, KB, MB, GB, TB, PB
    Note that bytes/KB will be reported in whole numbers but MB and above will have greater precision
    e.g. 1 byte, 43 bytes, 443 KB, 4.3 MB, 4.43 GB, etc
    """
    if size_bytes == 1:
        # because I really hate unnecessary plurals
        return "1 byte"

    suffixes_table = [('bytes', 0), ('KB', 0), ('MB', 1),
                      ('GB', 2), ('TB', 2), ('PB', 2)]

    num = float(size_bytes)
    for suffix, precision in suffixes_table:
        if num < 1024.0:
            break
        num /= 1024.0
        if precision == 0:
            formatted_size = "%d" % num
        else:
            formatted_size = str(round(num, ndigits=precision))

        return "%s %s" % (formatted_size, suffix)


def human_readable_data_quantity(quantity, multiple=1024):
    if quantity == 0:
        quantity = +0
    SUFFIXES = ["B"] + [i + {1000: "B", 1024: "iB"}[multiple]
                        for i in "KMGTPEZY"]
    for suffix in SUFFIXES:
        if quantity < multiple or suffix == SUFFIXES[-1]:
            if suffix == SUFFIXES[0]:
                return "%d%s" % (quantity, suffix)
            else:
                return "%.1f%s" % (quantity, suffix)
        else:
            quantity /= multiple


def human_readable_bytes(x):
    # hybrid of http://stackoverflow.com/a/10171475/2595465
    #      with http://stackoverflow.com/a/5414105/2595465
    from math import log
    if x == 0:
        return '0'
    magnitude = int(log(abs(x), 10.24))
    if magnitude > 16:
        format_str = '%iP'
        denominator_mag = 15
    else:
        float_fmt = '%2.1f' if magnitude % 3 == 1 else '%1.2f'
        illion = (magnitude + 1) // 3
        format_str = float_fmt + ['', ' Kb',
                                  ' Mb', ' Gb', ' Tb', ' Pb'][illion]
    # return (format_str % (x * 1.0 / (1024 ** illion))).lstrip('0')
    return (format_str % (x * 1.0 / (1024 ** illion)))


def get_human_readable_size(num):
    exp_str = [(0, 'B'), (10, 'KB'), (20, 'MB'),
               (30, 'GB'), (40, 'TB'), (50, 'PB'), ]
    i = 0
    while i + 1 < len(exp_str) and num >= (2 ** exp_str[i + 1][0]):
        i += 1
        rounded_val = round(float(num) / 2 ** exp_str[i][0], 2)
    return '%s %s' % (int(rounded_val), exp_str[i][1])


class Filesize(object):
    """
        this inly for float data import/in 
        example 72.56, for totalspace or freespace
    """
    chunk = 1024
    units = ['bytes', 'KB', 'MB', 'GB', 'TB', 'PB']
    precisions = [0, 0, 1, 2, 2, 2]

    def __init__(self, size):
        self.size = size

    def __int__(self):
        return self.size

    def __str__(self):
        if self.size == 0:
            return '0 bytes'
        from math import log
        unit = self.units[
            min(int(log(self.size, self.chunk)), len(self.units) - 1)]
        return self.format(unit)

    def format(self, unit):
        if unit not in self.units:
            raise Exception("Not a valid file size unit: %s" % unit)
        if self.size == 1 and unit == 'bytes':
            return '1 byte'
        exponent = self.units.index(unit)
        quotient = float(self.size) / self.chunk**exponent
        precision = self.precisions[exponent]
        format_string = '{:.%sf} {}' % (precision)
        return format_string.format(quotient, unit)


def getMaxLengthPath(listdata):
    a = []
    for i in listdata:
        b = os.path.basename(i)
        a.append(b)

    return len(map(max, [a])[0]), a


def get_folder_size(folderPath, exc=None, show_in_bites=None, detail=None):
    import win32com.client as com
    fd1= ''
    fd0 = ''
    fd = ''
    fso = com.Dispatch("Scripting.FileSystemObject")
    MB = 1024 * 1024.0
    GB = 1024 * 1024.0 * 1024.0
    if not exc == None:
        # print "type(exc) =", type(exc)
        if isinstance(exc, list):
            # print "AAA"
            folder_exc = 0
            for i in exc:
                # print "I               =", i
                # print "check i is file =", os.path.isfile(i)
                # print "-"*158
                if os.path.isfile(i):
                    f_sep_exc = fso.GetFile(i)
                elif os.path.isdir(i):
                    f_sep_exc = fso.GetFolder(i)
                else:
                    print ("NOT DIR OR FILE !")
                    return None
                folder_exc = folder_exc + f_sep_exc.Size
                # print "folder_exc 1 =", folder_exc
                # print "folder_exc 2 =", sizeof_fmt3(folder_exc)
        else:
            # print "BBB"
            # fso = com.Dispatch("Scripting.FileSystemObject")
            folder_exc = fso.GetFolder(folderPath).Size

    if isinstance(folderPath, list):
        folder = 0
        for i in folderPath:
            if os.path.isfile(i):
                #print "IS FILE:", i
                folder_sep = fso.GetFile(i)
            else:
                try:
                    folder_sep = fso.GetFolder(i)
                except:
                    pass
            if detail:
                n, listbasepath = getMaxLengthPath(folderPath)
                max_sep_length = n
                fd = "%.2f MB" % (folder_sep.size / MB)
                # print "n                                      =", n
                # print "type(n)                                =", type(n)
                # print "listbasepath                           =", listbasepath
                # print "folderPath.index(i)                    =", folderPath.index(i)
                # print "len(listbasepath[folderPath.index(i)]) =", len(listbasepath[folderPath.index(i)])
                # print "listbasepath[folderPath.index(i)]      =",
                # listbasepath[folderPath.index(i)]
                print ("Size Of Folder:", str(listbasepath[folderPath.index(i)]) + ((n - len(listbasepath[folderPath.index(i)])) + 2) * " " + " = ", fd)
                # print "-"*220
            try:
                folder += folder_sep.Size
            except:
                folder = 0

        if not exc == None:
            folder - folder_exc
        if not detail:
            fd = "%.2f MB" % (folder / MB)
            folder_str = " + ".join(folderPath)
            #print "TOTAL         : \"%s\" = " % (folder_str), fd
            print ("TOTAL         :", fd)
            return fd
        else:
            n, listbasepath = getMaxLengthPath(folderPath)
            fd = "%.2f MB" % (folder / MB)
            fd1 = "%.2f GB" % (folder / GB)
            print ("-" * (n + 35) + " + ")
            print (" " * (n + 18) + " = " + fd + " / " + fd1)
            return fd
    else:
        #print("folderPath =", folderPath)
        # fso = com.Dispatch("Scripting.FileSystemObject")
        if detail:
            pass
        if not exc == None:
            if isinstance(exc, list):
                folder_exc = 0
                for i in exc:
                    if os.path.isfile(i):
                        folder_sep_exc = fso.GetFile(i)
                    else:
                        folder_sep_exc = fso.GetFolder(i)
                    folder_exc += folder_sep_exc.Size
            else:
                # fso = com.Dispatch("Scripting.FileSystemObject")
                folder_exc = fso.GetFolder(folderPath).Size
            # print "FOLDER EXC SIZE                   =", folder_exc
            # print "FOLDER EXC SIZE 2                 =",
            # get_folder_size(folderPath)

        # print "FOLDER                            =", folderPath
        #print("folderPath =", folderPath)
        if ":" in str(folderPath[-1]) or "\\" in str(folderPath[-1]):
            # print "TotalSize(folderPath) 1           =", TotalSize(folderPath)
            # print "TotalSize(folderPath) 2           =", TotalSize(folderPath, True)
            # print "FreeSpace(folderPath)             =", FreeSpace(folderPath), "=", sizeof_fmt3(FreeSpace(folderPath))
            # print "sizeof_fmt3(FreeSpace(folderPath) =",
            # sizeof_fmt3(FreeSpace(str(folderPath)))
            folder = TotalSize(folderPath) - FreeSpace(folderPath)
            # print "FOLDER SPACE SIZE 1               =", folder
            # print "FOLDER SPACE SIZE 2               =", sizeof_fmt3(folder)
        else:
            #print "folderPath:", folderPath
            if os.path.isdir(folderPath):
                try:
                    folder = fso.GetFolder(folderPath).Size
                except:
                    folder = 'error'
                    #  print(folderPath + ":\    ERROR Get Info !")
            else:
                #folderPath = os.path.realpath(folderPath)
                #print("folderPath =", folderPath)
                #folder = fso.GetFile(folderPath).Size
                folder = get_folder_size2(str(folderPath))
            # print "FOLDER SIZE 1                     =", folder

        if not exc == None:
            fd = "%.2f MB" % ((folder - folder_exc) / MB)
            fd1 = "%.2f GB" % ((folder - folder_exc) / GB)
        else:
            if not folder == 'error':
                fd = "%.2f MB" % (folder / MB)
                fd1 = "%.2f GB" % (folder / GB)
        # print "type(fd1) =", type(fd1.split(" ")[0])
        # print "fd1       =", fd1.split(" ")[0]
        # print "fd1 >     =", float(fd1.split(" ")[0].strip()) > 1
        #folderPath = str(folderPath)
        if exc:
            if float(fd1.split(" ")[0].strip()) > 1:
                print ("Size Of Folder: \"%s\" - (%s) = " % (folderPath, str(" + ").join(exc)), fd, "/", fd1)
            else:
                print ("Size Of Folder: \"%s\" - (%s)path = " % (folderPath, str(" + ").join(exc)), fd)
        else:
            if fd1:
                if float(fd1.split(" ")[0].strip()) > 1:
                    print ("Size Of Folder: \"%s\" = " % (folderPath), fd, "/", fd1)
                else:
                    print ("Size Of Folder: \"%s\" = " % (folderPath), fd)
        return fd


def get_folder_size2(path):
    import win32con
    import win32file
    DIR_EXCLUDES = set(['.', '..'])
    MASK = win32con.FILE_ATTRIBUTE_DIRECTORY | win32con.FILE_ATTRIBUTE_SYSTEM
    REQUIRED = win32con.FILE_ATTRIBUTE_DIRECTORY
    FindFilesW = win32file.FindFilesW

    total_size = 0
    try:
        items = FindFilesW(path + r'\*')
    except pywintypes.error:
        return total_size

    for item in items:
        total_size += item[5]
        if (item[0] & MASK == REQUIRED):
            name = item[8]
            if name not in DIR_EXCLUDES:
                total_size += get_folder_size2(path + '\\' + name)
    # print "Size Of Folder: \"%s\" = %0.1f MB" % (path,total_size)
    return total_size


def get_folder_size3(root):
    size = 0
    for path, dirs, files in os.walk(root):
        for f in files:
            size += os.path.getsize(os.path.join(path, f))
    print ("Size Of Folder: \"%s\" = %0.1f MB" % (root, size))
    return size


def get_folder_size4(folder):
    folder_size = 0
    fd = ''
    for (path, dirs, files) in os.walk(folder):
        for file in files:
            filename = os.path.join(path, file)
            folder_size += os.path.getsize(filename)
            fd = folder_size / (1024 * 1024.0)
    print ("\n")
    print ("Size Of Folder: \"%s\" = %0.1f MB" % (folder, fd))
    return fd


def get_drive_type3(drive):
    DRIVE_TYPES = dict({0: 'Unknown',
                        1: 'Not Exist Directory',
                        2: ('Removable Disk').rjust(18),
                        3: 'Local Disk',
                        4: 'Network Drive',
                        5: 'CD/DVD Room Drive',
                        6: 'RAM Disk'})

    num_type = DRIVE_TYPES.keys()
    # print DRIVE_TYPES.get(1)
    type_drive = win32file.GetDriveType(drive)

    for i in num_type:
            # print i
        if i == type_drive:
            x = DRIVE_TYPES.get(int(i))
            return x
        else:
            pass

    return DRIVE_TYPES.get(0)


def main(skip_network_drive=True, exception=[], show_network_drive_only=False):
    try:
        import total_conf
        exception = total_conf.exception
    except:
        print ("ERROR: import module total_conf")
        print ("exc =", exception)
    drive_name = str(string.ascii_lowercase).upper()
    print ("\n")
    print ("-" * 52)
    print ("Drive |", "TotalUsed |", "FreeSpace | ", ("Type              | ").rjust(15))
    print ("-" * 52)
    for i in drive_name:
        if isinstance(exception, list) and str(i).lower() in exception:
            print ("I =", str(i))	
        else:
            if skip_network_drive:
                if get_drive_type3(str(i) + ":") == 'Network Drive':
                    pass
                else:
                    if TotalSize(str(i) + ":") != 0:
                        print ((i + ":\\").ljust(4), (sizeof_fmt2(TotalSize(str(i) + ":"))).rjust(12), (sizeof_fmt2(
                                                    FreeSpace(str(i) + ":"))).rjust(10), (get_drive_type3(str(i) + ":")).rjust(14))
                    elif get_drive_type3(str(i) + ":") == 'CD/DVD Room Drive':
                        print ((i + ":\\").ljust(4), (sizeof_fmt2(TotalSize(str(i) + ":"))).rjust(12), (sizeof_fmt2(
                                                    FreeSpace(str(i) + ":"))).rjust(10), (get_drive_type3(str(i) + ":")).rjust(21))
                    # else:
                    #     pass
            elif show_network_drive_only:
                if get_drive_type3(str(i) + ":") == 'Network Drive':
                    if TotalSize(str(i) + ":") != 0:
                        print ((i + ":\\").ljust(4), (sizeof_fmt2(TotalSize(str(i) + ":"))).rjust(12), (sizeof_fmt2(
                                                    FreeSpace(str(i) + ":"))).rjust(10), (get_drive_type3(str(i) + ":")).rjust(14))
            else:
                if TotalSize(str(i) + ":") != 0:
                    print ((i + ":\\").ljust(4), (sizeof_fmt2(TotalSize(str(i) + ":"))).rjust(12), (sizeof_fmt2(
                                            FreeSpace(str(i) + ":"))).rjust(10), (get_drive_type3(str(i) + ":")).rjust(14))
                elif get_drive_type3(str(i) + ":") == 'CD/DVD Room Drive':
                    print ((i + ":\\").ljust(4), (sizeof_fmt2(TotalSize(str(i) + ":"))).rjust(12), (sizeof_fmt2(
                                            FreeSpace(str(i) + ":"))).rjust(10), (get_drive_type3(str(i) + ":")).rjust(21))


def usage():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'PATH', help='Path Folders or Files calculation size to', nargs='*')
    parser.add_argument(
        '-e', '--excepts', help='Exception Folders or Files calculation size to', nargs='*')
    parser.add_argument(
        '-n', '--ndrive', help='Network Drive', action='store_false')
    parser.add_argument(
        '-N', '--ndrive-only', help='Show Network Drive Only', action='store_true')
    parser.add_argument(
        '-d', '--detail', help='List detail each of folder', action='store_true')
    parser.add_argument('-F', '--folder', help = 'Folder for Detail Only', action = 'store_true')
    if len(sys.argv) == 1:
        print ("Use: -h for help")
        main()
    else:
        if sys.argv[1] == '-n':
            main(False)
        if sys.argv[1] == '-N':
            main(False,show_network_drive_only=True)
        elif sys.argv[1] == '-e':
            if '-e' in sys.argv:
                index_e = sys.argv.index('-e')
                exception = sys.argv[index_e + 1:]
                print ("exception =", exception)
                if '-n' in sys.argv:
                    main(False, exception)
                else:
                    main(exception=exception)
        else:
            args = parser.parse_args()
            #print "args.PATH =", args.PATH
            if args.PATH == []:
                args.PATH = "."
            #print "args.PATH =", args.PATH
            if len(args.PATH) == 1:
                #get_folder_size(args.PATH[0], args.excepts)
            #else:
                #get_folder_size(args.PATH, args.excepts, detail=args.detail)
                if args.detail:
                    for i in args.PATH:
                        if args.folder:
                            listdir = os.listdir(i)
                            for a in listdir:
                                if os.path.isdir(a):
                                    try:
                                        get_folder_size(unicode(a).encode('utf-8'), args.excepts)
                                    except:
                                        print ("[ERROR] for FOLDER:", str(a))
                        else:
                            listdir = os.listdir(i)
                            for a in listdir:
                                try:
                                    if PYTHON_VER == 3:
                                        get_folder_size(a.encode('utf-8'), args.excepts)
                                    else:
                                        get_folder_size(unicode(a).encode('utf-8'), args.excepts)
                                except:
                                    print("ERROR =", traceback.format_exc() )
                                    if os.path.isfile(a):
                                        print ("[ERROR] for FILE:", str(a))
                                    elif os.path.isdir(a):
                                        print ("[ERROR] for FOLDER:", str(a))
                                    else:
                                        print ("[ERROR] for FILE/FOLDER:", str(a))
                else:
                    get_folder_size(args.PATH[0], args.excepts)
            else:
                if len(args.PATH) > 1:
                    for i in args.PATH:
                        get_folder_size(i, args.excepts)
                    get_folder_size(args.PATH, args.excepts)


if __name__ == "__main__":
    # if len(sys.argv) > 1:
        # d_size = get_folder_size2(sys.argv[1]) #this use
        #f_size1 = sizeof_fmt(d_size)
        #f_size2 = sizeof_fmt2(d_size)
        # f_size3 = sizeof_fmt3(d_size) #this use
        #f_size4 = sizeof_fmt4(d_size)
        #f_size = get_folder_size3(sys.argv[1])
        # print f_size1, "\n"
        # print f_size2, "\n"
        # print f_size3, "\n"
        # print f_size4, "\n"

        # get_folder_size(sys.argv[1])
        # print "\n"
        # get_folder_size3(sys.argv[1])
        # print "\n"
        # get_folder_size(sys.argv[1])
    # else:
        # main()
    usage()
