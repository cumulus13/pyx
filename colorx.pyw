#!/usr/bin/env python2

import sys
import os
from PyQt5.QtGui import QColor, QFont, QIcon
from PyQt5.QtWidgets import QApplication, QColorDialog, QWidget, QLabel, QPushButton, QLineEdit, QDesktopWidget
from PyQt5.QtCore import *
if sys.platform == 'win32':
	import pywintypes
	import win32clipboard as w 
	import win32con
else:
	import clipboard

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


class Example(QWidget):
	def __init__(self):
		super(Example, self).__init__()
		self.initUI()

	def initUI(self):
		color = QColor(0, 0, 0) 

		self.label = QLabel(self)
		self.label.setText("Color name : ")
		self.label.setGeometry(10, 43, 70, 8)
		self.label.setFont(QFont("Arial", 8, 600))
		
		self.labelcolor = QLabel(self)
		self.labelcolor.setText(str(color.name()).upper())
		self.labelcolor.setGeometry(83, 43, 45, 8)
		self.labelcolor.setFont(QFont("Arial", 8, 600))
		
		self.setWindowTitle('Colorx')
		self.setWindowIcon(QIcon(r'c:\pyx\Paint.png'))
		self.button = QPushButton('Chose Color', self)
		self.button.setFocusPolicy(Qt.NoFocus)
		self.button.move(8, 10)
		self.button1 = QPushButton('Set Color', self)
		self.button1.setFocusPolicy(Qt.NoFocus)
		self.button1.move(8, 60)
		
		self.editline =QLineEdit(self)
		self.editline.setGeometry(9, 93, 120, 20)
		#self.editline.setText('#')
		self.editline.editingFinished.connect(self.setColor)
		self.editline.textChanged.connect(self.checkLineEdit)

		self.widget = QWidget(self)
		self.widget.setStyleSheet("QWidget { background-color: %s }" % color.name())
		self.widget.setGeometry(140, 12, 105, 100)
		self.setWindowTitle('ColorDialog')
		self.setGeometry(300, 300, 250, 180)
		self.setFixedSize(250, 130)
		self.center()

		self.button.clicked.connect(self.showDialog)
		self.button1.clicked.connect(self.setColor)
		self.setFocus()
		
		QApplication.clipboard().dataChanged.connect(self.checkClipboard)
		
	def checkClipboard(self):
		if len(QApplication.clipboard().text()) == 7 and "#" == QApplication.clipboard().text()[0]:
			self.setColorFromClipboard()
		elif len(QApplication.clipboard().text()) == 6 and not "#" == QApplication.clipboard().text()[0]:
			self.setColorFromClipboard("#" + QApplication.clipboard().text())
		
	def checkLineEdit(self):
		if self.editline.text().lower() == 's' or self.editline.text().lower() == '#s':
			self.showDialog()
		else:
			if not "#" in self.editline.text():
				#print("TEXT 1 =", self.editline.text())
				self.editline.setText('#' + self.editline.text())
				#print("TEXT 2 =", self.editline.text())
			else:
				if len(self.editline.text()) == 7:
					self.setColor()
				elif len(self.editline.text()) > 7:
					self.editline.setText(self.editline.text()[:7])
		#else:
		#	self.editline.setText("#" + self.editline.text())

	def showDialog(self):
		col = QColorDialog.getColor()
		if col.isValid():
			if len(col.name()) == 7 and col.name()[0] == '#':
				self.widget.setStyleSheet("QWidget { background-color: %s }" % col.name())
			elif len(col.name()) == 6 and not col.name()[0] == '#':
				self.widget.setStyleSheet("QWidget { background-color: #%s }" % col.name())
			#if sys.version_info.major == 2:
			#	QApplication.clipboard().setText()
			#else:
			#	QApplication.clipboard().setText(col.name().upper())
			
			if sys.version_info.major == 2:
				self.labelcolor.setText(str(col.name()).upper())
			else:
				self.labelcolor.setText(col.name().upper())
			self.editline.setText(str(col.name()).upper())
			
			if sys.platform == 'win32':
				setText(w.CF_TEXT, str(col.name()).upper())
			else:
				clipboard.copy(str(col.name()).upper())
			
	def setColor(self):
		if len(self.editline.text()) == 7 and self.editline.text()[0] == '#':
			self.widget.setStyleSheet("QWidget { background-color: %s }" %(self.editline.text().lower()))
		elif len(self.editline.text()) == 6 and not self.editline.text()[0] == '#':
			self.widget.setStyleSheet("QWidget { background-color: #%s }" %(self.editline.text().lower()))
		
		QApplication.clipboard().setText(self.editline.text().upper())
		#if sys.platform == 'win32':
		#	setText(w.CF_TEXT, str(self.editline.text()).upper())
		#else:
		#	clipboard.copy(str(self.editline.text()).upper())
		#QApplication.clipboard().setText(str(self.editline.text()).upper())
		self.labelcolor.setText(self.editline.text().upper())
		
	def setColorFromClipboard(self, text=None):
		if not text:
			text = getText()
		if len(text) == 7 and text[0] == '#':
			self.widget.setStyleSheet("QWidget { background-color: %s }" % str(text))
		elif len(text) == 6 and not text[0] == '#':
			self.widget.setStyleSheet("QWidget { background-color: #%s }" % str(text))
		self.labelcolor.setText(str(text).upper())
				
	def center(self):
		screen = QDesktopWidget().screenGeometry()
		size =  self.geometry()
		self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)
		
	def keyPressEvent(self, event):
		if event.key() == Qt.Key_Escape:
			self.close()
		elif event.key() == Qt.Key_C:
			self.showDialog()
		elif event.key() == Qt.Key_S:
			self.setColor()
		else:
			if not "#" in self.editline.text():
				self.editline.setText('#' + self.editline.text())
			else:
				self.editline.setFocus()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	iconfile = os.path.join(os.path.dirname(__file__), 'colorx.png')
	app.setWindowIcon(QIcon(iconfile))
	ex = Example()
	ex.show()
	app.exec_()
