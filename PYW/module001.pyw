import sys,os
import errno
import module002

def usage(one):
    
    one = ""
    os.system('cls')
    print one

def main(data):

    sprt = " "
    
    try:
        os.system("start " + data + sprt + sys.argv[1])
        #os.execlp(data, sys.argv[1])
        
    except OSError, e:
        
        if e.errno == errno.ENOEXEC:
            os.system("cls")
            print "\n"
            print "\t\t Program Tidak Dapat Di Eksekusi !"

        elif e.errno == errno.ENOENT:
            os.system("cls")
            print "\n"
            print "\t\t Program Tidak Dapat Ditemukan !"

        else:
            os.system("cls")
            print "\n"
            print "\t\t Program Tidak Dapat Berjalan Pada Mode System Operasi Win32 !"
            
    except IndexError, e:
        
        if (sys.argv < 1):
            os.execlp(data)
            
        else: 
			try:
				if (sys.argv == "--help"):
					os.system('cls')
					print '--help'
					#usage(data)
    
				elif (sys.argv == "-h"):
					os.system('cls')
					print '-h'
					#usage(data)
                
				else:
					os.system('cls')
					#usage(data)
					print "Argument Not Present !"
					print "\n"
					module002.main(data)
					
			except IndexError, e:
				os.system('cls')
				print "\t Error With Status : ", e
        
