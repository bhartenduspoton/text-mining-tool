# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'keyword.ui'
#
# Created: Sat Jul 30 02:39:26 2016
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


class Ui_Form(object):
    def setupUi(self, Form,parse_type):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(477, 300)
        self.parse_type = parse_type
        self.checkBox = QtGui.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(270, 130, 161, 41))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.pushButton2_1 = QtGui.QPushButton(Form)
        self.pushButton2_1.setGeometry(QtCore.QRect(290, 30, 98, 27))
        self.pushButton2_1.setObjectName(_fromUtf8("pushButton2_1"))
        # self.pushButton2_2 = QtGui.QPushButton(Form)
        # self.pushButton2_2.setGeometry(QtCore.QRect(290, 70, 98, 27))
        # self.pushButton2_2.setObjectName(_fromUtf8("pushButton2_2"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(30, 30, 221, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Keyword", None))
        self.checkBox.setText(_translate("Form", "Regular Expression", None))
        self.pushButton2_1.setText(_translate("Form", "OK", None))
        #self.pushButton2_2.setText(_translate("Form", "Cancel", None))
        self.lineEdit.setPlaceholderText(_translate("Form", "Type words..", None))
        self.pushButton2_1.clicked.connect(self.accept)
        #self.pushButton2_2.clicked.connect(self.reject)

        print 'ressajsd'

    def accept(self):
        import concordance,collacate
        print 'accept'
        if self.parse_type == 1:
            self.Form = QtGui.QWidget()
            ui = concordance.Ui_Form()
            ui.setupUi(self.Form)
            self.Form.show()
        else:
            self.Form = QtGui.QWidget()
            ui = collacate.Ui_Form()
            ui.setupUi(self.Form)
            self.Form.show()
        pass

    def reject(self):
        print 'rejected'
        pass

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form,1)
    Form.show()
    sys.exit(app.exec_())

