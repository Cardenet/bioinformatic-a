from turtle import *

def draw():
    CURSOR_SIZE = 20

    turtle = Turtle('square', visible=False)
    turtle.penup()
    turtle.speed('fastest')
    turtle.color('black', 'brown')
    turtle.shapesize(15 / CURSOR_SIZE, 30 / CURSOR_SIZE, 4)

    for x in range(9):
        turtle.setposition(30*(x % 100),0)
        turtle.stamp()
        turtle.forward(30)
    for x in range(9):
            turtle.setposition(30*(x % 100),15)
            turtle.stamp()
            turtle.forward(30)
    for x in range(9):
            turtle.setposition(30*(x % 100),30)
            turtle.stamp()
            turtle.forward(30)
    for x in range(9):
            turtle.setposition(30*(x % 100),45)
            turtle.stamp()
            turtle.forward(30)
    for x in range(9):
            turtle.setposition(30*(x % 100),60)
            turtle.stamp()
            turtle.forward(30)

    for x in range(4):
            turtle.setposition(-30*(x % 100),0)
            turtle.stamp()
            turtle.forward(30)
    for x in range(4):
            turtle.setposition(-30*(x % 100),15)
            turtle.stamp()
            turtle.forward(30)
    for x in range(4):
            turtle.setposition(-30*(x % 100),30)
            turtle.stamp()
            turtle.forward(30)
    for x in range(4):
            turtle.setposition(-30*(x % 100),45)
            turtle.stamp()
            turtle.forward(30)
    for x in range(4):
            turtle.setposition(-30*(x % 100),60)
            turtle.stamp()
            turtle.forward(30)
