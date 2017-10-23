import sys,os
import errno

def main(data):

    sprt = " "
    
    try:
        #os.system("start " + data + sprt + sys.argv[1])
        os.execlp(data).joint(sys.argv[1])
        
    except OSError, e:
        
        if e.errno == errno.ENOEXEC:
            os.system("cls")
            print "\n";
            print "\t\t Program Tidak Dapat Di Eksekusi !"
        elif e.errno == errno.ENOENT:
            os.system("cls")
            print "\n";
            print "\t\t Program Tidak Dapat Ditemukan !"
        else:
            os.system("cls")
            print "\n";
            print "\t\t Program Tidak Dapat Berjalan Pada Mode System Operasi Win32 !"
            
    except IndexError, e:
		os.system('cls')
		print "\n"
		print "\t Error With Status : ", e

def kill(data):
    
    sprt = " "
    
    try:
	data2 = os.path.split(data)[1]
        #os.system("start " + data + sprt + sys.argv[1])
        #os.execlp(data).joint(sys.argv[1])
	os.system("processx -k " + data2)
        
    except OSError, e:
        
        if e.errno == errno.ENOEXEC:
            os.system("cls")
            print "\n";
            print "\t\t Program Tidak Dapat Di Eksekusi !"
        elif e.errno == errno.ENOENT:
            os.system("cls")
            print "\n";
            print "\t\t Program Tidak Dapat Ditemukan !"
        else:
            os.system("cls")
            print "\n";
            print "\t\t Program Tidak Dapat Berjalan Pada Mode System Operasi Win32 !"
            
    except IndexError, e:
		os.system('cls')
		print "\n"
		print "\t Error With Status : ", e
