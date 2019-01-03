"""
Script en Python de conexión ssh en Ubuntu
# las librerias
import paramiko
import os
from sys import stdin
# comando
print ('Comando a ejecutar (p.e: dir): ')
comando=str(stdin.readline())
# el cliente ssh del modulo paramiko
print ('Introduce ip del servidor ssh: ')
ip=str(stdin.readline())
# se establece la conexion
conexion = paramiko.Transport((ip, 22))
print ('usuario = ')
usuario=str(raw_input())
print ('clave = ')
clave=str(raw_input())
# validamos la conexion
conexion.connect(username = usuario, password = clave)
# sesion
canal = conexion.open_session()
# ejecutar comando, si es win y en Ingles el ssh-server -> p.e: arp -a | findstr "dynamic"
canal.exec_command(comando)
# la salida del comando
salida = canal.makefile('rb', -1).readlines()
print (salida)
conexion.close()
"""



#Programa que ejecuta un comando de forma remota

#Se importa el módulo paramiko
import paramiko

#Se crea la función ssh donde se le pasa el usuario, la IP del equipo remoto, el comando a ejecutar, la clave
#del usuario en el equipo remoto (en este caso se autentica por llaves), puerto de la conexión ssh y se guarda
#un log de la conexión.

def ssh(usuario,hostname,comando,puerto=22,log="DataBase.db"):
        #Se guarda el log
        paramiko.util.log_to_file(log)
        #Se define la ruta donde se encuentra la llave RSA
        llave = "/Users/schacon/.ssh/id_rsa"
        #Se carga la llave RSA
        key = paramiko.RSAKey.from_private_key_file(llave)
        #Se crea la instancia del cliente ssh
        conexion = paramiko.SSHClient()
        #Se carga las llaves del host para validar la autenticación por llaves.
        conexion.load_system_host_keys()
        #Se establece la conexión pasando la IP, puerto del equipo, el usuario y su clave.
        conexion.connect(hostname,puerto,usuario,pkey=key)
        #Se crea una tupla con la entrada estándar, salida estándar y los mensajes de error al ejecutar el comando.
        stdin,stdout,stderr = conexion.exec_command(comando)
        #Se lee la salida estándar y se presenta la información en pantalla.
        print (stdout.read())
        #Se cierra la conexión ssh.
        conexion.close()

if __name__ == "__main__":
        #Se ejecuta la función
        ssh("admin","192.168.10.1","ls -l")