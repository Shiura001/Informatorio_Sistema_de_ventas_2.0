import os
import shutil
from tkinter import filedialog, messagebox
from pathlib import Path  # ✅ Usamos pathlib para normalizar rutas
from util.Conexion import *



def abrir_imagen(self):
    # Diálogo para seleccionar imagen
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
        

def guardar_photo(self):
    try:
        # Verificamos que se haya seleccionado una imagen
        if not getattr(self, 'ruta_foto2', None) or not getattr(self, 'ruta_destino2', None):
            return

        # Copiar el archivo a la carpeta Fotos
        shutil.copy(self.ruta_foto2, self.ruta_destino2)

        # Guardar en base de datos
        conexion, cursor = conectar_bd()
        consulta = "INSERT INTO photos (id_photo, ruta) VALUES (%s, %s)"
        valores = (self.id_producto_generado, self.ruta_destino2)

        print("Insertando en DB:", valores)
        cursor.execute(consulta, valores)
        conexion.commit()

        messagebox.showinfo("Registro completado", "Foto guardada correctamente.")

    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al guardar la imagen:\n{e}")
    finally:
        # Limpiar las rutas para evitar uso accidental posterior
        self.ruta_foto2 = None
        self.ruta_destino2 = None

def actualizar_photo(self):
    try:
        # Verificamos que se haya seleccionado una imagen
        if not hasattr(self, 'ruta_foto2') or not hasattr(self, 'ruta_destino2'):
            return

        # Copiar el archivo a la carpeta Fotos
        shutil.copy(self.ruta_foto2, self.ruta_destino2)

        # Guardar en base de datos
        conexion, cursor = conectar_bd()
        consulta = "UPDATE photos SET ruta = %s WHERE id_photo = %s"
        valores = (self.ruta_destino2, self.id_producto_generado)

        print("actualizado en DB:", valores)
        cursor.execute(consulta, valores)
        conexion.commit()

        messagebox.showinfo("Registro completado", "Foto guardada correctamente.")

    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al guardar la imagen:\n{e}")
