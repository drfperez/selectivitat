import tkinter as tk
import markdown

# Funcions pels botons
def comprovar_resultat():
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
    if abs(P - valor_introduit_a) <= valor_a * tolerancia:
        etiqueta_resultat_a.config(text="Correcte")
    else:
        etiqueta_resultat_a.config(text="Incorrecte")

    if abs(q_comb - valor_introduit_b) <= valor_b * tolerancia:
        etiqueta_resultat_b.config(text="Correcte")
    else:
        etiqueta_resultat_b.config(text="Incorrecte")

    if abs(c - valor_introduit_c) <= valor_c_cost * tolerancia:
        etiqueta_resultat_c.config(text="Correcte")
    else:
        etiqueta_resultat_c.config(text="Incorrecte")

def mostrar_pista():
    # Pista amb les fórmules (usant Markdown)
    pista = """
    ### Fórmules

    a) **Potència Útil (P)**:

    $ P = \\frac{q \\cdot c_p \\cdot \Delta t}{60} $

    b) **Consum de butà (qcomb)**:

    $ q_{comb} = \\frac{q \\cdot c_p \\cdot \Delta t}{\eta \\cdot pc} $

    c) **Cost econòmic (c)**:

    $ c = \\frac{cb \\cdot t}{60} $
    """

    # Renderització de Markdown
    html_pista = markdown.markdown(pista)
    etiqueta_pista.config(text=html_pista)

def mostrar_resultats_detallats():
    # Detalls dels càlculs (usant Markdown)
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

    detalls = f"""
    ### Detalls dels càlculs

    - **Potència Útil (P)**: {P:.2f} kW
    - **Consum de butà (qcomb)**: {q_comb:.2f} g/s
    - **Cost econòmic (c)**: {c:.2f} €
    """

    # Renderització de Markdown
    html_detalls = markdown.markdown(detalls)
    etiqueta_detalls.config(text=html_detalls)

# Crear la finestra principal
root = tk.Tk()
root.title("Escalfador d'aigua")

# Resta del codi igual a com l'has presentat

root.mainloop()
