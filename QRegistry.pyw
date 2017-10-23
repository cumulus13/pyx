import sys, os, errno
from PyQt4 import QtGui, QtCore


class MainW(QtGui.QDialog):
	def __init__(self, parent=None):
		QtGui.QDialog.__init__(self, parent)
		self.setWindowTitle('QReg Clean')
		self.resize(170, 190)
		#self.resize(500, 500)

		screen = QtGui.QDesktopWidget().screenGeometry()
		size = self.geometry()
		self.move((screen.width() - self.width()) / 2, (screen.height() - self.height()) / 2)

		QtGui.QToolTip.setFont(QtGui.QFont('Arial', 10))
		self.setWindowIcon(QtGui.QIcon('c:/pyx/Armadillo.png'))

		#Registry Cleaner
		self.RCButton = QtGui.QPushButton('Registry\n Cleaner', self)
		self.RCButton.setGeometry(10, 10, 70, 50)
		self.RCButton.setToolTip('TuneUp 2009 Registry Cleaner')

		#Registry Mechanic
		self.RMButton = QtGui.QPushButton('Registry\n Mechanic', self)
		self.RMButton.setGeometry(90, 10, 70, 50)
		self.RMButton.setToolTip('PC Tools Registry Mechanic')
		
		#jv16 PowerTools
		self.JVButton = QtGui.QPushButton('jv16 2009', self)
		self.JVButton.setGeometry(10, 70, 70, 50)
		self.JVButton.setToolTip('Macecraft jv16 PowerTools 2009')

		#Max  Registry Cleaner
		self.MRButton = QtGui.QPushButton('Max Registry\n Cleaner', self)
		self.MRButton.setGeometry(90, 70, 70, 50)
		self.MRButton.setToolTip('Max Registry Cleaner')

		#RegVac Registry Cleaner
		self.RVButton = QtGui.QPushButton('RegVac\n Registry', self)
		self.RVButton.setGeometry(10, 130, 70, 50)
		self.RVButton.setToolTip('RegVac Registry Cleaner')
		
		#R-Winner Registry Cleaner
		self.WNButton = QtGui.QPushButton('R-Winner', self)
		self.WNButton.setGeometry(90, 130, 70, 50)
		self.WNButton.setToolTip('Registry Winner')
		#self.NRButton.setIcon(QtGui.QIcon('c:/pyx/nero2.png'))

		#Add Event Connect Button
		self.connect(self.RCButton, QtCore.SIGNAL("clicked()"), self.RC)
		self.connect(self.RMButton, QtCore.SIGNAL("clicked()"), self.RM)
		self.connect(self.JVButton, QtCore.SIGNAL("clicked()"), self.JV)
		self.connect(self.MRButton, QtCore.SIGNAL("clicked()"), self.MR)
		self.connect(self.RVButton, QtCore.SIGNAL("clicked()"), self.RV)
		self.connect(self.WNButton, QtCore.SIGNAL("clicked()"), self.RW)


	def RC(self):
		try:
			os.system('RegistryCleaner.py')

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
	def RM(self):
		try:
			os.system('regmechx.py')

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
	def JV(self):
		try:
			os.system('jv16.py')

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

	def MR(self):
		try:
			os.system('MaxRCleaner.py')

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

	def RV(self):
		try:
			os.system('RegVac.py')

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

	def RW(self):

		try:
			os.system('RWinner.py')

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




app = QtGui.QApplication(sys.argv)
myapp = MainW()
myapp.show()
sys.exit(app.exec_())

