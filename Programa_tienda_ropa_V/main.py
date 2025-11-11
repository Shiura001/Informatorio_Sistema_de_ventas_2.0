import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import customtkinter as ctk
from modules.Inicio import *
from util.util_centrar_ventana import *
from tkinter import ttk
from modules.Login import *
from xampp_start import *
from modules.clean import *
from modules.alerta_stock import *

import json
import os


class Ventana(tk.Tk):
    def __init__(self):
        super().__init__()        
        self.geometry("1200x700")
        
        self.title("Sistem_Register")
        self.configure(bg=config.COLOR_CUERPO_PRINCIPAL)
        w, h = 1200, 700        
        centrar_ventana(self, w, h)
        self.minsize(1200, 700)
        self.update_idletasks()
        self.ancho_ventana = self.winfo_width()
        self.alto_ventana = self.winfo_height()
        self.iconbitmap("imagenes/icon.ico")
        self.user_name=None
        self.stock_alerta_mostrada = False
        #variables tarjetas
        self.level=None
        self.archivo_datos = "Datos/tarjetas.json"
        self.lista_costos_tarjeta = []
        self.lista_tarjetas = []
        self.cargar_datos()
        #color de la tabla
        with open("config.json", "r") as archivo:
            self.colores = json.load(archivo)

        self.table_color = self.colores["table_color"]
        self.table_color_text = self.colores["table_color_text"]
        
        #abrir archivos de tarjetas
    def cargar_datos(self):
        if os.path.exists(self.archivo_datos):
            with open(self.archivo_datos, "r") as archivo:
                datos = json.load(archivo)
                self.lista_costos_tarjeta = datos.get("costos", [])
                self.lista_tarjetas = datos.get("tarjetas", [])    

    
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        confirmacion = messagebox.askyesno("Advertencia", "¿Estás seguro que quieres salir?")
        if not confirmacion:
            return
        if confirmacion:
            cerrar_xampp(self)
        # Luego cerrás la ventana
            self.destroy()
        

    

if __name__== "__main__":
    iniciar_xampp()
    ventana = Ventana()
    
    login(ventana)
    
    #inicio(ventana)
    #
    
    ventana.mainloop()

    