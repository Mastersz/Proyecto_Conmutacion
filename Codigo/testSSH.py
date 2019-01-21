from Codigo.funciones2 import login_ssh

def verificarIP(txt_1,txt_2,txt_3,txt_4):
    if txt_1.isnumeric() and (int(txt_1) < 256):
        if txt_2.isnumeric() and (int(txt_2) < 256):
            if txt_3.isnumeric() and (int(txt_3) < 256):
                if txt_4.isnumeric() and (int(txt_4) < 256):
                    return "ip correcto, se procede a realizar conexión ssh"
                else:
                    return "Error en el cuarto octeto"
            else:
                return "Error en el tercer octeto"
        else:
            return "Error en el segundo octeto"
    else:
        return "Error en el primer octeto"

'''Prueba de conexion_ssh
            esceario: Se establece conexion ssh 
            con el router
        '''

def test_conexion_ssh_entro(self):
    IP = "209.165.200.1"
    usuario = "admin"
    password = "admin"
    self.assertEqual(login_ssh(IP, usuario, password), 1)


'''Prueba de conexion_ssh
    esceario: No se establece conexion ssh 
    con el router
'''
def test_conexion_ssh_fallo(self):
    host = "209.165.200.1"
    usuario = "admin"
    password = "adminn"
    self.assertEqual(login_ssh(host,usuario,password),-1)
if __name__ == "__main__":
    #Error en el  primer octeto
    txt_1 = " "
    txt_2 = "1"
    txt_3 = "8"
    txt_4 = "45"
    verificar_sesion = verificarIP(txt_1, txt_2, txt_3, txt_4)
    print(verificar_sesion)
    # Error en el  segundo octeto
    txt_1 = '124'
    txt_2 = '781'
    txt_3 = '8'
    txt_4 = '45'
    verificar_sesion = verificarIP(txt_1,txt_2,txt_3,txt_4 )
    print(verificar_sesion)

    # Verifica dirección ip válido
    txt_1 = '124'
    txt_2 = '181'
    txt_3 = '8'
    txt_4 = '45'
    verificar_sesion = verificarIP(txt_1, txt_2, txt_3, txt_4)
    print(verificar_sesion)


