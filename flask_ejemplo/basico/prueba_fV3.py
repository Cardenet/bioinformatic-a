
from pickle import TRUE
from flask import Flask,render_template, Response
'''Ahora se una el jinja2'''
#1-Inilialiciación :app: Flask = Flask(__name__)
'''Return html'''
app = Flask(__name__)

#3-rutas (En caso de no especificar un str devuelve un html)
@app.route('/')
def index():
    html: str= render_template('index.html',title='Flask V3', name='Cardenet')
    
    return html 
#2-Run: if __name__ == "__main__"
if __name__ == "__main__":

    app.run(debug= True)