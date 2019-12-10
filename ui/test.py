# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(206, 105)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn01 = QtWidgets.QPushButton(Form)
        self.btn01.setObjectName("btn01")
        self.verticalLayout.addWidget(self.btn01)
        self.btn02 = QtWidgets.QPushButton(Form)
        self.btn02.setObjectName("btn02")
        self.verticalLayout.addWidget(self.btn02)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "testfrom"))
        self.btn01.setText(_translate("Form", "btn01"))
        self.btn02.setText(_translate("Form", "btn02"))

