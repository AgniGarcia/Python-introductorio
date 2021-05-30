dolar = input("¿Cuántos dolares gringos tienes?: ")
dolar = float(dolar)
valor_pesos = 4
pesos = valor_pesos * dolar
pesos = round(pesos, 2) 
pesos = str(pesos)
print("Tienes $" + pesos + " pesos")