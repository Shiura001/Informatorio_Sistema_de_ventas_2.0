import tkinter as tk
from customtkinter import *
from tkinter import messagebox, ttk
from tkcalendar import Calendar

# Módulos propios
from util.util_imagenes import *
from config import *
from modules.clean import *
from util.Conexion import conectar_bd
from modules.fecha import *


def register(self,usuario, nombre, descripcion, tipo,cantidad, total, metodo_pago):
    conexion, cursor = conectar_bd()
    fecha = self.fecha_completa
    consulta = """
        INSERT INTO registro (usuario, nombre, descripcion,cantidad, tipo, total, fecha, metodo_pago,fecha2)
        VALUES (%s, %s, %s, %s, %s,%s, %s, %s,%s)
    """
    fecha2=self.fecha_sola
    datos = (usuario, nombre, descripcion, tipo, cantidad, total, fecha, metodo_pago,fecha2)
    cursor.execute(consulta, datos)
    conexion.commit()
    conexion.close()


def interfaz_register(self, controller_menu):
    self.bind("<Escape>", lambda event: controller_menu(self, "inicio"))

    self.side_bar = tk.Frame(self, bg=config.COLOR_MENU_LATERAL, width=200)
    self.side_bar.pack(side=tk.LEFT, fill="both")

    self.btn_volver = CTkButton(
        self.side_bar, font=config.Font2,
        text="Volver", command=lambda: controller_menu(self, "inicio"),
        text_color=config.Color_1, fg_color="yellow",
        width=30, height=50, anchor="center", corner_radius=10)
    self.btn_volver.pack(pady=20, padx=20)

    self.label_filtro = CTkLabel(
        self.side_bar, text="Ordenar por",
        text_color=config.Color_2, font=config.Font3,
        bg_color=config.COLOR_MENU_LATERAL)
    self.label_filtro.pack(pady=5, padx=5)

    self.entry_filtro = CTkOptionMenu(
        self.side_bar, font=config.Font3,
        text_color=config.Color_1, width=220, height=30,
        fg_color="white", corner_radius=10,
        values=["Codigo", "Menor precio", "Mayor precio", "Nombre","Fecha"])
    self.entry_filtro.set("Nombre")  # Valor por defecto
    self.entry_filtro.pack(pady=10, padx=10)

    self.entry_buscar = CTkEntry(
        self.side_bar, font=config.Font3,
        width=220, height=30, fg_color="white",
        text_color=config.Color_1, corner_radius=10)
    self.entry_buscar.pack(pady=10, padx=10)

    self.btn_buscar = CTkButton(
        self.side_bar, font=config.Font3,
        text="Buscar", command=lambda: filtrar_clientes(self),
        text_color=config.Color_1, fg_color="#F3FF96",
        width=30, height=50, anchor="center", corner_radius=20)
    self.btn_buscar.pack(pady=10, padx=10)

    self.btn_limpiar = CTkButton(
        self.side_bar, font=config.Font3,
        text="Limpiar Filtros", command=lambda: limpiar_filtros(self),
        text_color=config.Color_1, fg_color="#F3FF96",
        width=30, height=50, anchor="center", corner_radius=20)
    self.btn_limpiar.pack(pady=10, padx=10)

    self.contenedor_central = tk.Frame(self, bg=config.COLOR_CUERPO_PRINCIPAL, width=300, height=300)
    self.contenedor_central.pack(side=tk.TOP, expand=True, anchor="center")

    label_titulo = CTkLabel(self.contenedor_central, text="Registro", font=config.Font2, text_color=config.Color_2)
    label_titulo.pack(side=tk.TOP, anchor="n", pady=10)

    table_register(self)


def table_register(self):
    style = ttk.Style()
    style.theme_use('clam')
    style.configure('Treeview.Heading', background=self.table_color,foreground=self.table_color_text)
    style.configure("Treeview", font=('Michroma', 12), rowheight=70, background="#D3D3D3")
    style.configure("Treeview.Heading", font=('Michroma', 13, 'bold'))
    style.map("Treeview", background=[('selected', '#347083')])

    frame_tabla = tk.Frame(self.contenedor_central)
    frame_tabla.pack()
    scroll_y = ttk.Scrollbar(frame_tabla, orient="vertical")

    self.tree_register = ttk.Treeview(
        frame_tabla,
        columns=('ID', 'usuario', 'nombre', 'descripcion','cantidad', 'tipo', 'total', 'fecha', 'metodo_pago'),
        show='headings',
        yscrollcommand=scroll_y.set
    )
    scroll_y.config(command=self.tree_register.yview)
    scroll_y.pack(side="right", fill="y")

    # Encabezados
    encabezados = ['ID', 'Usuario', 'Nombre', 'Descript','Cant', 'Tipo', 'Total', 'Fecha', 'Met.pago']
    for i, col in enumerate(self.tree_register["columns"]):
        self.tree_register.heading(col, text=encabezados[i])
        anchura = [0, 150, 200, 495, 230,150, 160, 230, 200][i]
        self.tree_register.column(col, width=anchura, anchor='center', stretch=False)

    # Colores
    self.tree_register.tag_configure("blanco", background="white")
    self.tree_register.tag_configure("gris", background="lightgray")
    self.tree_register.tag_configure("ventas", background="#79FF80")
    self.tree_register.tag_configure("Ingreso", background="#B0D5FA")
    self.tree_register.tag_configure("Eliminacion", background="#FF8585")

    # Cargar datos
    conexion, cursor = conectar_bd()
    consulta = "SELECT * FROM `registro` ORDER BY fecha DESC"
    cursor.execute(consulta)
    datos = cursor.fetchall()
    conexion.close()

    for i, fila in enumerate(datos):
        tipo = fila[5]
        tag = "blanco" if i % 2 == 0 else "gris"
        if tipo == 'Ventas':
            tag = "ventas"
        elif tipo == 'Ingreso de productos':
            tag = "Ingreso"
        elif tipo == 'Eliminación':
            tag = "Eliminacion"

        self.tree_register.insert('', 'end', values=fila, tags=(tag,))

    self.tree_register.pack(anchor="center", side=tk.TOP, fill='y')


def cargar_datos(self, filtro="", criterio="Nombre"):
    for row in self.tree_register.get_children():
        self.tree_register.delete(row)

    conexion, cursor = conectar_bd()

    # Columnas permitidas para filtro
    columnas = {
        "Nombre": "nombre",
        "Fecha": "fecha",
        "Metodo de pago": "metodo_pago",
        "Total": "total"
    }

    if criterio == "Menor precio":
        consulta = "SELECT * FROM registro ORDER BY total ASC"
        cursor.execute(consulta)
    elif criterio == "Mayor precio":
        consulta = "SELECT * FROM registro ORDER BY total DESC"
        cursor.execute(consulta)
    elif criterio == "Fecha":
        consulta = "SELECT * FROM registro ORDER BY fecha DESC"
        cursor.execute(consulta)
    else:
        columna_sql = columnas.get(criterio, "nombre")
        consulta = f"SELECT * FROM registro WHERE {columna_sql} LIKE %s"
        cursor.execute(consulta, (f"%{filtro}%",))

    resultados = cursor.fetchall()
    conexion.close()

    for i, fila in enumerate(resultados):
        tag = "blanco" if i % 2 == 0 else "gris"
        if fila[5] == 'Ventas':
            tag = "ventas"
        elif fila[5] == 'Ingreso de productos':
            tag = "Ingreso"
        elif fila[5] == 'Eliminación':
            tag = "Eliminacion"

        self.tree_register.insert('', 'end', values=fila, tags=(tag,))

def filtrar_clientes(self):
    filtro = self.entry_buscar.get().strip()
    criterio = self.entry_filtro.get()
    cargar_datos(self, filtro, criterio)


def limpiar_filtros(self):
    self.entry_buscar.delete(0, tk.END)
    self.entry_filtro.set("Nombre")
    cargar_datos(self)
