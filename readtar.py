import tarfile
import os
import sys

TEMP = os.getenv('TEMP')
if TEMP == None:
    raise SystemError('No Temp Directory FOUND !')

def read(filetar, readfile):
    ftar = tarfile.open(filetar)
    os.chdir(TEMP)
    for i in ftar.getnames():
        if i.endswith(readfile):
            f = ftar.extractfile(i)
            content = f.read()
            print content
    ftar.close()
    
if __name__ == "__main__":
    read(sys.argv[1], sys.argv[2])
    