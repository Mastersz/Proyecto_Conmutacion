from PyQt5 import QtCore, QtGui, QtWidgets
import configuracionBasica
import funciones2
import selectorConfiguracionMPLS


class Ui_SelectorLocal(object):

    """Esta función permite la navegación entre ventanas, creando la instancia de la ventana y mostrándola en pantalla."""
    def showConfiguracionBasicaWindow(self,SelectorLocal,remote_conn):
        self.configuracionBasicaWindow = QtWidgets.QDialog()
        self.ui = configuracionBasica.Ui_ConfiguracionBasica()
        self.ui.setupUi(self.configuracionBasicaWindow,remote_conn)
        self.configuracionBasicaWindow.show()
        SelectorLocal.close()

    """Esta función permite la navegación entre ventanas, creando la instancia de la ventana y mostrándola en pantalla."""
    def showSelectorMPLS(self,SelectorLocaL, remote_conn):
        self.selectorConfiguracionMPLS = QtWidgets.QDialog()
        self.ui = selectorConfiguracionMPLS.Ui_SelectorConfiguracionMPLS()
        self.ui.setupUi(self.selectorConfiguracionMPLS, remote_conn)
        self.selectorConfiguracionMPLS.show()
        SelectorLocaL.close()

    def salir(self,Form):
        #############################CODIGO PARA CERRAR CONEXION
        Form.close()



    def setupUi(self, SelectorLocal,remote_conn):
        print("setupU")
        SelectorLocal.setObjectName("SelectorLocal")
        SelectorLocal.resize(640, 200)
        self.btn_configuracionBasica = QtWidgets.QPushButton(SelectorLocal)
        self.btn_configuracionBasica.setGeometry(QtCore.QRect(80, 50, 181, 91))
        self.btn_configuracionBasica.setObjectName("btn_configuracionBasica")
        self.btn_configuracionMPLS = QtWidgets.QPushButton(SelectorLocal)
        self.btn_configuracionMPLS.setGeometry(QtCore.QRect(350, 50, 181, 91))
        self.btn_configuracionMPLS.setObjectName("btn_configuracionMPLS")
        self.btn_salir = QtWidgets.QPushButton(SelectorLocal)
        self.btn_salir.setGeometry(QtCore.QRect(510, 160, 93, 28))
        self.btn_salir.setObjectName("btn_salir")
        self.retranslateUi(SelectorLocal)
        QtCore.QMetaObject.connectSlotsByName(SelectorLocal)
        r=remote_conn

        #######################################################################
        self.btn_configuracionBasica.clicked.connect(lambda : self.showConfiguracionBasicaWindow(SelectorLocal,remote_conn))
        self.btn_configuracionMPLS.clicked.connect(lambda: self.showSelectorMPLS(SelectorLocal, remote_conn))
        self.btn_salir.clicked.connect(lambda: self.salir(SelectorLocal))

    def retranslateUi(self, SelectorLocal):
        _translate = QtCore.QCoreApplication.translate
        SelectorLocal.setWindowTitle(_translate("SelectorLocal", "Form"))
        self.btn_configuracionBasica.setText(_translate("SelectorLocal", "Configuracion Basica"))
        self.btn_configuracionMPLS.setText(_translate("SelectorLocal", "Configuracion MPLS-VPN"))
        self.btn_salir.setText(_translate("SelectorLocal", "Salir"))

