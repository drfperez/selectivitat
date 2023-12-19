import tkinter as tk
from PIL import Image, ImageTk
import subprocess

def execute_problem_1():
    subprocess.call(['python', 'problema1.py'])

def execute_problem_2():
    subprocess.call(['python', 'problema2.py'])

root = tk.Tk()
root.title("Menú de problemas")

# Carga del logo y redimensionamiento
logo_image = Image.open("ruta_del_logo.png")  # Reemplaza "ruta_del_logo.png" con la ruta real de tu logo
logo_image = logo_image.resize((75, 75), Image.ANTIALIAS)
logo_photo = ImageTk.PhotoImage(logo_image)

# Mostrar el logo en la esquina superior izquierda
logo_label = tk.Label(root, image=logo_photo)
logo_label.pack(anchor='nw', padx=0, pady=0)  # 'nw' (noroeste) para la esquina superior izquierda

# Texto justificado completamente con tamaño de fuente 18
text = "Tria els problemes de Tecnologia i Enginyeria corresponents a les proves d'accés a la Universitat de les convocatòries de Juny i Setembre de 2009"
text_label = tk.Label(root, text=text, font=("Helvetica", 18), justify='justify')
text_label.pack(fill='both', padx=10, pady=10)  # Rellenar en todas las direcciones

# Crea el menú desplegable
menu = tk.Menu(root)
root.config(menu=menu)

problem_menu = tk.Menu(menu)
menu.add_cascade(label="Elegir problema", menu=problem_menu)

problem_menu.add_command(label="Problema 1", command=execute_problem_1)
problem_menu.add_command(label="Problema 2", command=execute_problem_2)
# Añade las opciones para los otros problemas

root.mainloop()
