import tkinter as tk
from PIL import ImageTk, Image

# ... Tu código anterior ...

def mostrar_imagen(datos_imagenes):
    for datos in datos_imagenes:
        ruta_imagen = datos['ruta']
        x = datos['x']
        y = datos['y']
        resizex = datos['resizex']
        resizey = datos['resizey']
        
        imagen = Image.open(ruta_imagen)
        imagen = imagen.resize((resizex, resizey), Image.LANCZOS)
        imagen = ImageTk.PhotoImage(imagen)
        
        label_imagen = tk.Label(frame, image=imagen)
        label_imagen.image = imagen
        label_imagen.place(x=x, y=y)

# ... Tu código anterior ...

# Datos de ejemplo con las imágenes, ubicaciones y tamaños
datos_imagenes = [
    {
        'ruta': 'imagen1.png',
        'x': 50,
        'y': 50,
        'resizex': 200,
        'resizey': 200
    },
    {
        'ruta': 'imagen2.png',
        'x': 300,
        'y': 50,
        'resizex': 150,
        'resizey': 150
    }
]

# Llamada a la función para mostrar las imágenes
mostrar_imagen(datos_imagenes)

# ... Tu código posterior ...
