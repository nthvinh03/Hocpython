import turtle
import random


choose= random.uniform(1,3)

intmychoose=int(choose)

show=turtle.Screen()
show.bgcolor("black")
show.title("Circle")

pen=turtle.Turtle()
pen.shape("circle")

if intmychoose <1 :
    pen.color("green")
elif intmychoose <2:
    pen.color("yellow")
else:
    pen.color("red")

turtle.done()