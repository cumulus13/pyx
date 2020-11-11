import re
import operator
import os
import sys 
import os
from PyQt4.QtCore import * 
from PyQt4.QtGui import * 
 
def main(): 
    app = QApplication(sys.argv) 
    w = MyWindow() 
    w.show() 
    os.system("cls")
    sys.exit(app.exec_()) 
 
class MyWindow(QWidget): 
    def __init__(self, *args): 
        QWidget.__init__(self, *args) 

        # create table
        self.get_table_data()
        self.setWindowTitle("Drive Space")
        self.setWindowIcon(QIcon('d:\pyx\Stats.png'))
        self.setFixedSize(300, 460)
        self.resize(300, 460)
        
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - self.width()) / 2, (screen.height() - self.height()) / 4)
        
        table = self.createTable() 
         
        # layout
        layout = QVBoxLayout()
        layout.addWidget(table) 
        self.setLayout(layout) 

    def get_table_data(self):
        #stdouterr = os.popen4(r"c:\cygwin\bin\df.exe -h -v")[1].read()
        stdouterr = os.popen4("total3.py")[1].read()
        lines = stdouterr.splitlines()
        lines = lines[4:]
        print "lines = ", lines
        lines = lines[:-1]
        self.tabledata = [re.split(r"\s+", line, 5)
                     for line in lines]

    def createTable(self):
        # create the view
        tv = QTableView()

        # set the table model
        header = ['No','Drive', 'Size', 'Used', 'Avail', 'Use (%)']
        tm = MyTableModel(self.tabledata, header, self) 
        tv.setModel(tm)

        # set the minimum size
        tv.setMinimumSize(200, 200)

        # hide grid
        tv.setShowGrid(True)

        # set the font
        font = QFont("Courier New", 8)
        tv.setFont(font)

        # hide vertical header
        vh = tv.verticalHeader()
        vh.setVisible(False)

        # set horizontal header properties
        hh = tv.horizontalHeader()
        hh.setStretchLastSection(True)

        # set column width to fit contents
        tv.resizeColumnsToContents()

        # set row height
        nrows = len(self.tabledata)
        for row in xrange(nrows):
            tv.setRowHeight(row, 18)

        # enable sorting
        tv.setSortingEnabled(True)

        return tv
 
class MyTableModel(QAbstractTableModel): 
    def __init__(self, datain, headerdata, parent=None, *args): 
        """ datain: a list of lists
            headerdata: a list of strings
        """
        QAbstractTableModel.__init__(self, parent, *args) 
        self.arraydata = datain
        self.headerdata = headerdata
 
    def rowCount(self, parent): 
        return len(self.arraydata) 
 
    def columnCount(self, parent): 
        return len(self.arraydata[0]) 
 
    def data(self, index, role): 
		#try:
		if not index.isValid(): 
			return QVariant() 
		elif role != Qt.DisplayRole: 
			return QVariant() 
		return QVariant(self.arraydata[index.row()][index.column()]) 
		#except IndexError, e:
		#	pass

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self.headerdata[col])
        return QVariant()

    def sort(self, Ncol, order):
        """Sort table by given column number.
        """
        self.emit(SIGNAL("layoutAboutToBeChanged()"))
        self.arraydata = sorted(self.arraydata, key=operator.itemgetter(Ncol))        
        if order == Qt.DescendingOrder:
            self.arraydata.reverse()
        self.emit(SIGNAL("layoutChanged()"))

if __name__ == "__main__": 
    main()
