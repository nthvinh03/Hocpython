import turtle 
import random as r

pen=turtle.Turtle()
pen.pensize(3)
pen.speed(5)

list_color=["red","green","blue","black"]

for i in range (10):
    pen.left(5)
    for i in range (10):
        choose=r.choice(list_color)
        pen.color(choose)
        pen.right(144)
        pen.fd(100)



turtle.done()