import tkinter as tk
from PIL import Image, ImageTk

# Funcions pels botons
# (El teu codi de funcions)

# Crear la finestra principal
root = tk.Tk()
root.title("Escalfador d'aigua")

# Enunciat del problema amb imatge
enunciat_text = "Un escalfador d’aigua que funciona amb butà, de poder calorífic pc = 47,7 MJ/kg, té un rendiment η = 80 %, dóna un cabal q = 7 L/min i provoca un augment de la temperatura Δt = 25 °C. El butà se subministra en bombones que en contenen mb = 12,5 kg i valen cb = 13,5 €. La calor específica de l’aigua és cp = 4,187 J/(g · K). En aquestes condicions, determineu:\n\na) La potència útil P.\nb) El consum de butà, qcomb, en g/s.\nc) El cost econòmic c, en €, i la quantitat mcomb del combustible emprat en t = 10 min."
label_enunciat = tk.Label(root, text=enunciat_text, wraplength=800, anchor="w")
label_enunciat.pack()

# Afegir imatge d'enunciat
enunciat_image = Image.open("enunciat.png")
enunciat_photo = ImageTk.PhotoImage(enunciat_image)
label_enunciat.image = enunciat_photo  # Referència necessària per evitar la pèrdua de la imatge a causa de la recollida de l'escombraries
label_enunciat.config(image=enunciat_photo)
label_enunciat.pack()

# Interfície per introduir les dades
# (Les teves etiquetes d'entrada)

# Afegir imatge dels resultats
resultat_image = Image.open("resultat.png")
resultat_photo = ImageTk.PhotoImage(resultat_image)
label_resultat = tk.Label(root, image=resultat_photo)
label_resultat.image = resultat_photo  # Referència necessària per evitar la pèrdua de la imatge a causa de la recollida de l'escombraries
label_resultat.pack()

# Botons
# (Els teus botons)

# Etiquetes per mostrar els resultats
# (Les teves etiquetes de resultat)

# Bucle principal per mostrar la finestra
root.mainloop()
