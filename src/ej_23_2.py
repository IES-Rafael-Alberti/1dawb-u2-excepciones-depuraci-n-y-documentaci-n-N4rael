"""
Ejercicio 2.3.2¶

Escribir un programa que pida al usuario un número entero positivo y 
muestre por pantalla todos los números impares desde 1 hasta ese número 
separados por comas.

"""
def pedirNumero() -> int: 
    #asegura devolver un int en la función
    numero = input("Número: ")
    try:
        numero = int(numero)
        # convierte a int
        if numero <= 0:
            raise TypeError 
    except TypeError:
        #en caso de que sea un 0, lanzará un TypeError
        print("**ERROR** Tienes que introducir un número positivo o mayor que 0.")
        exit()
    except ValueError: 
        print("**ERROR** Tienes que introducir un número válido")
        exit()
        #en caso de que sea float o srt, lanzará un ValueError que capturaremos
        
    else:
        return numero

def bucle(numero: int):
    serie = ""
    if numero % 2 == 0: numero -= 1 
    # comprobamos que el número sea par o impar, ajustando el input a -1 en caso de que sea par para evitar problemas
    for i in range(1, numero + 1, 2):
        #el bucle for para que imprima la serie de números
        if i < numero:
            print(str(i), end=", ")
            serie += str(i) + ", "
            #reglas del bucle
        elif i == numero:
            print(str(i)) 
            serie += str(i)
            # cuando i sea igual que el input, imprimirá el número sin coma y con un /n
        else:
            exit()
    return serie

def main():
    numero = pedirNumero()
    bucle(numero)
if __name__ == "__main__":
    main()