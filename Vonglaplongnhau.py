import turtle

show=turtle.Screen()
show.bgcolor("black")

pen=turtle.Turtle()
pen.speed(20)
pen.color("#EE82EE""#FF0000")


for i in range (1,100):
    for j in range (1,6):
        pen.right(120)
        pen.fd(200)
    pen.left(5)


turtle.done()