

from customtkinter import *
import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
from config import *


def aplicar_descuento(self,table):
    try:
        # Crear ventana secundaria
        ventana_edicion = tk.Toplevel(self)
        ventana_edicion.title("Aplicar descuento")
        ventana_edicion.geometry("580x450")

        # Etiquetas y campos de entrada
        tk.Label(ventana_edicion, text="Descuento:").grid(row=0, column=0, padx=10, pady=5)

        label_descuento=CTkLabel(ventana_edicion,
        text="Valor fijo",
        text_color=config.Color_2,
        font=config.Font3,
        bg_color=config.COLOR_MENU_LATERAL)

        label_descuento.grid(row=1, column=1, padx=10, pady=5)
    

        entry_descuento_unidad=CTkEntry(ventana_edicion,
        font=config.Font3,
        text_color=config.Color_1,
        width=220,height=30,
        fg_color="white",
        corner_radius=10)

        entry_descuento_unidad.grid(row=2, column=1, padx=10, pady=5)



        label_descuento=CTkLabel(ventana_edicion,
        text="Valor por porcentaje",
        text_color=config.Color_2,
        font=config.Font3,
        bg_color=config.COLOR_MENU_LATERAL)

        label_descuento.grid(row=3, column=1, padx=10, pady=5)

       

        entry_porcentaje=CTkEntry(ventana_edicion,
        font=config.Font3,
        text_color=config.Color_1,
        width=220,height=30,
        fg_color="white",
        corner_radius=10)

        entry_porcentaje.grid(row=4, column=1, padx=(2, 0), pady=5)

        label_signo=CTkLabel(ventana_edicion,
        text="%",
        text_color=config.Color_2,
        font=config.Font3,
        bg_color=config.COLOR_MENU_LATERAL)
        
        label_signo.grid(row=4, column=2, padx=(0, 2), pady=5)





        btn_save=CTkButton(ventana_edicion,text="Guardar \n 'Enter'",fg_color="Green",font=config.Font2,width=150,height=30,command=lambda: aplicado(self,entry_descuento_unidad.get(),entry_porcentaje.get()))
        btn_save.grid(row=5, column=1, padx=10, pady=5)



    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona un producto")
    
    
def aplicado(self,descuento_unidad,porcentaje):
    if descuento_unidad!="" and descuento_unidad.isdigit():
        if int(descuento_unidad)>=0:
            descuento_unidad=int(descuento_unidad)
    else:
        descuento_unidad=0
    if porcentaje!="" and porcentaje.isdigit():
        if int(porcentaje)>=0:
            porcentaje=(self.total * float(porcentaje))/100
    else:
        porcentaje=0
    

    descuento = descuento_unidad + porcentaje
    self.descuento+=descuento
    self.total-=descuento
    self.total=round(self.total,2)
    self.label_total2.configure(text="$"+str(self.total))
    pass