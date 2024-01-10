import tkinter as tk

# Funcions pels botons
def comprovar_resultat():
    try:
        q = float(entry_q.get())
    except ValueError:
        etiqueta_detalls.config(text="Error: Introdueix dades per poder veure resultats.")
        return
    # Resta del codi...

def aplicar_justificat_widgets(parent):
    for widget in parent.winfo_children():
        if isinstance(widget, tk.Label):
            widget.config(anchor="w")
        elif isinstance(widget, tk.Frame) or isinstance(widget, tk.Toplevel) or isinstance(widget, tk.Tk):
            aplicar_justificat_widgets(widget)

def mostrar_pista():
    # Pista amb les fórmules
    pista = "a) Potència Útil (P): P = q * cp * Δt / 60\nb) Consum de butà (qcomb): qcomb = (q * cp * Δt) / (eta * pc)\nc) Cost econòmic (c): c = (cb * t) / 60"
    etiqueta_pista.config(text=pista)

def mostrar_resultats_detallats():
    # Detalls dels càlculs
    # Resta del codi...

# Crear la finestra principal
root = tk.Tk()
root.title("Escalfador d'aigua")

# Enunciat del problema
enunciat = "Un escalfador d’aigua que funciona amb butà, de poder calorífic pc = 47,7 MJ/kg, té un rendiment η = 80 %, dóna un cabal q = 7 L/min i provoca un augment de la temperatura Δt = 25 °C. El butà se subministra en bombones que en contenen mb = 12,5 kg i valen cb = 13,5 €. La calor específica de l’aigua és cp = 4,187 J/(g · K). En aquestes condicions, determineu:\n\na) La potència útil P.\nb) El consum de butà, qcomb, en g/s.\nc) El cost econòmic c, en €, i la quantitat mcomb del combustible emprat en t = 10 min."
label_enunciat = tk.Label(root, text=enunciat, wraplength=800, anchor="w")
label_enunciat.pack()

# Interfície per introduir les dades
label_q = tk.Label(root, text="Entra el cabal (L/min):")
entry_q = tk.Entry(root)
label_q.pack()
entry_q.pack()

label_resultat_a = tk.Label(root, text="Resultat a):")
entry_resultat_a = tk.Entry(root)
label_resultat_a.pack()
entry_resultat_a.pack()

label_resultat_b = tk.Label(root, text="Resultat b):")
entry_resultat_b = tk.Entry(root)
label_resultat_b.pack()
entry_resultat_b.pack()

label_resultat_c = tk.Label(root, text="Resultat c):")
entry_resultat_c = tk.Entry(root)
label_resultat_c.pack()
entry_resultat_c.pack()

# Botons
boton_comprovar = tk.Button(root, text="Comprovar Resultat", command=comprovar_resultat)
boton_comprovar.pack()

boton_pista = tk.Button(root, text="Pista amb les Fórmules", command=mostrar_pista)
boton_pista.pack()

boton_detalls = tk.Button(root, text="Mostrar Detalls dels Càlculs", command=mostrar_resultats_detallats)
boton_detalls.pack()

# Etiquetes per mostrar els resultats
etiqueta_resultat_a = tk.Label(root, text="")
etiqueta_resultat_b = tk.Label(root, text="")
etiqueta_resultat_c = tk.Label(root, text="")
etiqueta_detalls = tk.Label(root, text="")
etiqueta_pista = tk.Label(root, text="")

etiqueta_resultat_a.pack()
etiqueta_resultat_b.pack()
etiqueta_resultat_c.pack()
etiqueta_detalls.pack()
etiqueta_pista.pack()

# Aplicar justificat a tots els labels i widgets
aplicar_justificat_widgets(root)

# Bucle principal per mostrar la finestra
root.mainloop()
