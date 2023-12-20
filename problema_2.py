import tkinter as tk
# Change this import statement in both files
from PIL import ImageTk, Image


# Funcions pels botons
def comprovar_resultat():
    try:
        q = float(entry_q.get())
    except ValueError:
        etiqueta_detalls.config(text="Error: Introdueix dades per poder veure resultats.")
        return

    # Dades del problema
    pc = 47.7  # Poder calorífic en MJ/kg
    eta = 0.8  # Rendiment
    q = float(entry_q.get())  # Cabal en L/min
    delta_t = 25  # Increment de temperatura en °C
    mb = 12.5  # Massa de butà en kg
    cb = 13.5  # Cost de la bombona de butà en €
    cp = 4.187  # Calor específic de l'aigua en J/(g*K)
    t = 10  # Temps en minuts

    # Fórmules per als càlculs
    P = q * cp * delta_t / 60  # Convertim a minuts
    q_comb = (q * cp * delta_t) / (eta * pc)
    c = (cb * t) / 60

    # Valors correctes amb la tolerància del 5%
    valor_a = 1.89  # kW
    valor_b = 61.18  # g/s
    valor_c_cost = 1.35  # €

    # Obtenir els valors introduïts pels usuaris
    valor_introduit_a = float(entry_resultat_a.get())
    valor_introduit_b = float(entry_resultat_b.get())
    valor_introduit_c = float(entry_resultat_c.get())

    # Comprovació amb tolerància
    tolerancia = 0.05  # 5% d'error
    etiqueta_resultat_a.config(text="Correcte" if abs(P - valor_introduit_a) <= valor_a * tolerancia else "Incorrecte")
    etiqueta_resultat_b.config(text="Correcte" if abs(q_comb - valor_introduit_b) <= valor_b * tolerancia else "Incorrecte")
    etiqueta_resultat_c.config(text="Correcte" if abs(c - valor_introduit_c) <= valor_c_cost * tolerancia else "Incorrecte")

def mostrar_pista():
    # Pista amb les fórmules
    pista = "a) Potència Útil (P): P = q * cp * Δt / 60\nb) Consum de butà (qcomb): qcomb = (q * cp * Δt) / (eta * pc)\nc) Cost econòmic (c): c = (cb * t) / 60"
    etiqueta_pista.config(text=pista)

def mostrar_resultats_detallats():
    # Detalls dels càlculs
    pc = 47.7
    eta = 0.8
    q = float(entry_q.get())
    delta_t = 25
    mb = 12.5
    cb = 13.5
    cp = 4.187
    t = 10

    P = q * cp * delta_t / 60
    q_comb = (q * cp * delta_t) / (eta * pc)
    c = (cb * t) / 60

    # Crear una finestra per mostrar els detalls amb imatge i text
    detalls_image = Image.open("detalls.png")  # Substitueix amb el nom correcte del fitxer
    detalls_photo = ImageTk.PhotoImage(detalls_image)
    label_detalls = tk.Label(root, image=detalls_photo, text="Detalls dels càlculs:\n" +
                             f"Potència Útil (P): P = q * cp * Δt / 60\n"
                             f"  P = {q:.2f} L/min * {cp:.3f} J/(g·K) * {delta_t} °C / 60 = {P:.2f} kW\n\n"
                             f"Consum de butà (qcomb): qcomb = (q * cp * Δt) / (eta * pc)\n"
                             f"  qcomb = ({q:.2f} L/min * {cp:.3f} J/(g·K) * {delta_t} °C) / ({eta} * {pc} MJ/kg) = {q_comb:.2f} g/s\n\n"
                             f"Cost econòmic (c): c = (cb * t) / 60\n"
                             f"  c = ({cb} € * {t} min) / 60 = {c:.2f} €", compound="top", font=("Helvetica", 10), wraplength=600)
    label_detalls.image = detalls_photo
    label_detalls.pack()

# Crear la finestra principal
root = tk.Tk()
root.title("Escalfador d'aigua")

# Enunciat del problema amb placeholder d'imatge
enunciat_text = "Un escalfador d’aigua que funciona amb butà, de poder calorífic pc = 47,7 MJ/kg, té un rendiment η = 80 %, dóna un cabal q = 7 L/min i provoca un augment de la temperatura Δt = 25 °C. El butà se subministra en bombones que en contenen mb = 12,5 kg i valen cb = 13,5 €. La calor específica de l’aigua és cp = 4,187 J/(g · K). En aquestes condicions, determineu:\n\na) La potència útil P.\nb) El consum de butà, qcomb, en g/s.\nc) El cost econòmic c, en €, i la quantitat mcomb del combustible emprat en t = 10 min."
label_enunciat = tk.Label(root, text=enunciat_text, wraplength=800, anchor="w")
label_enunciat.pack()

# Afegir imatge d'enunciat
enunciat_image = Image.open("enunciat.png")  # Substitueix amb el nom correcte del fitxer
enunciat_photo = ImageTk.PhotoImage(enunciat_image)
label_enunciat.image = enunciat_photo
label_enunciat.config(image=enunciat_photo)
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

# Bucle principal per mostrar la finestra
root.mainloop()
