import turtle
import random as r



rua=turtle.Turtle()
rua.shape("turtle")

rua.hideturtle()
rua.pensize(4)
rua.color("green")
rua.speed(2)
rua.penup()
rua.goto(-200,0)
rua.pendown()
rua.showturtle()

count=0

while count<10:
    down=r.randint(20,100)
    up=r.randint(0,360)
    rua.penup()
    rua.forward(down)
    rua.left(up)
    count+=1

turtle.done()