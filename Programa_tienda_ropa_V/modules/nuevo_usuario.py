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
import bcrypt
import customtkinter






def nuevo_usuario(self):
    self.sub_menu="push_user"
    clean(self.contenedor_central)
    label_ejemple = CTkLabel(self.contenedor_central, text="Nuevo usuario", font=config.Font2, text_color=config.Color_2)
    label_ejemple.pack(side=TOP, anchor="n", pady=10)
    self.btn_save=CTkButton(self.contenedor_central,text="Registrar",fg_color="Green",font=config.Font2,width=150,height=30,command=lambda: insert_user(self))
    self.btn_save.pack(side=BOTTOM,pady=10)


    frame1 = CTkFrame(self.contenedor_central, fg_color=config.Color_4, corner_radius=20)
    frame1.pack(side=LEFT, expand=True, fill="both")

# Labels y Entries con grid (dos columnas: label y entrada)
# Fila, columna

    self.label_username = CTkLabel(frame1, text="Usuario", font=config.Font2, text_color=config.Color_1)
    self.label_username.grid(row=0, column=0, padx=50, pady=(20,30))
    self.entry_username = CTkEntry(frame1, font=config.Font2, width=200, height=30, fg_color=config.Color_2,
                                 border_color=config.Color_3, text_color=config.Color_1, corner_radius=50)
    self.entry_username.grid(row=0, column=1, padx=10, pady=5)

    self.label_password = CTkLabel(frame1, text="Contraseña", font=config.Font2, text_color=config.Color_1)
    self.label_password.grid(row=1, column=0, padx=50, pady=(20,30))
    self.entry_password = CTkEntry(frame1, font=config.Font2, width=200, height=30, fg_color=config.Color_2,
                                 border_color=config.Color_3, text_color=config.Color_1, corner_radius=50)
    self.entry_password.grid(row=1, column=1, padx=10, pady=5)

    self.label_rpassword = CTkLabel(frame1, text="Repetir contraseña", font=config.Font2, text_color=config.Color_1)
    self.label_rpassword.grid(row=3, column=0, padx=50, pady=(20,30))
    self.entry_rpassword = CTkEntry(frame1, font=config.Font2, width=200, height=30, fg_color=config.Color_2,
                                 border_color=config.Color_3, text_color=config.Color_1, corner_radius=50)
    self.entry_rpassword.grid(row=3, column=1, padx=10, pady=5)








def insert_user(self):
    user = self.entry_username.get()
    password = self.entry_password.get()
    rpassword = self.entry_rpassword.get()
   

    if not user or not password or not rpassword:
        messagebox.showerror("Error", "Todos los campos son obligatorios.")
        return

    try:

        if password != rpassword:
            raise ValueError("Las contraseñas no coinciden.")
        conexion, cursor = conectar_bd()

        # ✅ Verificar si el usuario existe
        cursor.execute("SELECT COUNT(*) FROM login WHERE username = %s", (user,)) # COUNT cuenta las veces que se repite la condicion de: username==user
        resultado = cursor.fetchone()
        if resultado[0] > 0:# 
            messagebox.showerror("Error", "El nombre de usuario ya existe. Ingrese uno diferente.")
            return
            

    except ValueError as e:
        messagebox.showerror("Error de validación", str(e))
        return
    

    from modules.registro import register

    try:
        # hashear contraseña
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        hashed_str_password = hashed.decode('utf-8')
        conexion, cursor = conectar_bd()

        consulta = """
            INSERT INTO login 
            (username,password)
            VALUES (%s, %s)
        """
        datos = (user,hashed_str_password)

        cursor.execute(consulta, datos)
        conexion.commit()
        self.id_producto_generado = cursor.lastrowid
        guardar_photo(self)

        messagebox.showinfo("Registro completado", "El usuario fue registrado correctamente.")

    except Exception as e:
        messagebox.showerror("Error al registrar", f"Ocurrió un error: {e}")

    finally:
        try:
            if conexion:
                conexion.close()
        except:
            pass