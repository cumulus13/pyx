import os
import traceback
import sys
import tarfile
import zipfile
import shutil
import optparse
import time
import send2trash
import thread

MASTER_PATH = r'd:\PYTHON_MODULES'

if os.getenv("MASTER_PATH") != None:
    MASTER_PATH = os.getenv("MASTER_PATH")

def translate(name):
    basename = os.path.basename(name)
    basedname = str(basename).split("-")
    return basedname[0]

def check_archive(name):
    if str(name).endswith(".gz"):
        try:
            tarname = tarfile.open(name)
            return True
        except:
            return False
    if str(name).endswith(".zip"):
        try:
            zipname = zipfile.ZipFile(name)
            testzip = zipname.testzip()
            if testzip == None:
                return True
            else:
                return False
        except:
            print "ERROR:",
            print traceback.format_exc()
            return False

def moved(filename, path=None, overwrite=None, quiet=None, masterpath=None, noclean=None):
    MASTER_PATH = r'd:\PYTHON_MODULES'
    if masterpath != None:
        MASTER_PATH = masterpath
    else:
        MASTER_PATH = MASTER_PATH
    for i in filename:
        M_PATH = os.path.join(MASTER_PATH, translate(i))
        DEST_NAME = os.path.join(M_PATH, os.path.basename(i))
        if path:
            if not os.path.isdir(path):
                os.makedirs(path)
                M_PATH = path
        else:
            if not os.path.isdir(M_PATH):
                os.makedirs(M_PATH)
        #print "DEST_NAME =", DEST_NAME
        #print "M_PATH =", M_PATH
        if os.path.isfile(DEST_NAME):
            if overwrite:
                os.remove(DEST_NAME)
            else:
                print "\n"
                q =  raw_input(" Overwrite ? (y/n): ")
                if str(q).lower() == 'y' or str(q).lower() == 'yes':
                    os.remove(DEST_NAME)
                if quiet:
                    os.remove(DEST_NAME)
        
        thread.start_new(shutil.copy2, (i, DEST_NAME))
        if noclean == None:
            time.sleep(1)
            send2trash.send2trash(i)
            
def usage():
    parser = optparse.OptionParser()
    parser.add_option('-o', '--overwrite', help='Overwrite File move to', action='store_true')
    parser.add_option('-d', '--destination', help='Destination Folder default: MASTER_PATH with defintion or environment', action='store')
    parser.add_option('-n', '--noclean', help='Dont delete source file', action='store_true')
    parser.add_option('-q', '--quiet', help='No Supress', action='store_true')
    option, argv = parser.parse_args()
    if len(sys.argv) == 1:
        parser.print_help()
    else:
        moved(argv, option.destination, option.overwrite, option.quiet, option.destination, option.noclean)

if __name__ == "__main__":
    #print translate(sys.argv[1])
    #check_archive(sys.argv[1])
    #data = sys.argv[1:len(sys.argv)]
    usage()
