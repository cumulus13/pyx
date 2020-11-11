#!c:/SDK/Anaconda2/python.exe
MODULE_PATH = r"D:\PROJECTS2"
import sys
sys.path.insert(0, MODULE_PATH)
from pmail import pmail

if __name__ == '__main__':
    mailer = pmail.pmail()
    mailer.usage()