import turtle

window=turtle.Screen()

window.bgcolor("#FFCCFF")

pen=turtle.Turtle()
pen.pensize(3)
pen.color("#990000")

pen.penup()
pen.goto(0,-50)
pen.pendown()
pen.fillcolor("red")
pen.begin_fill()

pen.left(140)
pen.fd(185)
pen.circle(-90,210)

pen.left(140)
pen.circle(-90,210)
pen.fd(185)
pen.end_fill()
turtle.done()