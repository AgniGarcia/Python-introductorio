def palindromo(palabra): 
    palabra = palabra.replace("","") # Sirve para reemplazar todos los espacios entre palabras
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run(): # funcion para correr el programa desde el principio, también se usa main
    palabra = input("Escribe una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Es palindromo")
    else:
        print("No es palindromo")


if __name__ == "__main__": # Punto de entrada para python, siempre comienza por aquí
    run()
