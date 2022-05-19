from pickle import TRUE
from flask import Flask, jsonify
from requests import Response

#1-Inilialiciación :app: Flask = Flask(__name__)
'''Return json'''
app = Flask(__name__)

#3-rutas
@app.route('/')
def index():
    data: dict= {'Pep':'Web App with Python Flask!'}
    response:Response= jsonify(data)
    return response
#2-Run: if __name__ == "__main__"
if __name__ == "__main__":

    app.run(debug= True)