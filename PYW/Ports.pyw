import gtk
import os
import sys
import cairo
import pygtk
import pango

class PyApp(gtk.Window): 
    def __init__(self):
        super(PyApp, self).__init__()
        
        self.set_size_request(200, 100)
        self.set_position(gtk.WIN_POS_CENTER)
        self.connect("destroy", gtk.main_quit)
        self.set_resizable(False)
        self.set_title("Check Ports")
        #self.set_icon(gtk.gdk.pixbuf_new_from_file("Color picker.png"))
        
        
        table = gtk.Table(2, 2, True);
        
        cports = gtk.Button("Cports")

        tcpview = gtk.Button("TCPView")

        
        cports.connect("clicked", self.on_info1)
        tcpview.connect("clicked", self.on_info2)
        
        table.attach(cports, 0, 2, 0, 1)
        table.attach(tcpview, 0, 2, 1, 2)
        
        
        self.add(table)
        self.show_all()

    def on_info1(self, widget):
        try:
            os.system("c:\WINDOWS\system32\cports.exe")
            
        except OSError, e:
            md = gtk.MessageDialog(self, 
                gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_ERROR, 
                gtk.BUTTONS_CLOSE, "Theres not open ports !\n e.message")
            md.run()
            md.destroy()

            
        
    
    def on_info2(self, widget):
        try:
            os.system("c:\pyx\Tcpview.exe")
            
        except OSError, e:
            md = gtk.MessageDialog(self, 
                gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_ERROR, 
                gtk.BUTTONS_CLOSE, "Theres not open ports !\n e.message")
            md.run()
            md.destroy()
    

PyApp()
gtk.main()
