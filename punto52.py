import requests
import json

def obtener_chiste_aleatorio():
    url = 'https://official-joke-api.appspot.com/random_joke'
    peticion = requests.get(url)
    print(peticion.url)
    print(peticion.status_code)

    data = json.loads(peticion.text)
    chiste = {
        'setup': data['setup'],
        'punchline': data['punchline']
    }
    return chiste

if __name__ == "__main__":
    chiste = obtener_chiste_aleatorio()
    print("Chiste aleatorio:")
    print("Pregunta:", chiste['setup'])
    print("Respuesta:", chiste['punchline'])
