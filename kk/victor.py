from turtle import *


setup (600,600)
def draw():
    CURSOR_SIZE = 20

    #screen = Screen()
    #screen.setup(600, 600)  # 12 x 24 ladrillos
    #screen.setworldcoordinates(0, 0, 12, 24)  # corneadas del bloque
        # screen.bgcolor('dodger blue')

    turtle = Turtle('square', visible=False)
    turtle.penup()
    turtle.speed('fastest')
    turtle.color('black', 'brown')
    turtle.shapesize(25 / CURSOR_SIZE, 50 / CURSOR_SIZE, 5)  # cursor se vuelve ladrillo


    for x in range(50):
        turtle.setposition(50*(x % 100),-500)
        turtle.stamp()
        turtle.forward(50)
    for x in range(50):
        turtle.setposition(-50*(x % 100),-500)
        turtle.stamp()
        turtle.forward(50)
    for x in range(50):
        turtle.setposition(-50*(x % 100), -475)
        turtle.stamp()
        turtle.forward(50)
    for x in range(50):
        turtle.setposition(50*(x % 100), -475)
        turtle.stamp()
        turtle.forward(50)
    for x in range(50):
        turtle.setposition(-50*(x % 100), -450)
        turtle.stamp()
        turtle.forward(50)
    for x in range(50):
        turtle.setposition(50*(x % 100), -450)
        turtle.stamp()
        turtle.forward(50)
