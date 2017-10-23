from win32com.shell import shell, shellcon
idl = shell.SHGetSpecialFolderLocation(0, shellcon.CSIDL_BITBUCKET)
d = shell.SHGetDesktopFolder()
sf = d.BindToObject(idl, None, shell.IID_IShellFolder)

for i in sf:
    print sf.GetDisplayNameOf(i, shellcon.SHGDN_NORMAL)
    print sf.GetDisplayNameOf(i, shellcon.SHGDN_FORPARSING)