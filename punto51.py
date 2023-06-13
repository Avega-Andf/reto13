import json
import requests

url = 'https://randomuser.me/api/'

def obtenerusuario():
    peticion = requests.get(url)
    print(peticion.url)
    print(peticion.status_code)

    data = json.loads(peticion.text)
    usuario = data['results'][0]
    return usuario

if __name__ == "__main__":
    usu = obtenerusuario()
    print("Usuario random:")
    print(usu)