import requests
from datetime import datetime
import threading
import time

def iniciar_fecha(self):
    self.fecha_obj = datetime.now()
    self.fecha_completa = self.fecha_obj.strftime("%d/%m/%Y %H:%M:%S")
    self.fecha_sola = self.fecha_completa.split(" ")[0]
    threading.Thread(target=lambda: obtener_fecha_segura(self), daemon=True).start()






import requests
import threading
import time
from datetime import datetime


def obtener_fecha_segura(self):
    while True:
        time.sleep(60)
        try:
            url = "http://worldtimeapi.org/api/timezone/America/Argentina/Buenos_Aires"
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()

            # Ejemplo de formato de "datetime": '2024-06-08T20:45:09.429872-03:00'
            fecha_str = data['datetime'].split('.')[0]  # Quitamos los microsegundos
            self.fecha_obj = datetime.strptime(fecha_str, "%Y-%m-%dT%H:%M:%S")

        except Exception as e:
            print("Error al obtener la hora online:", e)
            self.fecha_obj = datetime.now()

        self.fecha_completa = self.fecha_obj.strftime("%d/%m/%Y %H:%M:%S")
        self.fecha_sola = self.fecha_completa.split(" ")[0]

        print("La fecha completa es:", self.fecha_completa)



# Prueba


