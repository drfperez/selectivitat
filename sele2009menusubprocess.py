import tkinter as tk
import subprocess

def execute_problem_1():
    subprocess.call(['python', 'problema1.py'])

def execute_problem_2():
    subprocess.call(['python', 'problema2.py'])

# Define las funciones para los problemas restantes

root = tk.Tk()
root.title("Menú de problemas")

# Crea el menú desplegable
menu = tk.Menu(root)
root.config(menu=menu)

problem_menu = tk.Menu(menu)
menu.add_cascade(label="Elegir problema", menu=problem_menu)

problem_menu.add_command(label="Problema 1", command=execute_problem_1)
problem_menu.add_command(label="Problema 2", command=execute_problem_2)
# Añade las opciones para los otros problemas

root.mainloop()
