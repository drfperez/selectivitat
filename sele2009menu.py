# Importa les funcions de cada problema
from problema1 import resoldre_problema1
from problema2 import resoldre_problema2
from problema3 import resoldre_problema3

# Defineix una funció que mostra el menú i permet a l'usuari triar un problema
def menu():
    print("Benvingut al menú de selecció de problemes:")
    print("1. Problema 1")
    print("2. Problema 2")
    print("3. Problema 3")

    opcio = input("Selecciona un problema (1-3): ")

    if opcio == '1':
        resoldre_problema1()
    elif opcio == '2':
        resoldre_problema2()
    elif opcio == '3':
        resoldre_problema3()
    else:
        print("Opció invàlida. Torna a seleccionar.")

# Executa la funció del menú
if __name__ == "__main__":
    menu()
