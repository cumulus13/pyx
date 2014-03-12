import bluetooth
import os
import sys
from PyQt4 import QtGui, QtCore
import message

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mainapp = message.Messg()
    mainapp.hide()
    
    try:

        os.system("clear")
        print "\n\n"
        
        head =  """
        \t\t  ##############################################
        \t\t  #                                            #
        \t\t  #                 PyBlueScan                 #
        \t\t  #                     by                     #
        \t\t  #                   blackid                  #
        \t\t  #          livinginthecurl@gmail.com         #
        \t\t  #                                            #
        \t\t  ##############################################
    """
        #titik = "."
        
        print head
        
        def ssvc():
            j = 0
            if len(services) > 0:
                data001 = "Ada %d services yang berjalan pada %s \n" % (len(services),dev_ketemu)
                #os.system("sysloggen -q -t:192.168.128.1 -p:516 -f:0 -s:4 -m:\"" + str(data001) + "\"")
                #print "\t\t    Ada %d services yang berjalan pada %s \n" % (len(services),dev_ketemu)
                print "\t\t" + data001
                mainapp.message(data001)
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
                    
                    founded = """
                                \t\t\t\t"""+     + str(j) + "." + "Name         : %s \n" % svc["name"]+"""
                                \t\t\t\t"""+      + "  Host         : %s \n" % svc["host"]+"""
                                \t\t\t\t"""+       + "  Description  : %s \n" % svc["description"]+"""
                                \t\t\t\t"""+       + "  Provided by  : %s \n" % svc["provider"]+"""
                                \t\t\t\t"""+       + "  Protocol     : %s \n" % svc["protocol"]+"""
                                \t\t\t\t"""+       + "  Channel/PSM  : %s \n" % svc["port"]+"""
                                \t\t\t\t"""+       + "  SVC Classes  : %s \n" % svc["service-classes"]+"""
                                \t\t\t\t"""+       + "  Profiles     : %s \n" % svc["profiles"]+"""
                                \t\t\t\t"""+       + "  Service ID   : %s \n" % svc["service-id"]+"""
                                \n
                    """
                    mainapp.message(founded)
        
            else:
		#os.system("sysloggen -q -t:192.168.128.1 -p:516 -f:0 -s:4 -m:\"Tidak ditemukan adanya service yang berjalan ! \"")
		os.system("cls")
		print "\n"
		print "\t\t     Tidak ditemukan adanya service yang berjalan ! "
		sys.exit(app.exec_())
        
        
        #os.system("sysloggen -q -t:192.168.128.1 -p:516 -f:0 -s:4 -m:\"Cari Device Bluetooth . . . . \"")
        
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
	datahosttab = "\t\t "
	if len(dev_ketemu) <= 1:
	    #os.system("sysloggen -q -t:192.168.128.1 -p:516 -f:0 -s:4 -m:\"Tidak ada Device Bluetooth yang ditemukan !\"")
	    os.system("cls")
	    print "\n"
	    print "\t\t Tidak ada Device Bluetooth yang ditemukan !"
	else:   
	    datahost =  "Device %d ditemukan : \n" % len(dev_ketemu)
	    datahostc = datahosttab + datahost
	    #os.system("sysloggen -q -t:192.168.128.1 -p:516 -f:0 -s:4 -m:\"" + str(datahost) + "\"")
	    print datahostc
	    
	    for name, addr in dev_ketemu:
		data001 =  "\t\t " + str(i) + ")" + "." "Nama Bluetooth : %s \n" % (addr)
		data002 =  "\t\t    Alamat Fisik   : %s \n" % (name)
		#os.system("sysloggen -q -t:192.168.128.1 -p:516 -f:0 -s:4 -m:\"" + str(data001) + "\n" + str(data002) + "\"")
		print data001, "\n"
		print data002
		i = i + 1
		services = bluetooth.find_service(address=name)
		ssvc()

    except IOError, e:
	    #os.system("sysloggen -q -t:192.168.128.1 -p:516 -f:0 -s:4 -m:\" Bluetooth Adapter Mati !!!! \"")
	    os.system("cls")
	    print "\n\n"
	    print "\t\t\t  Bluetooth Adapter Mati !!!! \n"
	    sys.exit(app.exec_())


