from customtkinter import *
#Imagenes
from util.util_imagenes import *

#Configuraciones
from config import *

#Limpiart
from modules.clean import *
#sub-menu

#conexion
from util.Conexion import *

from tkinter import messagebox

from modules.imagen_producto import *




import os
from tkinter import messagebox
from modules.clean import clean  # Asumo que lo usás para refrescar tabla
from util.Conexion import conectar_bd

def eliminar_producto(self, table):
    confirmacion = messagebox.askyesno("Confirmar eliminación", "¿Estás seguro de que deseas eliminar este Producto?")
    if not confirmacion:
        return

    conexion, cursor = conectar_bd()
    try:
        item = self.tree_products.selection()
        if not item:
            messagebox.showwarning("Advertencia", "Primero seleccioná un producto para eliminar.")
            return

        item = item[0]  # Producto seleccionado
        valores = self.tree_products.item(item, "values")
        id_producto = valores[0]  # El ID debe estar en la primera columna

        # Obtener ruta de la foto para eliminar archivo si corresponde
        consulta_ruta = "SELECT ruta FROM photos WHERE id_photo = %s"
        cursor.execute(consulta_ruta, (id_producto,))
        resultado = cursor.fetchone()

        if resultado:
            ruta_foto = resultado[0]

            # Verificar si la misma ruta es usada por otro producto (excepto este)
            consulta_uso = "SELECT COUNT(*) FROM photos WHERE ruta = %s AND id_photo != %s"
            cursor.execute(consulta_uso, (ruta_foto, id_producto))
            cantidad_uso = cursor.fetchone()[0]

            # Solo borrar archivo si no está siendo usado por otro producto
            if cantidad_uso == 0:
                if os.path.isfile(ruta_foto):
                    try:
                        os.remove(ruta_foto)
                    except Exception as e:
                        messagebox.showwarning("Advertencia", f"No se pudo eliminar el archivo de imagen:\n{e}")

        # Eliminar de tabla photos
        consulta_foto = "DELETE FROM photos WHERE id_photo = %s"
        cursor.execute(consulta_foto, (id_producto,))

        # Obtener stock desde base de datos en vez de Treeview
        consulta_stock = "SELECT stock_total FROM productos WHERE id_producto = %s"
        cursor.execute(consulta_stock, (id_producto,))
        resultado_stock = cursor.fetchone()

        if resultado_stock:
            stock = resultado_stock[0]
        else:
            stock = 0  # O manejar error si es necesario

        # Eliminar de tabla productos
        consulta = "DELETE FROM productos WHERE id_producto = %s"
        cursor.execute(consulta, (id_producto,))

        conexion.commit()

        messagebox.showinfo("Éxito", "Producto eliminado correctamente")

        # Registro
        from modules.registro import register
        cod = valores[1]
        nom = valores[2]
        color = valores[3]
        talle = valores[4]
        marca = valores[5]
        prec_com = valores[9]
        stock=valores[7]
        
        prec_com = str(prec_com).replace("$", "")
        prec_com = int(prec_com) * int(stock)
        descripcion = f"color: {color} talle:{talle} marca:{marca} "

        register(self,self.user_name, nom, descripcion,stock, "Eliminación", prec_com, "-")
        img_producto_update(self)

        # Refrescar tabla
        clean(self.contenedor_central)
        table(self)
        conexion.close()

    except Exception as e:
        messagebox.showerror("Error", f"No se pudo eliminar el producto: {e}")
        conexion.rollback()
        conexion.close()

