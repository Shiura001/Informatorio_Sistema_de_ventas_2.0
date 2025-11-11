import requests
from datetime import datetime


def obtener_fecha_segura():
    try:
        url = "https://timeapi.io/api/Time/current/zone?timeZone=America/Argentina/Buenos_Aires"
        response = requests.get(url, timeout=0.5)
        response.raise_for_status()
        data = response.json()

        # Convertimos a objeto datetime para darle el mismo formato
        fecha_str = f"{data['date']} {data['time']}"
        fecha_obj = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M")
        return fecha_obj.strftime("%Y-%m-%d %H:%M:%S")

    except Exception as e:
        print("Error al obtener la hora online:", e)
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Prueba

def obtener_fecha_sola():
    fecha_completa = obtener_fecha_segura()
    return fecha_completa.split(" ")[0]