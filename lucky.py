from turtle import *

setup(600,600)

#cajita
def draw():
    fillcolor('gold')
    begin_fill()
    penup()
    goto(-105,-10)
    pendown()
    left(90)
    forward(80)
    left(90)
    forward(80)
    left(90)
    forward(80)
    left(90)
    forward(80)
    end_fill()
    #interrogante
    penup()
    goto(-140,-5)
    color('white')
    style = ('Courier', 70, 'italic')
    write('?', move=False, font=style, align='center')
    hideturtle()

