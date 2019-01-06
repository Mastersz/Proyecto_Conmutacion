'''Author: Marlon Segarra y Dayana Garzón
    Proyecto de Conmutaciòn y Enrutamiento
    Paralelo#1
    Profesor: Adriana Collaguazo
'''
"Librerias importadas"
import paramiko
from tkinter import messagebox as ms
import tkinter as tk
import tkinter.messagebox as tm
import sqlite3
from datetime import datetime
# make database and users (if not exists already) table at programme start up
with sqlite3.connect('DataBase.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL ,password TEX NOT NULL);')
db.commit()
db.close()
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

rbtn_value=0
class Mainframe(tk.Tk):
    def __init__(self):
        "Inicia la ventana principal y la hace visible"
        tk.Tk.__init__(self)
        self.frame = FirstFrame(self)
        self.frame.pack()

    def change(self, frame):
        "Define el cambio de ventana creando una nueva luego de un determinado suceso"
        self.frame.pack_forget()  # delete actual frame
        self.frame = frame(self)
        self.frame.pack()  # make new frame


class FirstFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        "Ventana principal que contiene el inicio de sesiòn del usuario"
        tk.Frame.__init__(self, master, **kwargs)

        master.title("Please enter your information")
        master.geometry("300x300")
        self.status = tk.Label(self, fg='red')
        self.status.pack()
        # Ingreso de la información del usuario para realizar la conexión
        rbtn_val = tk.IntVar()
        rbtn_val.set(1)
        lbl = tk.Label(self, text='Escoja la configuración a realizar', font=('', 12))
        r_btn1 = tk.Radiobutton(self, text='P', padx=20, variable=rbtn_val, value=1, font=('', 12))
        r_btn2 = tk.Radiobutton(self, text='PE', padx=20, variable=rbtn_val, value=2, font=('', 12))
        r_btn3 = tk.Radiobutton(self, text='CE', padx=20, variable=rbtn_val, value=3, font=('', 12))
        lbl.pack()
        r_btn1.pack()
        r_btn2.pack()
        r_btn3.pack()
        tipos = ["p","pe","ce"]
        ip = tk.Label(self, text='IP', font=('', 10))
        ip.pack()
        self.ip = tk.Entry(self)
        self.ip.pack()
        self.ip.focus()
        usr = tk.Label(self, text='Usuario', font=('', 10))
        usr.pack()
        self.usr = tk.Entry(self)
        self.usr.pack()
        self.usr.focus()
        lbl = tk.Label(self, text='Contraseña', font=('', 10))
        lbl.pack()
        self.pwd = tk.Entry(self, show="*")
        self.pwd.pack()
        self.pwd.focus()
        btn = tk.Button(self, text="Conectar", font=('', 10), command=lambda: self.conectar(btnS=rbtn_val.get(), tipoDispositivo= tipos[rbtn_val.get() - 1]))  # Al presionar Conectar se activa la función connecSSH
        btn.pack()

    def conectar(self, event=None, btnS=0, tipoDispositivo = ""):
        '''Chequea los eventos del botòn Login
                    Si los datos son correctos retorna Bienvenido (Nombre del usuario) y la siguiente ventana
                    Si la información de contraseña o usuario es incorrecta retorna el mensaje del contraseña o usuario incorrecto
                    Si falta informaciòn retorna el respectivo mensaje con la informaciòn que falte
                '''
        ''' eventos del botòn conectar
            evento 0: nombre de usuario incorrecto
            evento 1: sesión correcta
            evento 2: falta información
            evento 3: clave incorrecta
            evento 4: falla de conexión remota
            evento 5: error de conexión
            evento 6: falta dirección ip (se lo analiza aparte para evitar el IndexError)
            evento 7: La direccion ip ingresada no correspone al dispositivo ingresado
        Una vez chequeado el evento se procede a registrar la información ingresada en el historial de la base de datos
        '''
        time = datetime.now()
        with sqlite3.connect('DataBase.db') as db:
            c = db.cursor()

        # Find user If there is any take proper action
        find_user = ('SELECT * FROM user WHERE username = ? ')
        c.execute(find_user, [(self.usr.get()).strip(' ')])
        result = c.fetchall()

        find_dispIP = ('SELECT dispositivo_id FROM dispositivo WHERE direccion_ip= ? ')
        c.execute(find_dispIP, [(self.ip.get())])
        dispID = c.fetchall()

        if btnS == 0 or self.usr.get() == '' or self.pwd.get() == '' or self.ip.get() == '':
            tm.showerror('Oops!', 'Falta información, inténtelo de nuevo.')
            evento = 2
        elif btnS != 0 and result:
            find_pwd = ('SELECT * FROM user WHERE username = ? and password = ? ')
            c.execute(find_pwd, [(self.usr.get()), (self.pwd.get())])
            pwd_correcto = c.fetchall()
            if pwd_correcto:
                find_dispositivo = ('SELECT dispositivo_tipo FROM dispositivo WHERE direccion_ip= ? and dispositivo_tipo= ? ')
                c.execute(find_dispositivo, [(self.ip.get()), (tipoDispositivo)])
                dispositivo_correcto = c.fetchall()
                if dispositivo_correcto:
                    evento = 1
                    if tipoDispositivo == "p":
                        ssh.connect('192.168.1.10', port=22, username=self.usr.get(), password=self.pwd.get())
                        stdin, stdout, stderr = ssh.exec_command('show ip interface brief')
                        output = stdout.readlines()
                        type(output)
                        print('\n'.join(output))
                        self.master.change(ThirdFrame)
                    elif tipoDispositivo == "ce":
                        ssh.connect('192.168.1.10', port=22, username=self.usr.get(), password=self.pwd.get())
                        stdin, stdout, stderr = ssh.exec_command('show ip interface brief')
                        output = stdout.readlines()
                        type(output)
                        print('\n'.join(output))
                        self.master.change(FourthFrame)
                    elif tipoDispositivo == "pe":
                        ssh.connect('192.168.1.10', port=22, username=self.usr.get(), password=self.pwd.get())
                        stdin, stdout, stderr = ssh.exec_command('show ip interface brief')
                        output = stdout.readlines()
                        type(output)
                        print('\n'.join(output))
                        self.master.change(FifthFrame)
                else:
                    evento = 7
                    ms.showerror('Oops!', 'Dirección ip ingresada no corresponde al tipo de dispositivo seleccionado.')
            else:
                evento = 3
                ms.showerror('Oops!', 'Contraseña incorrecta.')
        else:
            evento = 0
            ms.showerror('Oops!', 'Nombre de usuario incorrecto.')

        try:
            inf = (self.usr.get(), time, dispID[0][0], evento)
            insert = ''' INSERT INTO historial(usuario,hora_fecha,dispositivo,evento)
                                              VALUES(?,?,?,?) '''
            c.execute(insert, inf)
            db.commit()
        except:
            evento = 6
            ms.showerror('Oops!', 'Ip necesaria para realizar conexión.')
            inf2 = (self.usr.get(), time, evento)
            insert2 = ''' INSERT INTO historial(usuario,hora_fecha,evento)
                                                          VALUES(?,?,?) '''
            c.execute(insert2, inf2)
            db.commit()

class ThirdFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        "Ventana para la configuraciòn del dispositivo principal"
        tk.Frame.__init__(self, master, **kwargs)
        master.title("Configuracion P")
        master.geometry("300x300")
        #el puerto SSH que use nuestro servidor
        ssh_puerto=22
        #el comando que vamos a ejecutar en el servidor
        comando='ls'
        # Conectamos al servidor
        conexion = paramiko.Transport((self.ip.get(), ssh_puerto))
        conexion.connect(self.usr.get(), self.pwd.get())
        # Abrimos una sesión en el servidor
        canal = conexion.open_session()
        # Ejecutamos el comando 'ls' para ver el listado de archivos y directorios
        canal.exec_command(comando)
        salida = canal.makefile('rb', -1).readlines()
        if salida:
            # Si ha ido todo bien mostramos el listado de directorios
            usr = tk.Label(self, salida, font=('', 10))
            usr.pack()
            btn_ret = tk.Button(self, text="atras", command=lambda: self.master.change(FirstFrame))
            btn_ret.pack()
        else:
            # Si se ha producido algún error lo mostramos
            error=canal.makefile_stderr('rb', -1).readlines()
            usr = tk.Label(self, error, font=('', 10))
            usr.pack()
            btn_ret = tk.Button(self, text="atras", command=lambda: self.master.change(FirstFrame))
            btn_ret.pack()
        conexion.close()



class FourthFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        "Ventana para la configuraciòn del dispositivo cliente"
        tk.Frame.__init__(self, master, **kwargs)
        master.title("Configuracion CE")
        master.geometry("300x300")
        usr = tk.Label(self, text="configuracion CE", font=('', 10))
        usr.pack()
        btn_ret = tk.Button(self, text="atras", command=lambda: self.master.change(FirstFrame))
        btn_ret.pack()



class FifthFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        "Ventana para la configuraciòn del dispositivo intermedio"
        tk.Frame.__init__(self, master, **kwargs)
        master.title("Configuracion PE")
        master.geometry("300x300")
        # el puerto SSH que use nuestro servidor
        ssh_puerto = 22
        # el comando que vamos a ejecutar en el servidor
        comando = 'ls'
        # Conectamos al servidor
        conexion = paramiko.Transport((self.ip.get(), ssh_puerto))
        conexion.connect(self.usr.get(), self.pwd.get())
        # Abrimos una sesión en el servidor
        canal = conexion.open_session()
        # Ejecutamos el comando 'ls' para ver el listado de archivos y directorios
        canal.exec_command(comando)
        salida = canal.makefile('rb', -1).readlines()
        if salida:
            # Si ha ido todo bien mostramos el listado de directorios
            usr = tk.Label(self, salida, font=('', 10))
            usr.pack()
            btn_ret = tk.Button(self, text="atras", command=lambda: self.master.change(FirstFrame))
            btn_ret.pack()
        else:
            # Si se ha producido algún error lo mostramos
            error = canal.makefile_stderr('rb', -1).readlines()
            usr = tk.Label(self, error, font=('', 10))
            usr.pack()
            btn_ret = tk.Button(self, text="atras", command=lambda: self.master.change(FirstFrame))
            btn_ret.pack()
        conexion.close()

if __name__ == "__main__":
    app = Mainframe()
    app.mainloop()