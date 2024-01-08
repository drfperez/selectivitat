import tkinter as tk
from tkinter import messagebox

# Llista de tuples amb les preguntes, les opcions i les respostes correctes
preguntes = [
    ("Qüestió 1: La tensió de ruptura d’un llautó és 550 MPa. Quina força axial cal per a provocar el trencament d’un eix massís de 6 mm de diàmetre?",
     ["10,37 kN", "15,55 kN", "19,80 kN", "62,20 kN"],
     "a"),
    ("Qüestió 2: En una línia de producció hi ha tres estacions i les operacions que es duen a terme sobre cada unitat produïda requereixen, respectivament, 15 s, 30 s i 20 s. En règim estacionari i amb la línia funcionant a màxim rendiment, cada quants segons surt una unitat de la línia?",
     ["20 s", "30 s", "15 s", "65 s"],
     "c"),
    ("Qüestió 3: Quina és la fórmula química de l'aigua?",
     ["H2O", "O2", "CO2", "CH4"],
     "a"),
    ("Qüestió 4: Quin és el valor de pi amb tres decimals?",
     ["3,141", "3,142", "3,143", "3,144"],
     "b")
]

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

# Crear la finestra
root = tk.Tk()
root.title("Comprovació de respostes")

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

root.mainloop()
