
"""
Escribir un programa que pida al usuario un número entero, 
si la entrada no es correcta, mostrará el mensaje "La entrada no es correcta" y lanzará la excepción capturada.

"""

def pedirNumero(num: str):
    # usamos la entencia try para comprobar si el input es un valor númerico
    try:
        if num.isnumeric():
            valor = "Correcto"
            #en caso de que lo sea, aplicamos el valor correcto a la variable valor
        else:
            raise ValueError 
    except ValueError:
         #en caso de que no lo sea, lanzaremos la excepción, y asignaremos el valor incorrecto a la variable
        valor = "La entrada no es correcta"
    finally:
        return valor
        #cerramos el bloque con la sentencia finally, que retornará el valor de tenga la función

def main():
    num = (input("Escribe un número entero: "))
    valor = pedirNumero(num)
    print(valor)

if __name__ == "__main__":
    main()