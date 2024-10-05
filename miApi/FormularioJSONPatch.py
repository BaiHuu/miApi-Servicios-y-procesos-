
# PATCH, para actualizar datos.

from urllib import response
from pip._vendor import requests


class JSONPatch:
    @staticmethod
    def patch (title, completedBoolean):

        api_url = "https://jsonplaceholder.typicode.com/todos/10"

        # CREACION OBJETO

        todo = {"title":"Mow lawn","completed":completedBoolean}

        # PETICION PATCH

        response = requests.patch(api_url, json=todo)
        print(response.json())
        print(response.status_code)

