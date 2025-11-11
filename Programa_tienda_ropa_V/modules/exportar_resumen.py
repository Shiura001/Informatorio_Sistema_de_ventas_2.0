import mysql.connector
from openpyxl import Workbook
from modules.fecha import *
from util.Conexion import *
from tkinter import messagebox
def exportar_resumen(self):
    fecha_hoy = self.fecha_sola
    conexion, cursor = conectar_bd()
    consulta=("SELECT nombre, descripcion, tipo, total, fecha FROM registro WHERE fecha2 = %s")
    cursor.execute(consulta,(fecha_hoy,))
    
    

    datos = cursor.fetchall()  # Traer todos los registros
    print(fecha_hoy,datos)
    # Crear archivo Excel
    wb = Workbook()
    ws = wb.active
    ws.title = "Resumen"

    # Agregar encabezados
    ws.append(["Nom", "Descrip", "Tipo", "Total", "Fecha","Total Día"])


    suma_total = 0.0

    # Agregar filas con datos
    for fila in datos:
        ws.append(fila)
        if fila[2] == "Ventas":  # fila[2] es la columna 'tipo'
            suma_total += float(fila[3])
    ws.append(["", "", "", "", "Total día:", suma_total])

    # Guardar el archivo
    nombre_archivo = "resumen_productos.xlsx"
    wb.save(nombre_archivo)

    # Cerrar cursor y conexión
    cursor.close()
    conexion.close()
    messagebox.showinfo("Exportación Exitosa", f"Archivo generado: {nombre_archivo}")

    
