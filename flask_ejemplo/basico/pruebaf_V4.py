
from pickle import TRUE
from flask import Flask,render_template, Response, request
'''Ahora se una el jinja2'''
#1-Inilialiciación :app: Flask = Flask(__name__)
'''Return html'''
app = Flask(__name__)
@app.route('/')
def index():
    return "Hello world"
#3-rutas (En caso de no especificar un str devuelve un html)
@app.route('/hello/<name>/<num>')
def hello(name:str, num:int):
    salutacion: str=f'Hello Costumer you bougth {name} volumen {num}'
    
    return salutacion
@app.route('/buy2')
#ruta/buy2?name=boladedrac&num=19
def buy2():
    comic: str = request.args.get("name")
    volumen: str = request.args.get("num")
    salutacion: str=f'Hello Costumer you bougth {comic} volumen {volumen}'
    return salutacion
#2-Run: if __name__ == "__main__"
if __name__ == "__main__":

    app.run(debug= True)