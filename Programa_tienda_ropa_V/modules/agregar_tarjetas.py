import tkinter as tk
from tkinter import messagebox
import json
from customtkinter import *
from config import *
from modules.clean import *
# ----- JSON -----
def cargar_tarjetas_desde_json():
    try:
        with open("Datos/tarjetas.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            return datos["tarjetas"], datos["costos"]
    except (FileNotFoundError, json.JSONDecodeError):
        return ["Ninguna", "Visa", "Naranja", "Master_Card"], [0.0, 1.5, 2.5, 1.5]

def guardar_tarjetas_en_json(lista_tarjetas, lista_costos_tarjeta):
    with open("Datos/tarjetas.json", "w", encoding="utf-8") as archivo:
        json.dump({"tarjetas": lista_tarjetas, "costos": lista_costos_tarjeta}, archivo, indent=4)


# ----- GUI -----
def agregar_tarjetas(self):
    clean(self.contenedor_central)
    # Cargar tarjetas
    self.lista_tarjetas, self.lista_costos_tarjeta = cargar_tarjetas_desde_json()
    self.tarjeta_seleccionada_idx = None

    # Scrollable frame de tarjetas
    self.frame_tarjetas = CTkScrollableFrame(self.contenedor_central, width=400, height=400)
    self.frame_tarjetas.pack(pady=5, fill="both", expand=True)

    actualizar_listbox(self)

    # Entrada tarjeta
    self.label_nombre = CTkLabel(self.contenedor_central, text="Nombre de tarjeta", font=config.Font2, text_color=config.Color_2)
    self.label_nombre.pack(pady=5)

    self.entry_tarjeta = CTkEntry(self.contenedor_central, font=config.Font2, text_color=config.Color_1, width=250, height=30,
                                   fg_color=config.Color_2, placeholder_text='Tarjeta Naranja')
    self.entry_tarjeta.pack(pady=5)

    # Entrada costo

    self.label_costo = CTkLabel(self.contenedor_central, text="Costo", font=config.Font2, text_color=config.Color_2)
    self.label_costo.pack(pady=5)

    self.entry_costo = CTkEntry(self.contenedor_central, font=config.Font2, width=250, height=30, text_color=config.Color_1,
                                 fg_color=config.Color_2, placeholder_text='1.0')
    self.entry_costo.pack(pady=5)

    # Botones
    self.btn_agregar = CTkButton(self.contenedor_central, text="Agregar tarjeta", command=lambda: agregar_tarjeta(self))
    self.btn_agregar.pack(pady=5)

    self.btn_eliminar = CTkButton(self.contenedor_central, text="Eliminar tarjeta seleccionada", command=lambda: eliminar_tarjeta(self))
    self.btn_eliminar.pack(pady=5)


def actualizar_listbox(self):
    for widget in self.frame_tarjetas.winfo_children():
        widget.destroy()

    for idx, (t, c) in enumerate(zip(self.lista_tarjetas, self.lista_costos_tarjeta)):
        label = CTkLabel(self.frame_tarjetas, text=f"{t} - Costo: {c}", font=config.Font2, anchor="w")
        label.pack(fill="x", padx=5, pady=2)

        # Click para seleccionar
        label.bind("<Button-1>", lambda e, i=idx, w=label: seleccionar_tarjeta(self, i, w))


def seleccionar_tarjeta(self, idx, widget):
    self.tarjeta_seleccionada_idx = idx

    # Quitar color de selección de todos
    for w in self.frame_tarjetas.winfo_children():
        w.configure(fg_color="transparent")

    # Aplicar color al seleccionado
    widget.configure(fg_color="gray30")


def agregar_tarjeta(self):
    nombre = self.entry_tarjeta.get().strip()
    try:
        costo = float(self.entry_costo.get())
    except ValueError:
        messagebox.showerror("Error", "El costo debe ser un número válido.")
        return

    if nombre == "":
        messagebox.showerror("Error", "El nombre de la tarjeta no puede estar vacío.")
        return

    self.lista_tarjetas.append(nombre)
    self.lista_costos_tarjeta.append(costo)
    guardar_tarjetas_en_json(self.lista_tarjetas, self.lista_costos_tarjeta)
    actualizar_listbox(self)

    self.entry_tarjeta.delete(0, tk.END)
    self.entry_costo.delete(0, tk.END)


def eliminar_tarjeta(self):
    if self.tarjeta_seleccionada_idx is None:
        messagebox.showerror("Error", "Seleccioná una tarjeta para eliminar.")
        return

    idx = self.tarjeta_seleccionada_idx
    del self.lista_tarjetas[idx]
    del self.lista_costos_tarjeta[idx]
    guardar_tarjetas_en_json(self.lista_tarjetas, self.lista_costos_tarjeta)
    self.tarjeta_seleccionada_idx = None
    actualizar_listbox(self)
