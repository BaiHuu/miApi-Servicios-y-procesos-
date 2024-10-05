
from urllib import response
from pip._vendor import requests


# PETICION GET 


class JSONGet:
    @staticmethod

    def get(userid,title,completedBolean):
     api_url = "https://jsonplaceholder.typicode.com/todos/10"
     
     # PETICION GET 
     response = requests.get(api_url)
     print(response.json())

     # CREACION OBJETO

     todo={"userid":userid,"title":title,"completed":completedBolean}

     # PETICION POST

     # response = requests.post(api_url,json=todo)
     # print (response.json())