from PIL import ImageTk,Image

def leer_imagen(path,size):
    # Abrir la imagen en modo RGBA (para conservar transparencia si existe)
    img = Image.open(path).convert("RGBA")
    
    # Redimensionar la imagen con antialiasing para mejor calidad
    img = img.resize(size, Image.LANCZOS)
    
    # Convertir a formato compatible con Tkinter
    return ImageTk.PhotoImage(img)
    #return ImageTk.PhotoImage(Image.open(path).resize(size, Image.ADAPTIVE))