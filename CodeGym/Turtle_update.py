import turtle as t 
import random


screen=t.Screen()
screen.setup(width=600,height=500)

pen=t.Turtle(visible=False)
pen.penup()
pen.speed(0)
pen.goto(-250,200)
for i in range (21):
    pen.write(i)
    pen.fd(25)

#Vẽ đường đứt trên đường đua và đánh dấu các cột mốc bên phải đường đua
x=-250
pen.goto(-250,200)
pen.right(90)

for i in range (21):
    for j in range (10):
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.fd(10)
    pen.penup()
    pen.fd(25)
    pen.write(i)
    pen.goto(x+(i+1)*25,200)

all_turtle=[]

y_position=[160,100,40,-20]
color_=["red","blue","green","black"]

for turtle in range(0,4):
    turtles=t.Turtle(shape="turtle")
    turtles.penup()

    turtles.goto(-250,y=y_position[turtle])

    turtles.color(color_[turtle])

    for i in range(5):
        turtles.left(72)
    
    all_turtle.append(turtles)

def random_walk(turtles):
    global run
    for turtle in turtles:
        turtle.fd(random.randint(1,10))
        if turtle.xcor()>250:
            run=False

run=True
while run:
    random_walk(all_turtle)
screen.exitonclick()

