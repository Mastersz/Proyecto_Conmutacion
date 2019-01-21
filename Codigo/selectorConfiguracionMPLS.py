# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectorConfiguracionMPlS.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import ctypes
from Codigo.funcionesDB import historial_bd
from PyQt5 import QtCore, QtGui, QtWidgets
import selectorLocal
from ConfigurarPE2 import Ui_ConfigurarPE2
from configurarCE import Ui_ConfigurarCE
import selectorLocal
import funciones2
import funciones_com
import paramiko
import sqlite3

class Ui_SelectorConfiguracionMPLS(object):
    def historial(dispID):
        bd = sqlite3.connect("DataBase.db")
        file = open("historial.txt", "r")
        for line in file:
            campos = line.split(",")
            username = campos[0]
            time = campos[1]
            evento = campos[2]
        inf = (username, time, dispID, evento)
        registro = historial_bd(bd, inf)
        print(registro)

    """Envía la configuración al enrutador obteniendo los datos de las funciones del archivo funciones2.py (ver funciones2.py)"""
    def configurarP(self, remote_conn):
        try:
            print("####################CODIGO PARA CONFIGURAR P")
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
            dispID=1
            self.historial(dispID)
        except:
            evento=5
            file = open("historial.txt", "a")
            file.write(evento)
            ctypes.windll.user32.MessageBoxW(0, "Error de conexión",
                                             "Done", 0)

    """Esta función permite la navegación entre ventanas, creando la instancia de la ventana y mostrándola en pantalla."""
    def showConfigurarPE(self,Form, remote_conn):
        bd = sqlite3.connect("DataBase.db")
        dispID = 2
        self.historial(dispID)
        self.configurarPE2 = QtWidgets.QDialog()
        self.ui = Ui_ConfigurarPE2()
        self.ui.setupUi(self.configurarPE2, remote_conn)
        self.configurarPE2.show()
        Form.close()

    """Esta función permite la navegación entre ventanas, creando la instancia de la ventana y mostrándola en pantalla."""
    def showConfigurarCE(self,Form, remote_conn):
        bd = sqlite3.connect("DataBase.db")
        dispID = 3
        self.historial(dispID)
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
        evento = 1
        arch = open("temp.txt", "r")
        nombre = ""
        time = ""
        for linea in arch:
            linea = linea.split(",")
            nombre = linea[0]
            time = linea[1]
        arch.close()

        file = open("historial.txt", "a")
        file.write(nombre + "," + time + "," + str(evento)+"\n")
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