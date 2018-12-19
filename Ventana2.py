import tkinter as tk
import tkinter.messagebox as tm
from tkinter import *
import paramiko
import os


class Mainframe(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.frame = FirstFrame(self)
        self.frame.pack()

    def change(self, frame):
        self.frame.pack_forget() # delete currrent frame
        self.frame = frame(self)
        self.frame.pack() # make new frame

#Primera Ventana de la Interfaz que pide usuario y contraseña
class FirstFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)

        master.title("Please enter your information")
        master.geometry("300x200")

        self.status = tk.Label(self, fg='red')
        self.status.pack()
        usr = tk.Label(self, text='Enter username')
        usr.pack()
        self.usr = tk.Entry(self)
        self.usr.pack()
        self.usr.focus()
        lbl = tk.Label(self, text='Enter password')
        lbl.pack()
        self.pwd = tk.Entry(self, show="*")
        self.pwd.pack()
        self.pwd.focus()
        self.pwd.bind('<Return>', self.check)
        btn = tk.Button(self, text="Done", command=self.check)
        btn.pack()

#Chequea eventos del botòn login

    def check(self, event=None):
        if self.pwd.get() == 'hola' and self.usr.get() == 'marlon':
            #incluir aqui la validacion de conexion ssh
            tm.showerror("Login info", "Bienvenido Marlon")
            self.master.change(SecondFrame)
        elif self.pwd.get() != 'hola' and self.usr.get() == 'marlon':
            tm.showerror("Login error", "Contraseña Incorrecta")
        elif self.pwd.get() == '' or self.usr.get() == '':
            tm.showerror("Login error", "Falta informaciòn, intèntelo de nuevo")
        else:
            tm.showerror("Login error", "Error de conexiòn")
#Ventana de selecciòn de dispositivo

class SecondFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        master.title("Main application")
        master.geometry("200x200")
        def configuration():
            if var.get() == 1:
                self.master.change(ThirdFrame)
            elif var.get()==2:
                self.master.change(FourthFrame)
            elif var.get()==3:
                self.master.change(FifthFrame)
            else:
                self.status.config(text="error inesperado")
        var=tk.IntVar()
        var.set(1)
        lbl = tk.Label(self, text='Escoja la configuración a realizar')
        op1=tk.Radiobutton(self,text='P',padx = 20, variable=var, value=1)
        op2=tk.Radiobutton(self,text='CE',padx = 20, variable=var, value=2)
        op3=tk.Radiobutton(self,text='PE',padx = 20, variable=var, value=3)
        lbl.pack()
        op1.pack()
        op2.pack()
        op3.pack()
        conf = tk.Button(self, text="Continuar",command=configuration)
        conf.pack()

#Ventana de configuraciòn del dispositivo P

class  ThirdFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        master.title("Configuracion P")
        master.geometry("300x300")
        ret = tk.Button(self, text="atras", command=lambda: self.master.change(SecondFrame))
        ret.pack()

#Ventana de configuraciòn del dispositivo CE
class  FourthFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        master.title("Configuracion CE")
        master.geometry("300x300")
        ret = tk.Button(self, text="atras", command=lambda: self.master.change(SecondFrame))
        ret.pack()

#Ventana de configuraciòn del dispositivo PE

class  FifthFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        master.title("Configuracion PE")
        master.geometry("300x300")
        ret = tk.Button(self, text="atràs", command=lambda: self.master.change(SecondFrame))
        ret.pack()

if __name__=="__main__":
    app=Mainframe()
    app.mainloop()