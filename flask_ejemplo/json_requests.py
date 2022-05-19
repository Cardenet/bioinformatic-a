import pprint
import requests 
from requests.models import Response
#cuando un servidor ofrece una serie de direcciones HTTP que devuelven json, 
#estas direcciones se llama una API(Application Programing Interface)
#Una API es un lenguaje de programacion es el conjunto de funciones ejemplo:
#do_something 1 (a:int) --> int
#do_something 2 (a:str) --> str
#do_something 3 (a:float) --> float


#my_server/do_something1 -->int  \
#my_server/do_something2 -->str   \______-> Web services
#my_server/do_something3 -->float /
# Make a GET Request
    
url: str='https://animechan.vercel.app/api/random'
response: Response =requests.get(url)
print(response)

pprint.pp(response.json())