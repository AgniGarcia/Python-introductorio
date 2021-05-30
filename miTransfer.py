print(""" BIENVENIDO A BANORTE """)

def COMISION(monto):
    if monto < saldo:
        continue
    else:
        print ("Saldo insuficiente, ingrese otra cantidad")


cuenta_cliente = 12345
SALDO = 1000000
horaDisp1 = range(9, 12)
horaDisp2 = range(15, 20)
referenciaDestino = "123"
CARGO = 1500

verificacion = int(input("Ingresa tu cuenta: "))
while verificacion == cuenta_cliente: 
    print("Bienvenido Agni")
else:
    print ("Cuenta inválida")
    verificacion = int(input("Ingresa otra cuenta: "))

hora = input("Ingrese hora: ")
if hora == horaDisp1 or horaDisp2:
    pass
else: 
    print("Lo sentimos, el próximo horario de atención es entre 9 - 12 am o 15 - 20 pm")

cuenta_destino = input("Ingrese la cuenta a la que desea transferir: ")
if cuenta_destino == referenciaDestino: 
    print("BANCO HERMANO")
    monto = int(input("Seleccione el monto que desea transferir: "))
    if monto < SALDO: 
        print("Transferencia exitosa")
    else:
        print("Fondos insuficientes")
elif cuenta_cliente != referenciaDestino: 
    print("BANCO CON COMISIÓN")
    monto = int(input("Seleccione el monto que desea transferir: "))
    monto = monto + CARGO
    if monto < SALDO:
        print("Transferencia exitosa")
    else:
        print("Fondos insuficientes")