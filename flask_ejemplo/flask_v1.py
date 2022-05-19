'''
Pesticiones pero con post
Problemas peticiones get:
1-Los parametros estan en la url. La url tienen tamaño limitados
2-Todos los parametros son publicos. No se pueden encriptar
Solucion:
-Usar peticiones POST
-Se usan normalmente en formularios 
'''
#Estrategias :
#1-Espero una peticion get en una ruta y devuelvo el formulario
#2-En el formulario se especifica que los datos se mandaran usando el metodo post
#3-Mi funcion distingue entre metodos get y post y si recibo una request post recoje los parametros del formulario

from flask import Flask,render_template, Response, request
'''Ahora se una el jinja2'''
#1-Inilialiciación :app: Flask = Flask(__name__)
'''Return html'''
app = Flask(__name__)
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        comic: str = request.form['comic']
        volumen: str = request.form['volume']
        return f'You have bought {comic}, volume{volumen}'
    return ''
#3-rutas (En caso de no especificar un str devuelve un html)
#2-Run: if __name__ == "__main__"
if __name__ == "__main__":

    app.run(debug= True)