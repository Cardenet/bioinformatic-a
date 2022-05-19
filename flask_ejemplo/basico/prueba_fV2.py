from pickle import TRUE
from flask import Flask
from requests import Response

#1-Inilialiciación :app: Flask = Flask(__name__)
'''Return html'''
app = Flask(__name__)

#3-rutas (En caso de no especificar un str devuelve un html)
@app.route('/')
def index():
    data: str= 'A si es doña soy <h1>CHUSER</h1>, asi es doña'
    
    return data 
#2-Run: if __name__ == "__main__"
if __name__ == "__main__":

    app.run(debug= True)