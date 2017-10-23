import sys
import os
import multiprocessing
#import subprocess

madplay =  r"c:\exe\madplay.exe"
filepid = os.path.join(os.getenv("TEMP"), "mpl.pid")

def mplayer(dirname):
    data_mp3 = os.popen("dir /s /b \"" + dirname + "\"").readlines()
    for i in  data_mp3:
        a =  str(os.path.abspath(i).split("\n")[0])
        print "FILE =", a
        f =  open(filepid, "w")
        f.write(str(os.getpid()))
        f.close()
        os.system(r"c:\\EXE\\chp.exe" + " " + madplay + " \"" + a + "\"")
        #subprocess.Popen([madplay, str(a)])
        
def player(path):
    #p = multiprocessing.Process(target=mplayer(path), args= (str(a)))
    #p.start()
    print "PID =", p.pid
    mplayer(path)

    
def kill(pid):
    # all this shit is because we are stuck with Python 2.5 and we cannot use Popen.terminate()
    if sys.platform == 'win32':
        import ctypes
        PROCESS_TERMINATE = 1
        handle = ctypes.windll.kernel32.OpenProcess(PROCESS_TERMINATE, False, pid)
        ctypes.windll.kernel32.TerminateProcess(handle, -1)
        ctypes.windll.kernel32.CloseHandle(handle)
    else:
        os.kill(pid, signal.SIGKILL)    
    
def kill2(pid):
    import ctypes
    PROCESS_TERMINATE = 1
    handle = ctypes.windll.kernel32.OpenProcess(PROCESS_TERMINATE, False, pid)
    ctypes.windll.kernel32.TerminateProcess(handle, -1)
    ctypes.windll.kernel32.CloseHandle(handle)
    
def usage():
    if sys.argv[1] == "kill":
        f = open(filepid, "r")
        pid =  f.readlines()
        #print pid
        f.close()
        kill(int(pid[0]))
    else:
        player(sys.argv[1])
    
if __name__ == "__main__":
    #player(sys.argv[1])
    usage()
    #kill(int(sys.argv[1]))