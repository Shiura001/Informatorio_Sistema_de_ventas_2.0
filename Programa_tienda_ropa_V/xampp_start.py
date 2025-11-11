import subprocess
import psutil
import os
from modules.clean import *
from config import *

def wait(self): 
    clean(self)
    self.label_loading = CTkLabel(self,
        text="Cerrando, espere por favor...",
        text_color=config.Color_2,
        font=config.Font3,
        bg_color=config.COLOR_CUERPO_PRINCIPAL)
    self.label_loading.pack(pady=10, padx=10)
    self.update()






def procesos_activos(procesos):
    """Chequea si alguno de los procesos listados está corriendo"""
    nombres = [p.name().lower() for p in psutil.process_iter()]
    return any(proceso.lower() in nombres for proceso in procesos)

def iniciar_xampp():
    xampp_start_path = r"C:\xampp\xampp_start.exe"
    procesos_xampp = ["httpd.exe", "mysqld.exe"]

    if procesos_activos(procesos_xampp):
        print("XAMPP ya está corriendo.")
        return

    try:
        subprocess.Popen(xampp_start_path, creationflags=subprocess.CREATE_NO_WINDOW)
        print("XAMPP iniciado correctamente.")
    except FileNotFoundError:
        print("Error: No se encontró el archivo xampp_start.exe. Verificá la ruta.")
    except Exception as e:
        print(f"Ocurrió un error al iniciar XAMPP: {e}")








def cerrar_xampp(self):
    xampp_stop_path = r"C:\xampp\xampp_stop.exe"
    procesos_xampp = ["httpd.exe", "mysqld.exe"]
    wait(self)

    





    # Primero intentar usar el script oficial de parada
    if os.path.exists(xampp_stop_path):
        try:
            subprocess.call(xampp_stop_path, creationflags=subprocess.CREATE_NO_WINDOW)
            print("XAMPP detenido correctamente usando xampp_stop.exe.")
            return
        except Exception as e:
            print(f"No se pudo ejecutar xampp_stop.exe: {e}")

    # Si no existe el script o falla, intentar detener servicios (si están como servicios Windows)
    servicios = ["Apache2.4", "MySQL"]  # Cambia los nombres según cómo estén registrados en tu sistema
    for servicio in servicios:
        try:
            resultado = subprocess.run(f'net stop {servicio}', shell=True, capture_output=True, text=True)
            if "se detuvo correctamente" in resultado.stdout.lower() or "already stopped" in resultado.stdout.lower():
                print(f"Servicio {servicio} detenido correctamente.")
            else:
                print(f"No se pudo detener el servicio {servicio}. Respuesta: {resultado.stdout.strip()}")
        except Exception as e:
            print(f"Error al detener servicio {servicio}: {e}")

    # Finalmente, si los procesos siguen activos, usar taskkill (último recurso)
    for proceso in procesos_xampp:
        if procesos_activos([proceso]):
            try:
                subprocess.call(f'taskkill /F /IM {proceso}', shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
                print(f"Proceso {proceso} cerrado forzadamente con taskkill.")
            except Exception as e:
                print(f"Ocurrió un error al cerrar {proceso}: {e}")
        else:
            print(f"Proceso {proceso} no está corriendo.")

# Ejemplo de uso
if __name__ == "__main__":
    iniciar_xampp()
    # acá tu código que necesita el servidor activo...
    cerrar_xampp()

