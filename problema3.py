import tkinter as tk

def calcular():
    # Obtenir les dades introduïdes pel usuari
    consumo = consumo_entry.get()
    dias_anio = dias_anio_entry.get()
    potencia_placa = potencia_placa_entry.get()
    area_placa = area_placa_entry.get()
    intensidad_solar = intensidad_solar_entry.get()
    factor_emision = factor_emision_entry.get()

    # Calcular l'energia total consumida en un any a l'edifici municipal
    energia_consumida = float(consumo) * float(dias_anio)

    # Calcular la potència que ha de subministrar la instaŀlació fotovoltaica
    potencia_foto = energia_consumida / 0.15

    # Mostrar els resultats
    resultado_label.config(text="Energia total consumida en un any a l'edifici municipal: " + str(energia_consumida) + " kW h\n" + "Potència que ha de subministrar la instaŀlació fotovoltaica: " + str(potencia_foto) + " kW")

root = tk.Tk()
root.title("Càlcul fotovoltaic en edifici")

# Estilització del formulari
form = tk.Frame(root, width=500, borderwidth=1, relief="solid")
form.pack(pady=20)

tk.Label(form, text="Càlcul fotovoltaic en edifici", font=("Arial", 16, "bold")).pack(pady=10)

consumo_label = tk.Label(form, text="Consum mitjà en kW h/dia:")
consumo_label.pack()
consumo_entry = tk.Entry(form)
consumo_entry.pack()

dias_anio_label = tk.Label(form, text="Nombre de dies d'un any:")
dias_anio_label.pack()
dias_anio_entry = tk.Entry(form)
dias_anio_entry.pack()

potencia_placa_label = tk.Label(form, text="Potència de la placa en W:")
potencia_placa_label.pack()
potencia_placa_entry = tk.Entry(form)
potencia_placa_entry.pack()

area_placa_label = tk.Label(form, text="Àrea efectiva de la placa en m²:")
area_placa_label.pack()
area_placa_entry = tk.Entry(form)
area_placa_entry.pack()

intensidad_solar_label = tk.Label(form, text="Intensitat de radiació solar en W/m²:")
intensidad_solar_label.pack()
intensidad_solar_entry = tk.Entry(form)
intensidad_solar_entry.pack()

factor_emision_label = tk.Label(form, text="Factor d'emissió en g CO2/(kW h):")
factor_emision_label.pack()
factor_emision_entry = tk.Entry(form)
factor_emision_entry.pack()

calcular_button = tk.Button(form, text="Calcular", command=calcular, bg="#4CAF50", fg="white", width=20)
calcular_button.pack(pady=10)

resultado_label = tk.Label(root, text="", font=("Arial", 14), borderwidth=1, relief="solid", padx=20, pady=20)
resultado_label.pack()

root.mainloop()
