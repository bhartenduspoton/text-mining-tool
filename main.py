# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Fri Jul 29 23:48:33 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

from ngram_bhartendu import get_ngram
import word_list
import ngram
import keyword
import concordance,collacate


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(780, 380)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 131, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 10, 141, 27))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 10, 121, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(430, 10, 121, 27))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(560, 10, 131, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 90, 101, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(200, 90, 111, 27))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(17, 60, 671, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(22, 170, 661, 27))
        self.lineEdit_2.setMaxLength(8)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(440, 90, 71, 27))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 90, 51, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.checkBox = QtGui.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(580, 90, 97, 22))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Ngram Tool", None))
        self.pushButton.setText(_translate("MainWindow", "Concordance", None))
        self.pushButton_3.setText(_translate("MainWindow", "WordList", None))
        self.pushButton_2.setText(_translate("MainWindow", "Collocate", None))
        self.pushButton_4.setText(_translate("MainWindow", "Ngram", None))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "search text", None))
        self.label.setText(_translate("MainWindow", "Corpus file", None))
        self.pushButton_5.setText(_translate("MainWindow", "Browse", None))
        self.pushButton_5.clicked.connect(self.getfiles)
        #self.pushButton.clicked.connect(self.concordance)
        self.pushButton.clicked.connect(self.keyword_concordance)
        self.pushButton_4.clicked.connect(self.keyword_ngram2)
        self.pushButton_2.clicked.connect(self.keyword_collacate)
        self.pushButton_3.clicked.connect(self.word_list)


        self.comboBox.setItemText(0, _translate("MainWindow", "2", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "3", None))
        self.label_2.setText(_translate("MainWindow", "N-gram", None))

        self.checkBox.setText(_translate("MainWindow", "Stopword", None))

    def getfiles(self):
        dlg = QtGui.QFileDialog()
        dlg.setFileMode(QtGui.QFileDialog.AnyFile)
        dlg.setFilter("Text files (*.txt)")
        #filenames = QStringList()
        if dlg.exec_():
            selected_filenames = dlg.selectedFiles()
            for filename in selected_filenames:
                print type(filename),str(filename)
                self.filename1 = str(filename)
                break
        self.lineEdit_2.setText(_translate("MainWindow", str(selected_filenames[0]), None))


    def keyword(self):
        print 'in corcodance'
        #sending_button = self.sender().text()
        #print self.button.text()
        #self.status_label.setText('%s Clicked!' % str(sending_button.objectName()))
        #app = QtGui.QApplication(sys.argv)
        self.Form_keyword = QtGui.QWidget()
        ui = keyword.Ui_Form()
        ui.setupUi(self.Form_keyword)
        self.Form_keyword.show()
        print 'out concordance'
        self.Form = QtGui.QWidget()
        ui = concordance.Ui_Form()
        ui.setupUi(self.Form)
        self.Form.show()

    def keyword_concordance(self):
        print 'in corcodance'
        #sending_button = self.sender().text()
        #print self.button.text()
        #self.status_label.setText('%s Clicked!' % str(sending_button.objectName()))
        #app = QtGui.QApplication(sys.argv)
        self.Form_concordance = QtGui.QWidget()
        ui = keyword.Ui_Form()
        ui.setupUi(self.Form_concordance,1)
        self.Form_concordance.show()
        #keyword.keyword_main(1)
        print 'out concordance'
        self.Form_concordance = QtGui.QWidget()
        ui = concordance.Ui_Form()
        ui.setupUi(self.Form_concordance)
        self.Form_concordance.show()

    def keyword_collacate(self):
        print 'in keyword_collacate'
        #sending_button = self.sender().text()
        #print self.button.text()
        #self.status_label.setText('%s Clicked!' % str(sending_button.objectName()))
        #app = QtGui.QApplication(sys.argv)

        # self.Form_collocate = QtGui.QWidget()
        # ui = keyword.Ui_Form()
        # ui.setupUi(self.Form_collocate,2)
        # self.Form_collocate.show()
        # print 'out concordance'
        self.Form_collocate = QtGui.QWidget()
        ui = collacate.Ui_Form()
        ui.setupUi(self.Form_collocate)
        self.Form_collocate.show()

    def keyword_ngram2(self):
        print 'in keyword_ngram2'
        #sending_button = self.sender().text()
        #print self.button.text()
        #self.status_label.setText('%s Clicked!' % str(sending_button.objectName()))
        #app = QtGui.QApplication(sys.argv)
        print self.filename1
        is_stopword = 1
        if self.checkBox.isChecked():
            is_stopword = 1
        else:
            is_stopword = 0
        text = str(self.comboBox.currentText())
        print 'seleceted',text
        n_text= int(text)
        lst = get_ngram(self.filename1 ,n_text,is_stopword)
        self.Form_nrgram = QtGui.QWidget()
        ui = ngram.Ui_Form(lst)
        ui.setupUi(self.Form_nrgram)
        self.Form_nrgram.show()
        print 'out concordance'


    def word_list(self):
        self.Form_word_list = QtGui.QWidget()
        ui = word_list.Ui_Form()
        ui.setupUi(self.Form_word_list)
        self.Form_word_list.show()
        print 'out concordance'




if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    #Form = QtGui.QWidget()
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

