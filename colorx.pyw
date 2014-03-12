# colordialog.py

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
import pywintypes
import win32clipboard as w 
import win32con
import sys
import os

def getText(): 
    w.OpenClipboard() 
    d=w.GetClipboardData(win32con.CF_TEXT) 
    w.CloseClipboard() 
    return d 
 
def setText(aType,aString): 
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(aType,aString) 
    w.CloseClipboard()


class Example(QtGui.QWidget):
	def __init__(self):
		super(Example, self).__init__()
		self.initUI()

	def initUI(self):
		color = QtGui.QColor(0, 0, 0) 

		self.label = QtGui.QLabel(self)
		self.label.setText("Color name : ")
		self.label.setGeometry(10, 50, 80, 20)
		self.label.setFont(QtGui.QFont("Arial", 8, 600))
		
		self.labelcolor = QtGui.QLabel(self)
		self.labelcolor.setText(str(color.name()).upper())
		self.labelcolor.setGeometry(83, 50, 50, 20)
		self.labelcolor.setFont(QtGui.QFont("Arial", 8, 600))
		
		self.setWindowTitle('Colorx')
		self.setWindowIcon(QtGui.QIcon(r'd:\pyx\Paint.png'))
		self.button = QtGui.QPushButton('Chose Color', self)
		self.button.setFocusPolicy(QtCore.Qt.NoFocus)
		self.button.move(8, 20)

		self.connect(self.button, QtCore.SIGNAL('clicked()'), self.showDialog)
		self.setFocus()

		self.widget = QtGui.QWidget(self)
		self.widget.setStyleSheet("QWidget { background-color: %s }" % color.name())
		self.widget.setGeometry(140, 22, 105, 100)
		self.setWindowTitle('ColorDialog')
		self.setGeometry(300, 300, 250, 180)
		self.setFixedSize(250, 130)
		self.center()

	def showDialog(self):
		col = QtGui.QColorDialog.getColor()
		if col.isValid():
			self.widget.setStyleSheet("QWidget { background-color: %s }" % col.name())
			setText(w.CF_TEXT, str(col.name()).upper())
			self.labelcolor.setText(str(col.name()).upper())
				
	def center(self):
		screen = QtGui.QDesktopWidget().screenGeometry()
		size =  self.geometry()
		self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)
		
	def keyPressEvent(self, event):
		if event.key() == QtCore.Qt.Key_Escape:
			self.close()



if __name__ == '__main__':
  
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()
