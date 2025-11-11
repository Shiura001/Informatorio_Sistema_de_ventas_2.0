import tkinter as tk
from customtkinter import *
#Imagenes
from util.util_imagenes import *
#Configuraciones
from config import *
#Limpiar
from modules.clean import *
#sub-menu
from util.Conexion import *
from tkinter import messagebox
from util.util_centrar_ventana import *
from modules.Inicio import *

def login(self):
    self.bind("<Return>", lambda event: inicio_s(self))
    font_awesome = family='FontAwesome',20
    fuente_pred = family='Bell MT',18
    self.geometry("480x440")
    self.resizable(False, False)
    self.minsize(400, 400)
    w, h = 480, 440
    centrar_ventana(self, w, h)
    self.update_idletasks()
    self.update()
    self.perfil=leer_imagen("imagenes/botones/perfil.png",(100,100))
    self.frame_l=tk.Canvas(self,bg=config.COLOR_BARRA_SUPERIOR,bd=0, highlightthickness=0)
    self.frame_l.pack(side=tk.TOP, fill="both",expand=True)
    perfil = tk.Label(self.frame_l, image=self.perfil,bg=config.COLOR_BARRA_SUPERIOR,foreground="black",bd=0)
    perfil.pack(side=TOP,pady=10,padx=20)

    self.register_label=tk.Label(self.frame_l,bg=config.COLOR_BARRA_SUPERIOR,text='Inicio de sesion',font=('Berlin Sans FB',25),fg='white')
    self.register_label.pack(side=tk.TOP)

    self.nombre_label=tk.Label(self.frame_l, text="Usuario",fg="#fff", font=fuente_pred, bg=config.COLOR_BARRA_SUPERIOR)
    self.nombre_label.pack(side=tk.TOP,padx=(0, 210),pady=(0,0))

    self.user_entry=CTkEntry(master=self.frame_l,fg_color='#393939',border_color='#00FFF0',text_color='white',width=300,height=30,font=font_awesome)
    self.user_entry.pack(side=tk.TOP,pady=(0,10),padx=90)

    self.contraseña_label=tk.Label(self.frame_l, text="Contraseña",fg="#fff", font=fuente_pred, bg=config.COLOR_BARRA_SUPERIOR)
    self.contraseña_label.pack(side=tk.TOP,padx=(0, 180),pady=(0,0))
    self.pass_entry=CTkEntry(master=self.frame_l,fg_color='#393939',border_color='#00FFF0',text_color='white',width=300,height=30,font=font_awesome,show="*")
    self.pass_entry.pack(side=tk.TOP,pady=(0,10),padx=90)

    self.iniciar_s = CTkButton(self.frame_l, text="Iniciar", text_color="white",command= lambda: inicio_s(self),font=("Bell MT", 25), fg_color=config.COLOR_BARRA_SUPERIOR)
    self.iniciar_s.pack(side=tk.TOP, pady=(0, 30), padx=(10, 0))



def inicio_s(self):
    conexion, cursor = conectar_bd()
    username = self.user_entry.get()
    password = self.pass_entry.get()

    try:
        consulta = "SELECT * FROM login WHERE username = %s"
        cursor.execute(consulta, (username,))
        resultado = cursor.fetchone()

        if resultado:
            # resultado[2] asumo es la columna password (hash)
            password_hash = resultado[2]

            # Validar la contraseña ingresada con el hash
            if bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8')):
                # Login exitoso
                self.user_name = resultado[1]
                self.level = resultado[3]

                conexion.close()
                clean(self)
                self.geometry("1200x700")
                self.resizable(True, True)
                self.minsize(1200, 700)
                w, h = 1200, 700
                centrar_ventana(self, w, h)
                self.update_idletasks()
                self.update()

                inicio(self)# Función para mostrar la pantalla inicial o siguiente
                stock_bajo(self)    
            else:
                messagebox.showerror("Error", "Contraseña incorrecta.")
        else:
            messagebox.showerror("Error", "El usuario no existe.")

    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")

    finally:
        try:
            cursor.close()
            conexion.close()
        except:
            pass
