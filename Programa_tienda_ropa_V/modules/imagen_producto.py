import tkinter as tk

from PIL import Image, ImageTk  # Asegurate de tener Pillow instalado

from customtkinter import *
from util.util_imagenes import *
from util.Conexion import *
from config import *



def img_producto(self):
    self.canvas = tk.Canvas(self.side_bar, width=200, height=200)
    self.canvas.pack()
# Mostrar la imagen en el canvas
    self.img1 = leer_imagen("imagenes/nada.png", (100, 100))
    self.canvas.create_image(100, 100, image=self.img1)  # Coordenadas x, y centradas
    self.canvas.image = self.img1  # Evita que se elimine por el recolector de basura


    self.btn_mostrar_img=CTkButton(self.side_bar,
        font=config.Font3,  
        command=lambda: mostrar_imagen(self),                
        text="Mostrar imagen",
        text_color=config.Color_1,
        fg_color="#8EFF47",
        width=30,height=50,
        anchor="center",
        corner_radius=20)
    
    self.btn_mostrar_img.pack(pady=50, padx=10)

    self.update()



def mostrar_imagen(self):
    conexion, cursor = conectar_bd()
    seleccionado = self.tree_products.selection()
    if seleccionado:
        item = self.tree_products.item(seleccionado)
        id_producto = item['values'][0]  # Asumiendo que el id está en la posición 0

        # Consulta correcta para MySQL
        cursor.execute("SELECT * FROM photos WHERE id_photo = %s", (id_producto,))
        resultado = cursor.fetchone()
        
        if resultado:
            ruta_imagen = resultado[1]
            try:
                img = Image.open(ruta_imagen)
                img = img.resize((200, 200))  # Ajusta tamaño al canvas
                self.imagen_canvas = ImageTk.PhotoImage(img)
                self.canvas.delete("all")
                self.canvas.create_image(0, 0, anchor="nw", image=self.imagen_canvas)
            except Exception as e:
                print("Error cargando la imagen:", e)
        else:
            self.canvas.delete("all")
            self.imagen_canvas = None



def img_producto_update(self):
    self.canvas.delete("all")
    self.img1 = leer_imagen("imagenes/nada.png", (100, 100))
    self.canvas.create_image(100, 100, image=self.img1)  # Coordenadas x, y centradas
    self.canvas.image = self.img1  # Evita que se elimine por el recolector de basura

    self.update()