import os
import sys

os.system("FTYPE Python.CompiledFile=\"C:\Python32\python.exe\" \"%1\" %*")
os.system("FTYPE Python.File=\"c:\Python32\python.exe\" \"%1\" %*")
os.system("FTYPE Python.NoConFile=\"C:\Python32\pythonw.exe\" \"%1\" %*")