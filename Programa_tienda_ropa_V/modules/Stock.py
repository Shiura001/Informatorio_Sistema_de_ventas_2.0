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

from modules.nuevo_producto import *
#sub-menu
from tkinter import ttk

from util.Conexion import *

from modules.modificar import *

from modules.eliminar import *
from modules.imagen_producto import *
import time

import sys







def stock(self,controller_menu):
    self.bind("<F10>", lambda event: nuevo_producto(self))
    self.bind("<Delete>", lambda event: eliminar_producto(self,table))
    self.bind("<F11>", lambda event: abrir_ventana_edicion(self,table))
    self.bind("<Escape>", lambda event: controller_menu(self,"inicio"))
    
    
    # variable menu_activo
    self.Menu_activo = "Stock"
    self.side_bar=tk.Frame(self,bg=config.COLOR_MENU_LATERAL,width=200)
    self.side_bar.pack(side=tk.LEFT, fill="both")

    self.top_bar=tk.Frame(self,bg=config.COLOR_BARRA_SUPERIOR,height=120)
    self.top_bar.pack(side=tk.TOP, fill="both")

    self.contenedor_central = tk.Frame(self, bg=config.COLOR_CUERPO_PRINCIPAL, width=300, height=300)
    self.contenedor_central.pack(side=tk.TOP, expand=True, anchor="center")

    
    

    #-----------------------------------------------------------------------------------
    #
    #---------------------BOTONES SIDE BAR-------------------------------------------------------
    #
    #-----------------------------------------------------------------------------------
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

    self.label_subtitulo=CTkLabel(self.side_bar,
        text="Productos",
        text_color=config.Color_2,
        font=config.Font2,
        bg_color=config.COLOR_MENU_LATERAL)
    self.label_subtitulo.pack(pady=(50,50), padx=20)

    ##-----------------------------------------------------------------------------------
    #
    #---------------------Entry-------------------------------------------------------
    #
    #-----------------------------------------------------------------------------------
    
    #codigo-------------
    self.label_codigo=CTkLabel(self.side_bar,
        text="Codigo de barras",
        text_color=config.Color_2,
        font=config.Font3,
        bg_color=config.COLOR_MENU_LATERAL)
    self.label_codigo.pack(pady=5, padx=5)
    
    
    self.entry_buscar=CTkEntry(self.side_bar,
        font=config.Font3,
        text_color=config.Color_1,
        width=220,height=30,
        fg_color="white",
        corner_radius=10)
    self.entry_buscar.pack(pady=10, padx=10)

    #Nombre-------------


   

    #Precio-------------
    self.label_filtro=CTkLabel(self.side_bar,
        text="Ordenar por",
        text_color=config.Color_2,
        font=config.Font3,
        bg_color=config.COLOR_MENU_LATERAL)
    self.label_filtro.pack(pady=5, padx=5)

    self.entry_filtro=CTkOptionMenu(self.side_bar,
        font=config.Font3,
        text_color=config.Color_1,
        width=220,height=30,
        fg_color="white",
        corner_radius=10,
        values=["Codigo","Menor precio","Mayor precio","Nombre","Marca","Categoria","Color","Talle"],)
    self.entry_filtro.pack(pady=10, padx=10)

    #Talle------------- 
    

    self.btn_buscar=CTkButton(self.side_bar,
        font=config.Font3,                  
        text="Buscar",
        command=lambda: filtrar_clientes(self),
        text_color=config.Color_1,
        fg_color="#F3FF96",
        width=30,height=50,
        anchor="center",
        corner_radius=20)
    self.btn_buscar.pack(pady=10, padx=10)

    self.btn_limpiar=CTkButton(self.side_bar,
        font=config.Font3,                  
        text="Limpiar Filtros",
        command=lambda: limpiar_filtros(self),
        text_color=config.Color_1,
        fg_color="#F3FF96",
        width=30,height=50,
        anchor="center",
        corner_radius=20)
    self.btn_limpiar.pack(pady=10, padx=10)

    img_producto(self)




                     

    #-----------------------------------------------------------------------------------
    #
    #---------------------BOTONES BARRA TOP-------------------------------------------------------
    #
    #-----------------------------------------------------------------------------------

    self.btn_agregar_producto=CTkButton(self.top_bar,
        font=config.Font3,                  
        text="Agregar Producto\nF10",
        text_color=config.Color_1,
        fg_color="#64FF45",
        width=30,height=50,
        anchor="center",
        corner_radius=20,
        command=lambda: nuevo_producto(self))
    
    self.btn_agregar_producto.pack(pady=10, padx=10, side=tk.LEFT)

    self.btn_quitar_producto=CTkButton(self.top_bar,
        font=config.Font3,       
        command=lambda: eliminar_producto(self,table),           
        text="Quitar Producto\nSupr",
        text_color=config.Color_1,
        fg_color="#FF373A",
        width=30,height=50,
        anchor="center",
        corner_radius=20)
    self.btn_quitar_producto.pack(pady=10, padx=10, side=tk.LEFT)

    self.btn_modificar_producto=CTkButton(self.top_bar,
        font=config.Font3, 
        command=lambda: abrir_ventana_edicion(self,table),                 
        text="Modificar Producto\nF11",
        text_color=config.Color_1,
        fg_color="#E1FF00",
        width=100,height=50,
        anchor="center",
        corner_radius=20)
    self.btn_modificar_producto.pack(pady=10, padx=10, side=tk.RIGHT)
    
    wait(self)
    

#pantalla de carga------------------------------------

def wait(self): 
    print("wait")
    self.update_idletasks()
    self.label_loading = CTkLabel(self.contenedor_central,
        text="Cargando productos...",
        text_color=config.Color_2,
        font=config.Font3,
        bg_color=config.COLOR_CUERPO_PRINCIPAL)
    self.label_loading.pack(pady=10, padx=10)
    self.update_idletasks()
    # Simular un tiempo de carga  # Destruir la etiqueta de carga
    self.after(300, lambda: cargar_y_eliminar(self))

    


def cargar_y_eliminar(self):
    table(self)
    self.label_loading.destroy()
    print("cargar eliminar")
    




#-----------------------------------------------------------------------------------
#
#---------------------TABLA STOCK-------------------------------------------------------
#
#-----------------------------------------------------------------------------------

def table(self):
    style = ttk.Style()

#Configurar estilo al encabezado
    style.theme_use('clam')
    style.configure('Treeview.Heading', background=self.table_color,foreground=self.table_color_text)



    style.configure("Treeview", font=('Michroma', 12),rowheight=70,background="#D3D3D3")  # Fuente y tamaño
    style.configure("Treeview.Heading", font=('Michroma', 13, 'bold'))  # Encabezados



    frame_tabla = tk.Frame(self.contenedor_central)
    frame_tabla.pack()
    scroll_y = ttk.Scrollbar(frame_tabla, orient="vertical")
    


# Crear la tabla
    self.tree_products = ttk.Treeview(frame_tabla, columns=('ID', 'Codigo_producto', 'Nombre', 'Color', 'Talle', 'Marca', 'Categoria', 'Stock_total', 'Stock_min', 'Precio_compra', 'Precio_venta'), show='headings', yscrollcommand=scroll_y.set)
    scroll_y.config(command=self.tree_products.yview)
    scroll_y.pack(side="right", fill="y")
# Definir los encabezados
    self.tree_products.heading('ID', text='ID')
    self.tree_products.heading('Codigo_producto', text='Código')
    self.tree_products.heading('Nombre', text='Nombre')
    self.tree_products.heading('Color', text='Color')
    self.tree_products.heading('Talle', text='Talle')
    self.tree_products.heading('Marca', text='Marca')
    self.tree_products.heading('Categoria', text='Categoría')
    self.tree_products.heading('Stock_total', text='Stock Total')
    self.tree_products.heading('Stock_min', text='Stock Min')
    self.tree_products.heading('Precio_compra', text='Prec.Compra')
    self.tree_products.heading('Precio_venta', text='Prec.Venta')
    
    # Columnas (podés ajustar los widths a gusto)
    self.tree_products.column('ID', width=0, stretch=False)
    self.tree_products.column('Codigo_producto', anchor='center', width=170)
    self.tree_products.column('Nombre', anchor='center', width=300)
    self.tree_products.column('Color', anchor='center', width=130)
    self.tree_products.column('Talle', anchor='center', width=80)
    self.tree_products.column('Marca', anchor='center', width=145)
    self.tree_products.column('Categoria', anchor='center', width=150)
    self.tree_products.column('Stock_total', anchor='center', width=150)
    self.tree_products.column('Stock_min', anchor='center', width=150)
    self.tree_products.column('Precio_compra', anchor='center', width=165)
    self.tree_products.column('Precio_venta', anchor='center', width=150)


    self.tree_products.tag_configure("blanco", background="white")
    self.tree_products.tag_configure("gris", background="lightgray")
    self.tree_products.tag_configure("alerta", background="#FF9A67")





# Consulta
    conexion, cursor=conectar_bd()
    consulta = "SELECT * FROM `productos`"
    cursor.execute(consulta)
    conexion.close()
    i=0
    for fila in cursor.fetchall():
        i+=1
        if fila[7]<=fila[8]:
            tag = "alerta"
        else:
            tag = "blanco" if i % 2 == 0 else "gris"  # Alternar colores
        self.tree_products.insert('', 'end', values=(
        fila[0],  # id_producto
        fila[1],  # codigo_producto
        fila[2],  # nombre
        fila[3], # color
        fila[4],  # talle
        fila[5],  # marca
        fila[6],  # categoria
        fila[7],  # stock_total
        fila[8],  # stock_min
        "$"+str(fila[9]),  # precio_compra
        "$"+str(fila[10]),  # precio_venta
        ), tags=(tag,))

# Posicionar la tabla en la ventana
    self.tree_products.pack(anchor="center",side=TOP,fill='y')
    print("tabla ready")


# Cambiar el color de fondo para la fila seleccionada
    style.map("Treeview",
          background=[('selected', '#347083')])
    (   'winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')







#-----------------------------------------------------------------------------------
#
#---------------------FILTRAR PRODUCTOS---------------------------------------------
#
#-----------------------------------------------------------------------------------







def cargar_datos(self, filtro="", criterio="Nombre"):
    """Carga los datos desde la BD y los muestra en la tabla. Puede aplicar un filtro según el criterio seleccionado."""
    
    # Borrar datos previos en la tabla
    for row in self.tree_products.get_children():
        self.tree_products.delete(row)

    conexion, cursor = conectar_bd()
    #values=["Menor precio","Mayor precio","Nombre","Marca","Categoria"],)

    # Mapeo de criterios a columnas SQL
    columnas = {"Nombre": "nombre","Codigo": "codigo_producto", "Marca": "marca", "Categoria": "categoria", "Mayor_precio": "precio_venta","Color":"color","Talle":"talle"}
    if criterio == "Menor precio":
        consulta= "SELECT * FROM productos ORDER BY precio_venta ASC"
    elif criterio == "Mayor precio":
        consulta= "SELECT * FROM productos ORDER BY precio_venta DESC"
    else:
        columna_sql = columnas.get(criterio, "Nombre")  # Si no existe, usa "Nombre" por defecto
        consulta = f"SELECT * FROM productos WHERE {columna_sql} LIKE '%{filtro}%'"
    
    cursor.execute(consulta)

    # Consulta con filtro
    

    
    resultados = cursor.fetchall()
    
        
    # Insertar filas en la tabla
    for i, fila in enumerate(resultados):
        if fila[7]<=fila[8]:
            tag = "alerta"
        else:
            tag = "blanco" if i % 2 == 0 else "gris"  # Alternar colores
        self.tree_products.insert('', 'end', values=(
        fila[0],  # id_producto
        fila[1],  # codigo_producto
        fila[2],  # nombre
        fila[3], # color
        fila[4],  # talle
        fila[5],  # marca
        fila[6],  # categoria
        fila[7],  # stock_total
        fila[8],  # stock_min
        "$"+str(fila[9]),  # precio_compra
        "$"+str(fila[10]),  # precio_venta
        ), tags=(tag,))
    conexion.close()
    





def filtrar_clientes(self):
    """Filtra los clientes según el texto ingresado y el criterio seleccionado en el Combobox."""
    filtro = self.entry_buscar.get().strip()
    criterio = self.entry_filtro.get()  # Obtener criterio seleccionado (Nombre, Apellido o DNI)
    cargar_datos(self, filtro, criterio)


def limpiar_filtros(self):
    """Limpia los filtros aplicados en la tabla de clientes."""
    self.entry_buscar.delete(0, tk.END)
    self.entry_filtro.set("Nombre")  # Restablecer a "Nombre" por defecto
    cargar_datos(self)  # Cargar todos los datos nuevamente