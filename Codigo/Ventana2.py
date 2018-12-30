'''Author: Marlon Segarra
    Proyecto de Conmutaciòn y Enrutamiento
    Paralelo#1
    Profesor: Adriana Collaguazo
'''
"Librerias importadas"
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
        master.geometry("300x200")
        self.status = tk.Label(self, fg='red')
        self.status.pack()
        usr = tk.Label(self, text='Enter username', font=('', 15))
        usr.pack()
        self.usr = tk.Entry(self)
        self.usr.pack()
        self.usr.focus()
        lbl = tk.Label(self, text='Enter password', font=('', 15))
        lbl.pack()
        self.pwd = tk.Entry(self, show="*")
        self.pwd.pack()
        self.pwd.focus()
        self.pwd.bind('<Return>', self.check)
        btn = tk.Button(self, text="Login", font=('', 15), command=self.check)

        btn.pack()

    def check(self, event=None):
        '''Chequea los eventos del botòn Login
            Si los datos son correctos retorna Bienvenido (Nombre del usuario) y la siguiente ventana
            Si la contraseña es incorrecta retorna el mensaje Contraseña incorrecta
            Si falta informaciòn retorna el respectivo mensaje con la informaciòn que falte
        '''
        with sqlite3.connect('DataBase.db') as db:
            c = db.cursor()

        # Find user If there is any take proper action
        find_user = ('SELECT * FROM user WHERE username = ? ')
        c.execute(find_user, [(self.usr.get()).strip(' ')])
        result = c.fetchall()
        if self.usr.get() == '' and self.pwd.get() == '':
            tm.showerror("Login error", "Ingrese información")
        elif self.usr.get() == '':
            tm.showerror("Login error", "Usuario faltante")
        elif self.pwd.get() == '':
            tm.showerror("Login error", "Contraseña faltante")
        elif result:
            find_pwd = ('SELECT * FROM user WHERE password = ? ')
            c.execute(find_pwd, [(self.pwd.get())])
            pwd_correcto = c.fetchall()
            if pwd_correcto:
                tm.showinfo("Login info", self.usr.get() + '\n Bienvenid@')
                self.master.change(ConfigFrame)
            else:
                ms.showerror('Oops!', 'Contraseña incorrecta.')
        else:
            ms.showerror('Oops!', 'Nombre de usuario incorrecto.')
        # Frame Packing Methords

class ConfigFrame(tk.Frame):

    def __init__(self, master=None, **kwargs):
        "Ventana principal que contiene el inicio de sesiòn del usuario"
        tk.Frame.__init__(self, master, **kwargs)

        master.title("Conectar por SSH")
        master.geometry("300x300")
        self.status = tk.Label(self, fg='red')
        self.status.pack()
        rbtn_val = tk.IntVar()
        rbtn_val.set(1)
        lbl = tk.Label(self, text='Escoja la configuración a realizar', font=('', 12))
        r_btn1 = tk.Radiobutton(self, text='P', padx=20, variable=rbtn_val, value=1, font=('', 12))
        r_btn2 = tk.Radiobutton(self, text='CE', padx=20, variable=rbtn_val, value=2, font=('', 12))
        r_btn3 = tk.Radiobutton(self, text='PE', padx=20, variable=rbtn_val, value=3, font=('', 12))
        lbl.pack()
        r_btn1.pack()
        r_btn2.pack()
        r_btn3.pack()
        rbtn_value = rbtn_val.get()
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
        btn = tk.Button(self, text="Conectar", font=('', 10), command=lambda: self.check2(btnS=rbtn_value))
        btn.pack()

    def check2(self, event=None,btnS=0):
        '''Chequea los eventos del botòn Login
            Si los datos son correctos retorna Bienvenido (Nombre del usuario) y la siguiente ventana
            Si la contraseña es incorrecta retorna el mensaje Contraseña incorrecta
            Si falta informaciòn retorna el respectivo mensaje con la informaciòn que falte
        '''
        time = datetime.now()
        with sqlite3.connect('DataBase.db') as db:
            c = db.cursor()

        # Find user If there is any take proper action
        find_user = ('SELECT * FROM user WHERE username = ? ')
        c.execute(find_user, [(self.usr.get()).strip(' ')])
        result = c.fetchall()

        find_dispIP= ('SELECT dispositivo_id FROM dispositivo WHERE direccion_ip= ? ')
        c.execute(find_dispIP, [(self.ip.get())])
        dispIP= c.fetchall()
        if btnS== 0 or self.usr.get() == '' or self.pwd.get() == ''or self.ip.get() == '':
            tm.showerror('Oops!','Falta información, inténtelo de nuevo.')
            evento=2
        elif btnS!= 0 and result:
            find_pwd = ('SELECT * FROM user WHERE password = ? ')
            c.execute(find_pwd, [(self.pwd.get())])
            pwd_correcto = c.fetchall()
            print(pwd_correcto)
            if pwd_correcto:
                evento = 1
                if btnS== 1:
                    self.master.change(ThirdFrame)
                elif btnS == 2:
                    self.master.change(FourthFrame)
                elif btnS == 3:
                    self.master.change(FifthFrame)
            else:
                evento=3
                ms.showerror('Oops!', 'Contraseña incorrecta.')
        else:
            evento = 0
            ms.showerror('Oops!', 'Nombre de usuario incorrecto.')

        try:
            inf = (self.usr.get(), time, dispIP[0][0], evento)
            insert = ''' INSERT INTO historial(usuario,hora_fecha,dispositivo,evento)
                                      VALUES(?,?,?,?) '''
            c.execute(insert, inf)
            db.commit()
        except:
            evento = 6
            ms.showerror('Oops!','Ip necesaria para realizar conexión.')
            inf2 = (self.usr.get(),time, evento)
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
        btn_ret = tk.Button(self, text="atras", command=lambda: self.master.change(ConfigFrame))
        btn_ret.pack()


class FourthFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        "Ventana para la configuraciòn del dispositivo cliente"
        tk.Frame.__init__(self, master, **kwargs)
        master.title("Configuracion CE")
        master.geometry("300x300")
        btn_ret = tk.Button(self, text="atras", command=lambda: self.master.change(ConfigFrame))
        btn_ret.pack()


class FifthFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        "Ventana para la configuraciòn del dispositivo intermedio"
        tk.Frame.__init__(self, master, **kwargs)
        master.title("Configuracion PE")
        master.geometry("300x300")
        btn_ret = tk.Button(self, text="atràs", command=lambda: self.master.change(ConfigFrame))
        btn_ret.pack()


if __name__ == "__main__":
    app = Mainframe()
    app.mainloop()