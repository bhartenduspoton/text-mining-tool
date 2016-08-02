# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ngram.ui'
#
# Created: Fri Jul 29 23:34:31 2016
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

    def __init__(self,data=None):
        self.lst = data
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(491, 579)
        self.tableWidget = QtGui.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(30, 50, 401, 501))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(2)
        print 'len',len(self.lst)
        self.tableWidget.setRowCount(len(self.lst))
        item = QtGui.QTableWidgetItem()

        for i in range(len(self.lst)):
            self.tableWidget.setVerticalHeaderItem(i, item)
            item = QtGui.QTableWidgetItem()

        # self.tableWidget.setVerticalHeaderItem(1, item)
        # item = QtGui.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(2, item)
        # item = QtGui.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(3, item)
        # item = QtGui.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(4, item)
        # item = QtGui.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(5, item)
        # item = QtGui.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(6, item)
        # item = QtGui.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(7, item)
        # item = QtGui.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(8, item)
        # item = QtGui.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(9, item)
        # item = QtGui.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(10, item)
        # item = QtGui.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(11, item)
        # item = QtGui.QTableWidgetItem()

        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()

        for i in range(len(self.lst)):
            self.tableWidget.setItem(i, 0, item)
            item = QtGui.QTableWidgetItem()
            self.tableWidget.setItem(i, 1, item)
            item = QtGui.QTableWidgetItem()
        # self.tableWidget.setItem(0, 0, item)
        # item = QtGui.QTableWidgetItem()
        # self.tableWidget.setItem(0, 1, item)
        # item = QtGui.QTableWidgetItem()
        # self.tableWidget.setItem(1, 0, item)
        # item = QtGui.QTableWidgetItem()
        # self.tableWidget.setItem(1, 1, item)
        # item = QtGui.QTableWidgetItem()
        # self.tableWidget.setItem(2, 0, item)
        # item = QtGui.QTableWidgetItem()
        # self.tableWidget.setItem(2, 1, item)
        # item = QtGui.QTableWidgetItem()
        # self.tableWidget.setItem(3, 0, item)
        # item = QtGui.QTableWidgetItem()
        # self.tableWidget.setItem(3, 1, item)
        # item = QtGui.QTableWidgetItem()
        # self.tableWidget.setItem(4, 0, item)
        # item = QtGui.QTableWidgetItem()
        # self.tableWidget.setItem(4, 1, item)
        # item = QtGui.QTableWidgetItem()
        # self.tableWidget.setItem(5, 0, item)
        # item = QtGui.QTableWidgetItem()
        # self.tableWidget.setItem(5, 1, item)
        # item = QtGui.QTableWidgetItem()
        # self.tableWidget.setItem(6, 0, item)
        # item = QtGui.QTableWidgetItem()
        # self.tableWidget.setItem(6, 1, item)
        # item = QtGui.QTableWidgetItem()
        # self.tableWidget.setItem(7, 0, item)
        # item = QtGui.QTableWidgetItem()
        # self.tableWidget.setItem(7, 1, item)
        # item = QtGui.QTableWidgetItem()
        # self.tableWidget.setItem(8, 0, item)
        # item = QtGui.QTableWidgetItem()
        # self.tableWidget.setItem(8, 1, item)
        # item = QtGui.QTableWidgetItem()
        # self.tableWidget.setItem(9, 0, item)
        # item = QtGui.QTableWidgetItem()
        # self.tableWidget.setItem(9, 1, item)
        # item = QtGui.QTableWidgetItem()
        # self.tableWidget.setItem(10, 0, item)
        # item = QtGui.QTableWidgetItem()
        # self.tableWidget.setItem(10, 1, item)
        # item = QtGui.QTableWidgetItem()
        # self.tableWidget.setItem(11, 0, item)
        # item = QtGui.QTableWidgetItem()
        # self.tableWidget.setItem(11, 1, item)

        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(198)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(108)
        self.tableWidget.verticalHeader().setMinimumSectionSize(8)
        self.toolButton = QtGui.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(30, 10, 91, 31))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(300, 10, 113, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Ngram", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Ngram", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Count", None))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        i = 0
        for kk in self.lst:
            #print kk
            #raw_input()
            item = self.tableWidget.item(i, 0)
            item.setText(_translate("Form", kk[0], None))
            item = self.tableWidget.item(i, 1)
            item.setText(_translate("Form", str(kk[1]), None))
            i = i+1

        # item = self.tableWidget.item(0, 0)
        # item.setText(_translate("Form", "a", None))
        # item = self.tableWidget.item(0, 1)
        # item.setText(_translate("Form", "1", None))
        # item = self.tableWidget.item(1, 0)
        # item.setText(_translate("Form", "bullying", None))
        # item = self.tableWidget.item(1, 1)
        # item.setText(_translate("Form", "2", None))
        # item = self.tableWidget.item(2, 0)
        # item.setText(_translate("Form", "cut", None))
        # item = self.tableWidget.item(2, 1)
        # item.setText(_translate("Form", "1", None))
        # item = self.tableWidget.item(3, 0)
        # item.setText(_translate("Form", "dull", None))
        # item = self.tableWidget.item(3, 1)
        # item.setText(_translate("Form", "1", None))
        # item = self.tableWidget.item(4, 0)
        # item.setText(_translate("Form", "error", None))
        # item = self.tableWidget.item(4, 1)
        # item.setText(_translate("Form", "1", None))
        # item = self.tableWidget.item(5, 0)
        # item.setText(_translate("Form", "digit", None))
        # item = self.tableWidget.item(5, 1)
        # item.setText(_translate("Form", "56", None))
        # item = self.tableWidget.item(6, 0)
        # item.setText(_translate("Form", "wash", None))
        # item = self.tableWidget.item(6, 1)
        # item.setText(_translate("Form", "5", None))
        # item = self.tableWidget.item(7, 0)
        # item.setText(_translate("Form", "sun", None))
        # item = self.tableWidget.item(7, 1)
        # item.setText(_translate("Form", "5", None))
        # item = self.tableWidget.item(8, 0)
        # item.setText(_translate("Form", "fat", None))
        # item = self.tableWidget.item(8, 1)
        # item.setText(_translate("Form", "4", None))
        # item = self.tableWidget.item(9, 0)
        # item.setText(_translate("Form", "saturday", None))
        # item = self.tableWidget.item(9, 1)
        # item.setText(_translate("Form", "34", None))
        # item = self.tableWidget.item(10, 0)
        # item.setText(_translate("Form", "monday", None))
        # item = self.tableWidget.item(10, 1)
        # item.setText(_translate("Form", "2", None))
        # item = self.tableWidget.item(11, 0)
        # item.setText(_translate("Form", "ractify", None))
        # item = self.tableWidget.item(11, 1)
        # item.setText(_translate("Form", "1", None))
        #self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.toolButton.setText(_translate("Form", "Copy", None))
        self.lineEdit.setPlaceholderText(_translate("Form", "search text...", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

