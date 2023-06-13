import requests
import json

url = 'https://dog.ceo/api/breeds/image/random'

def obtenerperro():
    peticion = requests.get(url)
    print(peticion.url)
    print(peticion.status_code)

    data = json.loads(peticion.text)
    imagen = data['message']
    return imagen

if __name__ == "__main__":
    imagenperro = obtenerperro()
    print("Imagen aleatoria de perro:")
    print(imagenperro)