
# PATCH, para actualizar datos.

from urllib import response
import requests

api_url = "https://jsonplaceholder.typicode.com/todos/10"

todo = {"title":"Mow lawn"}

# PETICION PATCH

response = requests.patch(api_url, json=todo)
print(response.json())
print(response.status_code)

