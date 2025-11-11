import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from customtkinter import *
#Imagenes
from util.util_imagenes import *
from PIL import ImageTk,Image
#Configuraciones
from config import *
from tkinter import ttk
#Limpiart
from modules.clean import *
#sub-menu

#conexion
from util.Conexion import *

from tkinter import messagebox

from modules.crud_img_producto import *

def abrir_ventana_edicion(self,table):
    try:
        item = self.tree_products.selection()[0]  # Cliente seleccionado
        valores = self.tree_products.item(item, "values")
        id_producto = valores[0]  # El ID debe estar en la primera columna
        self.id_producto_generado = id_producto

        # Crear ventana secundaria
        ventana_edicion = tk.Toplevel(self)
        ventana_edicion.title("Editar Cliente")
        ventana_edicion.geometry("580x450")
        ventana_edicion.iconbitmap("imagenes/icon.ico")

        # Etiquetas y campos de entrada
        tk.Label(ventana_edicion, text="Codigo:").grid(row=0, column=0, padx=10, pady=5)
        entry_codigo = tk.Entry(ventana_edicion)
        entry_codigo.grid(row=0, column=1, padx=10, pady=5)
        entry_codigo.insert(0, valores[1])  # Nombre actual

        tk.Label(ventana_edicion, text="Nombre:").grid(row=1, column=0, padx=10, pady=5)
        entry_nombre = tk.Entry(ventana_edicion)
        entry_nombre.grid(row=1, column=1, padx=10, pady=5)
        entry_nombre.insert(0, valores[2])  # Apellido actual

        tk.Label(ventana_edicion, text="Color:").grid(row=2, column=0, padx=10, pady=5)
        entry_color = tk.Entry(ventana_edicion)
        entry_color.grid(row=2, column=1, padx=10, pady=5)
        entry_color.insert(0, valores[3])  # DNI actual

        tk.Label(ventana_edicion, text="Talle:").grid(row=3, column=0, padx=10, pady=5)
        entry_talle = tk.Entry(ventana_edicion)
        entry_talle.grid(row=3, column=1, padx=10, pady=5)
        entry_talle.insert(0, valores[4])  # Teléfono actual


        tk.Label(ventana_edicion, text="Marca:").grid(row=4, column=0, padx=10, pady=5)
        entry_marca = tk.Entry(ventana_edicion)
        entry_marca.grid(row=4, column=1, padx=10, pady=5)
        entry_marca.insert(0, valores[5]) 
        
        tk.Label(ventana_edicion, text="Categoria:").grid(row=5, column=0, padx=10, pady=5)
        entry_categoria = tk.Entry(ventana_edicion)
        entry_categoria.grid(row=5, column=1, padx=10, pady=5)
        entry_categoria.insert(0, valores[6]) 
        
        
        tk.Label(ventana_edicion, text="Stock total:").grid(row=6, column=0, padx=10, pady=5)
        entry_stock = tk.Entry(ventana_edicion)
        entry_stock.grid(row=6, column=1, padx=10, pady=5)
        entry_stock.insert(0, valores[7]) # Email actual

        tk.Label(ventana_edicion, text="Stock minimo:").grid(row=7, column=0, padx=10, pady=5)
        entry_stockm = tk.Entry(ventana_edicion)
        entry_stockm.grid(row=7, column=1, padx=10, pady=5)
        entry_stockm.insert(0, valores[8]) # Email actual

        tk.Label(ventana_edicion, text="Precio compra:").grid(row=0, column=2, padx=10, pady=5)
        entry_precio = tk.Entry(ventana_edicion)
        entry_precio.grid(row=0, column=3, padx=10, pady=5)
        entry_precio.insert(0, valores[9].replace("$", "")) # Email actual

        tk.Label(ventana_edicion, text="Precio venta:").grid(row=1, column=2, padx=10, pady=5)
        entry_preciov = tk.Entry(ventana_edicion)
        entry_preciov.grid(row=1, column=3, padx=10, pady=5)
        entry_preciov.insert(0, valores[10].replace("$", "")) 

        btn_select=CTkButton(ventana_edicion,text="Selecionar_Foto",font=config.Font,height=30,text_color=config.Color_2,command=lambda:abrir_imagen2())
        btn_select.grid(row=4, column=3, padx=10, pady=(0,2))



                            
   
        def abrir_imagen2():
            ruta_foto = filedialog.askopenfilename(
                title="Seleccionar imagen",
                filetypes=[("Archivos de imagen", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")]
            )
            if ruta_foto:
                carpeta_destino = "Fotos"
                os.makedirs(carpeta_destino, exist_ok=True)  # Crea la carpeta si no existe

                nombre_archivo = os.path.basename(ruta_foto)

        # ✅ Normalizamos rutas con pathlib
                ruta_foto_normalizada = Path(ruta_foto).as_posix()
                ruta_destino = Path(os.path.join(carpeta_destino, nombre_archivo)).as_posix()

        # Guardamos las rutas como atributos de instancia
                self.ruta_foto2 = ruta_foto_normalizada
                self.ruta_destino2 = ruta_destino

                print("Ruta destino:", ruta_destino)
                ventana_edicion.focus_set() 





        # Función para guardar los cambios
        def guardar_cambios():
            nuevo_codigo = entry_codigo.get()
            nuevo_nombre = entry_nombre.get()
            nuevo_color = entry_color.get()
            nuevo_talle = entry_talle.get()
            nuevo_marca = entry_marca.get()
            nuevo_categoria = entry_categoria.get()
            nuevo_stock = entry_stock.get()
            nueva_stockmin = entry_stockm.get()
            nuevo_precio = entry_precio.get()
            nuevo_preciov = entry_preciov.get()

            conexion, cursor = conectar_bd()
            try:
                consulta = """
                    UPDATE productos 
                    SET codigo_producto = %s,  nombre= %s, color = %s, talle = %s, marca = %s, categoria = %s, stock_total = %s, stock_min = %s, precio_compra = %s, precio_venta = %s
                    WHERE id_producto = %s
                """
                cursor.execute(consulta, (nuevo_codigo,nuevo_nombre, nuevo_color, nuevo_talle, nuevo_marca, nuevo_categoria, nuevo_stock, nueva_stockmin, nuevo_precio, nuevo_preciov, id_producto))
                conexion.commit()
                
                actualizar_photo(self)
                messagebox.showinfo("Éxito", "Producto actualizado correctamente")
                ventana_edicion.destroy()
                clean(self.contenedor_central)
                table(self) 
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo actualizar: {e}")
                conexion.rollback() # Refrescar la tabla


        



        # Botón para guardar cambios
        btn_guardar = tk.Button(ventana_edicion, text="Guardar", command=guardar_cambios)
        btn_guardar.grid(row=8, column=0, columnspan=2, pady=10)
        

    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona un producto para editar")
        #añade aqui tambien pra cambiar la foto del producto seleccionado