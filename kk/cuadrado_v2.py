#--------------------------------------------

class square:

    def __init__(self, x: float, y: float, length: float):
        #constructor
        self.x = x
        self.y = y
        self.length = length
    def get_upper_left(self) -> float:
        #constructor
        "Esta función devuelve un vertice del cuadrado"
        midlength: float = self.length / 2
    
        upper_left_x = self.x - midlength
        upper_left_y = self.y + midlength

        return  upper_left_x, upper_left_y
        
    def get_upper_right(self) -> float:
        #constructor
        "Esta función devuelve un vertice del cuadrado"
        midlength: float = self.length / 2
    
        upper_right_x = self.x + midlength
        upper_right_y = self.y + midlength

        return upper_right_x, upper_right_y
        

s: square = square(0 , 0, 10)
print("atributos del cuasdrado s:")
print(s.x)
print(s.y)
print(s.length)

print("Vertice superior izquierdo del cuadrado s:")
print(s.get_upper_left()) 
print("Vértice superior derecho del cuadrado s:")
print(s.get_upper_right())
