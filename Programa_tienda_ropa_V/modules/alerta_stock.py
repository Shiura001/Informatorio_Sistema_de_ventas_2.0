import tkinter as tk
from customtkinter import *
from util.Conexion import *
from config import *

def stock_bajo(self):
    if self.stock_alerta_mostrada:
        return  # Ya se mostró, no hacer nada más

    conexion, cursor = conectar_bd()
    cursor.execute("SELECT COUNT(*) FROM productos WHERE stock_total <= stock_min")
    resultado = cursor.fetchone()
    conexion.close()

    if resultado[0] > 0:
        self.label_stock_bajo = CTkLabel(
            self,
            text="🔔 Alerta de Stock bajo",
            fg_color="#FF5512",
            font=config.Font2,
            width=150,
            height=30
        )

        start_y = -30
        final_y = 0

        def animar_subida(y_pos):
            if y_pos > start_y:
                y_pos -= 3  # subir 3 pixeles cada paso
                self.label_stock_bajo.place_configure(y=y_pos)
                self.after(10, lambda: animar_subida(y_pos))
            else:
                self.label_stock_bajo.destroy()

        def animar_bajada(y_pos):
            if y_pos == start_y:
                self.label_stock_bajo.place(relx=1.0, y=y_pos, anchor="ne")
            if y_pos < final_y:
                y_pos += 3  # bajar 3 pixeles cada paso
                self.label_stock_bajo.place_configure(y=y_pos)
                self.after(10, lambda: animar_bajada(y_pos))
            else:
                # Una vez abajo, espera 5 segundos y luego sube
                self.after(5000, lambda: animar_subida(y_pos))

        # Demora 1 segundo antes de iniciar la animación de bajada
        self.after(1000, lambda: animar_bajada(start_y))

        self.stock_alerta_mostrada = True

