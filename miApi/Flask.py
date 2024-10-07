#coding: latin1

from operator import index
from flask import *

# Creamos una instancia de una aplicaci�n Flask que se utilizar� par a manejar solicitudes web y definir rutas, vistas y comportamientos espec�ficos de la aplicaci�n.
# __name__ es una variable especial de Python que se refiere al nombre del m�dulo en el que se encuentra el c�digo.
app = Flask(__name__)

countries = [  # Aqui creamos un
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
]

ciudades = [
    {"id_ciudad":1, "nombreCiudad": "Madrid", "pais": "Espa�a", "area": 60},
    {"id_ciudad":1, "nombreCiudad": "Par�s", "pais": "Francia", "area": 40},
    {"id_ciudad":1, "nombreCiudad": "Oslo", "pais": "Noruega", "area": 200},
]

@app.get("/countries")
@app.get("/countries/")
def get_countries():
    return jsonify(countries)


@app.get("/countries/<int:id>")
@app.get("/country/<int:id>")
def get_country(id):
    for country in countries:
        if country['id'] == id:
            return country, 200
    return {"error": "Country not found"}, 404


@app.route("/")  # Definimos la ruta raiz
def index():  # decimos que se muestra cuando accedemos al index
    return 'Hola a todos! :)'



def _find_next_id():
    return max(country["id"] for country in countries) + 1
@app.post("/countries") # Indicamos de que es una petici�n de tipo POST
# Definimos la funci�n correspondiente
def add_country():
    #Se comprueba que lo que nos ha llegado cumple con el formato JSON:
    if request.is_json:
        country = request.get_json()
        ## Le indicamos al diccionario country que su nuevo id es el que nos devuelve la funci�n _find_next_id()
        country['id'] = _find_next_id()
        # A�adimos el nuevo pais a nuestra lista
        countries.append(country)
        # Devolvemos el pa�s en formato diccionario y el c�digo 201 para indicar que e ha a�adido
        return country, 201
    # Si la petici�n no cumple con el formato JSON devuelve un mensaje de error y el c�digo 415
    return {"error": "Not enough arguments"}, 400


def _find_next_id():
    return max(ciudad["id"] for ciudad in ciudades) + 1

@app.get("/ciudades/<int:id>")
@app.get("/ciudad/<int:id>")
def get_ciudad(id):
    for ciudad in ciudades:
        if ciudad['id'] == id:
            return ciudad, 200
    return {"error": "Not enough arguments"}, 400

@app.post("/ciudades")
def add_ciudades():
    #Se comprueba que lo que nos ha llegado cumple con el formato JSON:
    if request.is_json:
        ciudad = request.get_json()
        ## Le indicamos al diccionario country que su nuevo id es el que nos devuelve la funci�n _find_next_id()
        ciudad['id'] = _find_next_id()
        # A�adimos el nuevo pais a nuestra lista
        ciudades.append(ciudad)
        # Devolvemos el pa�s en formato diccionario y el c�digo 201 para indicar que e ha a�adido
        return ciudad, 201
    # Si la petici�n no cumple con el formato JSON devuelve un mensaje de error y el c�digo 415
    return {"error": "Not enough arguments"}, 400

if __name__ == '__main__':
    # Por defecto usar� la IP 0.0.0.0 y el puerto 5050, lo que implica que nuestra pagina wev puede ser accesible desde otro ordenador
    # Al ponerlo en modo debug si se produce un error nos mostrar� informaci�n relevante.
    app.run(debug=True, host='0.0.0.0', port=5050)
