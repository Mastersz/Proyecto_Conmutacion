# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'configurarPE2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import ctypes
import time
from PyQt5 import QtCore, QtGui, QtWidgets
import funciones2
import funciones_com
import paramiko

import selectorConfiguracionMPLS
import agregarCliente

MAX_BUFFER = 65535
class Ui_ConfigurarPE2(object):
    """Esta función permite la navegación entre ventanas, creando la instancia de la ventana y mostrándola en pantalla."""
    def showSelectorMPLS(self, Form, remote_conn):
        self.selectorMpls = QtWidgets.QDialog()
        self.ui = selectorConfiguracionMPLS.Ui_SelectorConfiguracionMPLS()
        self.ui.setupUi(self.selectorMpls, remote_conn)
        self.selectorMpls.show()
        Form.close()

    """Esta función permite la navegación entre ventanas, creando la instancia de la ventana y mostrándola en pantalla."""
    def showAgregarCliente(self,Form,remote_conn):
        self.agregarCliente = QtWidgets.QDialog()
        self.ui = agregarCliente.Ui_AgregarCliente()
        self.ui.setupUi(self.agregarCliente, remote_conn)
        self.agregarCliente.show()
        Form.close()


    def setupUi(self, Dialog, remote_conn):
        Dialog.setObjectName("Dialog")
        Dialog.resize(650, 610)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 20, 81, 16))
        self.label.setObjectName("label")
        self.txt_vrf = QtWidgets.QLineEdit(Dialog)
        self.txt_vrf.setGeometry(QtCore.QRect(210, 20, 113, 22))
        self.txt_vrf.setObjectName("txt_vrf")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 60, 141, 16))
        self.label_2.setObjectName("label_2")
        self.txt_ip1_1 = QtWidgets.QLineEdit(Dialog)
        self.txt_ip1_1.setGeometry(QtCore.QRect(210, 60, 61, 22))
        self.txt_ip1_1.setObjectName("txt_ip1_1")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(280, 70, 16, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(360, 70, 16, 16))
        self.label_4.setObjectName("label_4")
        self.txt_ip1_2 = QtWidgets.QLineEdit(Dialog)
        self.txt_ip1_2.setGeometry(QtCore.QRect(290, 60, 61, 22))
        self.txt_ip1_2.setObjectName("txt_ip1_2")
        self.txt_ip1_3 = QtWidgets.QLineEdit(Dialog)
        self.txt_ip1_3.setGeometry(QtCore.QRect(370, 60, 61, 22))
        self.txt_ip1_3.setObjectName("txt_ip1_3")
        self.txt_ip1_4 = QtWidgets.QLineEdit(Dialog)
        self.txt_ip1_4.setGeometry(QtCore.QRect(450, 60, 61, 22))
        self.txt_ip1_4.setObjectName("txt_ip1_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(440, 70, 16, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(440, 110, 16, 16))
        self.label_6.setObjectName("label_6")
        self.txt_mask1_4 = QtWidgets.QLineEdit(Dialog)
        self.txt_mask1_4.setGeometry(QtCore.QRect(450, 100, 61, 22))
        self.txt_mask1_4.setObjectName("txt_mask1_4")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(360, 110, 16, 16))
        self.label_7.setObjectName("label_7")
        self.txt_mask1_1 = QtWidgets.QLineEdit(Dialog)
        self.txt_mask1_1.setGeometry(QtCore.QRect(210, 100, 61, 22))
        self.txt_mask1_1.setObjectName("txt_mask1_1")
        self.txt_mask1_2 = QtWidgets.QLineEdit(Dialog)
        self.txt_mask1_2.setGeometry(QtCore.QRect(290, 100, 61, 22))
        self.txt_mask1_2.setObjectName("txt_mask1_2")
        self.txt_mask1_3 = QtWidgets.QLineEdit(Dialog)
        self.txt_mask1_3.setGeometry(QtCore.QRect(370, 100, 61, 22))
        self.txt_mask1_3.setObjectName("txt_mask1_3")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(280, 110, 16, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(280, 150, 16, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(440, 150, 16, 16))
        self.label_10.setObjectName("label_10")
        self.txt_ip2_4 = QtWidgets.QLineEdit(Dialog)
        self.txt_ip2_4.setGeometry(QtCore.QRect(450, 140, 61, 22))
        self.txt_ip2_4.setObjectName("txt_ip2_4")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(360, 150, 16, 16))
        self.label_11.setObjectName("label_11")
        self.txt_ip2_3 = QtWidgets.QLineEdit(Dialog)
        self.txt_ip2_3.setGeometry(QtCore.QRect(370, 140, 61, 22))
        self.txt_ip2_3.setObjectName("txt_ip2_3")
        self.txt_ip2_1 = QtWidgets.QLineEdit(Dialog)
        self.txt_ip2_1.setGeometry(QtCore.QRect(210, 140, 61, 22))
        self.txt_ip2_1.setObjectName("txt_ip2_1")
        self.txt_ip2_2 = QtWidgets.QLineEdit(Dialog)
        self.txt_ip2_2.setGeometry(QtCore.QRect(290, 140, 61, 22))
        self.txt_ip2_2.setObjectName("txt_ip2_2")
        self.txt_mask2_3 = QtWidgets.QLineEdit(Dialog)
        self.txt_mask2_3.setGeometry(QtCore.QRect(370, 180, 61, 22))
        self.txt_mask2_3.setObjectName("txt_mask2_3")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(280, 190, 16, 16))
        self.label_12.setObjectName("label_12")
        self.txt_mask2_4 = QtWidgets.QLineEdit(Dialog)
        self.txt_mask2_4.setGeometry(QtCore.QRect(450, 180, 61, 22))
        self.txt_mask2_4.setObjectName("txt_mask2_4")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(440, 190, 16, 16))
        self.label_13.setObjectName("label_13")
        self.txt_mask2_1 = QtWidgets.QLineEdit(Dialog)
        self.txt_mask2_1.setGeometry(QtCore.QRect(210, 180, 61, 22))
        self.txt_mask2_1.setObjectName("txt_mask2_1")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(360, 190, 16, 16))
        self.label_14.setObjectName("label_14")
        self.txt_mask2_2 = QtWidgets.QLineEdit(Dialog)
        self.txt_mask2_2.setGeometry(QtCore.QRect(290, 180, 61, 22))
        self.txt_mask2_2.setObjectName("txt_mask2_2")
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(50, 140, 81, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(Dialog)
        self.label_17.setGeometry(QtCore.QRect(30, 180, 161, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(Dialog)
        self.label_18.setGeometry(QtCore.QRect(50, 100, 131, 16))
        self.label_18.setObjectName("label_18")
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(50, 260, 81, 16))
        self.label_15.setObjectName("label_15")
        self.txt_vlan = QtWidgets.QLineEdit(Dialog)
        self.txt_vlan.setGeometry(QtCore.QRect(210, 260, 113, 22))
        self.txt_vlan.setObjectName("txt_vlan")
        self.txt_interfaz = QtWidgets.QLineEdit(Dialog)
        self.txt_interfaz.setGeometry(QtCore.QRect(210, 300, 113, 22))
        self.txt_interfaz.setObjectName("txt_interfaz")
        self.label_19 = QtWidgets.QLabel(Dialog)
        self.label_19.setGeometry(QtCore.QRect(50, 300, 81, 16))
        self.label_19.setObjectName("label_19")
        self.txt_Clientes = QtWidgets.QTextEdit(Dialog)
        self.txt_Clientes.setGeometry(QtCore.QRect(160, 340, 450, 200))
        self.txt_Clientes.setObjectName("txt_Clientes")
        self.btn_anadir = QtWidgets.QPushButton(Dialog)
        self.btn_anadir.setGeometry(QtCore.QRect(300, 560, 93, 28))
        self.btn_anadir.setObjectName("btn_anadir")
        self.btn_atras = QtWidgets.QPushButton(Dialog)
        self.btn_atras.setGeometry(QtCore.QRect(510, 560, 93, 28))
        self.btn_atras.setObjectName("btn_atras")
        self.label_20 = QtWidgets.QLabel(Dialog)
        self.label_20.setGeometry(QtCore.QRect(80, 350, 55, 16))
        self.label_20.setObjectName("label_20")
        self.txt_AS = QtWidgets.QLineEdit(Dialog)
        self.txt_AS.setGeometry(QtCore.QRect(30, 380, 113, 22))
        self.txt_AS.setObjectName("txt_AS")
        self.btn_agregarCliente = QtWidgets.QPushButton(Dialog)
        self.btn_agregarCliente.setGeometry(QtCore.QRect(60, 560, 121, 28))
        self.btn_agregarCliente.setObjectName("btn_agregarCliente")
        self.label_21 = QtWidgets.QLabel(Dialog)
        self.label_21.setGeometry(QtCore.QRect(360, 230, 16, 16))
        self.label_21.setObjectName("label_21")
        self.txt_mask3_4 = QtWidgets.QLineEdit(Dialog)
        self.txt_mask3_4.setGeometry(QtCore.QRect(450, 220, 61, 22))
        self.txt_mask3_4.setObjectName("txt_mask3_4")
        self.label_22 = QtWidgets.QLabel(Dialog)
        self.label_22.setGeometry(QtCore.QRect(280, 230, 16, 16))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(Dialog)
        self.label_23.setGeometry(QtCore.QRect(30, 220, 141, 16))
        self.label_23.setObjectName("label_23")
        self.txt_mask3_2 = QtWidgets.QLineEdit(Dialog)
        self.txt_mask3_2.setGeometry(QtCore.QRect(290, 220, 61, 22))
        self.txt_mask3_2.setObjectName("txt_mask3_2")
        self.txt_mask3_1 = QtWidgets.QLineEdit(Dialog)
        self.txt_mask3_1.setGeometry(QtCore.QRect(210, 220, 61, 22))
        self.txt_mask3_1.setObjectName("txt_mask3_1")
        self.label_24 = QtWidgets.QLabel(Dialog)
        self.label_24.setGeometry(QtCore.QRect(440, 230, 16, 16))
        self.label_24.setObjectName("label_24")
        self.txt_mask3_3 = QtWidgets.QLineEdit(Dialog)
        self.txt_mask3_3.setGeometry(QtCore.QRect(370, 220, 61, 22))
        self.txt_mask3_3.setObjectName("txt_mask3_3")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        ##################################################################################
        self.btn_agregarCliente.clicked.connect(lambda : self.showAgregarCliente(Dialog,remote_conn))

        self.btn_anadir.clicked.connect(lambda: self.ConfPE(remote_conn))
        self.btn_atras.clicked.connect(lambda: self.showSelectorMPLS(Dialog, remote_conn))
        self.txt_Clientes.setDisabled(True)

    """Permite la configuración de un dispositivo PE, validando que los campos ingresados para direcciones IP sean
    correctos. Luego, se procede a configurar los protocolos iBGP, MP-BGP, CEF, LDP, MPLS, creación de VRF y enrutamiento
    entre dispositivos PE y CE."""
    def ConfPE(self, remote_conn):
        if self.verificarIP(self.txt_ip1_1,self.txt_ip1_2,self.txt_ip1_3,self.txt_ip1_4):
            if self.verificarIP(self.txt_ip2_1, self.txt_ip2_2, self.txt_ip2_3, self.txt_ip2_4):
                if self.verificarIP(self.txt_mask1_1, self.txt_mask1_2, self.txt_mask1_3, self.txt_mask1_4):
                    if self.verificarIP(self.txt_mask2_1, self.txt_mask2_2, self.txt_mask2_3, self.txt_mask2_4):
                        if self.verificarIP(self.txt_mask3_1, self.txt_mask3_2, self.txt_mask3_3, self.txt_mask3_4):
                            if self.txt_vlan.text().isnumeric() and ((int(self.txt_AS.text()))<=65535) and self.txt_AS.text().isnumeric() and self.txt_vrf.text()!="" and self.txt_interfaz.text()!="" :

                                if (type(remote_conn) is paramiko.channel.Channel):
                                    funciones2.back_home(remote_conn)
                                    print("1")
                                    funciones2.config_iBGP(remote_conn)
                                    print("2")
                                    time.sleep(1)
                                    funciones2.config_MP_BGP(remote_conn)
                                    print("3")
                                    time.sleep(1)
                                    funciones2.config_cef_mpls_ldp(remote_conn)
                                    print("4")
                                    time.sleep(1)
                                    funciones2.config_vrf(remote_conn, self.txt_vrf.text(), self.txt_AS.text(), self.txt_vlan.text())
                                    print("5")
                                    time.sleep(1)
                                    redCliente = self.txt_ip2_1.text() + "." + self.txt_ip2_2.text() + "." + self.txt_ip2_3.text() + "." + self.txt_ip2_4.text()
                                    maskCliente = self.txt_mask2_1.text() + "." + self.txt_mask2_2.text() + "." + self.txt_mask2_3.text() + "." + self.txt_mask2_4.text()
                                    dirCliente = self.txt_ip1_1.text() + "." + self.txt_ip1_2.text() + "." + self.txt_ip1_3.text() + "." + self.txt_ip1_4.text()
                                    maskDirCliente = self.txt_mask1_1.text() + "." + self.txt_mask1_2.text() + "." + self.txt_mask1_3.text() + "." + self.txt_mask1_4.text()
                                    gatewayCliente = self.txt_mask3_1.text()+"."+self.txt_mask3_2.text()+"."+self.txt_mask3_3.text()+"."+self.txt_mask3_4.text()
                                    print("6")
                                    time.sleep(1)
                                    funciones2.config_add_interfaz_vrf(remote_conn, self.txt_vrf.text(), self.txt_vlan.text(),
                                                                       self.txt_interfaz.text(), dirCliente, maskDirCliente)
                                    print("7")
                                    time.sleep(1)
                                    funciones2.config_route_PE_CE(remote_conn, self.txt_vrf.text(), redCliente, maskCliente,
                                                                  gatewayCliente)
                                    print("8")
                                    time.sleep(1)
                                    funciones2.redistribute_vrf(remote_conn, self.txt_vrf.text())
                                    print("9")
                                    time.sleep(4)
                                    remote_conn.recv(MAX_BUFFER)
                                    self.txt_Clientes.setText(funciones2.show_res(remote_conn))
                                    ctypes.windll.user32.MessageBoxW(0, "Configuración realizada con éxito",
                                                                     "Done", 0)
                                else:
                                    funciones_com.config_OSPF(remote_conn)
                                    print("1")
                                    funciones_com.config_iBGP(remote_conn)
                                    print("2")
                                    funciones_com.config_MP_BGP(remote_conn)
                                    print("3")
                                    funciones_com.config_cef_mpls_ldp(remote_conn)
                                    print("4")
                                    funciones_com.config_vrf(remote_conn, self.txt_vrf.text(), self.txt_AS.text(), self.txt_vlan.text())
                                    print("5")
                                    redCliente = self.txt_ip2_1.text() + "." + self.txt_ip2_2.text() + "." + self.txt_ip2_3.text() + "." + self.txt_ip2_4.text()
                                    maskCliente = self.txt_mask2_1.text() + "." + self.txt_mask2_2.text() + "." + self.txt_mask2_3.text() + "." + self.txt_mask2_4.text()
                                    dirCliente = self.txt_ip1_1.text() + "." + self.txt_ip1_2.text() + "." + self.txt_ip1_3.text() + "." + self.txt_ip1_4.text()
                                    maskDirCliente = self.txt_mask1_1.text() + "." + self.txt_mask1_2.text() + "." + self.txt_mask1_3.text() + "." + self.txt_mask1_4.text()
                                    print("6")
                                    funciones_com.config_add_interfaz_vrf(remote_conn, self.txt_vrf.text(), self.txt_vlan.text(),
                                                                       self.txt_interfaz.text(), dirCliente, maskDirCliente)
                                    print("7")
                                    funciones_com.config_route_PE_CE(remote_conn, self.txt_vrf.text(), redCliente, maskCliente,
                                                                  self.txt_interfaz.text())
                                    print("8")
                                    funciones_com.redistribute_vrf(remote_conn, self.txt_vrf.text())
                                    print("9")
                                    self.txt_Clientes.setText(funciones_com.show_res(remote_conn))

                            else:
                                self.txt_Clientes.setText("Error al configurar el dispositivo")
                        else:
                            self.txt_Clientes.setText("Error al configurar el dispositivo")
                    else:
                        self.txt_Clientes.setText("Error al configurar el dispositivo")
                else:
                    self.txt_Clientes.setText("Error al configurar el dispositivo")
            else:
                self.txt_Clientes.setText("Error al configurar el dispositivo")
        else:
            self.txt_Clientes.setText("Error al configurar el dispositivo")


    def verificarIP(self, txt_1,txt_2,txt_3,txt_4):
        if (txt_1.text()!="" or txt_2.text()!="" or txt_3.text()!="" or txt_4.text()!=""):
            if txt_1.text().isnumeric() and (int(txt_1.text()) < 256):
                if txt_2.text().isnumeric() and (int(txt_2.text()) < 256):
                    if txt_3.text().isnumeric() and (int(txt_3.text()) < 256):
                        if txt_4.text().isnumeric() and (int(txt_4.text()) < 256):
                            ip = txt_1.text() + "." + txt_2.text() + "." + txt_3.text() + "." + txt_4.text()
                            return True
                        else:
                            ctypes.windll.user32.MessageBoxW(0, "Error en el cuarto octeto", "Error", 1)
                    else:
                        ctypes.windll.user32.MessageBoxW(0, "Error en el tercer octeto", "Error", 1)
                else:
                    ctypes.windll.user32.MessageBoxW(0, "Error en el segundo octeto", "Error", 1)
            else:
                ctypes.windll.user32.MessageBoxW(0, "Error en el primer octeto", "Error", 1)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Configurar PE", "Form"))
        self.label.setText(_translate("Configurar PE", "NOMBRE VRF"))
        self.label_2.setText(_translate("Configurar PE", "DIRECCION IP CLIENTE"))
        self.label_3.setText(_translate("Configurar PE", "."))
        self.label_4.setText(_translate("Configurar PE", "."))
        self.label_5.setText(_translate("Configurar PE", "."))
        self.label_6.setText(_translate("Configurar PE", "."))
        self.label_7.setText(_translate("Configurar PE", "."))
        self.label_8.setText(_translate("Configurar PE", "."))
        self.label_9.setText(_translate("Configurar PE", "."))
        self.label_10.setText(_translate("Configurar PE", "."))
        self.label_11.setText(_translate("Configurar PE", "."))
        self.label_12.setText(_translate("Configurar PE", "."))
        self.label_13.setText(_translate("Configurar PE", "."))
        self.label_14.setText(_translate("Configurar PE", "."))
        self.label_16.setText(_translate("Configurar PE", "LAN CLIENTE"))
        self.label_17.setText(_translate("Configurar PE", "MASCARA LAN CLIENTE"))
        self.label_18.setText(_translate("Configurar PE", "MASCARA CLIENTE"))
        self.label_15.setText(_translate("Configurar PE", "VLAN"))
        self.label_19.setText(_translate("Configurar PE", "INTERFAZ"))
        self.btn_anadir.setText(_translate("Configurar PE", "Añadir"))
        self.btn_atras.setText(_translate("Configurar PE", "Atras"))
        self.label_20.setText(_translate("Configurar PE", "AS"))
        self.btn_agregarCliente.setText(_translate("Configurar PE", "Agregar Cliente"))
        self.label_21.setText(_translate("Configurar PE", "."))
        self.label_22.setText(_translate("Configurar PE", "."))
        self.label_23.setText(_translate("Configurar PE", "GATEWAY LAN CLIENTE"))
        self.label_24.setText(_translate("Configurar PE", "."))

