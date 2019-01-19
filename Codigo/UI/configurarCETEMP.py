# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'configurarCE.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ConfigurarCE(object):
    def setupUi(self, ConfigurarCE):
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
        self.txt_ip1 = QtWidgets.QLineEdit(ConfigurarCE)
        self.txt_ip1.setGeometry(QtCore.QRect(190, 70, 51, 22))
        self.txt_ip1.setMaxLength(3)
        self.txt_ip1.setObjectName("txt_ip1")
        self.txt_ip2 = QtWidgets.QLineEdit(ConfigurarCE)
        self.txt_ip2.setGeometry(QtCore.QRect(260, 70, 51, 22))
        self.txt_ip2.setMaxLength(3)
        self.txt_ip2.setObjectName("txt_ip2")
        self.txt_ip3 = QtWidgets.QLineEdit(ConfigurarCE)
        self.txt_ip3.setGeometry(QtCore.QRect(330, 70, 51, 22))
        self.txt_ip3.setMaxLength(3)
        self.txt_ip3.setObjectName("txt_ip3")
        self.txt_ip4 = QtWidgets.QLineEdit(ConfigurarCE)
        self.txt_ip4.setGeometry(QtCore.QRect(400, 70, 51, 22))
        self.txt_ip4.setMaxLength(3)
        self.txt_ip4.setObjectName("txt_ip4")
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

    def retranslateUi(self, ConfigurarCE):
        _translate = QtCore.QCoreApplication.translate
        ConfigurarCE.setWindowTitle(_translate("ConfigurarCE", "Form"))
        self.label.setText(_translate("ConfigurarCE", "IP ruta estatica"))
        self.btn_configurar.setText(_translate("ConfigurarCE", "Configurar"))
        self.btn_atras.setText(_translate("ConfigurarCE", "Atras"))
        self.label_2.setText(_translate("ConfigurarCE", "."))
        self.label_3.setText(_translate("ConfigurarCE", "."))
        self.label_4.setText(_translate("ConfigurarCE", "."))

