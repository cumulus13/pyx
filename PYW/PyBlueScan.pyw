import bluetooth
import os

try:

    os.system("clear")
    print "\n\n"
    
    head =  """
	      \t\t  ##############################################
	      \t\t  #                                            #
	      \t\t  #                 PyBlueScan                 #
			  #                     by                     #
			  #                   blackid                  #
			  #          livinginthecurl@gmail.com         #
	      \t\t  #                                            #
			  ##############################################
	      """
    #titik = "."
    
    print head
    
    def ssvc():
	j = 0
	if len(services) > 0:
	    print "\t\t    Ada %d services yang berjalan pada %s \n" % (len(services),dev_ketemu)
	    print "\t\t     Service yang berjalan    : \n"
	    for svc in services:
		j = j + 1
		print "\t\t\t\t    " + str(j) + "." + "Name         : %s \n" % svc["name"]
		print "\t\t\t\t    "  + "  Host         : %s \n" % svc["host"]
		print "\t\t\t\t    "  + "  Description  : %s \n" % svc["description"]
		print "\t\t\t\t    "  + "  Provided by  : %s \n" % svc["provider"]
		print "\t\t\t\t    "  + "  Protocol     : %s \n" % svc["protocol"]
		print "\t\t\t\t    "  + "  Channel/PSM  : %s \n" % svc["port"]
		print "\t\t\t\t    "  + "  SVC Classes  : %s \n" % svc["service-classes"]
		print "\t\t\t\t    "  + "  Profiles     : %s \n" % svc["profiles"]
		print "\t\t\t\t    "  + "  Service ID   : %s \n" % svc["service-id"]
		print "\n"
    
	else:
	    print "\t\t     Tidak ditemukan adanya service yang berjalan ! "
    
    print "\t\t\t  Cari Device Bluetooth . . . ." #+ titik
    
    dev_ketemu = bluetooth.discover_devices(lookup_names = True)
    
    #if len(dev_ketemu) < 1:
	
    i = 1
    #j = 0
    #titik = "."
	
    #print "\t\t Cari Device Bluetooth . . " + titik

    
    os.system("clear")
    print "\n\n"
    print head
    print "\n\n"
    print "\t\t Device %d ditemukan : \n" % len(dev_ketemu)
    
    for name, addr in dev_ketemu:
	print "\t\t " + str(i) + ")" + "." "Nama Bluetooth : %s \n" % (addr)
	print "\t\t    Alamat Fisik   : %s \n" % (name)
	i = i + 1
	services = bluetooth.find_service(address=name)
	ssvc()

except IOError, e:
    print "\n\n"
    print "\t\t\t  Bluetooth Adapter Mati !!!! \n"


