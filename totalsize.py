# get disk/flash drive information on Windows
# using the win32 extension module from:
# http://sourceforge.net/projects/pywin32/files/
# tested on Windows XP with Python25 and Python31 by vegaseat
 
import win32file
import os
 
os.system('cls')
print "\n\n"
 
def get_drivestats(drive=None):
    '''
    drive for instance 'C'
    returns total_space, free_space and drive letter
    '''
    # if no drive given, pick the current working directory's drive
    if drive == None:
        drive = os.path.splitdrive(os.getcwd())[0].rstrip(':')
    sectPerCluster, bytesPerSector, freeClusters, totalClusters = \
        win32file.GetDiskFreeSpace(drive + ":\\")
    total_space = totalClusters*sectPerCluster*bytesPerSector
    free_space = freeClusters*sectPerCluster*bytesPerSector
    return total_space, free_space, drive
 
# use default drive (current drive)
# or specify drive for instance C --> get_drivestats('C')

def main():

	data = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	print "Drive|           Total           |           Free           |                   Used                   | \n"
	print "     |    Bytes   |   MB   |  GB |    Bytes   |   MB   | GB |    Bytes   |      MB      |      GB      | \n"
	print "-----|---------------------------|--------------------------|---------------------------|--------------|  \n"
	
	for i in(data):
		#print str(i)
		if (os.path.isdir(str(i) + ":\\") == True):
	
			total_space, free_space, drive = get_drivestats(str(i))
			mb = float(1024 * 1024)
			gb = float(1024 * 1024 * 1024)
			datamb = free_space/mb
			
			if (total_space < 10000000000 and total_space/mb < 100000 and total_space/gb < 100):
				print "%s    |%d0 |%0.2f0|%0.2f0|%d  |%0.2f |%0.2f|%d |%0.2f|%0.2f| \n" %(drive, total_space, (total_space/mb), (total_space/gb), free_space, (free_space/mb), (free_space/gb), (total_space - free_space), (total_space - free_space/mb), (total_space - free_space/gb))  
				
			elif (free_space < 1000000000):
					print "%s    |%d0|%0.2f|%0.2f|%d0  |%0.2f |%0.2f|%d |%0.2f|%0.2f| \n" %(drive, total_space, (total_space/mb), (total_space/gb), free_space, (free_space/mb), (free_space/gb), (total_space - free_space), (total_space - free_space/mb), (total_space - free_space/gb)) 
					
			elif (datamb < 1000):
					print "%s    |%d0|%0.2f|%0.2f|%d0  |%0.2f0 |%0.2f|%d |%0.2f|%0.2f| \n" %(drive, total_space, (total_space/mb), (total_space/gb), free_space, (free_space/mb), (free_space/gb), (total_space - free_space), (total_space - free_space/mb), (total_space - free_space/gb)) 
						
			else:
						print "%s    |%d |%0.2f|%0.2f|%d  |%0.2f |%0.2f|%d |%0.2f|%0.2f| \n" %(drive, total_space, (total_space/mb), (total_space/gb), free_space, (free_space/mb), (free_space/gb), (total_space - free_space), (total_space - free_space/mb), (total_space - free_space/gb))   
						
			#print "--------------------------------------------------------------------------------|  \n"
			#print( "%s" % drive)
			#print( "total_space = %d bytes" % total_space )
			#print( "free_space  = %d bytes" % free_space )
			#print( "used_space  = %d bytes" % (total_space - free_space) )
			 
			#print( '-'*40 )
			#mb = float(1024 * 1024)  # float() needed for Python2
			 
			#print( "Drive = %s" % drive )
			#print( "total_space = %0.2f Mb" % (total_space/mb) )
			#print( "free_space  = %0.2f Mb" % (free_space/mb) )
			#print( "used_space  = %0.2f Mb" % ((total_space - free_space)/mb) )
			 
			#print( '-'*40 )
			#gb = float(1024 * 1024 * 1024)
			 
			#print( "Drive = %s" % drive )
			#print( "total_space = %0.2f Gb" % (total_space/gb) )
			#print( "free_space  = %0.2f Gb" % (free_space/gb) )
			#print( "used_space  = %0.2f Gb" % ((total_space - free_space)/gb) )
			#print "################################################################################## \n"
			
			 
			"""possible output -->
			Drive = D
			total_space = 59674370048 bytes
			free_space  = 48973877248 bytes
			used_space  = 10700492800 bytes
			----------------------------------------
			Drive = D
			total_space = 56909.91 Mb
			free_space  = 46705.13 Mb
			used_space  = 10204.79 Mb
			----------------------------------------
			Drive = D
			total_space = 55.58 Gb
			free_space  = 45.61 Gb
			used_space  = 9.97 Gb
			"""
			
if __name__ == '__main__':
	main()