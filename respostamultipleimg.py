

import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image

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
     "a"),
     ("Qüestió 6: La tensió de ruptura d’un llautó és 550 MPa. Quina força axial cal per a provocar el trencament d’un eix massís de 6 mm de diàmetre?",
     ["10,37 kN", "15,55 kN", "19,80 kN", "62,20 kN"],
     "a"),
    ("Qüestió 7: En una línia de producció hi ha tres estacions i les operacions que es duen a terme sobre cada unitat produïda requereixen, respectivament, 15 s, 30 s i 20 s. En règim estacionari i amb la línia funcionant a màxim rendiment, cada quants segons surt una unitat de la línia?",
     ["20 s", "30 s", "15 s", "65 s"],
     "c"),
    ("Qüestió 8: Quina és la fórmula química de l'aigua?",
     ["H2O", "O2", "CO2", "CH4"],
     "a"),
    ("Qüestió 9: Quin és el valor de pi amb tres decimals?",
     ["3,141", "3,142", "3,143", "3,144"],
     "b"),
    ("Qüestió 10: Quin és l'animal que representa la famosa teoria de l'evolució de Charles Darwin?",
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
# Creamos un canvas para contener el contenido y permitir el scroll
canvas = tk.Canvas(root)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Añadimos un scrollbar para desplazamiento vertical
scrollbar = tk.Scrollbar(root, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas.config(yscrollcommand=scrollbar.set)

# Creamos un frame para poner dentro del canvas (para el contenido)
frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor='nw')

respostes_correctes = []
respostes_seleccionades = []
labels_respostes = []

y = 10

for i, pregunta_info in enumerate(preguntes):
    pregunta, opcions, resposta_correcta = pregunta_info

    label_pregunta = tk.Label(frame, text=pregunta, justify='left')
    label_pregunta.pack(anchor='w')

    resposta_seleccionada = tk.StringVar()
    resposta_seleccionada.set(None)
    respostes_seleccionades.append(resposta_seleccionada)

    for j, opcio in enumerate(opcions):
        radio = tk.Radiobutton(frame, text=opcio, variable=resposta_seleccionada, value=chr(ord('a') + j))
        radio.pack(anchor='w')

    label_resposta = tk.Label(frame, text="Resposta " + str(i + 1), width=20)
    label_resposta.pack(anchor='w')
    labels_respostes.append(label_resposta)

    respostes_correctes.append(resposta_correcta)

# Función para mostrar la imagen
def mostrar_imagen1():
    ruta_imagen = "io.png"  # Ruta de la imagen original
    imagen = Image.open(ruta_imagen)
    imagen = imagen.resize((200, 200), Image.LANCZOS)  # Cambiar el tamaño de la imagen
    imagen = ImageTk.PhotoImage(imagen)

    label_imagen = tk.Label(frame, image=imagen)
    label_imagen.image = imagen
    label_imagen.place(x=500, y=350)  # Posición de la esquina superior izquierda del widget
# Llamada a la función para mostrar la imagen (puedes llamarla en el lugar que prefieras)
mostrar_imagen1()

btn_comprovar = tk.Button(frame, text="Comprovar respostes", command=lambda: comprovar_respostes(respostes_correctes, respostes_seleccionades, labels_respostes))
btn_comprovar.pack()

# Función para configurar el scroll del canvas cuando cambie el tamaño del frame
def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

frame.bind("<Configure>", on_frame_configure)

root.mainloop()
