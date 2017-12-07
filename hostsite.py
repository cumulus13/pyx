import os
import sys
import MySQLdb
from PyQt4 import QtGui, QtCore
import time
import traceback

filename = os.path.split(sys.argv[0])[1]
usage = "\t Use " + filename + """ [add|del|gui] [name of site] 
         example : """ + filename + """ www.example.com
"""
usage_gui = "insert name of vhost to database, name of vhost will add\n\nautomatic,it same with command \"addvhost [name of vhost] \"\nexample : www.host.com"

class DError(QtGui.QDialog):
    def __init__(self, info=None, data=None, parent=None):
        #QtGui.QDialog.__init__(self)
        super(DError, self).__init__(parent)
        self.info = info
        self.data = data

        if os.getcwd() == os.path.split(sys.argv[0])[0]:
            if "pyx" in os.path.split(sys.argv[0])[0]:
                mypath = os.path.split(sys.argv[0])[0] + "/images/"
            else:
                mypath = os.path.split(sys.argv[0])[0] + "d:/pyx/images/"
        else:
            if "d:/" in os.getcwd():
                if "pyx" in os.getcwd():
                    mypath = os.getcwd() + '/images/' 
                else:
                    mypath = 'd:/pyx/images/' 
            else:
                mypath = 'd:/pyx/images/' 

        #print "mypath = ", mypath                #for test only
        #print "os.getcwd() = ", os.getcwd()      #for test only
        #print "sys.argv[0] = ", sys.argv[0]      #for test only

        self.setGeometry(300, 300, 550, 350)
        self.setFixedSize(500, 350)
        self.setWindowTitle(str(self.info))
        self.setWindowIcon(QtGui.QIcon(mypath + str(self.info) + '2.png'))

        self.btOK = QtGui.QPushButton('Close', self)
        self.btOK.setFocusPolicy(QtCore.Qt.NoFocus)

        self.btOK.move(225, 310)
        self.connect(self.btOK, QtCore.SIGNAL('clicked()'), QtCore.SLOT('close()'))
        self.setFocus()

        self.img_label = QtGui.QLabel(self)
        self.img_label.setMinimumSize(50, 50)
        self.img_label.setGeometry(5, 5, 50, 50)
        self.img_info = QtGui.QImage(mypath + str(self.info) + '2.png')
        self.img_label.setPixmap(QtGui.QPixmap.fromImage(self.img_info))

        self.label = QtGui.QTextEdit(self)
        self.label.setGeometry(70, 10, 420, 280)
        self.label.setFont(QtGui.QFont('Arial',15, 500))
        self.label.setText(str(self.data))
        self.label.setBackgroundRole(QtGui.QPalette.Dark)
        self.label.setAutoFillBackground(True)
        self.label.setReadOnly(True)
        #self.label.setHtml(text)

        self.center()

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

class gui(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self)
        #super(gui, self).__init__(parent)


        self.setGeometry(300, 300, 400, 200)
        self.setFixedSize(400, 200)
        self.setWindowTitle("AddVhost Gui")
        self.setWindowIcon(QtGui.QIcon("addvhost.png"))

        self.head = QtGui.QLabel(self)
        self.head.setGeometry(120, 10, 200, 20)
        self.head.setText("AddVhost Gui")
        self.head.setFont(QtGui.QFont("Arial", 15, 600))

        self.inputName = QtGui.QLineEdit(self)
        self.inputName.setText("www.")
        self.inputName.setGeometry(100, 50, 230, 20)


        self.namevhost = QtGui.QLabel(self)
        self.namevhost.setGeometry(5, 50, 100, 20)
        self.namevhost.setText("Name Of Vhost : ")
        self.namevhost.setFont(QtGui.QFont("arial", 9, 600))

        self.bt_add = QtGui.QPushButton(self)
        self.bt_add.setText("Add")
        self.bt_add.setGeometry(340, 50, 50, 20)
        self.bt_add.connect(self.bt_add, QtCore.SIGNAL('clicked()'), self.add)

        self.bt_del = QtGui.QPushButton(self)
        self.bt_del.setText("Del")
        self.bt_del.setGeometry(340, 70, 50, 20)
        self.bt_del.connect(self.bt_del, QtCore.SIGNAL('clicked()'), self.delete)

        #self.bt_chA = QtGui.QRadioButton(self)
        #self.bt_chA.setGeometry(170,70,50,20)
        #self.bt_chA.setText("Add")
        #self.connect(self.bt_chA, QtCore.SIGNAL("triggered()"), self.ch_bt_text)

        #self.bt_chB = QtGui.QRadioButton(self)
        #self.bt_chB.setGeometry(240,70,50,20)
        #self.bt_chB.setText("Del")
        #self.connect(self.bt_chA, QtCore.SIGNAL("triggered()"), self.ch_bt_text)


        self.set_center

        self.info = QtGui.QGroupBox(self)
        self.info.setGeometry(10,95,380,95)

        self.infoimg_label = QtGui.QLabel(self.info)
        self.infoimg_label.setGeometry(5,5,50,50)
        self.info_img = QtGui.QImage(r"d:\pyx\addvhost_info.png")
        self.infoimg_label.setPixmap(QtGui.QPixmap.fromImage(self.info_img))

        self.infost = QtGui.QLabel(self.info)
        self.infost.setGeometry(100,70,200,20)
        self.infost.setText("")
        self.infost.setFont(QtGui.QFont("Arial",13,600,True))

        self.info_text = QtGui.QLabel(self.info)
        self.info_text.setGeometry(60,5,300,60)
        self.info_text.setText("insert name of vhost to database, name of vhost will add\n\nautomatic,it same with command \"addvhost [name of vhost] \"")


    def set_center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()

    def show_error(self, info, data):
        myapp = DError(info, data, self)
        myapp.show()
        del(myapp)
        #self.inputName.setText("www.")
        #self.infost.setText(" ")

    def clear(self):
        if self.inputName.isChecked == True:
            self.bt_add.setText("Add")
        elif self.bt_chB.isChecked == True:
            self.bt_add.setText("Del")
        else:
            self.bt_add.setText("XXX")

    def add(self):
        try:
            db = MySQLdb.connect("localhost", "root", "blackid", "mysite")
            cursor = db.cursor()
            datax = str(self.inputName.text)
            if len(datax) > 1 :
                sql = "insert into site(site) values('" + str(self.inputName.text()) + "')"
                cursor.execute(sql)
                db.commit()
                db.close()
                self.infost.setText("vhost successfull added !")
                #time.sleep(10)
                #self.infost.setText(" ")
                self.inputName.setText("www.")
            else:
                self.show_error('error',usage_gui)

        except MySQLdb.DatabaseError, e:
            if "Duplicate" in e[1]:
                self.infost.setText("vhost has been added !")
                self.show_error('error','Vhost has been added !')
                #time.sleep(5)
                self.inputName.setText("www.")
                #self.infost.setText(" ")
            else:
                pass
            
        except:
            self.infost.setText("vhost failed to added !")
            data_error = traceback.format_exc()            
            self.show_error('error',str(data_error))

    def delete(self):
        try:
            db = MySQLdb.connect("localhost", "root", "blackid", "mysite")
            cursor = db.cursor()
            datax = str(self.inputName.text)
            if len(datax) > 1 :
                #sql = "insert into site(site) values('" + str(self.inputName.text()) + "')"
                sql = "delete from site where site = '" + str(self.inputName.text()) + "'"
                cursor.execute(sql)
                db.commit()
                db.close()
                self.infost.setText("vhost successfull delete !")
                #time.sleep(10)
                #self.infost.setText(" ")
                self.inputName.setText("www.")
            else:
                self.show_error('error',usage_gui)

        except:
            self.infost.setText("vhost failed to delete !")
            data_error = traceback.format_exc()            
            self.show_error('error',str(data_error))
            #time.sleep(10)
            #self.infost.setText(" ")

def add(data):
    try:
        db = MySQLdb.connect("localhost", "root", "blackid", "mysite")
        cursor = db.cursor()

        if len(sys.argv) > 1:
            sql = "insert into site(site) values('www." + str(data) + "')"
            cursor.execute(sql)
            db.commit()
            db.close()
            print "\t Host succesfull addded ! \n"
        else:
            os.system('cls')
            print "\n"
            print usage
            sys.exit()

    except IndexError, e:
        os.system('cls')
        print "\n"
        print "\t ERROR = " + str(e)
        sys.exit()

    except MySQLdb.DatabaseError, e:
        if "Duplicate" in e[1]:
            print "\n"
            print "\t Vhost has been added ! \n"
        else:
            pass
            
def delete(data):
        try:
            db = MySQLdb.connect("localhost", "root", "blackid", "mysite")
            cursor = db.cursor()
            if len(data) > 1 :
                sql = "delete from site where site = '" + str(data) + "'"
                cursor.execute(sql)
                db.commit()
                db.close()
                print "\tvhost successfull delete !\n"
            else:
                self.show_error('error',usage_gui)

        except:
            print "\t vhost failed to delete !"
            data_error = traceback.format_exc()            
            print "\t ERROR : "
            print "\t" + str(data_error)


if __name__ == '__main__':
    try:
        if sys.argv[1:]:
            if sys.argv[1] == 'gui':
                app = QtGui.QApplication(sys.argv)
                myapp = gui()
                myapp.show()
                app.exec_()
            elif sys.argv[1] == 'gui':
                app = QtGui.QApplication(sys.argv)
                myapp = gui()
                myapp.show()
                app.exec_()
            elif sys.argv[1] =='add':
                add(sys.argv[2])
            elif sys.argv[1] =='del':
                delete(sys.argv[2])
            elif sys.argv[1] == "delele":
                delete(sys.argv[2])
            else:
                print "\n"
                print "\t " + usage
        else:
            add()
    except IndexError, e:
        print "\t ERROR = ", str(e)