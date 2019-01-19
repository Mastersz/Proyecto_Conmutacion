from GUI_FINAL.funciones2 import *
from GUI_FINAL.remote import *
import unittest

class test_funciones_principales(unittest.TestCase):
    '''Prueba de validar_formato_IP
           esceario: Al ingresar un octeto de la
           direccion ip no es decimal retorna false
       '''

    def test_verificarIP(self, Form):
        ip = "192.168.5"
        self.verificarIP(ip,Form)


    '''Prueba de conexion_ssh
        esceario: Se establece conexion ssh 
        con el router
    '''
    def test_login_ssh(self):
        host = "209.165.200.1"
        usuario = "admin"
        password = "admin"
        self.assertEqual(login_ssh(host,usuario,password),1)



if __name__ == '__main__':
    unittest.main()