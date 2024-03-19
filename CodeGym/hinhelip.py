import turtle
import random as r

pen=turtle.Turtle()

pen.pensize(3)
pen.penup()
pen.goto(-100,0)
pen.pendown()

color=["green","red","yellow","blue","black"]

count=0

while True:
    pen.speed(20)
    
    choose=r.choice(color)
    pen.color(choose)
    pen.right(45)
    pen.circle(120,90)
    pen.circle(60,90)
    pen.circle(120,90)
    pen.circle(60,90)
    pen.right(10)
    count+=1
    if count==100:
        break


turtle.done()


