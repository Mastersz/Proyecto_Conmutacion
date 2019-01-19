# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'anadirUsuario.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import ctypes

from PyQt5 import QtCore, QtWidgets
import selectorCredenciales
import funciones2

class Ui_AnadirUsuario(object):

    def addUsuario(self, AnadirUsuario, remote_conn):
        print("########################CODIGO ANADIR USUARIOS")
        print(type(remote_conn))
        if (self.txt_privilegio.text().isnumeric() and ((int(self.txt_privilegio.text())) <= 15)
                and self.txt_usuario.text() != "" and self.txt_contrasena.text() != ""):
            funciones2.conf_credencial(remote_conn, self.txt_usuario.text(),
                                       self.txt_contrasena.text(), self.txt_privilegio.text())
            ctypes.windll.user32.MessageBoxW(0, "Configuracion realizada con éxito", "éxito!", 0)
            self.atras(AnadirUsuario, remote_conn)
        else:
            ctypes.windll.user32.MessageBoxW(0, "Verifica los campos,"
                                                " asegúrese del valor de privilegio", "Error!!", 0)

    def atras(self, AnadirUsuario, remote_conn):
        self.SelectorCredenciales = QtWidgets.QDialog()
        self.ui = selectorCredenciales.Ui_SelectorCredenciales()
        self.ui.setupUi(self.SelectorCredenciales, remote_conn)
        self.SelectorCredenciales.show()
        AnadirUsuario.close()

    def setupUi(self, AnadirUsuario, remote_conn):
        AnadirUsuario.setObjectName("AnadirUsuario")
        AnadirUsuario.resize(375, 223)
        self.label = QtWidgets.QLabel(AnadirUsuario)
        self.label.setGeometry(QtCore.QRect(60, 50, 55, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(AnadirUsuario)
        self.label_2.setGeometry(QtCore.QRect(60, 90, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(AnadirUsuario)
        self.label_3.setGeometry(QtCore.QRect(60, 130, 55, 16))
        self.label_3.setObjectName("label_3")
        self.txt_usuario = QtWidgets.QLineEdit(AnadirUsuario)
        self.txt_usuario.setGeometry(QtCore.QRect(140, 50, 151, 22))
        self.txt_usuario.setObjectName("txt_usuario")
        self.txt_contrasena = QtWidgets.QLineEdit(AnadirUsuario)
        self.txt_contrasena.setGeometry(QtCore.QRect(140, 90, 151, 22))
        self.txt_contrasena.setObjectName("txt_contrasena")
        self.txt_privilegio = QtWidgets.QLineEdit(AnadirUsuario)
        self.txt_privilegio.setGeometry(QtCore.QRect(140, 130, 151, 22))
        self.txt_privilegio.setObjectName("txt_privilegio")
        self.btn_anadir = QtWidgets.QPushButton(AnadirUsuario)
        self.btn_anadir.setGeometry(QtCore.QRect(80, 180, 93, 28))
        self.btn_anadir.setObjectName("btn_anadir")
        self.btn_atras = QtWidgets.QPushButton(AnadirUsuario)
        self.btn_atras.setGeometry(QtCore.QRect(210, 180, 93, 28))
        self.btn_atras.setObjectName("btn_atras")
        self.retranslateUi(AnadirUsuario)
        QtCore.QMetaObject.connectSlotsByName(AnadirUsuario)
        ##################################################################

        self.btn_atras.clicked.connect(lambda: self.atras(AnadirUsuario, remote_conn))
        self.btn_anadir.clicked.connect(lambda: self.addUsuario(AnadirUsuario, remote_conn))

    def retranslateUi(self, AnadirUsuario):
        _translate = QtCore.QCoreApplication.translate
        AnadirUsuario.setWindowTitle(_translate("AnadirUsuario", "Form"))
        self.label.setText(_translate("AnadirUsuario", "Usuario"))
        self.label_2.setText(_translate("AnadirUsuario", "Contraseña"))
        self.label_3.setText(_translate("AnadirUsuario", "Privilegio"))
        self.btn_anadir.setText(_translate("AnadirUsuario", "Añadir"))
        self.btn_atras.setText(_translate("AnadirUsuario", "Atras"))

