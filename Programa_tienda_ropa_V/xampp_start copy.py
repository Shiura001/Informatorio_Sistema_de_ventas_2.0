import subprocess
import os
from modules.clean import *
from config import *

def iniciar_xampp():
    # Ruta al archivo xampp_start.exe
    # Cambia la ruta según la ubicación de tu instalación de XAMPP
    xampp_path = r"C:\xampp\xampp_start.exe"

    try:
    # Ejecuta el archivo sin mostrar la consola
        subprocess.Popen(xampp_path, creationflags=subprocess.CREATE_NO_WINDOW)
        print("XAMPP iniciado correctamente.")
    except FileNotFoundError:
        print("Error: No se encontró el archivo xampp_start.exe. Verificá la ruta.")
    except Exception as e:
        print(f"Ocurrió un error al iniciar XAMPP: {e}")


def cerrar_xampp(self):
    try:
        subprocess.call('taskkill /F /IM httpd.exe', shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
        subprocess.call('taskkill /F /IM mysqld.exe', shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
        print("XAMPP cerrado correctamente.")
    except Exception as e:
        print(f"Ocurrió un error al cerrar XAMPP: {e}")





    
    # Simular un tiempo de carga  # Destruir la etiqueta de carga
  