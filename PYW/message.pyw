import os
import sys
from PyQt4 import QtGui, QtCore

class Messg(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        #super(Messg, self).__init__(parent)
        
        self.setWindowTitle("Message")
        self.setWindowIcon(QtGui.QIcon("Customize.png"))
        
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 3, (screen.height() - size.height()) / 3)
        self.setFixedSize(900, 650)
        
    def message(self, data):
        msger2 = QtGui.QMessageBox.question(self, 'Message', data, QtGui.QMessageBox.Close)
        if msger2 == QtGui.QMessageBox.Close:
            self.destroy()
            sys.exit()
        else:
            return(1)
        
    
            
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mainapp = Messg()
    mainapp.hide()
    mainapp.message("Hello Coy !")
    sys.exit(app.exec_())
        