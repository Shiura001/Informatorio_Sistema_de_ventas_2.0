

import tkinter as tk
#from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from customtkinter import *
#Imagenes
#from PIL import ImageTk,Image
#Configuraciones
from config import *
#from tkinter import ttk
#Limpiart
from modules.clean import *
from modules.guardar_colores import *


#sub-menu
from tkinter import ttk
import time
from modules.agregar_tarjetas import *
from modules.nuevo_usuario import *
from modules.exportar_resumen import *
import sys


def color_tabla(self):
       color_actual=self.colorbox.get()
       if color_actual=='Verde':
           color_actual='#008D26'
       elif color_actual=='Verde 2':
           color_actual="#00FF44"
       elif color_actual=='Rosa':
           color_actual="#FF8EE5"
       elif color_actual=='Magneta':
           color_actual='#FF00F2'
       self.table_color=color_actual
       self.label_intensidad.configure(fg_color=self.table_color)
       self.update_idletasks()
       guardar_colores(self)
#cambiar color de la letra de la tabla

def color_letra_tabla(self):
       color_actual=self.colorbox_letra.get()
       if color_actual=='Blanco':
           color_actual="#FFFFFF"
       elif color_actual=='Blanco 2':
           color_actual="#D3D3D3"
       elif color_actual=='Negro':
           color_actual="#000000"
       elif color_actual=='Negro 2':
           color_actual="#1B1B1B"
       elif color_actual=='Gris':
           color_actual="#676767"
       self.table_color_text=color_actual
       self.label_intensidad.configure(text_color=self.table_color_text)
       self.update_idletasks()
       guardar_colores(self)







def configuration(self,controller_menu):
    self.bind("<Escape>", lambda event: controller_menu(self,"inicio"))
    
    # variable menu_activo
    self.Menu_activo = "Configuration"

    self.side_bar=tk.Frame(self,bg=config.COLOR_MENU_LATERAL,width=200)
    self.side_bar.pack(side=tk.LEFT, fill="both")


    self.btn_volver=CTkButton(self.side_bar,
        font=config.Font2,                  
        text="Volver",
        command=lambda: controller_menu(self,"inicio"),
        text_color=config.Color_1,
        fg_color="yellow",
        width=30,height=50,
        anchor="center",
        corner_radius=10)
    self.btn_volver.pack(pady=20, padx=20)

    self.contenedor_central = tk.Frame(self, bg=config.COLOR_CUERPO_PRINCIPAL, width=300, height=300)
    self.contenedor_central.pack(side=tk.TOP, expand=True, anchor="center")




    self.btn_tarjeta=CTkButton(self.side_bar,
        font=config.Font3,
        command= lambda: agregar_tarjetas(self),                
        text="Tarjetas",
        text_color=config.Color_1,
        fg_color="#F3FF96",
        width=30,height=50,
        anchor="center",
        corner_radius=20)
    self.btn_tarjeta.pack(pady=10, padx=30)


    if self.level=="admin":
        self.btn_nuevo_usuario=CTkButton(self.side_bar,
            font=config.Font3,
            command= lambda: nuevo_usuario(self),                
            text="Crear nuevo usuario",
            text_color=config.Color_1,
            fg_color="#F3FF96",
            width=30,height=50,
            anchor="center",
            corner_radius=20)
        self.btn_nuevo_usuario.pack(pady=10, padx=10)

    self.btn_export=CTkButton(self.side_bar,
            font=config.Font3,
            command= lambda: exportar_resumen(self),                
            text="Exportar Resumen",
            text_color=config.Color_1,
            fg_color="#F3FF96",
            width=30,height=50,
            anchor="center",
            corner_radius=20)
    self.btn_export.pack(pady=10, padx=10)

#cambiar color de la tabla
    
    self.label_color_texto=CTkLabel(self.side_bar,
        font=config.Font3,                
        text="Color Texto",
        text_color=config.Color_2,
        fg_color=config.COLOR_BARRA_SUPERIOR,
        width=30,height=50,
        anchor="center")
    self.label_color_texto.pack()
    
    self.colorbox_letra=CTkComboBox(self.side_bar,values=['Blanco','Blanco 2','Negro','Negro 2','Gris'], command = lambda opcion: color_letra_tabla(self))
    self.colorbox_letra.pack()

    self.label_color_tabla=CTkLabel(self.side_bar,
        font=config.Font3,                
        text="Color Tabla",
        text_color=config.Color_2,
        fg_color=config.COLOR_BARRA_SUPERIOR,
        width=30,height=50,
        anchor="center")
    self.label_color_tabla.pack()

    self.colorbox=CTkComboBox(self.side_bar,values=['Verde','Verde 2','Rosa','Magneta'], command = lambda opcion: color_tabla(self))
    self.colorbox.pack()


    self.label_intensidad=CTkButton(self.side_bar,
        font=config.Font3,                
        text="Color",
        text_color=config.Color_1,
        fg_color=self.table_color,
        width=30,height=50,
        anchor="center")
    
    self.label_intensidad.pack(pady=10, padx=30)

    self.slider1=CTkSlider(self.side_bar,from_=0, to=255,command= lambda valor: intensidad(self))
    self.slider1.pack()

def intensidad(self):
     valor= int(self.slider1.get())
     print(valor)
     intensidad1=int(self.table_color[1:3],16)
     color=self.table_color[3:]
     intensidad1=valor
     self.table_color=f"#{intensidad1:02X}{color}"
     print(self.table_color)
     self.label_intensidad.configure(fg_color=self.table_color)
     self.update_idletasks()
     guardar_colores(self)

     
     
    
#style.configure("Treeview", font=('Michroma', 12),rowheight=70,background="#FF00F2")
 
#F3FF96
   

