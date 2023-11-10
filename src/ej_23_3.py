"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás 
desde ese número hasta cero separados por comas. Deberá solicitar el número hasta introducir uno correcto. 

"""

def pedirNumero() -> int:
    #asegura devolver un int en la función
    cont = True
    while cont == True:
        try:
            numero = int(input("Introduce un número entero positivo: "))
            if numero > 0:
                cont = False
                return numero
            else:
                print("Debes introducir un número positivo mayor que 0.")
        except ValueError:
            print("Debes introducir un número válido.")

def bucle(numero):
    #es un bucle como el de 23_3, que devuelve el valor a la inversa
    serie = ""
    for i in range(numero, -1, -1):
        if i > 0:
            serie += str(i) + ", "
        else:
            serie += str(i)
    return serie

def main():
    numero = pedirNumero()
    serie = bucle(numero)
    print(serie)

if __name__ == "__main__":
    main()