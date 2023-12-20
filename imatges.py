import tkinter as tk
from PIL import Image, ImageTk

# Funcions pels botons
def comprovar_resultat():
    # (El teu codi per comprovar el resultat)

def mostrar_pista():
    # (El teu codi per mostrar la pista)

def mostrar_resultats_detallats():
    # (El teu codi per mostrar els detalls)

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

# Afegir imatge dels resultats dins la funció mostrar_resultats_detallats
def mostrar_resultats_detallats():
    resultat_image = Image.open("resultat.png")  # Substitueix amb el nom correcte del fitxer
    resultat_photo = ImageTk.PhotoImage(resultat_image)
    label_resultat = tk.Label(root, image=resultat_photo)
    label_resultat.image = resultat_photo
    label_resultat.pack()
    # Resta del teu codi per mostrar els detalls

# Botons

# Etiquetes per mostrar els resultats

# Bucle principal per mostrar la finestra
root.mainloop()
