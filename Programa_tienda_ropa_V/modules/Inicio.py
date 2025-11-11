import tkinter as tk
#from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from customtkinter import *
#Imagenes
from util.util_imagenes import *
#from PIL import ImageTk,Image
#Configuraciones
from config import *
#from tkinter import ttk
#Limpiart
from modules.clean import *
#sub-menu
from modules.Stock import *

from modules.registro import *

from modules.venta import *
from modules.configuracion import *
from modules.alerta_stock import *
import sys

import webbrowser



#----------------------------------------controlador menu----------------------------------------------------------------------
def controller_menu(self,menu):
        if self.Menu_activo==menu:
            pass
        else:
            try:
                if menu=="stock":
                    clean(self)
                    stock(self,controller_menu)
                    self.Menu_activo="stock"
                    print(self.Menu_activo)
                if menu=="registro":
                    if self.level=="admin":
                        clean(self)
                        interfaz_register(self,controller_menu)
                        self.Menu_activo="registro"
                        print(self.Menu_activo)
                if menu=="inicio":
                    if self.sub_menu=="push_stock":
                        clean(self)
                        stock(self,controller_menu)
                        print("holas")
                        self.sub_menu=None
                    else:       
                        clean(self)
                        inicio(self)
                        self.Menu_activo="inicio"
                        print(self.Menu_activo)
                if menu=="ventas":
                    clean(self)
                    venta(self,controller_menu)
                    self.Menu_activo="ventas"
                    print(self.Menu_activo)
                if menu=="configuration":
                    clean(self)
                    configuration(self,controller_menu)
                    self.Menu_activo="ventas"
                    print(self.Menu_activo)
                
            except AttributeError:
                 pass




#######################################################################################################################


#INICIO DE PANTALLA
def inicio(self):
    iniciar_fecha(self)
    self.sub_menu= None
    # variable menu_activo
    self.Menu_activo = None

    # Contenedor principal (cuerpo)
    self.contenedor1 = tk.Frame(self, bg=config.COLOR_CUERPO_PRINCIPAL, width=300, height=300)
    self.contenedor1.pack(side=tk.RIGHT, fill="both", expand=True, anchor="center")

    # Barra lateral izquierda (con el título)
    self.side_bar0 = tk.Frame(self, bg=config.COLOR_CUERPO_PRINCIPAL, width=300)
    self.side_bar0.pack(side=tk.LEFT, fill="both", expand=True)
    
    
    
    

    # Contenedores de botones a la derecha
    self.side_bar2 = tk.Frame(self.contenedor1, bg="blue", width=100)
    self.side_bar2.pack(side=tk.RIGHT, fill="both", expand=True, anchor="center")

    self.side_bar = tk.Frame(self.contenedor1, bg="green", width=100)
    self.side_bar.pack(side=tk.RIGHT, fill="both", expand=True, anchor="center")
    
    # Imágenes
    
    self.ventas = leer_imagen("imagenes/botones/ventas.png", (100, 100))
    self.stock = leer_imagen("imagenes/botones/stock.png", (100, 100))
    self.compras = leer_imagen("imagenes/botones/compras.png", (100, 100))
    self.config = leer_imagen("imagenes/botones/config.png", (100, 100))
    self.perfil_1 = leer_imagen("imagenes/botones/perfil.png", (100, 100))

    # Configuración para que los botones se expandan equitativamente en side_bar
    self.side_bar.grid_rowconfigure((0, 1), weight=1)
    self.side_bar.grid_columnconfigure(0, weight=1)

    self.side_bar2.grid_rowconfigure((0, 1), weight=1)
    self.side_bar2.grid_columnconfigure(0, weight=1)

   
    self.perfil = tk.Label(self.side_bar0, image=self.perfil_1, background=config.COLOR_CUERPO_PRINCIPAL,foreground="black",bd=0)
    self.perfil.pack(side=TOP,anchor="w")

    self.label_user = tk.Label(
        self.side_bar0,
        text=self.user_name,
        fg="white",
        font=("MuseoModerno", 13),
        bg=config.COLOR_CUERPO_PRINCIPAL)
    self.label_user.pack(side=tk.TOP, anchor="w",padx=14)


    self.label_titulo = tk.Label(
        self.side_bar0,
        text="Sistema de Ventas\n Fixware",
        fg="white",
        font=("MuseoModerno", 45),
        bg=config.COLOR_CUERPO_PRINCIPAL)
    self.label_titulo.pack(side=tk.TOP, anchor="center", expand=True,pady=0)

    

    self.btn_ayuda = CTkButton(
        self.side_bar0,
        text="Contactanos",
        command= lambda: abrir_link(),
        fg_color=config.COLOR_CUERPO_PRINCIPAL,
        font=("MuseoModerno", 30),
        border_color="white",
        border_width=1,
        border_spacing=5,
        corner_radius=10,)
    self.btn_ayuda.pack(side=tk.TOP, anchor="s",padx=10)

    self.btn_ayuda2 = CTkButton(
        self.side_bar0,
        command= lambda: abrir_link(),
        text="Terminos y condiciones",
        fg_color=config.COLOR_CUERPO_PRINCIPAL,
        font=("MuseoModerno", 10),
        border_color="white",
        border_width=1,
        border_spacing=5,
        corner_radius=10,)
    self.btn_ayuda2.pack(side=tk.RIGHT, anchor="sw",padx=10)
    

    self.label_marca = tk.Label(
        self.side_bar0,
        text="Power by: GR Fixware             Version 1.0",
        fg="white",
        font=("Michroma", 12),
        bg=config.COLOR_CUERPO_PRINCIPAL)
    self.label_marca.pack(side=tk.BOTTOM, anchor="sw", expand=True,pady=0)

 # Botones------------------------------------------------------------------------------------------------------------------------------------


    btn_ventas = tk.Button(self.side_bar,image=self.ventas,compound="top", text="Ventas", command = lambda: controller_menu(self,"ventas"), font=config.Font, bd=0,background="#140087", foreground="white", activebackground=config.FORGROUND_COLOR,width=200)
    btn_ventas.grid(row=0, column=0, sticky="nsew")

    btn_compras = tk.Button(self.side_bar,image=self.compras,compound="top", text="Registros", command = lambda: controller_menu(self,"registro"), font=config.Font, bd=0,background="#008709", foreground="white", activebackground=config.FORGROUND_COLOR,width=200)
    btn_compras.grid(row=1, column=0, sticky="nsew")

    btn_stock = tk.Button(self.side_bar2,image=self.stock,compound="top", text="Stock", command = lambda: controller_menu(self,"stock"), font=config.Font, bd=0,background="#550096", foreground="white", activebackground=config.FORGROUND_COLOR,width=200)
    btn_stock.grid(row=0, column=0, sticky="nsew")

    btn_config = tk.Button(self.side_bar2,image=self.config,compound="top", text="Config", command = lambda: controller_menu(self,"configuration"), font=config.Font, bd=0,background="#2C3240", foreground="white", activebackground=config.FORGROUND_COLOR,width=200)
    btn_config.grid(row=1, column=0, sticky="nsew")

        


def salir(self):
    self.destroy()  # Cierra la ventana de Tkinter
    sys.exit() 
     
    
def abrir_link():
        webbrowser.open("https://sites.google.com/view/fixware/p%C3%A1gina-principal")




    
    

# menu de configuraciones------------------------------------------------------------------------------------------------------------------------------------

    
    
        
     