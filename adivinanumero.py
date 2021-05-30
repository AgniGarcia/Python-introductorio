print("""BIENVENIDO A ATÍNALE AL NÚMERO 🧙🏻‍♂️; 
A CONTINUACIÓN PENSARÉ UN NÚMERO Y TRATARÁS DE ADIVINARLO. 
SÍ TE TOMA MÁS DE 5 INTENTOS PAGARÁS 1 CRÉDITO POR INTENTO EQUIVALENTE A UN BESO""")

import random


def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input("Elige un número del 1 al 100: "))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print("Busca un número más grande")
        else:
            print("Busca un número más pequeño")
        numero_elegido = int(input("Escoge otro numero: "))   
    if numero_elegido == numero_aleatorio:
        print("Ganaste!")
        break

if __name__ == "__main__":
    run() 