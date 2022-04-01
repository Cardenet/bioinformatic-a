from turtle import *
import turtle

import pipe

def location1_cloud():
    penup()
    goto(200, 200)
    pendown
def location2_cloud():
    penup()
    goto(-400, 230)
    pendown()
    
def filled_circle(radius, color):
    turtle.color("white", "white")
    fillcolor("white")
    begin_fill()
    circle(radius)
    end_fill()


def cloud(radius, cloud_color="white"):
    filled_circle(radius,cloud_color)
    forward(radius)
    filled_circle(radius,cloud_color)
    right(90)
    filled_circle(radius,cloud_color)
    right(90)
    filled_circle(radius,cloud_color)
    right(90)
    filled_circle(radius,cloud_color)
    right(90)

def draw():
    pipe.draw()

    turtle.speed('fastest')
    Screen().bgcolor("dodgerblue")
    
    radius = 35
    location1_cloud()
    cloud(radius)
    location2_cloud()
    cloud(radius)
    penup()

