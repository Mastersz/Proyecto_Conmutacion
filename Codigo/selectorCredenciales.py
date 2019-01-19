# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectorCredenciales.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import ctypes

from PyQt5 import QtCore, QtWidgets

import anadirUsuario
import configuracionBasica
import funciones2
import time


class Ui_SelectorCredenciales(object):

    """Hace el llamado a un método que devuelve los usuarios existentes en el router y los muestra en pantalla"""
    def verUsuarios(self,remote_conn):
        funciones2.back_home(remote_conn)
        lista=funciones2.sh_usernames(remote_conn)
        time.sleep(2)

        print("AQUIIIIIIIIIIIIIIIII")
        print(lista)

        ctypes.windll.user32.MessageBoxW(0,lista ,
                                         "Información usuarios", 0)

    """Valida el tipo de dato de los campos de texto y si todo es correcto añade un usuario al enrutador mediante otra función."""
    def showAnadirUsuario(self,SelectorCredenciales,remote_conn):
        print("here 1")
        self.AnadirUsuario = QtWidgets.QDialog()
        self.ui = anadirUsuario.Ui_AnadirUsuario()
        self.ui.setupUi(self.AnadirUsuario,remote_conn)
        self.AnadirUsuario.show()
        SelectorCredenciales.close()

    def atras(self,SelectorCredenciales,remote_conn):
        self.configuracionBasica = QtWidgets.QDialog()
        self.ui = configuracionBasica.Ui_ConfiguracionBasica()
        self.ui.setupUi(self.configuracionBasica,remote_conn)
        self.configuracionBasica.show()
        SelectorCredenciales.close()



    def setupUi(self, SelectorCredenciales, remote_conn):
        SelectorCredenciales.setObjectName("SelectorCredenciales")
        SelectorCredenciales.resize(343, 157)
        self.btn_anadirUsuario = QtWidgets.QPushButton(SelectorCredenciales)
        self.btn_anadirUsuario.setGeometry(QtCore.QRect(60, 50, 93, 28))
        self.btn_anadirUsuario.setObjectName("btn_anadirUsuario")
        self.btn_verUsuarios = QtWidgets.QPushButton(SelectorCredenciales)
        self.btn_verUsuarios.setGeometry(QtCore.QRect(200, 50, 93, 28))
        self.btn_verUsuarios.setObjectName("btn_verUsuarios")
        self.btn_atras = QtWidgets.QPushButton(SelectorCredenciales)
        self.btn_atras.setGeometry(QtCore.QRect(130, 100, 93, 28))
        self.btn_atras.setObjectName("btn_atras")
        self.retranslateUi(SelectorCredenciales)
        QtCore.QMetaObject.connectSlotsByName(SelectorCredenciales)

        #######################################################################
        self.btn_anadirUsuario.clicked.connect(lambda : self.showAnadirUsuario(SelectorCredenciales,remote_conn))
        self.btn_verUsuarios.clicked.connect(lambda : self.verUsuarios(remote_conn))
        self.btn_atras.clicked.connect(lambda : self.atras(SelectorCredenciales,remote_conn))




    def retranslateUi(self, SelectorCredenciales):
        _translate = QtCore.QCoreApplication.translate
        SelectorCredenciales.setWindowTitle(_translate("SelectorCredenciales", "Form"))
        self.btn_anadirUsuario.setText(_translate("SelectorCredenciales", "Añadir usuario"))
        self.btn_verUsuarios.setText(_translate("SelectorCredenciales", "Ver usuarios"))
        self.btn_atras.setText(_translate("SelectorCredenciales", "Atras"))

