import sys,os
import errno

def usage(data):

    data = ""
    os.system('cls')
    print data

def main(data):

    sprt = " "

    try:
        #os.system("start " + data + sprt + sys.argv[1])
        #os.execlp(data)
        os.system("start " + data + sys.argv[1])

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

        if (sys.argv <= 1):
            os.system('cls')
            #usage(data)
            print "ERROR !"

        elif (sys.argv == '--help'):
            os.system('cls')
            usage(data)

        elif (sys.argv == '-h'):
            os.system('cls')
            usage(data)

        else:
            os.system('cls')
            os.execlp(data)
