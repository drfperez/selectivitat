import tkinter as tk

def calcular():
    # Llegir les dades de l'formulari
    potencia_paneles = float(potencia_paneles_entry.get())
    num_paneles = float(num_paneles_entry.get())
    rendimiento_paneles = float(rendimiento_paneles_entry.get())
    horas_sol = float(horas_sol_entry.get())
    dias_funcionamiento = float(dias_funcionamiento_entry.get())
    precio_venta = float(precio_venta_entry.get())

    # Calcular la potència elèctrica útil
    potencia_util = (potencia_paneles * num_paneles * rendimiento_paneles/100 * horas_sol * dias_funcionamiento) / 1000
    ganancia = potencia_util * precio_venta

    # Mostrar el resultat
    resultado_label.configure(text=f"La potència elèctrica útil generada per l'instal·lació és de {potencia_util:.2f} kW h/any i la ganancia és de {ganancia:.2f} cèntims d'euro/any.")


root = tk.Tk()
root.title("Càlcul de potència elèctrica útil de instal·lació fotovoltaica")

potencia_paneles_label = tk.Label(root, text="Potència de cada panel fotovoltaic (en W):")
potencia_paneles_label.grid(row=0, column=0, padx=5, pady=5)
potencia_paneles_entry = tk.Entry(root)
potencia_paneles_entry.grid(row=0, column=1, padx=5, pady=5)

num_paneles_label = tk.Label(root, text="Nombre de panells fotovoltaics:")
num_paneles_label.grid(row=1, column=0, padx=5, pady=5)
num_paneles_entry = tk.Entry(root)
num_paneles_entry.grid(row=1, column=1, padx=5, pady=5)

rendimiento_paneles_label = tk.Label(root, text="Rendiment dels panells fotovoltaics (%):")
rendimiento_paneles_label.grid(row=2, column=0, padx=5, pady=5)
rendimiento_paneles_entry = tk.Entry(root)
rendimiento_paneles_entry.grid(row=2, column=1, padx=5, pady=5)

horas_sol_label = tk.Label(root, text="Hores de sol diàries:")
horas_sol_label.grid(row=3, column=0, padx=5, pady=5)
horas_sol_entry = tk.Entry(root)
horas_sol_entry.grid(row=3, column=1, padx=5, pady=5)

dias_funcionamiento_label = tk.Label(root, text="Dies de funcionament de l'instal·lació:")
dias_funcionamiento_label.grid(row=4, column=0, padx=5, pady=5)
dias_funcionamiento_entry = tk.Entry(root)
dias_funcionamiento_entry.grid(row=4, column=1, padx=5, pady=5)

precio_venta_label = tk.Label(root, text="Preu de venda de l'energia fotovoltaica en cèntims d'euro per kW h:")
precio_venta_label.grid(row=5, column=0, padx=5, pady=5)
precio_venta_entry = tk.Entry(root)
precio_venta_entry.grid(row=5, column=1, padx=5, pady=5)
calcular_button = tk.Button(root, text="Calcular", command=calcular)
calcular_button.grid(row=6, column=0, padx=5, pady=5)

resultado_label = tk.Label(root, text="")
resultado_label.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
