import tkinter as tk
from tkinter import messagebox
import json

# Crear la finestra principal
root = tk.Tk()

# Obre el fitxer JSON amb el mode de lectura
fitxer = open("preguntes.json", mode="r", encoding="utf-8")

# Carrega el contingut del fitxer JSON en una variable
preguntes = json.load(fitxer)

# Tanca el fitxer
fitxer.close()

# Funció per a comprovar les respostes
def comprovar_respostes(respostes_correctes, respostes_seleccionades, labels_respostes):
    colors = []  # Llista per a emmagatzemar els colors (vermell o verd)
    correctes = []  # Llista per a emmagatzemar els valors booleans de les respostes

    # Comprovar respostes i assignar els colors i els valors booleans
    for i in range(len(respostes_correctes)):
        if respostes_seleccionades[i] == respostes_correctes[i]:
            colors.append('green')  # Si és correcte, verd
            correctes.append(True)  # Si és correcte, True
        else:
            colors.append('red')  # Si és incorrecte, vermell
            correctes.append(False)  # Si és incorrecte, False

    # Mostrar els colors en les etiquetes corresponents
    for i in range(len(labels_respostes)):
        labels_respostes[i].config(bg=colors[i])

    # Calcular el número de respostes correctes
    num_correctes = sum(correctes)

    # Mostrar el missatge informatiu amb el resultat
    messagebox.showinfo("Resultat", f"Has encertat {num_correctes} de {len(respostes_correctes)} preguntes.")

# Crear les variables, els botons de ràdio i les etiquetes per a cada pregunta
respostes_correctes = []  # Llista per a emmagatzemar les respostes correctes
respostes_seleccionades = []  # Llista per a emmagatzemar les respostes seleccionades
labels_respostes = []  # Llista per a emmagatzemar les etiquetes de les respostes

# Posicions inicials dels widgets
x = 10
y = 10

for i in range(len(preguntes)):
    # Obtenir la pregunta, les opcions i la resposta correcta de la llista de tuples
    pregunta, opcions, resposta_correcta = preguntes[i]

    # Crear una etiqueta amb el text de la pregunta
    label_pregunta = tk.Label(root, text=pregunta)
    label_pregunta.place(x=x, y=y)

    # Actualitzar la posició y
    y += 20

    # Crear una variable per a emmagatzemar la resposta seleccionada
    resposta_seleccionada = tk.StringVar()
    respostes_seleccionades.append(resposta_seleccionada)

    # Crear els botons de ràdio amb les opcions
    for j in range(len(opcions)):
        radio = tk.Radiobutton(root, text=opcions[j], variable=resposta_seleccionada, value=chr(ord('a') + j))
        radio.place(x=x, y=y)

        # Actualitzar la posició y
        y += 20

    # Crear una etiqueta per a mostrar el color de la resposta
    label_resposta = tk.Label(root, text="Resposta " + str(i + 1), width=20)
    label_resposta.place(x=x, y=y)
    labels_respostes.append(label_resposta)

    # Afegir la resposta correcta a la llista
    respostes_correctes.append(resposta_correcta)

    # Actualitzar la posició x i y
    x += 100
    y = 10

# Botó per a comprovar les respostes
# Utilitzar una funció lambda per a passar els paràmetres a la funció comprovar_respostes
btn_comprovar = tk.Button(root, text="Comprovar respostes", command=lambda: comprovar_respostes(respostes_correctes, respostes_seleccionades, labels_respostes))
btn_comprovar.place(x=10, y=200)

# Iniciar el bucle principal
root.mainloop()
