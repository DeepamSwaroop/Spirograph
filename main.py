from turtle import  Turtle,Screen
import turtle
import random

t=Turtle()
turtle.colormode(255)

def random_color():
    r=random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color=(r,g,b)    # for rgb colormode
    return color
t.speed(10)
def draw_spirograph(sizeofgap): #limit the overlapping of one circle with other
    for i in range(int(360/sizeofgap)): # as one circle=360 degree we divide 360/5 we will get the limiting condition
        t.color(random_color())
        t.circle(100)
        current_heading= t.heading()
        new_heading=t.setheading(current_heading+sizeofgap)    # change the tilt of the circle
draw_spirograph(5)

screen=Screen()
screen.exitonclick()