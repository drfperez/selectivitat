import tkinter as tk
from PIL import Image, ImageTk
import matplotlib.pyplot as plt

# Funcions pels botons
def comprovar_resultat():
    # (El teu codi de comprovació de resultats)

def mostrar_pista():
    # (El teu codi per mostrar la pista amb les fórmules)

def mostrar_resultats_detallats():
    # Codi original per calcular els detalls
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

    # Convertir els resultats a format LaTeX
    latex_detalls = (
        f"\\text{{Detalls dels càlculs:}}\n"
        f"\\text{{Potència Útil (P):}} {P:.2f} \\text{{ kW}}\n"
        f"\\text{{Consum de butà (qcomb):}} {q_comb:.2f} \\text{{ g/s}}\n"
        f"\\text{{Cost econòmic (c):}} {c:.2f} \\text{{ €}}"
    )

    # Mostrar els detalls en la etiqueta corresponent
    mostrar_formula_latex(latex_detalls, etiqueta_detalls)

# La resta del codi roman igual
