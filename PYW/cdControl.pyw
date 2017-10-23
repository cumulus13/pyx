import gtk
import os
import sys
import cairo
import pygtk
import pango

class PyApp(gtk.Window): 
    def __init__(self):
        super(PyApp, self).__init__()
        
        self.set_size_request(250, 100)
        self.set_position(gtk.WIN_POS_CENTER)
        self.connect("destroy", gtk.main_quit)
        self.set_resizable(False)
        self.set_title("CD Control")
        #self.set_icon(gtk.gdk.pixbuf_new_from_file("Color picker.png"))
        
        
        table = gtk.Table(2, 2, True);
        
        info = gtk.Button("Eject CD")
        warn = gtk.Button("Eject DVD")
        ques = gtk.Button("Close CD")
        erro = gtk.Button("Close DVD")

        
        info.connect("clicked", self.on_info)
        warn.connect("clicked", self.on_warn)
        ques.connect("clicked", self.on_ques)
        erro.connect("clicked", self.on_erro)
        
        table.attach(info, 0, 1, 0, 1)
        table.attach(warn, 1, 2, 0, 1)
        table.attach(ques, 0, 1, 1, 2)
        table.attach(erro, 1, 2, 1, 2)
        
        
        self.add(table)
        self.show_all()

    def on_info(self, widget):
        try:
            os.system("eject cd")
            
        except OSError, e:
            md = gtk.MessageDialog(self, 
                gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_ERROR, 
                gtk.BUTTONS_CLOSE, "CD Hase been Eject !\n e.message")
            md.run()
            md.destroy()

            
        
    
    def on_erro(self, widget):
        try:
            os.system("close dvd")
            
        except OSError, e:
            md = gtk.MessageDialog(self, 
                gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_ERROR, 
                gtk.BUTTONS_CLOSE, "DVD Hase been Close !\n e.message")
            md.run()
            md.destroy()

    
    
    
    def on_ques(self, widget):
        try:
            os.system("close cd")
            
        except OSError, e:
            md = gtk.MessageDialog(self, 
                gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_ERROR, 
                gtk.BUTTONS_CLOSE, "CD Hase been Close !\n e.message")
            md.run()
            md.destroy()

    
    
    def on_warn(self, widget):
        try:
            os.system("eject dvd")
            
        except OSError, e:
            md = gtk.MessageDialog(self, 
                gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_ERROR, 
                gtk.BUTTONS_CLOSE, "DVD Hase been Eject !\n e.message")
            md.run()
            md.destroy()

    

PyApp()
gtk.main()
