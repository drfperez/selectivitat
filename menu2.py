import os
import subprocess
import tkinter as tk
# Check if Pillow is installed
try:
    from PIL import ImageTk, Image
except ImportError:
    # Pillow is not installed, so install it
    subprocess.call(['pip', 'install', 'Pillow'])
    # If you are using a virtual environment, you might want to use:
    # subprocess.call(['pip', 'install', 'Pillow'], shell=True)

# Now you can import ImageTk without any issues
from PIL import ImageTk


def execute_problem_1():
    subprocess.call(['python', 'problema_1.py'])

def execute_problem_2():
    subprocess.call(['python', 'problema_2.py'])

root = tk.Tk()
root.title("Selectivitat TiE 2009")

# Carga del logo y redimensionamiento
logo_image = Image.open("logo.png")  # Reemplaza "ruta_del_logo.png" con la ruta real de tu logo
logo_image = logo_image.resize((75, 75), Image.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo_image)

# Mostrar el logo en la esquina superior izquierda
logo_label = tk.Label(root, image=logo_photo)
logo_label.pack(anchor='nw', padx=0, pady=0)  # 'nw' (noroeste) para la esquina superior izquierda

# Texto justificado completamente con tamaño de fuente 18
text = "Tria els problemes de Tecnologia i Enginyeria corresponents a les proves d'accés \na la Universitat de les convocatòries de Juny i Setembre de 2009"
text_label = tk.Label(root, text=text, font=("Helvetica", 18), justify='left')
text_label.pack(fill='both', padx=10, pady=10)  # Rellenar en todas las direcciones

# Crea el menú desplegable
menu = tk.Menu(root)
root.config(menu=menu)

problem_menu = tk.Menu(menu)
menu.add_cascade(label="Escull aquí un problema", menu=problem_menu)

problem_menu.add_command(label="Problema 1", command=execute_problem_1)
problem_menu.add_command(label="Problema 2", command=execute_problem_2)
# Añade las opciones para los otros problemas

root.mainloop()
