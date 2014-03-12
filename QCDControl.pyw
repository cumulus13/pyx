
import sys, os, errno
from PyQt4 import QtGui, QtCore


class MainW(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QDialog.__init__(self, parent)
		self.setWindowTitle('QCdControl')
		self.resize(170, 270)
		self.setFixedSize(170, 270)
		#self.resize(500, 500)

		screen = QtGui.QDesktopWidget().screenGeometry()
		size = self.geometry()
		self.move((screen.width() - self.width()) / 2, (screen.height() - self.height()) / 2)

		QtGui.QToolTip.setFont(QtGui.QFont('Arial', 10))
		self.setWindowIcon(QtGui.QIcon('d:\pyx\iDVD.png'))

		#Ad Button
		self.ECDButton = QtGui.QPushButton('Eject CD', self)
		self.ECDButton.setGeometry(10, 10, 70, 50)
		self.ECDButton.setToolTip('Eject CD')

		self.CCDButton = QtGui.QPushButton('Close CD', self)
		self.CCDButton.setGeometry(90, 10, 70, 50)
		self.CCDButton.setToolTip('Close CD')

		self.EVDButton = QtGui.QPushButton('Eject DVD', self)
		self.EVDButton.setGeometry(10, 70, 70, 50)
		self.EVDButton.setToolTip('Eject DVD')

		self.CVDButton = QtGui.QPushButton('Close DVD', self)
		self.CVDButton.setGeometry(90, 70, 70, 50)
		self.CVDButton.setToolTip('Close DVD')

		self.OrontButton = QtGui.QPushButton('Oront', self)
		self.OrontButton.setGeometry(10, 150, 70, 50)
		self.OrontButton.setToolTip('Burning With Oront Burning')
		self.OrontButton.setIcon(QtGui.QIcon('d:/pyx/oront2.png'))

		self.NeroButton = QtGui.QPushButton('Nero', self)
		self.NeroButton.setGeometry(90, 150, 70, 50)
		self.NeroButton.setToolTip('Burning With Nero')
		self.NeroButton.setIcon(QtGui.QIcon('d:/pyx/nero2.png'))

		self.CheckButton = QtGui.QPushButton('CDCheck', self)
		self.CheckButton.setGeometry(10, 210, 70, 50)
		self.CheckButton.setToolTip('Check Verified youre CD/DVD From Damage & Error Data')
		self.CheckButton.setIcon(QtGui.QIcon('d:/pyx/cdcheck.png'))

       		self.ARButton = QtGui.QPushButton('AnyRead', self)
	        self.ARButton.setGeometry(90, 210, 70, 50)
        	self.ARButton.setToolTip('Any Reader Cd or Dvd From Damage Data and File')
	        self.ARButton.setIcon(QtGui.QIcon('d:/pyx/AnyReader.ico'))

		#Add Label
        	self.NLabel = QtGui.QLabel(self)
	        self.NLabel.setMinimumSize(150, 50)
       		self.NLabel.setGeometry(10, 110, 10, 10)
	        self.NImage = QtGui.QImage('d:/pyx/burning.png')
       		self.NLabel.setPixmap(QtGui.QPixmap.fromImage(self.NImage))

		#Add Event Connect Button
	        self.connect(self.ECDButton, QtCore.SIGNAL("clicked()"), self.ecd)
       		self.connect(self.CCDButton, QtCore.SIGNAL("clicked()"), self.ccd)
	        self.connect(self.EVDButton, QtCore.SIGNAL("clicked()"), self.evd)
       		self.connect(self.CVDButton, QtCore.SIGNAL("clicked()"), self.cvd)
	        self.connect(self.OrontButton, QtCore.SIGNAL("clicked()"), self.oront)
	       	self.connect(self.NeroButton, QtCore.SIGNAL("clicked()"), self.nero)
        	self.connect(self.CheckButton, QtCore.SIGNAL("clicked()"), self.cdcheck)


	def ecd(self):
		os.system('eject cd')
	def ccd(self):
		os.system('close cd')
	def evd(self):
		os.system('eject dvd')
	def cvd(self):
		os.system('close dvd')
	def oront(self):
		try:
			os.system('oront.py')

		except OSError, e:
			if e.errno == errno.ENOENT:
				msg = QtGui.QMessageBox.warning(self, 'ERROR !', "PROGRAM TIDAK DITEMUKAN !\nLanjut ?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
				if msg == QtGui.QMessageBox.Yes:
					return(1)
				else:
					sys.exit()

			elif e.errno == errno.ENOEXEC:
				msg = QtGui.QMessageBox.warning(self, 'ERROR !', 'PROGRAM BUKAN PROGRAM EXECUTABLE !\nLanjut ?', QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
				if msg == QtGui.QMessageBox.Yes:
					return(1)
				else:
					sys.exit()

			else:
				msg = QtGui.QMessageBox.warning(self, 'ERROR !', 'PROGRAM TIDAK DAPAT BERJALAN DI Win32 ATAU COMMANDLINE ! \n Lanjut ?', QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
				if msg == QtGui.QMessageBox.Yes:
					return(1)
				else:
					sys.exit()
	def nero(self):
		try:
			os.system("nero.py")

		except OSError, e:
			if e.errno == errno.ENOENT:
				msg = QtGui.QMessageBox.warning(self, 'ERROR !', 'PROGRAM TIDAK DITEMUKAN ! \n Lanjut ?', QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
				if msg == QtGui.QMessageBox.Yes:
					return(1)
				else:
					sys.exit()

			elif e.errno == errno.ENOEXEC:
				msg = QtGui.QMessageBox.warning(self, 'ERROR !', 'PROGRAM BUKAN PROGRAM EXECUTABLE ! \n Lanjut ?', QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
				if msg == QtGui.QMessageBox.Yes:
					return(1)
				else:
					sys.exit()

			else:
				msg = QtGui.QMessageBox.warning(self, 'ERROR !', 'PROGRAM TIDAK DAPAT BERJALAN DI Win32 ATAU COMMANDLINE ! \n Lanjut ?', QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
				if msg == QtGui.QMessageBox.Yes:
					return(1)
				else:
					sys.exit()
	def cdcheck(self):
		try:
			os.system("cdcheck.py")

		except OSError, e:
			if e.errno == errno.ENOENT:
				msg = QtGui.QMessageBox.warning(self, 'ERROR !', 'PROGRAM TIDAK DITEMUKAN ! \n Lanjut ?', QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
				if msg == QtGui.QMessageBox.Yes:
					return(1)
				else:
					sys.exit()

			elif e.errno == errno.ENOEXEC:
				msg = QtGui.QMessageBox.warning(self, 'ERROR !', 'PROGRAM BUKAN PROGRAM EXECUTABLE ! \n Lanjut ?', QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
				if msg == QtGui.QMessageBox.Yes:
					return(1)
				else:
					sys.exit()

			else:
				msg = QtGui.QMessageBox.warning(self, 'ERROR !', 'PROGRAM TIDAK DAPAT BERJALAN DI Win32 ATAU COMMANDLINE ! \n Lanjut ?', QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
				if msg == QtGui.QMessageBox.Yes:
					return(1)
				else:
					sys.exit()

def AnyRead(self):
		try:
			os.system("AnyReader.py")

		except OSError, e:
			if e.errno == errno.ENOENT:
				msg = QtGui.QMessageBox.warning(self, 'ERROR !', 'PROGRAM TIDAK DITEMUKAN ! \n Lanjut ?', QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
				if msg == QtGui.QMessageBox.Yes:
					return(1)
				else:
					sys.exit()

			elif e.errno == errno.ENOEXEC:
				msg = QtGui.QMessageBox.warning(self, 'ERROR !', 'PROGRAM BUKAN PROGRAM EXECUTABLE ! \n Lanjut ?', QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
				if msg == QtGui.QMessageBox.Yes:
					return(1)
				else:
					sys.exit()

			else:
				msg = QtGui.QMessageBox.warning(self, 'ERROR !', 'PROGRAM TIDAK DAPAT BERJALAN DI Win32 ATAU COMMANDLINE ! \n Lanjut ?', QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
				if msg == QtGui.QMessageBox.Yes:
					return(1)
				else:
					sys.exit()




app = QtGui.QApplication(sys.argv)
myapp = MainW()
myapp.show()
sys.exit(app.exec_())

