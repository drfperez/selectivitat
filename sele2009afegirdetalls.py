def mostrar_resultats_detallats():
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

    detalls = f"Detalls dels càlculs:\n"
    detalls += f"Potència Útil (P): P = q * cp * Δt / 60\n"
    detalls += f"  P = {q:.2f} L/min * {cp:.3f} J/(g·K) * {delta_t} °C / 60 = {P:.2f} kW\n\n"
    detalls += f"Consum de butà (qcomb): qcomb = (q * cp * Δt) / (eta * pc)\n"
    detalls += f"  qcomb = ({q:.2f} L/min * {cp:.3f} J/(g·K) * {delta_t} °C) / ({eta} * {pc} MJ/kg) = {q_comb:.2f} g/s\n\n"
    detalls += f"Cost econòmic (c): c = (cb * t) / 60\n"
    detalls += f"  c = ({cb} € * {t} min) / 60 = {c:.2f} €"
    
    etiqueta_detalls.config(text=detalls)
