import module006
import module004
import os
import sys
import time

def cekstate(data):
  
    datacek001 = "START_PENDING"
    
    for i in range(0, 100):
	waitme = ". " * (i/10)
    
	if datacek001 == module006.status(data):
	    os.system("cls")
	    print "\n"
	    
	    try:
		print "\n"
		print "\t\t Please wait . " + str(waitme) 
	    except:
		pass
	    
	    
	else:
	
	    print "data = " , module006.status(data)
	    
    time.sleep(10)	
    os.system("cls")
    print "\n"
    module004.status(data)