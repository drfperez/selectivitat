from tkinter import *

def calcular():
    # Llegir les dades de l'formulari
    num_aerogeneradores = int(num_aerogeneradores_entry.get())
    diametre = int(diametre_entry.get())
    rendimiento_aerog = float(rendimiento_aerog_entry.get())
    velocidad_viento = int(velocidad_viento_entry.get())
    dias_funcionamiento = int(dias_funcionamiento_entry.get())
    horas_diarias = int(horas_diarias_entry.get())
    densidad_aire = int(densidad_aire_entry.get())
    coef_aprovechamiento_viento = float(coef_aprovechamiento_viento_entry.get())
    precio_venta = float(precio_venta_entry.get())
    
    # Calcular la potència elèctrica útil
    area_escombratge = ((diametre / 2) ** 2) * 3.1416
    densidad = densidad_aire / 1000
    potencia_especifica = 0.5 * densidad * coef_aprovechamiento_viento * (velocidad_viento ** 3)
    potencia_eolica = potencia_especifica * area_escombratge
    potencia_electrica = num_aerogeneradores * potencia_eolica * rendimiento_aerog * dias_funcionamiento * horas_diarias
    
    # Mostrar el resultat
    resultado_label.config(text="La potència elèctrica útil del parc eòlic és de {:.2f} kW.".format(potencia_electrica))
    beneficio_label.config(text="El benefici anual del parc eòlic és de {:.2f} euros.".format((potencia_electrica * precio_venta * 365) / 100))
    

# Crear la finestra
window = Tk()
window.title("Càlcul de potència elèctrica útil de parc eòlic")

# Crear els widgets
num_aerogeneradores_label = Label(window, text="Nombre d'aerogeneradors:")
num_aerogeneradores_entry = Entry(window)
diametre_label = Label(window, text="Diàmetre de l'àrea d'escombratge de les pales en m:")
diametre_entry = Entry(window)
rendimiento_aerog_label = Label(window, text="Rendiment dels aerogeneradors:")
rendimiento_aerog_entry = Entry(window)
velocidad_viento_label = Label(window, text="Velocitat mitjana del vent en km/h:")
velocidad_viento_entry = Entry(window)
dias_funcionamiento_label = Label(window, text="Dies de funcionament del parc:")
dias_funcionamiento_entry = Entry(window)
horas_diarias_label = Label(window, text="Hores diàries de funcionament del parc:")
horas_diarias_entry = Entry(window)
densidad_aire_label = Label(window, text="Densitat de l'aire en g/m³:")
densidad_aire_entry = Entry(window)
coef_aprovechamiento_viento_label = Label(window, text="Coeficient d'aprofitament del vent:")
coef_aprovechamiento_viento_entry = Entry(window)
precio_venta_label.grid(row=8, column=0)
precio_venta_entry.grid(row=8, column=1)
calcular_button.grid(row=9, column=1)
resultado_label.grid(row=10, column=1)
beneficio_label.grid(row=11, column=1)
#Mostrar la finestra
window.mainloop()
