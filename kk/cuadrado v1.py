#--------------------------------------------
def get_upper_left_x(x: float,
                    y: float,
                    length: float) -> float:
    "Esta función devuelve un vertice del cuadrado"
        
    midlength: float = length / 2
        
    upper_left_x = x - midlength
    upper_left_y = y + midlength

    result = upper_left_x

    return result


x = 0
y = 0
length = 10

upper_left_x = get_upper_left_x(x, y, length)

print("la x del vertice izquierdo es;")
print(upper_left_x)
#----------------------------------------------------------------------------------

def get_upper_right_x(x: float,
                    y: float,
                    length: float) -> float:
    "Esta función devuelve un vertice del cuadrado"
    
    midlength: float = length / 2
    
    upper_right_x = x + midlength
    upper_right_y = y + midlength

    result = upper_right_x
    return result
x = 0
y = 0
length = 10

upper_left_x = get_upper_right_x(x, y, length)

print("la x del vertice izquierdo es;")
print(upper_left_x)

def get_down_left_x(x: float,
                    y: float,
                    length: float) -> float:
    "Esta función devuelve un vertice del cuadrado"
    
    midlength: float = length / 2
    
    down_left_x = x - midlength
    down_left_y = y - midlength

    result = down_left_x

    return result
x = 0
y = 0
length = 10

down_left_x = get_down_left_x(x, y, length)

print("la x del vertice derecho es;")
print(down_left_x)

def get_down_right_x(x: float,
                    y: float,
                    length: float) -> float:
    "Esta función devuelve un vertice del cuadrado"
    
    midlength: float = length / 2
    
    down_right_x = x + midlength
    down_right_x = y - midlength

    result = down_right_x

    return result

x = 0
y = 0
length = 10

down_right_x = get_down_right_x(x, y, length)

print("la x del vertice derecho es;")
print(down_right_x)


print("El vertice superior izquierdo es:")
print(get_upper_left_x(x, y, length))
print(get_upper_right_x(x, y ,length))

print("El vertice inferior derecho es:")
print(get_down_left_x(x, y, length))
print(get_down_right_x(x, y , length))