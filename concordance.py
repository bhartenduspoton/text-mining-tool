# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'concordance.ui'
#
# Created: Fri Jul 29 23:22:55 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import  pyqtSignal,pyqtSlot

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
        Form.resize(519, 474)
        self.tableWidget = QtGui.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 40, 481, 391))
        self.tableWidget.setMaximumSize(QtCore.QSize(481, 16777215))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(13)
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
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setKerning(True)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(2, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(2, 3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(3, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(3, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(3, 3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(4, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(4, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(4, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(4, 3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(5, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(5, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(5, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(5, 3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(6, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(6, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(6, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(6, 3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(7, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(7, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(7, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(7, 3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(8, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(8, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(8, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(8, 3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(9, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(9, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(9, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(9, 3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(10, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(10, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(10, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(10, 3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(11, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(11, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(11, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(11, 3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(12, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(12, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(12, 3, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(126)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(200)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.progressBar = QtGui.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(80, 440, 281, 23))
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.toolButton = QtGui.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(10, 10, 121, 25))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(152, 10, 331, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Concordance", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Line", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Left", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Key", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Right", None))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("Form", "1", None))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("Form", "1 more than", None))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("Form", "number", None))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("Form", "some things right", None))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("Form", "2", None))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("Form", "more than ", None))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("Form", "number", None))
        item = self.tableWidget.item(1, 3)
        item.setText(_translate("Form", "every", None))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("Form", "5", None))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("Form", "one", None))
        item = self.tableWidget.item(2, 2)
        item.setText(_translate("Form", "number", None))
        item = self.tableWidget.item(2, 3)
        item.setText(_translate("Form", "two", None))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("Form", "8", None))
        item = self.tableWidget.item(3, 1)
        item.setText(_translate("Form", "three", None))
        item = self.tableWidget.item(3, 2)
        item.setText(_translate("Form", "number", None))
        item = self.tableWidget.item(3, 3)
        item.setText(_translate("Form", "four", None))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("Form", "11", None))
        item = self.tableWidget.item(4, 1)
        item.setText(_translate("Form", "ram is ", None))
        item = self.tableWidget.item(4, 2)
        item.setText(_translate("Form", "number", None))
        item = self.tableWidget.item(4, 3)
        item.setText(_translate("Form", "climbing", None))
        item = self.tableWidget.item(5, 0)
        item.setText(_translate("Form", "19", None))
        item = self.tableWidget.item(5, 1)
        item.setText(_translate("Form", "set", None))
        item = self.tableWidget.item(5, 2)
        item.setText(_translate("Form", "number", None))
        item = self.tableWidget.item(5, 3)
        item.setText(_translate("Form", "fire", None))
        item = self.tableWidget.item(6, 0)
        item.setText(_translate("Form", "20", None))
        item = self.tableWidget.item(6, 1)
        item.setText(_translate("Form", "high", None))
        item = self.tableWidget.item(6, 2)
        item.setText(_translate("Form", "number", None))
        item = self.tableWidget.item(6, 3)
        item.setText(_translate("Form", "five", None))
        item = self.tableWidget.item(7, 0)
        item.setText(_translate("Form", "21", None))
        item = self.tableWidget.item(7, 1)
        item.setText(_translate("Form", "sit", None))
        item = self.tableWidget.item(7, 2)
        item.setText(_translate("Form", "number", None))
        item = self.tableWidget.item(7, 3)
        item.setText(_translate("Form", "on the chair", None))
        item = self.tableWidget.item(8, 0)
        item.setText(_translate("Form", "25", None))
        item = self.tableWidget.item(8, 1)
        item.setText(_translate("Form", "never", None))
        item = self.tableWidget.item(8, 2)
        item.setText(_translate("Form", "number", None))
        item = self.tableWidget.item(8, 3)
        item.setText(_translate("Form", "again", None))
        item = self.tableWidget.item(9, 0)
        item.setText(_translate("Form", "26", None))
        item = self.tableWidget.item(9, 1)
        item.setText(_translate("Form", "you", None))
        item = self.tableWidget.item(9, 2)
        item.setText(_translate("Form", "number", None))
        item = self.tableWidget.item(9, 3)
        item.setText(_translate("Form", "are good", None))
        item = self.tableWidget.item(10, 0)
        item.setText(_translate("Form", "27", None))
        item = self.tableWidget.item(10, 1)
        item.setText(_translate("Form", "good ", None))
        item = self.tableWidget.item(10, 2)
        item.setText(_translate("Form", "number", None))
        item = self.tableWidget.item(10, 3)
        item.setText(_translate("Form", "fellas", None))
        item = self.tableWidget.item(11, 0)
        item.setText(_translate("Form", "28", None))
        item = self.tableWidget.item(11, 1)
        item.setText(_translate("Form", "all is ", None))
        item = self.tableWidget.item(11, 2)
        item.setText(_translate("Form", "number", None))
        item = self.tableWidget.item(11, 3)
        item.setText(_translate("Form", "well", None))
        item = self.tableWidget.item(12, 1)
        item.setText(_translate("Form", "good", None))
        item = self.tableWidget.item(12, 2)
        item.setText(_translate("Form", "number", None))
        item = self.tableWidget.item(12, 3)
        item.setText(_translate("Form", "bad", None))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.toolButton.setText(_translate("Form", "Copy", None))
        self.toolButton.clicked.connect(self.copy)
        self.lineEdit.setText(_translate("Form", "/home/bhartendu/text-mining-tool/order13.csv", None))

    @pyqtSlot()
    def copy(self):
        print 'copy'

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
