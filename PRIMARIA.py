import tkinter as tk
import random
import time

def pregunta_operacio(operacio, min_num, max_num, decimals):
    num1 = random.uniform(min_num, max_num)
    num2 = random.uniform(min_num, max_num)
    if operacio == '/':
        num1 = round(num1, decimals)
        num2 = round(num2, decimals)
        while num2 == 0:  # Evitar divisió per zero
            num2 = random.uniform(min_num, max_num)
            num2 = round(num2, decimals)
    num1 = round(num1, decimals)
    num2 = round(num2, decimals)
    pregunta = f"Quin és el resultat de {num1} {operacio} {num2}? "
    resultat_correcte = eval(f"{num1} {operacio} {num2}")
    return pregunta, resultat_correcte

def comprova_resposta(pregunta, resposta, resultat_correcte):
    if resposta == resultat_correcte:
        return True
    return False

def generar_pregunta():
    operacio = operacions_var.get()
    min_num = float(min_num_entry.get())
    max_num = float(max_num_entry.get())
    decimals = int(decimals_var.get())
    pregunta, resultat_correcte = pregunta_operacio(operacio, min_num, max_num, decimals)
    pregunta_label.config(text=pregunta)
    resposta_entry.delete(0, tk.END)
    
    global temps_inicial
    temps_inicial = time.time()  # Captura el temps inicial
    
    return resultat_correcte

def comprovar_resposta():
    resultat_correcte = pregunta_actual[1]
    resposta = resposta_entry.get()
    if resposta:
        resposta = float(resposta) if '/' in pregunta_actual[0] else round(float(resposta), int(decimals_var.get()))
        correcte = comprova_resposta(pregunta_actual[0], resposta, resultat_correcte)
        if correcte:
            global respostes_correctes
            respostes_correctes += 1
            respostes_correctes_label.config(text=f"Respostes correctes: {respostes_correctes}")
        global preguntes_fetes
        preguntes_fetes += 1
        preguntes_fetes_label.config(text=f"Preguntes fetes: {preguntes_fetes}")
        
        temps_final = time.time()  # Captura el temps final
        temps_resposta = round(temps_final - temps_inicial, 2)  # Calcula el temps de resposta
        temps_label.config(text=f"Temps de resposta: {temps_resposta} segons")

        pregunta_actual = generar_pregunta()

# Configuració de la interfície gràfica
root = tk.Tk()
root.title("Practicant de Matemàtiques")

preguntes_fetes = 0
respostes_correctes = 0
pregunta_actual = None

operacions = ['+', '-', '*', '/']

operacions_var = tk.StringVar(root)
operacions_var.set(operacions[0])

operacions_menu = tk.OptionMenu(root, operacions_var, *operacions)
operacions_menu.pack()

min_num_label = tk.Label(root, text="Nombre mínim:")
min_num_label.pack()

min_num_entry = tk.Entry(root)
min_num_entry.pack()

max_num_label = tk.Label(root, text="Nombre màxim:")
max_num_label.pack()

max_num_entry = tk.Entry(root)
max_num_entry.pack()

decimals_label = tk.Label(root, text="Decimals en divisió:")
decimals_label.pack()

decimals_var = tk.StringVar(root)
decimals_var.set("0")

decimals_menu = tk.OptionMenu(root, decimals_var, "0", "1", "2")
decimals_menu.pack()

pregunta_label = tk.Label(root, text="")
pregunta_label.pack()

resposta_entry = tk.Entry(root)
resposta_entry.pack()

comprovar_button = tk.Button(root, text="Comprovar", command=comprovar_resposta)
comprovar_button.pack()

respostes_correctes_label = tk.Label(root, text=f"Respostes correctes: {respostes_correctes}")
respostes_correctes_label.pack()

preguntes_fetes_label = tk.Label(root, text=f"Preguntes fetes: {preguntes_fetes}")
preguntes_fetes_label.pack()

temps_label = tk.Label(root, text="")
temps_label.pack()

pregunta_actual = generar_pregunta()

root.mainloop()
