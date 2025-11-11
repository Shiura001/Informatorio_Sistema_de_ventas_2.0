import json

def guardar_colores(self):
    colores = {
        "table_color": self.table_color,
        "table_color_text": self.table_color_text
    }

    try:
        with open("config.json", "w") as archivo:
            json.dump(colores, archivo, indent=4)
        print("🎨 Colores guardados correctamente en 'config.json'")
    except Exception as e:
        print("❌ Error al guardar los colores:", e)
