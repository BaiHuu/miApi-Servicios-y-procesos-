#coding: latin1

import json
import requests

userID = input("Introduce tu identificador: ")
title = input("Crea un titulo para esto: ")
completed = False
completedBoolean = bool(input("Completado True/False: "))
if completed == ("True"):
    completedBoolean = True
    

api_url ="https://jsonplaceholder.typicode.com/todos/"

# Creamos diccionario con todos los datos del nuevo todo
todo = {"userID": userID, "title": title, "Completed": completedBoolean}
response = requests.post(api_url,json=todo)

# Imprimimos el json de respuesta
print(response.json())

# Imprimir el estado de la respuesta para ver como ha ido
print("Código de estado:" , response.status_code)

