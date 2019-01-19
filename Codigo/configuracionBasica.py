# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'configuracionBasica.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
import selectorCredenciales
import direccionamientoLocal
import selectorLocal
from plantilla import Ui_Plantilla


class Ui_ConfiguracionBasica(object):
    """Esta función permite la navegación entre ventanas,
    creando la instancia de la ventana y mostrándola en pantalla."""
    def showPlantilla(self, Form, remote_conn):
        self.plantilla = QtWidgets.QDialog()
        self.ui = Ui_Plantilla()
        self.ui.setupUi(self.plantilla, remote_conn)
        self.plantilla.show()
        Form.close()

    """Esta función permite la navegación entre ventanas,
     creando la instancia de la ventana y mostrándola en pantalla."""
    def showSelectorCredenciales(self, Form, remote_conn):
        self.selectorCredenciales = QtWidgets.QDialog()
        self.ui = selectorCredenciales.Ui_SelectorCredenciales()
        self.ui.setupUi(self.selectorCredenciales, remote_conn)
        self.selectorCredenciales.show()
        Form.close()

    """Esta función permite la navegación entre ventanas, 
    creando la instancia de la ventana y mostrándola en pantalla."""
    def showDireccionamientoLocal(self, Form, remote_conn):
        self.direccionamientoLocal = QtWidgets.QDialog()
        self.ui = direccionamientoLocal.Ui_DireccionamientoLocal()
        self.ui.setupUi(self.direccionamientoLocal, remote_conn)
        self.direccionamientoLocal.show()
        Form.close()

    """Esta función permite la navegación entre ventanas, 
    creando la instancia de la ventana y mostrándola en pantalla."""
    def showSelectorLocal(self, Form, remote_conn):
        self.selectorLocal = QtWidgets.QDialog()
        self.ui = selectorLocal.Ui_SelectorLocal()
        self.ui.setupUi(self.selectorLocal, remote_conn)
        self.selectorLocal.show()
        Form.close()

    def setupUi(self, Form, remote_conn):
        Form.setObjectName("Form")
        Form.resize(273, 181)
        self.btn_direccionamiento = QtWidgets.QPushButton(Form)
        self.btn_direccionamiento.setGeometry(QtCore.QRect(80, 100, 111, 28))
        self.btn_direccionamiento.setObjectName("btn_direccionamiento")
        self.btn_plantilla = QtWidgets.QPushButton(Form)
        self.btn_plantilla.setGeometry(QtCore.QRect(90, 20, 93, 28))
        self.btn_plantilla.setObjectName("btn_plantilla")
        self.btn_atras = QtWidgets.QPushButton(Form)
        self.btn_atras.setGeometry(QtCore.QRect(90, 140, 93, 28))
        self.btn_atras.setObjectName("btn_atras")
        self.btn_credenciales = QtWidgets.QPushButton(Form)
        self.btn_credenciales.setGeometry(QtCore.QRect(90, 60, 93, 28))
        self.btn_credenciales.setObjectName("btn_credenciales")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        ####################################################################################
        self.btn_plantilla.clicked.connect(lambda: self.showPlantilla(Form, remote_conn))
        self.btn_credenciales.clicked.connect(lambda: self.showSelectorCredenciales(Form, remote_conn))
        self.btn_direccionamiento.clicked.connect(lambda: self.showDireccionamientoLocal(Form, remote_conn))
        self.btn_atras.clicked.connect(lambda: self.showSelectorLocal(Form, remote_conn))
        print(type(remote_conn))







    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_direccionamiento.setText(_translate("Form", "Direccionamiento"))
        self.btn_plantilla.setText(_translate("Form", "Plantilla"))
        self.btn_atras.setText(_translate("Form", "Atras"))
        self.btn_credenciales.setText(_translate("Form", "Credenciales"))


