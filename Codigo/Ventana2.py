'''Author: Marlon Segarra
    Proyecto de Conmutaciòn y Enrutamiento
    Paralelo#1
    Profesor: Adriana Collaguazo
'''
"Librerias importadas"

import tkinter as tk
import tkinter.messagebox as tm



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
        master.geometry("400x300")
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
        btn = tk.Button(self, text="Login", command=self.check)

        btn.pack()

    def check(self, event=None):
        '''Chequea los eventos del botòn Login
            Si los datos son correctos retorna Bienvenido (Nombre del usuario) y la siguiente ventana
            Si la contraseña es incorrecta retorna el mensaje Contraseña incorrecta
            Si falta informaciòn retorna el respectivo mensaje con la informaciòn que falte
        '''
        if self.pwd.get() == 'hola' and self.usr.get() == 'marlon':
            # incluir aqui la validacion de conexion ssh
            tm.showerror("Login info", "Bienvenido Marlon")
            self.master.change(SecondFrame)
        elif self.pwd.get() != 'hola' and self.usr.get() == 'marlon':
            tm.showerror("Login error", "Contraseña Incorrecta")
        elif self.usr.get() == '':
            tm.showerror("Login error", "Usuario faltante")
        elif self.pwd.get() == '':
            tm.showerror("Login error", "Contraseña faltante")


class SecondFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        "Inicializa la segunda ventana con los dispositivos a configurar"
        tk.Frame.__init__(self, master, **kwargs)
        master.title("Main application")
        master.geometry("200x200")

        def configuration():
            '''alida el redio botòn seleccionado y despliega la ventana correspondiente
            para realizar la configuraciòn del dispositivo
            '''
            if rbtn_val.get() == 1:
                self.master.change(ThirdFrame)
            elif rbtn_val.get() == 2:
                self.master.change(FourthFrame)
            elif rbtn_val.get() == 3:
                self.master.change(FifthFrame)
            else:
                self.status.config(text="error inesperado")

        rbtn_val = tk.IntVar()
        rbtn_val.set(1)
        lbl = tk.Label(self, text='Escoja la configuración a realizar')
        r_btn1 = tk.Radiobutton(self, text='P', padx=20, variable=rbtn_val, value=1)
        r_btn2 = tk.Radiobutton(self, text='CE', padx=20, variable=rbtn_val, value=2)
        r_btn3 = tk.Radiobutton(self, text='PE', padx=20, variable=rbtn_val, value=3)
        lbl.pack()
        r_btn1.pack()
        r_btn2.pack()
        r_btn3.pack()
        btn_continuar = tk.Button(self, text="Continuar", command=configuration)
        btn_log_out = tk.Button(self, text="Cerrar Sesiòn", command=lambda: self.master.change(FirstFrame))
        btn_continuar.pack()
        btn_log_out.pack()


class ThirdFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        "Ventana para la configuraciòn del dispositivo principal"
        tk.Frame.__init__(self, master, **kwargs)
        master.title("Configuracion P")
        master.geometry("300x300")
        btn_ret = tk.Button(self, text="atras", command=lambda: self.master.change(SecondFrame))
        btn_ret.pack()


class FourthFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        "Ventana para la configuraciòn del dispositivo cliente"
        tk.Frame.__init__(self, master, **kwargs)
        master.title("Configuracion CE")
        master.geometry("300x300")
        btn_ret = tk.Button(self, text="atras", command=lambda: self.master.change(SecondFrame))
        btn_ret.pack()


class FifthFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        "Ventana para la configuraciòn del dispositivo intermedio"
        tk.Frame.__init__(self, master, **kwargs)
        master.title("Configuracion PE")
        master.geometry("300x300")
        btn_ret = tk.Button(self, text="atràs", command=lambda: self.master.change(SecondFrame))
        btn_ret.pack()


if __name__ == "__main__":
    app = Mainframe()
    app.mainloop()
