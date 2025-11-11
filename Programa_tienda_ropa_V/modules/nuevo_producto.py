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
from tkinter import ttk
from modules.crud_img_producto import *

from tkcalendar import Calendar

import customtkinter






def nuevo_producto(self):
    self.sub_menu="push_stock"
    clean(self.contenedor_central)

    label_ejemple = CTkLabel(self.contenedor_central, text="Agregar Producto", font=config.Font2, text_color=config.Color_2)
    label_ejemple.pack(side=TOP, anchor="n", pady=10)
    self.btn_save=CTkButton(self.contenedor_central,text="Guardar",fg_color="Green",font=config.Font2,width=150,height=30,command=lambda: insert_product(self))
    self.btn_save.pack(side=BOTTOM,pady=10)


    frame1 = CTkFrame(self.contenedor_central, fg_color=config.Color_4, corner_radius=20)
    frame1.pack(side=LEFT, expand=True, fill="both")

# Labels y Entries con grid (dos columnas: label y entrada)
# Fila, columna

    self.label_codigo = CTkLabel(frame1, text="Codigo", font=config.Font2, text_color=config.Color_1)
    self.label_codigo.grid(row=0, column=0, padx=50, pady=(20,30))
    self.entry_codigo = CTkEntry(frame1, font=config.Font2, width=200, height=30, fg_color=config.Color_2,
                                 border_color=config.Color_3, text_color=config.Color_1, corner_radius=50)
    self.entry_codigo.grid(row=0, column=1, padx=10, pady=5)

    self.label_nombre = CTkLabel(frame1, text="Nombre", font=config.Font2, text_color=config.Color_1)
    self.label_nombre.grid(row=1, column=0, padx=10, pady=(20,30))
    self.entry_nombre = CTkEntry(frame1, font=config.Font2, width=200, height=30, fg_color=config.Color_2,
                                 border_color=config.Color_3, text_color=config.Color_1, corner_radius=50)
    self.entry_nombre.grid(row=1, column=1, padx=10, pady=5)

    self.label_color = CTkLabel(frame1, text="Color", font=config.Font2, text_color=config.Color_1)
    self.label_color.grid(row=2, column=0, padx=10, pady=(20,30))
    self.entry_color = CTkEntry(frame1, font=config.Font2, width=200, height=30, fg_color=config.Color_2,
                                border_color=config.Color_3, text_color=config.Color_1, corner_radius=50)
    self.entry_color.grid(row=2, column=1, padx=10, pady=5)

    self.label_talle = CTkLabel(frame1, text="Talle", font=config.Font2, text_color=config.Color_1)
    self.label_talle.grid(row=3, column=0, padx=10, pady=(20,30))
    self.entry_talle = CTkEntry(frame1, font=config.Font2, width=200, height=30, fg_color=config.Color_2,
                                border_color=config.Color_3, text_color=config.Color_1, corner_radius=50)
    self.entry_talle.grid(row=3, column=1, padx=10, pady=5)

    self.label_marca = CTkLabel(frame1, text="Marca", font=config.Font2, text_color=config.Color_1)
    self.label_marca.grid(row=4, column=0, padx=10, pady=(20,30))
    self.entry_marca = CTkEntry(frame1, font=config.Font2, width=200, height=30, fg_color=config.Color_2,
                                border_color=config.Color_3, text_color=config.Color_1, corner_radius=50)
    self.entry_marca.grid(row=4, column=1, padx=10, pady=5)

    self.label_categoria = CTkLabel(frame1, text="Categoría", font=config.Font2, text_color=config.Color_1)
    self.label_categoria.grid(row=5, column=0, padx=10, pady=(20,30))
    
    self.entry_categoria = CTkEntry(frame1, font=config.Font2, width=200, height=30, fg_color=config.Color_2,
                                    border_color=config.Color_3, text_color=config.Color_1, corner_radius=50)
    self.entry_categoria.grid(row=5, column=1, padx=10, pady=5)

    self.label_stock = CTkLabel(frame1, text="Stock_total", font=config.Font2, text_color=config.Color_1)
    self.label_stock.grid(row=0, column=2, padx=50, pady=(20,30))
    self.entry_stock = CTkEntry(frame1, font=config.Font2, width=200, height=30, fg_color=config.Color_2,
                                border_color=config.Color_3, text_color=config.Color_1, corner_radius=50)
    self.entry_stock.grid(row=0, column=3, padx=10, pady=(0,2))

    self.label_stock_min = CTkLabel(frame1, text="Stock_minimo", font=config.Font2, text_color=config.Color_1)
    self.label_stock_min.grid(row=1, column=2, padx=50, pady=(20,30))
    self.entry_stock_min = CTkEntry(frame1, font=config.Font2, width=200, height=30, fg_color=config.Color_2,
                                    border_color=config.Color_3, text_color=config.Color_1, corner_radius=50)
    self.entry_stock_min.grid(row=1, column=3, padx=10, pady=(0,2))

    self.label_precio_compra = CTkLabel(frame1, text="Precio de compra", font=config.Font2, text_color=config.Color_1)
    self.label_precio_compra.grid(row=2, column=2, padx=50, pady=(20,30))
    self.entry_precio_compra = CTkEntry(frame1, font=config.Font2, width=200, height=30, fg_color=config.Color_2,
                                        border_color=config.Color_3, text_color=config.Color_1, corner_radius=50)
    self.entry_precio_compra.grid(row=2, column=3, padx=10, pady=(0,2))
#
    self.label_precio_venta = CTkLabel(frame1, text="Precio de venta", font=config.Font2, text_color=config.Color_1)
    self.label_precio_venta.grid(row=3, column=2, padx=50, pady=(20,30))
    self.entry_precio_venta = CTkEntry(frame1, font=config.Font2, width=200, height=30, fg_color=config.Color_2,
                                       border_color=config.Color_3, text_color=config.Color_1, corner_radius=50)
    self.entry_precio_venta.grid(row=3, column=3, padx=10, pady=(0,2))

    self.btn_select=CTkButton(frame1,text="Selecionar_Foto",font=config.Font,height=30,text_color=config.Color_2,command=lambda:abrir_imagen(self))
    self.btn_select.grid(row=4, column=3, padx=10, pady=(0,2))



 
import re
def insert_product(self):
    cod = self.entry_codigo.get()
    nom = self.entry_nombre.get()
    color = self.entry_color.get()
    talle = self.entry_talle.get()
    marca = self.entry_marca.get()
    categ = self.entry_categoria.get()
    stock = self.entry_stock.get()
    stockm = self.entry_stock_min.get()
    prec_com = self.entry_precio_compra.get()
    prec_ven = self.entry_precio_venta.get()

    if not cod or not nom or not color or not talle or not marca or not categ or not stock or not stockm or not prec_com or not prec_ven:
        messagebox.showerror("Error", "Todos los campos son obligatorios.")
        return

    try:
        stock = int(stock)
        stockm = int(stockm)
        prec_com = float(prec_com)
        prec_ven = float(prec_ven)

        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")
        if stockm < 0:
            raise ValueError("El stock mínimo no puede ser negativo.")
        if prec_com <= 0 or prec_ven <= 0:
            raise ValueError("Los precios deben ser mayores a 0.")
        if prec_ven < prec_com:
            raise ValueError("El precio de venta no puede ser menor que el de compra.")

    except ValueError as e:
        messagebox.showerror("Error de validación", str(e))
        return

    from modules.registro import register

    try:
        conexion, cursor = conectar_bd()

        # ✅ Verificar si el código ya existe
        cursor.execute("SELECT COUNT(*) FROM productos WHERE codigo_producto = %s", (cod,))
        resultado = cursor.fetchone()
        if resultado[0] > 0:
            messagebox.showerror("Error", "El código de producto ya existe. Ingrese uno diferente.")
            return

        consulta = """
            INSERT INTO productos 
            (codigo_producto, nombre, color, talle, marca, categoria, stock_total, stock_min, precio_compra, precio_venta)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        datos = (cod, nom, color, talle, marca, categ, stock, stockm, prec_com, prec_ven)

        cursor.execute(consulta, datos)
        conexion.commit()
        self.id_producto_generado = cursor.lastrowid
        guardar_photo(self)

        messagebox.showinfo("Registro completado", "El producto fue registrado correctamente.")
        descripcion = f"color: {color} talle:{talle} marca:{marca}"
        prec_com=(prec_com*stock)
        register(self,self.user_name,nom, descripcion, stock, "Ingreso de productos", prec_com, "-")
        self.entry_codigo.delete(0, tk.END)
        

    except Exception as e:
        messagebox.showerror("Error al ingresar producto", f"Ocurrió un error: {e}")

    finally:
        try:
            if conexion:
                conexion.close()
        except:
            pass






    
    
    