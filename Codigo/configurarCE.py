# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'configurarCE.ui'
# Created by: PyQt5 UI code generator 5.9.2
import ctypes

from PyQt5 import QtCore, QtWidgets
import selectorConfiguracionMPLS
import funciones2


class Ui_ConfigurarCE(object):

    """Esta función permite la navegación entre ventanas,
    creando la instancia de la ventana y mostrándola en pantalla."""
    def showSelectorMPLS(self, Form, remote_conn):
        self.selectorMpls = QtWidgets.QDialog()
        self.ui = selectorConfiguracionMPLS.Ui_SelectorConfiguracionMPLS()
        self.ui.setupUi(self.selectorMpls, remote_conn)
        self.selectorMpls.show()
        Form.close()

    """Envía la configuración al enrutador obteniendo
    los datos de las funciones del archivo funciones2.py (ver funciones2.py)"""
    def configurar(self, Form, remote_conn):
        if self.verificarIP():
            print("ENTROOOOOOOOOOOOOOO")
            texto1=self.txt_1.text()
            texto2=self.txt_2.text()
            texto3= self.txt_3.text()
            texto4=self.txt_4.text()
            funciones2.conf_route_CE(remote_conn, texto1 + "." + texto2 + "." + texto3 + "." + texto4)
            ctypes.windll.user32.MessageBoxW(0, "Configuración realizada con éxito",
                                             "Done", 0)

    def setupUi(self, ConfigurarCE, remote_conn):
        ConfigurarCE.setObjectName("ConfigurarCE")
        ConfigurarCE.resize(546, 197)
        self.label = QtWidgets.QLabel(ConfigurarCE)
        self.label.setGeometry(QtCore.QRect(70, 70, 111, 16))
        self.label.setObjectName("label")
        self.btn_configurar = QtWidgets.QPushButton(ConfigurarCE)
        self.btn_configurar.setGeometry(QtCore.QRect(170, 130, 93, 28))
        self.btn_configurar.setObjectName("btn_configurar")
        self.btn_atras = QtWidgets.QPushButton(ConfigurarCE)
        self.btn_atras.setGeometry(QtCore.QRect(320, 130, 93, 28))
        self.btn_atras.setObjectName("btn_atras")
        self.txt_1 = QtWidgets.QLineEdit(ConfigurarCE)
        self.txt_1.setGeometry(QtCore.QRect(190, 70, 51, 22))
        self.txt_1.setMaxLength(3)
        self.txt_1.setObjectName("txt_ip1")
        self.txt_2 = QtWidgets.QLineEdit(ConfigurarCE)
        self.txt_2.setGeometry(QtCore.QRect(260, 70, 51, 22))
        self.txt_2.setMaxLength(3)
        self.txt_2.setObjectName("txt_ip2")
        self.txt_3 = QtWidgets.QLineEdit(ConfigurarCE)
        self.txt_3.setGeometry(QtCore.QRect(330, 70, 51, 22))
        self.txt_3.setMaxLength(3)
        self.txt_3.setObjectName("txt_ip3")
        self.txt_4 = QtWidgets.QLineEdit(ConfigurarCE)
        self.txt_4.setGeometry(QtCore.QRect(400, 70, 51, 22))
        self.txt_4.setMaxLength(3)
        self.txt_4.setObjectName("txt_ip4")
        self.label_2 = QtWidgets.QLabel(ConfigurarCE)
        self.label_2.setGeometry(QtCore.QRect(250, 80, 16, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(ConfigurarCE)
        self.label_3.setGeometry(QtCore.QRect(320, 80, 16, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(ConfigurarCE)
        self.label_4.setGeometry(QtCore.QRect(390, 80, 16, 16))
        self.label_4.setObjectName("label_4")
        self.retranslateUi(ConfigurarCE)
        QtCore.QMetaObject.connectSlotsByName(ConfigurarCE)
        #########################################################################3
        self.btn_atras.clicked.connect(lambda: self.showSelectorMPLS(ConfigurarCE, remote_conn))
        self.btn_configurar.clicked.connect(lambda: self.configurar(ConfigurarCE, remote_conn))

    def verificarIP(self):
        if self.txt_1.text().isnumeric() and (int(self.txt_1.text()) < 256):
            if self.txt_2.text().isnumeric() and (int(self.txt_2.text()) < 256):
                if self.txt_3.text().isnumeric() and (int(self.txt_3.text()) < 256):
                    if self.txt_4.text().isnumeric() and (int(self.txt_4.text()) < 256):
                        print("estableciendo conexion...")
                        ip = self.txt_1.text() + "." + self.txt_2.text() + "." + self.txt_3.text() + "." + self.txt_4.text()
                        return True
                    else:
                        ctypes.windll.user32.MessageBoxW(0, "Error en el cuarto octeto", "Error", 1)
                        return False
                else:
                    ctypes.windll.user32.MessageBoxW(0, "Error en el tercer octeto", "Error", 1)
                    return False
            else:
                ctypes.windll.user32.MessageBoxW(0, "Error en el segundo octeto", "Error", 1)
                return False
        else:
            ctypes.windll.user32.MessageBoxW(0, "Error en el primer octeto", "Error", 1)
            return False

    def retranslateUi(self, ConfigurarCE):
        _translate = QtCore.QCoreApplication.translate
        ConfigurarCE.setWindowTitle(_translate("ConfigurarCE", "Form"))
        self.label.setText(_translate("ConfigurarCE", "IP ruta estatica"))
        self.btn_configurar.setText(_translate("ConfigurarCE", "Configurar"))
        self.btn_atras.setText(_translate("ConfigurarCE", "Atras"))
        self.label_2.setText(_translate("ConfigurarCE", "."))
        self.label_3.setText(_translate("ConfigurarCE", "."))
        self.label_4.setText(_translate("ConfigurarCE", "."))

