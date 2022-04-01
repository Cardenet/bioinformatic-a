from calendar import c
from importlib.resources import path
import pathlib


from pathlib import Path
from turtle import home
from unittest import result
#Simula bucles usando solo funciones
#La recursividad te permite calcular más cosas que un bucle (más potente, mas general)
#Es mas potente porque los bucles hacem una via
#Cuando los datos son recursivos se utiliza esto ejemplo (sistema de ficheros del ordenador)
#--------------------------------------------------------
def say_hello_v1():
    
     while True:  
         print("Hello!")
#--------------------------------------------------------
def say_hello_v2():
    
    print("Hello!")
    say_hello_v2()
#--------------------------------------------------------
def say_hello_v3():
    
    for _ in range (5):
        print("Hello!")
#--------------------------------------------------------
def say_hello_v4(num:int):
    if (num > 0) :
        print("Hello!")
        say_hello_v4(num -1)
    if (num == 0):
        print("finished!")
#--------------------------------------------------------
def say_hello_v5(num:int):
    
    #Recursive branch
    if (num > 0) :
        print("Hello!")
        say_hello_v5(num -1)    
    #Termination branch
    if (num == 0):
        pass

#--------------------------------------------------------

#say_hello_v5(4)
#--------------------------------------------------------
def get_filepath_list(arch: Path) :

    #Recursive branch
    
    if (arch.is_dir()):
            
        path_rec:   list[Path] =sorted(arch.glob('*'))
        for path in path_rec:
            get_filepath_list(path)
    
    
    #Termination branch
    if (arch.is_file()):
        print(str(arch))
#--------------------------------------------------------
def get_filepath_listV2(arch: Path)-> list[str] :

    result: list[str]=[]
    #Recursive branch
    
    if (arch.is_dir()):
            
        path_rec:   list[Path] =sorted(arch.glob('*'))
        for path in path_rec:
           result.extend(get_filepath_listV2(path))
    
    
    #Termination branch
    if (arch.is_file()):
        result.append(str(arch))
    return result    

#--------------------------------------------------------

#--------------------------------------------------------