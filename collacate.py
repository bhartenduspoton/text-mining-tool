# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'collacate.ui'
#
# Created: Fri Jul 29 23:21:14 2016
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
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(638, 364)
        self.toolButton = QtGui.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(10, 10, 81, 31))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.tableWidget = QtGui.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 60, 611, 251))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(11)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(2, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(2, 3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(2, 4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(2, 5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(2, 6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(2, 7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(3, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(3, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(3, 3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(3, 4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(3, 5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(3, 6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(3, 7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(4, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(4, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(4, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(4, 3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(4, 4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(4, 5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(4, 6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(4, 7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(5, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(5, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(5, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(5, 3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(5, 4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(5, 5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(5, 6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(5, 7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(6, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(6, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(6, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(6, 3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(6, 4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(6, 5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(6, 6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(6, 7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(7, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(7, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(7, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(7, 3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(7, 4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(7, 5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(7, 6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(7, 7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(8, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(8, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(8, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(8, 3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(8, 4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(8, 5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(8, 6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(8, 7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(9, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(9, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(9, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(9, 3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(9, 4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(9, 5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(9, 6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(9, 7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(10, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(10, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(10, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(10, 3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(10, 4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(10, 5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(10, 6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(10, 7, item)
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(110, 10, 501, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.progressBar = QtGui.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(130, 330, 311, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Collocate", None))
        self.toolButton.setText(_translate("Form", "Copy", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Word", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Count", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "L3", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "L2", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "L1", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "R3", None))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "R2", None))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "R1", None))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("Form", "a", None))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("Form", "1", None))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("Form", "1", None))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("Form", "0", None))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("Form", "0", None))
        item = self.tableWidget.item(0, 5)
        item.setText(_translate("Form", "0", None))
        item = self.tableWidget.item(0, 6)
        item.setText(_translate("Form", "0", None))
        item = self.tableWidget.item(0, 7)
        item.setText(_translate("Form", "0", None))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("Form", "ability", None))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("Form", "34", None))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("Form", "3", None))
        item = self.tableWidget.item(1, 3)
        item.setText(_translate("Form", "2", None))
        item = self.tableWidget.item(1, 4)
        item.setText(_translate("Form", "15", None))
        item = self.tableWidget.item(1, 5)
        item.setText(_translate("Form", "5", None))
        item = self.tableWidget.item(1, 6)
        item.setText(_translate("Form", "5", None))
        item = self.tableWidget.item(1, 7)
        item.setText(_translate("Form", "4", None))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("Form", "abash", None))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("Form", "5", None))
        item = self.tableWidget.item(2, 2)
        item.setText(_translate("Form", "2", None))
        item = self.tableWidget.item(2, 3)
        item.setText(_translate("Form", "1", None))
        item = self.tableWidget.item(2, 4)
        item.setText(_translate("Form", "1", None))
        item = self.tableWidget.item(2, 5)
        item.setText(_translate("Form", "1", None))
        item = self.tableWidget.item(2, 6)
        item.setText(_translate("Form", "0", None))
        item = self.tableWidget.item(2, 7)
        item.setText(_translate("Form", "0", None))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("Form", "accurate", None))
        item = self.tableWidget.item(3, 1)
        item.setText(_translate("Form", "4", None))
        item = self.tableWidget.item(3, 2)
        item.setText(_translate("Form", "2", None))
        item = self.tableWidget.item(3, 3)
        item.setText(_translate("Form", "1", None))
        item = self.tableWidget.item(3, 4)
        item.setText(_translate("Form", "0", None))
        item = self.tableWidget.item(3, 5)
        item.setText(_translate("Form", "0", None))
        item = self.tableWidget.item(3, 6)
        item.setText(_translate("Form", "0", None))
        item = self.tableWidget.item(3, 7)
        item.setText(_translate("Form", "1", None))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("Form", "amuse", None))
        item = self.tableWidget.item(4, 1)
        item.setText(_translate("Form", "45", None))
        item = self.tableWidget.item(4, 2)
        item.setText(_translate("Form", "41", None))
        item = self.tableWidget.item(4, 3)
        item.setText(_translate("Form", "1", None))
        item = self.tableWidget.item(4, 4)
        item.setText(_translate("Form", "1", None))
        item = self.tableWidget.item(4, 5)
        item.setText(_translate("Form", "1", None))
        item = self.tableWidget.item(4, 6)
        item.setText(_translate("Form", "1", None))
        item = self.tableWidget.item(4, 7)
        item.setText(_translate("Form", "1", None))
        item = self.tableWidget.item(5, 0)
        item.setText(_translate("Form", "bond", None))
        item = self.tableWidget.item(5, 1)
        item.setText(_translate("Form", "2", None))
        item = self.tableWidget.item(5, 2)
        item.setText(_translate("Form", "1", None))
        item = self.tableWidget.item(5, 3)
        item.setText(_translate("Form", "1", None))
        item = self.tableWidget.item(5, 4)
        item.setText(_translate("Form", "0", None))
        item = self.tableWidget.item(5, 5)
        item.setText(_translate("Form", "0", None))
        item = self.tableWidget.item(5, 6)
        item.setText(_translate("Form", "0", None))
        item = self.tableWidget.item(5, 7)
        item.setText(_translate("Form", "0", None))
        item = self.tableWidget.item(6, 0)
        item.setText(_translate("Form", "bash", None))
        item = self.tableWidget.item(6, 1)
        item.setText(_translate("Form", "34", None))
        item = self.tableWidget.item(6, 2)
        item.setText(_translate("Form", "23", None))
        item = self.tableWidget.item(6, 3)
        item.setText(_translate("Form", "1", None))
        item = self.tableWidget.item(6, 4)
        item.setText(_translate("Form", "1", None))
        item = self.tableWidget.item(6, 5)
        item.setText(_translate("Form", "12", None))
        item = self.tableWidget.item(6, 6)
        item.setText(_translate("Form", "23", None))
        item = self.tableWidget.item(6, 7)
        item.setText(_translate("Form", "0", None))
        item = self.tableWidget.item(7, 0)
        item.setText(_translate("Form", "bull", None))
        item = self.tableWidget.item(7, 1)
        item.setText(_translate("Form", "4", None))
        item = self.tableWidget.item(7, 2)
        item.setText(_translate("Form", "2", None))
        item = self.tableWidget.item(7, 3)
        item.setText(_translate("Form", "1", None))
        item = self.tableWidget.item(7, 4)
        item.setText(_translate("Form", "1", None))
        item = self.tableWidget.item(7, 5)
        item.setText(_translate("Form", "0", None))
        item = self.tableWidget.item(7, 6)
        item.setText(_translate("Form", "0", None))
        item = self.tableWidget.item(7, 7)
        item.setText(_translate("Form", "1", None))
        item = self.tableWidget.item(8, 0)
        item.setText(_translate("Form", "bolt", None))
        item = self.tableWidget.item(8, 1)
        item.setText(_translate("Form", "67", None))
        item = self.tableWidget.item(8, 2)
        item.setText(_translate("Form", "45", None))
        item = self.tableWidget.item(8, 3)
        item.setText(_translate("Form", "23", None))
        item = self.tableWidget.item(8, 4)
        item.setText(_translate("Form", "4", None))
        item = self.tableWidget.item(8, 5)
        item.setText(_translate("Form", "9", None))
        item = self.tableWidget.item(8, 6)
        item.setText(_translate("Form", "8", None))
        item = self.tableWidget.item(8, 7)
        item.setText(_translate("Form", "2", None))
        item = self.tableWidget.item(9, 0)
        item.setText(_translate("Form", "boss", None))
        item = self.tableWidget.item(9, 1)
        item.setText(_translate("Form", "11", None))
        item = self.tableWidget.item(9, 2)
        item.setText(_translate("Form", "8", None))
        item = self.tableWidget.item(9, 3)
        item.setText(_translate("Form", "1", None))
        item = self.tableWidget.item(9, 4)
        item.setText(_translate("Form", "1", None))
        item = self.tableWidget.item(9, 5)
        item.setText(_translate("Form", "1", None))
        item = self.tableWidget.item(9, 6)
        item.setText(_translate("Form", "0", None))
        item = self.tableWidget.item(9, 7)
        item.setText(_translate("Form", "2", None))
        item = self.tableWidget.item(10, 0)
        item.setText(_translate("Form", "cat", None))
        item = self.tableWidget.item(10, 1)
        item.setText(_translate("Form", "23", None))
        item = self.tableWidget.item(10, 2)
        item.setText(_translate("Form", "11", None))
        item = self.tableWidget.item(10, 3)
        item.setText(_translate("Form", "5", None))
        item = self.tableWidget.item(10, 4)
        item.setText(_translate("Form", "3", None))
        item = self.tableWidget.item(10, 5)
        item.setText(_translate("Form", "1", None))
        item = self.tableWidget.item(10, 6)
        item.setText(_translate("Form", "0", None))
        item = self.tableWidget.item(10, 7)
        item.setText(_translate("Form", "3", None))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.lineEdit.setText(_translate("Form", "/home/bhartendu/text-mining-tool/o89nsnjd.csv", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
