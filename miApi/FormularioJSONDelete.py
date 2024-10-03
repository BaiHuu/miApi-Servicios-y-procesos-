
# Ejemplo de PUT, donde metemos los datos

from urllib import response
import requests
api_url = "https://jsonplaceholder.typicode.com/todos/10"

 # PETICION DELETE

response = requests.delete(api_url)
print(response.json())
print (response.status_code)
