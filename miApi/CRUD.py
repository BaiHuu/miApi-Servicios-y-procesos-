# Coding: latin1
from FormularioJSONPost import *
from FormularioJSONGet import *
from FormularioJSONPatch import *
from FormularioJSONDelete import *
from pip._vendor import requests

def menuOpciones():
    continuar = True
    while (continuar): 
      

        opcionCorrecta = False

        while (opcionCorrecta == False):
    
            print("==================================================")
            print("                    OPCIONES                      ")
            print("==================================================")
            print("1. POST")
            print("2. GET")
            print("3. PATCH")
            print("4. DELETE")
            print("5. SALIDA")

            opcion = int(input("Seleccione una opci�n de las siguientes: "))

            if opcion < 1 or opcion > 5:
                print("Parece que seleccion� una respuesta inv�lida, vuelva a introducir una opci�n: ")
            elif opcion == 5:
                print("Muchas gracias, espero que vuelvas!")
                break
            else:
                opcionCorrecta = True
                opcionSeleccionada();


def opcionSeleccionada(opcion):

    if opcion==1: 
        JSONPost.post (userID, title, completedBoolean)
    elif opcion == 2: 
        JSONGet.get (userID, title, completedBoolean)
    elif opcion == 3:
        JSONPatch.patch (title, completedBoolean)
    elif opcion == 4:
        JSONDelete.delete()
    elif opcion == 0:
        continuar = True
    else: 
        print("Seleccionaste una opci�n no v�lida")
print ("Has salido del programa")

menuOpciones()

input("presiona cualquier tecla para continuar...")