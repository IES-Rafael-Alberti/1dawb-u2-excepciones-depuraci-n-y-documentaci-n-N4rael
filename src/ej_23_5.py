"""
Escribir que solicite una contraseña, y si no coincide con la que se tiene, 
lance la excepción NameError con el mensaje, "Incorrect Password!!" 

"""

def pedir_contraseña(input_user, contraseña):
    #con la sentencia try comparamos que el input y la contraseña sean la misma
    try:
        if input_user == contraseña:
            valor = "Password is correct! Redirecting... "
            #en caso de que si lo sean, asignamos un valor bueno a una variable
        else:
            raise NameError
    except NameError:
        valor = "Incorrect Password!"
        # en caso de que no sean iguales, lanzamos un NameError, 
        # al capturarlo se le asignará un valor malo a la variable
    
    finally:
        return valor
    #con la sentencia finally retornamos el valor que tenga la función, lance el error o no



def main():
    contraseña = "hola_mundo"
    input_user = input("Escriba la contraseña: ")
    valor = pedir_contraseña(contraseña, input_user)
    print(valor)

if __name__ == "__main__":
    main()