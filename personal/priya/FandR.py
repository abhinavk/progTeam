# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FindAndReplace.ui'
#
# Created: Sat Mar 22 16:05:37 2014
#      by: PyQt4 UI code generator 4.10
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

class Ui_Find(object):
    def setupUi(self, Find):
        Find.setObjectName(_fromUtf8("Find"))
        Find.resize(504, 234)
        Find.setAutoFillBackground(False)
        Find.setSizeGripEnabled(False)
        Find.setModal(False)
        self.horizontalLayout_5 = QtGui.QHBoxLayout(Find)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.Plk = QtGui.QPlainTextEdit(Find)
        self.Plk.setObjectName(_fromUtf8("Plk"))
        self.gridLayout.addWidget(self.Plk, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(Find)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.textEdit = QtGui.QTextEdit(Find)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout.addWidget(self.textEdit, 1, 1, 1, 1)
        self.label = QtGui.QLabel(Find)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.checkBox = QtGui.QCheckBox(Find)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.horizontalLayout_2.addWidget(self.checkBox)
        self.checkBox_2 = QtGui.QCheckBox(Find)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.horizontalLayout_2.addWidget(self.checkBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(Find)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.comboBox = QtGui.QComboBox(Find)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem = QtGui.QSpacerItem(20, 28, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.line = QtGui.QFrame(Find)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout_5.addWidget(self.line)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.pushButton = QtGui.QPushButton(Find)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(Find)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtGui.QPushButton(Find)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.verticalLayout_2.addWidget(self.pushButton_3)
        spacerItem1 = QtGui.QSpacerItem(20, 78, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.pushButton_4 = QtGui.QPushButton(Find)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.retranslateUi(Find)
        QtCore.QMetaObject.connectSlotsByName(Find)

    def retranslateUi(self, Find):
        Find.setWindowTitle(_translate("Find", "Find and replace", None))
        self.label_2.setText(_translate("Find", "Replace with", None))
        self.label.setText(_translate("Find", "Find what", None))
        self.checkBox.setText(_translate("Find", "Match Case", None))
        self.checkBox_2.setText(_translate("Find", "Whole words", None))
        self.label_3.setText(_translate("Find", "Syntax", None))
        self.comboBox.setItemText(0, _translate("Find", "Literal Text ", None))
        self.comboBox.setItemText(1, _translate("Find", "Regular Expression", None))
        self.pushButton.setText(_translate("Find", "Find", None))
        self.pushButton_2.setText(_translate("Find", "Replace", None))
        self.pushButton_3.setText(_translate("Find", "Replace All", None))
        self.pushButton_4.setText(_translate("Find", "Close", None))

