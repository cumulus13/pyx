import os
import sys
from PyQt4 import QtGui, QtCore
import systray

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    if not QtGui.QSystemTrayIcon.isSystemTrayAvailable():
        QtGui.QMessageBox.critical(None, QtCore.QObject.tr(app, "Systray"),
                QtCore.QObject.tr(app, "I couldn't detect any system tray on "
                    "this system."))
        sys.exit(1)

    window = systray.Window()
    window.show()
    sys.exit(app.exec_())