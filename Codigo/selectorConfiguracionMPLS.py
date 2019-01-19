# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectorConfiguracionMPlS.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import ctypes

from PyQt5 import QtCore, QtGui, QtWidgets
import selectorLocal
from ConfigurarPE2 import Ui_ConfigurarPE2
from configurarCE import Ui_ConfigurarCE
import selectorLocal
import funciones2
import funciones_com
import paramiko

class Ui_SelectorConfiguracionMPLS(object):

    """Envía la configuración al enrutador obteniendo los datos de las funciones del archivo funciones2.py (ver funciones2.py)"""
    def configurarP(self, remote_conn):
        print("####################33CODIGO PARA CONFIGURAR P")
        if (type(remote_conn) is paramiko.channel.Channel):
            funciones2.config_OSPF(remote_conn)
            funciones2.save_ID(remote_conn)
        else:
            funciones_com.config_OSPF(remote_conn)
        print("1")
        funciones2.config_cef_mpls_ldp(remote_conn)
        print("2")
        ctypes.windll.user32.MessageBoxW(0, "Configuración realizada con éxito",
                                         "Done", 0)

    """Esta función permite la navegación entre ventanas, creando la instancia de la ventana y mostrándola en pantalla."""
    def showConfigurarPE(self,Form, remote_conn):
        self.configurarPE2 = QtWidgets.QDialog()
        self.ui = Ui_ConfigurarPE2()
        self.ui.setupUi(self.configurarPE2, remote_conn)
        self.configurarPE2.show()
        Form.close()

    """Esta función permite la navegación entre ventanas, creando la instancia de la ventana y mostrándola en pantalla."""
    def showConfigurarCE(self,Form, remote_conn):
        self.configurarCE = QtWidgets.QDialog()
        self.ui = Ui_ConfigurarCE()
        self.ui.setupUi(self.configurarCE, remote_conn)
        self.configurarCE.show()
        Form.close()

    """Esta función permite la navegación entre ventanas, creando la instancia de la ventana y mostrándola en pantalla."""
    def showSelectorLocal(self, Form, remote_conn):
        self.selectorLocal = QtWidgets.QDialog()
        self.ui = selectorLocal.Ui_SelectorLocal()
        self.ui.setupUi(self.selectorLocal, remote_conn)
        self.selectorLocal.show()
        Form.close()


    def setupUi(self, SelectorConfiguracionMPLS, remote_conn):
        SelectorConfiguracionMPLS.setObjectName("SelectorConfiguracionMPLS")
        SelectorConfiguracionMPLS.resize(317, 266)
        self.btn_configurarP = QtWidgets.QPushButton(SelectorConfiguracionMPLS)
        self.btn_configurarP.setGeometry(QtCore.QRect(120, 50, 93, 28))
        self.btn_configurarP.setObjectName("btn_configurarP")
        self.btn_configurarPE = QtWidgets.QPushButton(SelectorConfiguracionMPLS)
        self.btn_configurarPE.setGeometry(QtCore.QRect(120, 110, 93, 28))
        self.btn_configurarPE.setObjectName("btn_configurarPE")
        self.btn_configurarCE = QtWidgets.QPushButton(SelectorConfiguracionMPLS)
        self.btn_configurarCE.setGeometry(QtCore.QRect(120, 170, 93, 28))
        self.btn_configurarCE.setObjectName("btn_configurarCE")
        self.btn_atras = QtWidgets.QPushButton(SelectorConfiguracionMPLS)
        self.btn_atras.setGeometry(QtCore.QRect(120, 220, 93, 28))
        self.btn_atras.setObjectName("btn_atras")
        self.retranslateUi(SelectorConfiguracionMPLS)
        QtCore.QMetaObject.connectSlotsByName(SelectorConfiguracionMPLS)

        #######################################################################
        self.btn_configurarP.clicked.connect(lambda : self.configurarP(remote_conn))
        self.btn_configurarPE.clicked.connect(lambda : self.showConfigurarPE(SelectorConfiguracionMPLS, remote_conn))
        self.btn_configurarCE.clicked.connect(lambda : self.showConfigurarCE(SelectorConfiguracionMPLS, remote_conn))
        self.btn_atras.clicked.connect(lambda : self.showSelectorLocal(SelectorConfiguracionMPLS, remote_conn))

    def retranslateUi(self, SelectorConfiguracionMPLS):
        _translate = QtCore.QCoreApplication.translate
        SelectorConfiguracionMPLS.setWindowTitle(_translate("SelectorConfiguracionMPLS", "Form"))
        self.btn_configurarP.setText(_translate("SelectorConfiguracionMPLS", "Configurar P"))
        self.btn_configurarPE.setText(_translate("SelectorConfiguracionMPLS", "Configurar PE"))
        self.btn_configurarCE.setText(_translate("SelectorConfiguracionMPLS", "Configurar CE"))
        self.btn_atras.setText(_translate("SelectorConfiguracionMPLS", "Atras"))
