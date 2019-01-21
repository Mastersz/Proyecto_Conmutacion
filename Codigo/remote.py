4# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'remote.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import ctypes
import string
from PyQt5 import QtCore, QtWidgets

import selectorLocal
from funciones2 import *


class Ui_Remote(object):
    """Esta función permite la navegación entre ventanas, creando la instancia de la ventana y mostrándola en pantalla."""
    def showSelectorLocal(self,remote_conn):
        self.selectorLocal = QtWidgets.QDialog()
        self.ui = selectorLocal.Ui_SelectorLocal()
        self.ui.setupUi(self.selectorLocal,remote_conn)
        self.selectorLocal.show()


    def setupUi(self, Form):

        Form.setObjectName("Form")
        Form.resize(452, 200)


        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(100, 50, 55, 21))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(100, 90, 55, 21))
        self.label_2.setObjectName("label_2")

        self.txt_1 = QtWidgets.QLineEdit(Form)
        self.txt_1.setGeometry(QtCore.QRect(160, 50, 31, 22))
        self.txt_1.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.txt_1.setMaxLength(3)
        self.txt_1.setObjectName("txt_1")

        self.txt_2 = QtWidgets.QLineEdit(Form)
        self.txt_2.setGeometry(QtCore.QRect(210, 50, 31, 22))
        self.txt_2.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.txt_2.setMaxLength(3)
        self.txt_2.setObjectName("txt_2")

        self.txt_3 = QtWidgets.QLineEdit(Form)
        self.txt_3.setGeometry(QtCore.QRect(260, 50, 31, 22))
        self.txt_3.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.txt_3.setMaxLength(3)
        self.txt_3.setObjectName("txt_3")

        self.txt_4 = QtWidgets.QLineEdit(Form)
        self.txt_4.setGeometry(QtCore.QRect(310, 50, 31, 22))
        self.txt_4.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.txt_4.setMaxLength(3)
        self.txt_4.setObjectName("txt_4")

        self.txt_usuario = QtWidgets.QLineEdit(Form)
        self.txt_usuario.setGeometry(QtCore.QRect(180, 90, 151, 21))
        self.txt_usuario.setInputMethodHints(QtCore.Qt.ImhNone)
        self.txt_usuario.setObjectName("txt_usuario")
        self.txt_contrasena = QtWidgets.QLineEdit(Form)
        self.txt_contrasena.setGeometry(QtCore.QRect(180, 120, 151, 21))
        self.txt_contrasena.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_contrasena.setObjectName("txt_contrasena")
        self.btn_conectar = QtWidgets.QPushButton(Form)
        self.btn_conectar.setGeometry(QtCore.QRect(200, 160, 93, 28))
        self.btn_conectar.setObjectName("btn_conectar")

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(200, 60, 16, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(250, 60, 16, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(300, 60, 16, 16))
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(100, 120, 71, 21))
        self.label_6.setObjectName("label_6")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        ################################################################
        self.btn_conectar.clicked.connect(lambda : self.verificarIP(Form))


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Conectar por SSH"))
        self.label.setText(_translate("Form", "Ip"))
        self.label_2.setText(_translate("Form", "Usuario"))
        self.btn_conectar.setText(_translate("Form", "Conectar"))
        self.label_3.setText(_translate("Form", "."))
        self.label_4.setText(_translate("Form", "."))
        self.label_5.setText(_translate("Form", "."))
        self.label_6.setText(_translate("Form", "Contraseña"))


    """Obtiene los datos de los campos de texto de ip ingresados por el cliente, Si todos los campos están correctos intenta
    realizar la conexión por medio de ssh. Si ocurre algún problema muestra mensaje popup informando en que campo en específico
    existe una inconsistencia."""
    def verificarIP(self, Form):
        if self.txt_1.text().isnumeric() and (int(self.txt_1.text()) < 256):
            if self.txt_2.text().isnumeric() and (int(self.txt_2.text()) < 256):
                if self.txt_3.text().isnumeric() and (int(self.txt_3.text()) < 256):
                    if self.txt_4.text().isnumeric() and (int(self.txt_4.text()) < 256):

                        print("estableciendo conexion...")
                        ip = self.txt_1.text() + "." + self.txt_2.text() + "." + self.txt_3.text() + "." + self.txt_4.text()
                        print(
                            self.txt_1.text() + "." + self.txt_2.text() + "." + self.txt_3.text() + "." + self.txt_4.text()+" "+self.txt_usuario.text()+" "+self.txt_contrasena.text())
                        try:
                            remote_conn_pre, remote_conn = login_ssh(ip, self.txt_usuario.text(),self.txt_contrasena.text())

                            print("1")
                            disable_paging(remote_conn)
                            print("2")
                            back_home(remote_conn)
                            print("3")
                            self.showSelectorLocal(remote_conn)
                            print("4")
                            Form.close()
                        except Exception :
                            evento=4
                            arch = open("temp.txt", "r")
                            nombre=""
                            time=""
                            for linea in arch:
                                linea = linea.split(",")
                                nombre = linea[0]
                                time = linea[1]
                            arch.close()

                            file = open("historial.txt", "a")
                            file.write(nombre +","+ time +","+ str(evento)+"\n")
                            ctypes.windll.user32.MessageBoxW(0, "No se pudo establecer la conexion, verificar ip o credenciales.", "Error", 0)


                    else:
                        ctypes.windll.user32.MessageBoxW(0, "Error en el cuarto octeto", "Error", 1)
                else:
                    ctypes.windll.user32.MessageBoxW(0, "Error en el tercer octeto", "Error", 1)
            else:
                ctypes.windll.user32.MessageBoxW(0, "Error en el segundo octeto", "Error", 1)
        else:
            ctypes.windll.user32.MessageBoxW(0, "Error en el primer octeto", "Error", 1)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loginWindow = QtWidgets.QDialog()
    ui = Ui_Remote()
    ui.setupUi(loginWindow)
    loginWindow.show()
    sys.exit(app.exec_())