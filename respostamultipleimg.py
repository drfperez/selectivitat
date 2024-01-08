import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image

preguntes = [
    ("Qüestió 1: La tensió de ruptura d’un llautó és 550 MPa. Quina força axial cal per a provocar el trencament d’un eix massís de 6 mm de diàmetre?",
     ["10,37 kN", "15,55 kN", "19,80 kN", "62,20 kN"],
     "A"),
    # Altres preguntes van aquí...
    ("Pregunta 5: Què és una imatge?",
     [
         {"text": "Un conjunt de píxels", "img_path": "ruta_imatge_resposta1.jpg"},
         {"text": "Un bloc de text", "img_path": "ruta_imatge_resposta2.jpg"},
         # ... altres respostes
     ],
     "A")
]

def comprovar_respostes(respostes_correctes, respostes_seleccionades):
    colors = []
    correctes = []

    for i in range(len(respostes_correctes)):
        if respostes_seleccionades[i].get() == respostes_correctes[i]:
            colors.append('green')
            correctes.append(True)
        else:
            colors.append('red')
            correctes.append(False)

    num_correctes = sum(correctes)
    messagebox.showinfo("Resultat", f"Has encertat {num_correctes} de {len(respostes_correctes)} preguntes.")

# Inicialització de la finestra i preguntes actuals
root = tk.Tk()
root.title("Preguntes amb imatge")

# Funció per carregar imatges
def carregar_imatge(path, width, height):
    img = Image.open(path)
    img = img.resize((width, height), Image.ANTIALIAS)
    return ImageTk.PhotoImage(img)

def mostrar_pregunta(pregunta, respostes):
    # Aquesta és la variable que has d'assignar amb el camí de la imatge de la pregunta
    ruta_imatge_pregunta = "ruta_imatge_pregunta.jpg"
    label_imatge_pregunta = tk.Label(root, image=carregar_imatge(ruta_imatge_pregunta, 200, 200))
    label_imatge_pregunta.pack()

    label_text_pregunta = tk.Label(root, text=pregunta, justify='left')
    label_text_pregunta.pack()

    resposta_seleccionada = tk.StringVar()
    resposta_seleccionada.set(None)

    labels_imatges_respostes = []
    for i, resposta in enumerate(respostes):
        text = resposta["text"]
        # Aquesta és la clau correcta per accedir al camí de la imatge de la resposta
        img_resposta = carregar_imatge(resposta["img_path"], 100, 100)

        radio = tk.Radiobutton(root, text=text, variable=resposta_seleccionada, value=chr(ord('A') + i))
        radio.pack()

        label_imatge_resposta = tk.Label(root, image=img_resposta)
        label_imatge_resposta.pack()
        labels_imatges_respostes.append(label_imatge_resposta)

    return resposta_seleccionada, labels_imatges_respostes

respostes_correctes = []
respostes_seleccionades = []

for pregunta, respostes, resposta_correcta in preguntes:
    resposta_seleccionada, labels_respostes = mostrar_pregunta(pregunta, respostes)
    respostes_correctes.append(resposta_correcta)
    respostes_seleccionades.append(resposta_seleccionada)

btn_comprovar = tk.Button(root, text="Comprovar respostes", command=lambda: comprovar_respostes(respostes_correctes, respostes_seleccionades))
btn_comprovar.pack()

root.mainloop()
