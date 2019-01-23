# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectorConfiguracionMPlS.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import ctypes
from Codigo.funcionesDB import historial_bd
from PyQt5 import QtCore, QtGui, QtWidgets
import Codigo.selectorLocal
from Codigo.ConfigurarPE2 import Ui_ConfigurarPE2
from Codigo.configurarCE import Ui_ConfigurarCE
import Codigo.funciones2
import Codigo.funciones_com
import paramiko
import sqlite3

class Ui_SelectorConfiguracionMPLS(object):
    disp  = 0
    def historial(dispID, username, time, evento):
        bd = sqlite3.connect("DataBase.db")
        inf = (str(username), time, dispID, str(evento))
        registro = historial_bd(bd, inf)
        print(registro)

    """Envía la configuración al enrutador obteniendo los datos de las funciones del archivo funciones2.py (ver funciones2.py)"""
    def configurarP(self, remote_conn):
        #try:
            print("####################CODIGO PARA CONFIGURAR P")
            if (type(remote_conn) is paramiko.channel.Channel):
                Codigo.funciones2.config_OSPF(remote_conn)
                Codigo.funciones2.save_ID(remote_conn)
            else:
                Codigo.funciones_com.config_OSPF(remote_conn)
            print("1")
            Codigo.funciones2.config_cef_mpls_ldp(remote_conn)
            print("2")
            ctypes.windll.user32.MessageBoxW(0, "Configuración realizada con éxito",
                                             "Done", 0)

            dispID=1
            self.disp = dispID
            evento=1
            arch = open("temp.txt", "r")
            nombre = ""
            time = ""
            for linea in arch:
                linea = linea.split(",")
                nombre = linea[0]
                time = linea[1]
            arch.close()

            file = open("historial.txt", "a")
            file.write(nombre + "," + time + "," + str(evento) + "\n")
            file.close()
            print(nombre, time)
            #self.historial(dispID,nombre, time, evento)
        #except:
    """ evento=5
        arch = open("temp.txt", "r")
        nombre = ""
        time = ""
        for linea in arch:
            linea = linea.split(",")
            nombre = linea[0]
            time = linea[1]
        arch.close()

        file = open("historial.txt", "a")
        file.write(nombre + "," + time + "," + str(evento) + "\n")
        ctypes.windll.user32.MessageBoxW(0, "Error de conexión P",
                                         "Done", 0)"""


    """Esta función permite la navegación entre ventanas, creando la instancia de la ventana y mostrándola en pantalla."""
    def showConfigurarPE(self,Form, remote_conn):
        try:
            self.configurarPE2 = QtWidgets.QDialog()
            self.ui = Ui_ConfigurarPE2()
            self.ui.setupUi(self.configurarPE2, remote_conn)
            self.configurarPE2.show()
            Form.close()

            dispID = 2
            self.disp = dispID
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
            file.write(nombre + "," + time + "," + str(evento) + "\n")
            file.close()
            print(nombre, time)
            #self.historial(dispID)
        except:
            evento = 5
            arch = open("temp.txt", "r")
            nombre = ""
            time = ""
            for linea in arch:
                linea = linea.split(",")
                nombre = linea[0]
                time = linea[1]
            arch.close()

            file = open("historial.txt", "a")
            file.write(nombre + "," + time + "," + str(evento) + "\n")
            ctypes.windll.user32.MessageBoxW(0, "Error de conexión PE",
                                             "Done", 0)
    """Esta función permite la navegación entre ventanas, creando la instancia de la ventana y mostrándola en pantalla."""
    def showConfigurarCE(self,Form, remote_conn):
        #try:
            self.configurarCE = QtWidgets.QDialog()
            self.ui = Ui_ConfigurarCE()
            self.ui.setupUi(self.configurarCE, remote_conn)
            self.configurarCE.show()
            Form.close()
            dispID = 3
            self.disp = dispID
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
            file.write(nombre + "," + time + "," + str(evento) + "\n")
            file.close()
            print(nombre, time)
            #self.historial(dispID)
        #except:
            """evento = 5
            arch = open("temp.txt", "r")
            nombre = ""
            time = ""
            for linea in arch:
                linea = linea.split(",")
                nombre = linea[0]
                time = linea[1]
            arch.close()

            file = open("historial.txt", "a")
            file.write(nombre + "," + time + "," + str(evento) + "\n")
            ctypes.windll.user32.MessageBoxW(0, "Error de conexión CE",
                                             "Done", 0)"""

    """Esta función permite la navegación entre ventanas, creando la instancia de la ventana y mostrándola en pantalla."""
    def showSelectorLocal(self, Form, remote_conn):
        self.selectorLocal = QtWidgets.QDialog()
        self.ui = Codigo.selectorLocal.Ui_SelectorLocal()
        self.ui.setupUi(self.selectorLocal, remote_conn)
        self.selectorLocal.show()
        Form.close()
        evento = 1
        arch = open("temp.txt", "r")
        nombre = ""
        time = ""
        for linea in arch:
            linea = linea.split(",")
            nombre = linea[0]
            time = linea[1]
        arch.close()
        self.historial(self.disp, nombre, time, evento)

        file = open("historial.txt", "a")
        file.write(nombre + "," + time + "," + str(evento) + "\n")


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
