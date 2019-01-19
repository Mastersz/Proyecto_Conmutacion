# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'agregarCliente.ui'
# Created by: PyQt5 UI code generator 5.9.2

from PyQt5 import QtCore, QtWidgets
import ConfigurarPE2
import funciones2

class Ui_AgregarCliente(object):

    def atras(self, Form, remote_conn):
        self.configurarPE2 = QtWidgets.QDialog()
        self.ui = ConfigurarPE2.Ui_ConfigurarPE2()
        self.ui.setupUi(self.configurarPE2, remote_conn)
        self.configurarPE2.show()
        Form.close()

    def add_import(self, remote_conn, vrf, vlan):
        funciones2.add_import(remote_conn, vrf, vlan)

    def setupUi(self, AgregarCliente, remote_conn):
        AgregarCliente.setObjectName("AgregarCliente")
        AgregarCliente.resize(478, 207)
        self.btn_anadir = QtWidgets.QPushButton(AgregarCliente)
        self.btn_anadir.setGeometry(QtCore.QRect(120, 150, 93, 28))
        self.btn_anadir.setObjectName("btn_anadir")
        self.btn_atras = QtWidgets.QPushButton(AgregarCliente)
        self.btn_atras.setGeometry(QtCore.QRect(280, 150, 93, 28))
        self.btn_atras.setObjectName("btn_atras")
        self.label = QtWidgets.QLabel(AgregarCliente)
        self.label.setGeometry(QtCore.QRect(80, 40, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(AgregarCliente)
        self.label_2.setGeometry(QtCore.QRect(80, 90, 71, 16))
        self.label_2.setObjectName("label_2")
        self.txt_nombreVrf = QtWidgets.QLineEdit(AgregarCliente)
        self.txt_nombreVrf.setGeometry(QtCore.QRect(182, 40, 151, 22))
        self.txt_nombreVrf.setObjectName("txt_nombreVrf")
        self.txt_vlan = QtWidgets.QLineEdit(AgregarCliente)
        self.txt_vlan.setGeometry(QtCore.QRect(182, 90, 151, 22))
        self.txt_vlan.setObjectName("txt_vlan")
        self.retranslateUi(AgregarCliente)
        QtCore.QMetaObject.connectSlotsByName(AgregarCliente)
        ################################################################
        self.btn_atras.clicked.connect(lambda: self.atras(AgregarCliente, remote_conn))
        self.btn_anadir.clicked.connect(
            lambda: self.add_import(remote_conn, self.txt_nombreVrf.text(), self.txt_vlan.text()))

    def retranslateUi(self, AgregarCliente):
        _translate = QtCore.QCoreApplication.translate
        AgregarCliente.setWindowTitle(_translate("AgregarCliente", "Form"))
        self.btn_anadir.setText(_translate("AgregarCliente", "Añadir"))
        self.btn_atras.setText(_translate("AgregarCliente", "Atras"))
        self.label.setText(_translate("AgregarCliente", "Nombre VRF"))
        self.label_2.setText(_translate("AgregarCliente", "Vlan"))
