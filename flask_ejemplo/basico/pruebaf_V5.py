'''
Paginas web dinamicas vs estaticas 
-Dinamicas
 ·No existe el fichero .html en disco
 ·Cuando se recibe un request, se llama a una funcion que genera el codigo html y se devuelve directamente cada vez
 ·Este codigo html generado puede cambiar en cada peticion
-Estatico
 ·Existe el archivo .html a disco


Lo que queremos ahora es poder pasar a parametros esta funcio
Varios a aprender a pasar parametros mediante peticiones Get y Post
'''
#----------------------------------------------------------------------------
#Peticiones get: Parametros
#http://www.myapp.com/welcome/luis
#protocolo,domibio    ,ruta dentro de la web app




from pickle import TRUE
from flask import Flask,render_template, Response
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
#2-Run: if __name__ == "__main__"
if __name__ == "__main__":

    app.run(debug= True)