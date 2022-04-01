#OOP: object-oriented-programming
#Object = data + functions
#python oop (java, c++, c#)
#---------------------------------------------------
#PYTHON
#   Class = Type (int, float bool, str...)
#   Object = Variables
#   Method = Function in a object
#---------------------------------------------------
#class Dog :
#   Constructor Method: Initializes the data inside the object
'''
Object-Oriented-Programming (OOP) in python
'''
#Classes start with a capital letter and follow CamelCase notation
class BadExample:
    pass
#Classes usually have a constructor method (__init__)
#Constructor
    #On definition, we write __init__()
    #On calling, we write Dog()
#Methods
    #All methods have a special parameter: self
    #When calling the methods, we don't write it 
#Methods
    #Attribute are values stored inside the object 
    #They are created by the Constructor
    #Methods in the objects can acces attributes directly
    #To acces them write: self.<attribute>
class Dog:
    
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello! My name is {self.name}")
#---------------------------------------------------
Firulais:Dog= Dog("Firulais",5)
Firulais.greet()
Dama:Dog= Dog("Dama",4)
Dama.greet()
#---------------------------------------------------
