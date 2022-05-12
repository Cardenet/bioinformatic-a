#HTTP: Hyper Text Transfer Protocol
#-Principales metodos de Request son: 
#   ·GET 
#   ·POST(tambien se usa para conseguir datos)
#   ·PUT(subir datos al servidor)
#   ·DELETE(borrar datos del servidor)
#   ·UPDATE(actulizar un fichero del servidor)
#HTTP: Hyper Text (cualquier cosa)
#Dos tipos de informacion:
#1- Para ser consumido por persona: html
#2- Para ser consumido por maquina: json(xml)
#En javascript los objetos son diccionarios
import json
data =['foo', {'bar': ('baz', None, 1.0, 2)}]
py_str:str=str(data)
json_str: str = json.dumps(data)
new_data= json.loads(json_str)
print(json_str)
print(py_str)
print(new_data)