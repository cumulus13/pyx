import gtk


class PyApp(gtk.Window): 
    def __init__(self):
        super(PyApp, self).__init__()
        #self.show_all()

    def errorcontent(self):
        md = gtk.MessageDialog(self, gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_INFO, gtk.BUTTONS_CLOSE, "List & Tree Folder Succesfully \n\nCek List & Tree Report !")
        md.set_position(gtk.WIN_POS_CENTER)
        md.run()
        md.destroy()
        
       
if __name__ == '__main__':
    PyApp().errorcontent()
    #gtk.main()
