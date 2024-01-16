# app.py
from flask import Flask, render_template
import requests
from config import NASA_API_KEY  # Importez la clé API depuis le fichier de configuration

app = Flask(__name__)

def obtenir_image_aleatoire_nasa():
    url = "https://api.nasa.gov/planetary/apod"
    params = {
        "api_key": NASA_API_KEY,  # Utilisez la clé API importée ici
        "count": 1,
    }

    reponse = requests.get(url, params=params)
    if reponse.status_code == 200:
        return reponse.json()[0]
    else:
        return None

@app.route('/')
def index():
    image_nasa = obtenir_image_aleatoire_nasa()
    return render_template('index.html', image_nasa=image_nasa)

if __name__ == '__main__':
    app.run(debug=True)
