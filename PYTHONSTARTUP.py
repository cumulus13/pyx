from cls import cls
import rlcompleter
import readline
readline.parse_and_bind('tab:complete')
import clipboard
import os


#def copy(data):
#    clipboard.copy(str(data))


def cd(path):
    return os.chdir(path)


def ls(path=None):
    if path == None:
        path = os.getcwd()
    return os.listdir(path)


def mkdir(path):
    return os.makedirs(path)


def kill(pid):
    return os.kill(pid, pid)
