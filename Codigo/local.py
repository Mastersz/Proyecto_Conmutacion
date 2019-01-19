# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\carlo\Desktop\ProyectoCE\GUI\local.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import ctypes

import serial
from PyQt5 import QtCore, QtGui, QtWidgets
from selectorLocal import Ui_SelectorLocal
import funciones_com
class Ui_local(object):

    def showSelectorLocal(self,remote_conn):
        self.selectorLocal = QtWidgets.QDialog()
        self.ui = Ui_SelectorLocal()
        self.ui.setupUi(self.selectorLocal, remote_conn)
        self.selectorLocal.show()

    def conectarLocal(self,Form, puerto):
        print("aquii")
        if (puerto=="COM1"):
            puerto="COM5"
        print(puerto)
        ser = funciones_com.login_com(puerto)
        ###################################AQUI VA EL CODIGO TUYO###################
        print(ser)
        if (ser==None):
            ctypes.windll.user32.MessageBoxW(0, "Conexion no establecida",
                                             "Error", 0)
        else:
            self.showSelectorLocal(ser)

        Form.close()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(283, 157)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 40, 55, 21))
        self.label_2.setObjectName("label_2")
        self.btn_conectar = QtWidgets.QPushButton(Form)
        self.btn_conectar.setGeometry(QtCore.QRect(100, 110, 93, 28))
        self.btn_conectar.setObjectName("btn_conectar")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(140, 40, 73, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("COM1")
        self.comboBox.addItem("COM2")
        self.comboBox.addItem("COM2")
        self.comboBox.addItem("COM2")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        ########################################################
        self.btn_conectar.clicked.connect(lambda: self.conectarLocal(Form, self.comboBox.currentText()))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Port"))
        self.btn_conectar.setText(_translate("Form", "Conectar"))
        self.comboBox.setItemText(0, _translate("Form", "COM1"))
        self.comboBox.setItemText(1, _translate("Form", "COM2"))
        self.comboBox.setItemText(2, _translate("Form", "SERIAL"))
        self.comboBox.setItemText(3, _translate("Form", "USB"))

