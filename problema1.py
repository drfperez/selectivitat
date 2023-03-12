# Obtain input data from user
potencia = float(input("Introdueix la potència del motor en kW: "))
calor_especifica = float(input("Introdueix la calor específica del gasoil en kJ/kg: "))
poder_calorifico_superior = float(input("Introdueix el poder calorífic superior del gasoil en MJ/kg: "))
rendimiento = float(input("Introdueix el rendiment del motor en %: "))

# Calculate the amount of heat produced per minute
calor = potencia * 60

# Calculate the mass of diesel needed to produce this amount of heat
massa_gasoil = calor / (calor_especifica * poder_calorifico_superior * 1000)

# Calculate the flow of diesel to be supplied to the engine per minute
cabal_gasoil = massa_gasoil / 60

# Print the results
print("La quantitat de calor que es produeix cada minut es de", calor, "kJ.")
print("La massa de gasoil necessària per produir aquesta quantitat de calor és de", massa_gasoil, "kg/min.")
print("El cabal de gasoil que s'ha de fer arribar al motor cada minut és de", cabal_gasoil, "kg/min.")
