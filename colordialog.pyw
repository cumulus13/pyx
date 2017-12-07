#!/usr/bin/python

# colordialog.py
#!/usr/bin/env python
#coding:utf-8
"""
  Author:  LICFACE --<licface@yahoo.com>
  Purpose: Show Color for web and any development
  Created: 11/18/2017
"""

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
import clipboard
import time
import warnings

class ColorDialog(QtGui.QDialog):
    def __init__(self, parent=None):

        QtGui.QWidget.__init__(self, parent)
        self.widget = QtGui.QWidget(self)
        color = QtGui.QColor(0, 0, 0)
    
        #self.setGeometry(300, 300, 250, 180)
        self.setGeometry(927, 505, 250, 180)
        self.setWindowTitle('ColorDialog')
        self.setWindowIcon(QtGui.QIcon(r'F:\IMAGES\programming\pyqt4.png'))

        self.button = QtGui.QPushButton('Dialog', self)
        self.button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button.move(20, 20)
        
        self.button1 = QtGui.QPushButton('Translate', self)
        self.button1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button1.move(20, 138)

        self.lineedit = QtGui.QLineEdit(self)
        #self.lineedit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lineedit.setGeometry(0,0, 100,21)
        self.lineedit.move(130, 139)

        self.connect(self.button, QtCore.SIGNAL('clicked()'), self.showDialog)
        self.connect(self.button1, QtCore.SIGNAL('clicked()'), self.setColor)
        #self.connect(self.lineedit, QtCore.SIGNAL('click()'), self.clear_text_lineedit)
        self.setFocus()

        self.widget.setStyleSheet("QWidget { background-color: %s }" 
            % color.name())
        self.widget.setGeometry(130, 22, 100, 100)
        #import thread
        #thread.start_new_thread(self.check_clipboard, ())
        
    def check_clipboard(self):
        str_clipboard = ''
        warnings.filterwarnings('ignore')
        while 1:
            if str_clipboard != clipboard.paste():
                if str(clipboard.paste()).strip()[0] == '#' or str(clipboard.paste()).strip() == 6:
                    str_color = str(clipboard.paste()).strip()
                    if "#" in str_color:
                        color = str_color
                    else:
                        color = "#" + str_color
                    col = QtGui.QColor(color)
                    self.widget.setStyleSheet("QWidget { background-color: %s }" % col.name())
                else:                
                    time.sleep(1)        
        
    def clear_text_lineedit(self):
        self.lineedit.text = ''
        
    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()    

    def setColor(self):
        if "#" in self.lineedit.text():
            color = str(self.lineedit.text()).strip()
        else:
            color = "#" + str(self.lineedit.text()).strip()
        col = QtGui.QColor(color)
        #print "col name =", col.name()
        clipboard.copy(color)
        self.widget.setStyleSheet("QWidget { background-color: %s }" % col.name())

    def showDialog(self):
        if "#" in self.lineedit.text():
            color = str(self.lineedit.text()).strip()
            cq = QtGui.QColor(color)
            col = QtGui.QColorDialog.getColor(cq)
        else:
            color = "#" + str(self.lineedit.text()).strip()
            cq = QtGui.QColor(color)
            col = QtGui.QColorDialog.getColor(cq)
        #print "type(col) =", type(col)

        if col.isValid():
            clipboard.copy(str(col.name()))
            self.widget.setStyleSheet("QWidget { background-color: %s }"
                % col.name())
            self.lineedit.setText(col.name())

app = QtGui.QApplication(sys.argv)
cd = ColorDialog()
cd.show()
app.exec_()
