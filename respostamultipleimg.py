import tkinter as tk
from tkinter import messagebox



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

import tkinter as tk
from tkinter import messagebox
import requests

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
     "b"),
    ("Qüestió 5: Quin és l'animal que representa la famosa teoria de l'evolució de Charles Darwin?",
     ["Tortuga", "Elefante", "Pinguino", "Gallo"],
     "a")
]

def comprovar_respostes(respostes_correctes, respostes_seleccionades, labels_respostes):
    colors = []
    correctes = []

    for i in range(len(respostes_correctes)):
        if respostes_seleccionades[i].get() == respostes_correctes[i]:
            colors.append('green')
            correctes.append(True)
        else:
            colors.append('red')
            correctes.append(False)

    for i in range(len(labels_respostes)):
        labels_respostes[i].config(bg=colors[i])

    num_correctes = sum(correctes)
    messagebox.showinfo("Resultat", f"Has encertat {num_correctes} de {len(respostes_correctes)} preguntes.")

root = tk.Tk()
root.title("Comprovació de respostes")

respostes_correctes = []
respostes_seleccionades = []
labels_respostes = []

y = 10

for i, pregunta_info in enumerate(preguntes):
    pregunta, opcions, resposta_correcta = pregunta_info

    label_pregunta = tk.Label(root, text=pregunta, justify='left')
    label_pregunta.place(x=10, y=y)

    y += 25

    resposta_seleccionada = tk.StringVar()
    resposta_seleccionada.set(None)
    respostes_seleccionades.append(resposta_seleccionada)

    for j, opcio in enumerate(opcions):
        radio = tk.Radiobutton(root, text=opcio, variable=resposta_seleccionada, value=chr(ord('a') + j))
        radio.place(x=30, y=y)
        y += 20

    label_resposta = tk.Label(root, text="Resposta " + str(i + 1), width=20)
    label_resposta.place(x=10, y=y)
    labels_respostes.append(label_resposta)

    respostes_correctes.append(resposta_correcta)

    y += 30

# Función para mostrar la imagen
def mostrar_imagen():
    # Ruta local de la imagen
    ruta_imagen = "io.png"  # Reemplaza con el nombre y formato de tu imagen

    imagen = tk.PhotoImage(file=ruta_imagen)
    label_imagen = tk.Label(root, image=imagen)
    label_imagen.image = imagen
    label_imagen.place(x=700, y=200)


# Llamada a la función para mostrar la imagen (puedes llamarla en el lugar que prefieras)
mostrar_imagen()

btn_comprovar = tk.Button(root, text="Comprovar respostes", command=lambda: comprovar_respostes(respostes_correctes, respostes_seleccionades, labels_respostes))
btn_comprovar.place(x=10, y=y)

root.mainloop()
