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

from modules.aplicar_descuento import *

from modules.registro import *
from modules.imagen_producto import *
import time
from modules.combinar import *
import sys


Menu_Activo="None"


#interruptur para saber si ya sumo antes


def venta(self,controller_menu):
    self.bind("<Return>", lambda event: agregar_producto(self,self.entry_codigo1.get()))
    self.bind("<Delete>", lambda event: quitar_producto(self))
    self.bind("<F10>", lambda event: aplicar_descuento(self,table))
    self.bind("<F1>", lambda event: nueva_venta())
    self.bind("<F12>", lambda event: realizar_venta())

    
    # variable menu_activo
    self.Menu_activo = None
    self.side_bar=tk.Frame(self,bg=config.COLOR_MENU_LATERAL,width=200)
    self.side_bar.pack(side=tk.LEFT, fill="both")

    self.top_bar=tk.Frame(self,bg=config.COLOR_BARRA_SUPERIOR,height=120)
    self.top_bar.pack(side=tk.TOP, fill="both")

    self.contenedor_central = tk.Frame(self, bg=config.COLOR_CUERPO_PRINCIPAL, width=300, height=300)
    self.contenedor_central.pack(side=tk.TOP, expand=True, anchor="center")

    self.total=0.0


    
    

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
    self.label_codigo.pack(pady=5, padx=80)
    
    
    self.entry_codigo1=CTkEntry(self.side_bar,
        font=config.Font3,
        text_color=config.Color_1,
        width=220,height=30,
        fg_color="white",
        corner_radius=10)
    self.entry_codigo1.pack(pady=10, padx=10)

    #Nombre-------------
    self.label_tarjetas=CTkLabel(self.side_bar,
        text="Tarjetas/costos",
        text_color=config.Color_2,
        font=config.Font3,
        bg_color=config.COLOR_MENU_LATERAL)
    self.label_tarjetas.pack(pady=5, padx=5)


    #funcion para los costos de tarjetas
    #-----------------------------------
    #-----------------------------------
    
    def opcion_tarjeta_seleccionada(opcion):
        x=0
        for i in self.lista_tarjetas:
            if opcion==i:
                self.costos_metodo_pago=self.lista_costos_tarjeta[x]
            else:
                x+=1
        #interruptur para saber si ya sumo antes
        
        self.costo_tarjeta=round(self.total/100)*self.costos_metodo_pago
        self.costo_tarjeta=round(self.costo_tarjeta)

        self.label_tarjeta_total.configure(text=str(self.costos_metodo_pago)+" %")
        self.label_total2.configure(text="$"+str(self.total+self.costo_tarjeta))
        self.update()

        
     


    
    
    
    self.optionmenu_tarjetas=CTkOptionMenu(self.side_bar,
        values=self.lista_tarjetas,
        command=opcion_tarjeta_seleccionada,
        font=config.Font3,
        text_color=config.Color_1,
        fg_color="white",
        width=220,height=30,
        anchor="center",
        corner_radius=10)
    self.optionmenu_tarjetas.pack(pady=10, padx=10)


    self.costos_metodo_pago=0.0

    self.label_tarjeta_total=CTkLabel(self.side_bar,
        font=config.Font3,                  
        text=str(self.costos_metodo_pago)+" %",
        text_color=config.Color_1,
        fg_color="white",
        width=200,height=50,
        anchor="center",
        corner_radius=20,)
    self.label_tarjeta_total.pack(pady=10, padx=10)

    self.btn_nueva_venta=CTkButton(self.side_bar,
        font=config.Font3,  
        command=lambda: nueva_venta(),                
        text="Nueva Venta\nF1",
        text_color=config.Color_1,
        fg_color="#8EFF47",
        width=30,height=50,
        anchor="center",
        corner_radius=20)
    
    
    
    self.btn_nueva_venta.pack(pady=50, padx=10)
    img_producto(self)




    




#-----------------------------------------------------  
#
#Nueva Venta
#
#-----------------------------------------------------

    def nueva_venta():
        self.total=0
        self.costo_tarjeta=0
        self.label_total2.configure(text="$"+str(self.total))
        self.optionmenu_tarjetas.set("Ninguna")
        if self.tree_products.get_children():
            for item in self.tree_products.get_children():
                self.tree_products.delete(item)

        self.update()

#-----------------------------------------------------  
#
#REALIZAR VENTA
#
#-----------------------------------------------------

    def realizar_venta():
       if self.tree_products.get_children():
           productos_agrupados = {}

           # Agrupar productos por código
           for item in self.tree_products.get_children():
               datos = self.tree_products.item(item, 'values')
               cod = datos[1]
               nom = datos[2]
               color = datos[3]
               talle = datos[4]
               marca = datos[5]
               prec_com = datos[8]

               if cod not in productos_agrupados:
                   productos_agrupados[cod] = {
                       "nom": nom,
                       "color": color,
                       "talle": talle,
                       "marca": marca,
                       "cantidad": 1,
                       "precio": prec_com
                   }
               else:
                   productos_agrupados[cod]["cantidad"] += 1

           # Registrar cada producto una sola vez
           for cod, producto in productos_agrupados.items():
               nom = producto["nom"]
               color = producto["color"]
               talle = producto["talle"]
               marca = producto["marca"]
               cantidad = producto["cantidad"]
               prec_com = producto["precio"]
               prec_com = str(prec_com).replace("$", "")
               prec_com=float(prec_com)

               if self.descuento > 0:
                   descripcion = f"color: {color} talle: {talle} marc: {marca} cant: {cantidad} desc: {self.descuento}"
               else:
                   descripcion = f"color: {color} talle: {talle} marca: {marca} cantidad: {cantidad}"

               metodo_pago = self.entry_metodo_pago.get()
               if self.optionmenu_tarjetas.get() != 'Ninguna':
                   if self.entry_metodo_pago=="Combinado":
                        metodo_pago = self.entry_metodo_pago.get()
                   else:
                        metodo_pago += f" {self.optionmenu_tarjetas.get()}"


               register(self.user_name, nom, descripcion, "Ventas", prec_com*int(cantidad), metodo_pago)
               
           
               

               # Actualizar stock en la base de datos
               conexion, cursor = conectar_bd()

               cursor.execute("UPDATE productos SET stock_total = stock_total - %s WHERE codigo_producto = %s", (cantidad, cod))
               conexion.commit()
               conexion.close()

           messagebox.showinfo("Genial", "Venta realizada con éxito")

           # Limpiar la lista de productos
           for item in self.tree_products.get_children():
               self.tree_products.delete(item)

       else:
           messagebox.showwarning("Error", "Primero agrega productos a la lista.")

    
        

        
        
        
        

    

    


                     

    #-----------------------------------------------------------------------------------
    #
    #---------------------BOTONES BARRA TOP-------------------------------------------------------
    #
    #-----------------------------------------------------------------------------------

    self.btn_quitar_producto=CTkButton(self.top_bar,
        font=config.Font3,
        command=lambda: quitar_producto(self),                  
        text="Quitar Producto\nSupr",
        text_color=config.Color_1,
        fg_color="#FF373A",
        width=30,height=50,
        anchor="center",
        corner_radius=20)
    self.btn_quitar_producto.pack(pady=10, padx=10, side=tk.LEFT)



    
    


    self.descuento=0
    self.btn_aplicar_descuento=CTkButton(self.top_bar,
        font=config.Font3,                  
        text="Aplicar descuento\nF10",
        command=lambda: aplicar_descuento(self,table),
        text_color=config.Color_1,
        fg_color="#EBFFB9",
        width=30,height=50,
        anchor="center",
        corner_radius=20)
    self.btn_aplicar_descuento.pack(pady=10, padx=10, side=tk.LEFT)

    self.label_metodo_pago=CTkLabel(self.top_bar,
        font=config.Font3,                  
        text="Metodo de pago",
        text_color=config.Color_2,
        fg_color=config.COLOR_BARRA_SUPERIOR,
        width=30,height=50,
        anchor="center",
        )
    self.label_metodo_pago.pack(pady=10, padx=10, side=tk.LEFT)

    
    self.entry_metodo_pago=CTkOptionMenu(self.top_bar,
        values=["Efectivo", "Tarjeta", "Transferencia","Combinar"],
        command=lambda x: None,
        font=config.Font3,
        text_color=config.Color_1,
        fg_color="white",
        width=200,height=50,
        anchor="center",
        corner_radius=20)
    self.entry_metodo_pago.pack(pady=10, padx=10, side=tk.LEFT)

    self.btn_finalizar_venta=CTkButton(self.top_bar,
        font=config.Font3,                  
        text="Finalizar venta\nF12",
        command=lambda : realizar_venta(),
        text_color=config.Color_1,
        fg_color="#00EF00",
        width=30,height=50,
        anchor="center",
        corner_radius=20)
    self.btn_finalizar_venta.pack(pady=10, padx=10, side=tk.LEFT)

    



    self.label_total2=CTkLabel(self.top_bar,
        font=config.Font3,                  
        text="$"+str(self.total),
        text_color=config.Color_1,
        fg_color="white",
        width=200,height=50,
        anchor="center",
        corner_radius=20,
    )
    self.label_total2.pack(pady=10, padx=10, side=tk.RIGHT)

    self.label_total=CTkLabel(self.top_bar,
        font=config.Font3,                  
        text="Total",
        text_color=config.Color_2,
        fg_color=config.COLOR_BARRA_SUPERIOR,
        width=30,height=50,
        anchor="center",
        )
    self.label_total.pack(pady=10, padx=10, side=tk.RIGHT)
    


    



    wait(self)
    
  
def wait(self): 
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
    




#-----------------------------------------------------------------------------------
#
#---------------------TABLA STOCK-------------------------------------------------------
#
#-----------------------------------------------------------------------------------

def table(self):
    style = ttk.Style()

#Configurar estilo al encabezado
    style.theme_use('clam')
    style.configure('Treeview.Heading', background='green',foreground="white")



    style.configure("Treeview", font=('Michroma', 12),rowheight=70,background="#D3D3D3")  # Fuente y tamaño
    style.configure("Treeview.Heading", font=('Michroma', 13, 'bold'))  # Encabezados



    frame_tabla = tk.Frame(self.contenedor_central)
    frame_tabla.pack()
    scroll_y = ttk.Scrollbar(frame_tabla, orient="vertical")
    


# Crear la tabla
    self.tree_products = ttk.Treeview(frame_tabla, columns=('ID', 'Codigo_producto', 'Nombre', 'Color', 'Talle', 'Marca', 'Categoria', 'Stock_total', 'Precio_venta',), show='headings', yscrollcommand=scroll_y.set)
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
    self.tree_products.heading('Stock_total', text='Stock')
    self.tree_products.heading('Precio_venta', text='Precio')
    
    
    # Columnas (podés ajustar los widths a gusto)
    self.tree_products.column('ID', width=0, stretch=False)
    self.tree_products.column('Codigo_producto', anchor='center', width=170)
    self.tree_products.column('Nombre', anchor='center', width=300)
    self.tree_products.column('Color', anchor='center', width=130)
    self.tree_products.column('Talle', anchor='center', width=80)
    self.tree_products.column('Marca', anchor='center', width=145)
    self.tree_products.column('Categoria', anchor='center', width=150)
    self.tree_products.column('Stock_total', anchor='center', width=150)
    self.tree_products.column('Precio_venta', anchor='center', width=150)



    self.tree_products.tag_configure("blanco", background="white")
    self.tree_products.tag_configure("gris", background="lightgray")





# Posicionar la tabla en la ventana
    self.tree_products.pack(anchor="center",side=TOP,fill='y')
    self.alternador=0




def agregar_producto(self, codigo1):
    print("codigo: ", codigo1)
    codigo = codigo1
    conexion, cursor = conectar_bd()
    consulta = "SELECT * FROM `productos` WHERE codigo_producto = %s"
    cursor.execute(consulta, (codigo,))
    filas = cursor.fetchall()
    conexion.close()

    if not filas:
        messagebox.showwarning("Advertencia", "Producto no encontrado.")
        return

    for fila in filas:
        stock_disponible = fila[7]  # stock_total

        # Contar cuántas veces ya se agregó ese producto
        cantidad_en_tree = sum(
            1 for item in self.tree_products.get_children()
            if self.tree_products.item(item, 'values')[1] == codigo
        )

        if cantidad_en_tree >= stock_disponible:
            messagebox.showwarning("Stock insuficiente", f"Ya has agregado todas las unidades disponibles del producto '{fila[2]}'.")
            return

        self.alternador += 1
        tag = "blanco" if self.alternador % 2 == 0 else "gris"  # Alternar colores

        self.tree_products.insert('', 'end', values=(
            fila[0],  # id_producto
            fila[1],  # codigo_producto
            fila[2],  # nombre
            fila[3],  # color
            fila[4],  # talle
            fila[5],  # marca
            fila[6],  # categoría
            fila[7],  # stock_total
            "$" + str(fila[10]),  # precio_venta
        ), tags=(tag,))

        self.total += float(fila[10])
        print("total: ", self.total)

    if self.alternador % 2 == 0:
        self.alternador = 0

    self.label_total2.configure(text="$" + str(self.total))
    self.entry_codigo1.delete(0, tk.END)
    self.update()




    
def quitar_producto(self):
    item = self.tree_products.selection()
    if not item:
        messagebox.showwarning("Advertencia", "Primero seleccioná un producto para quitar.")
        return
    item = self.tree_products.selection()[0]  # Producto seleccionado
    valores = self.tree_products.item(item, "values")
    precio_str = valores[8]
    precio_sin_simbolo = int(precio_str.replace("$", ""))


    self.total-=precio_sin_simbolo
    self.total= round(self.total,2)
    self.label_total2.configure(text="$"+str(self.total))
    self.update()
    print(valores)  # El ID debe estar en la primera columna
    self.tree_products.delete(item)


    hijos = self.tree_products.get_children()
    if hijos:
        primer_item = hijos[0]
        self.tree_products.focus(primer_item)
        self.tree_products.selection_set(primer_item)

    







    # Suponé que ya insertaste filas en self.tree      # Seleccionarlo visualmente