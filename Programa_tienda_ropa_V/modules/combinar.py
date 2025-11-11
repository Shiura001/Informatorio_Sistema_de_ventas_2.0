
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from customtkinter import *
from tkinter import messagebox

from tkinter import messagebox  # Asegurate de importarlo

def combinar(self):
    # Condición 1: verificar método de pago
    if self.entry_metodo_pago.get() != "Combinar":
        messagebox.showerror("Error", "El método de pago debe ser 'Combinar' para usar esta función.")
        return

    # Condición 2: verificar si la tabla tiene productos
    if not self.tree_products.get_children():
        messagebox.showerror("Error", "No hay productos en la tabla para combinar medios de pago.")
        return

    # Sumamos el total de los productos
    total = 0
    productos_agrupados = {}
    for item in self.tree_products.get_children():
        datos = self.tree_products.item(item, 'values')
        cod = datos[1]
        prec_com = datos[8]

        precio_limpio = prec_com.replace('$', '').replace(',', '').strip()

        try:
            precio_float = float(precio_limpio)
        except ValueError:
            precio_float = 0

        if cod not in productos_agrupados:
            productos_agrupados[cod] = {
                "cantidad": 1,
                "precio": precio_float
            }
        else:
            productos_agrupados[cod]["cantidad"] += 1

    for p in productos_agrupados.values():
        total += p["cantidad"] * p["precio"]

    # Crear ventana secundaria
    ventana_edicion = tk.Toplevel(self)
    ventana_edicion.title("Combinar medios de pago")
    ventana_edicion.geometry("300x220")
    ventana_edicion.iconbitmap("imagenes/icon.ico")

    tk.Label(ventana_edicion, text=f"Total a pagar: ${total:.2f}").grid(row=0, column=0, columnspan=2, pady=10)

    tk.Label(ventana_edicion, text="Efectivo:").grid(row=1, column=0, padx=10, pady=5)
    entry_efectivo = tk.Entry(ventana_edicion)
    entry_efectivo.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(ventana_edicion, text="Tarjeta:").grid(row=2, column=0, padx=10, pady=5)
    entry_tarjeta = tk.Entry(ventana_edicion)
    entry_tarjeta.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(ventana_edicion, text="Transferencia:").grid(row=3, column=0, padx=10, pady=5)
    entry_transferencia = tk.Entry(ventana_edicion)
    entry_transferencia.grid(row=3, column=1, padx=10, pady=5)

    def combinar_medios():
        medios = {}
        suma = 0
        for nombre, entry in [("efec", entry_efectivo), ("tarj", entry_tarjeta), ("transf.", entry_transferencia)]:
            valor = entry.get().strip()
            if valor:
                try:
                    v = float(valor)
                    if v > 0:
                        medios[nombre] = v
                        suma += v
                except ValueError:
                    pass

        if abs(suma - total) > 0.01:
            messagebox.showerror("Error", f"La suma de los medios de pago (${suma:.2f}) no coincide con el total a pagar (${total:.2f}).")
            return

        self.medios_combinados = " ".join(f"{k}:{v}" for k, v in medios.items())
        print("Medios combinados:", medios)
        ventana_edicion.destroy()

    btn_combinar = tk.Button(ventana_edicion, text="Combinar", command=combinar_medios)
    btn_combinar.grid(row=4, column=0, columnspan=2, pady=10)
