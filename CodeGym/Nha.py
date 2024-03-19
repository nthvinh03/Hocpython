import turtle

pen=turtle.Turtle()
pen.pensize(3)
pen.speed(3)
pen.color("blue")
pen.hideturtle()

#nhà

for i in range(2):
    pen.forward(300)
    pen.right(90)
    pen.forward (140)
    pen.right(90)

#mái
pen.goto(80,80)
pen.goto(160,0)

#ống khói
pen.penup()
pen.goto(120,40)
pen.pendown()
pen.left(90)
pen.forward(40)
pen.left(90)
pen.forward(20)
pen.left(90)
pen.forward(20)

pen.penup()
pen.goto(120,110)
pen.pendown()
pen.forward(20)

pen.penup()
pen.goto(100,120)
pen.pendown()
pen.forward(30)

pen.penup()
pen.goto(-170,-250)
pen.down()
pen.fillcolor("#330000")
pen.begin_fill()
pen.goto(-120,-250)
pen.goto(-130,-150)
pen.goto(-160,-150)
pen.goto(-170,-250)
pen.end_fill()
#tang cay 1 
pen.fillcolor("#339900")
pen.begin_fill()
pen.goto(-160,-150)
pen.goto(-225,-150)
pen.goto(-145,-100)
pen.goto(-75,-150)
pen.goto(-160,-150)
pen.end_fill()
#tang cay 2
pen.penup()
pen.goto(-160,-100)
pen.down()
pen.fillcolor("#339900")
pen.begin_fill()
pen.goto(-215,-100)
pen.goto(-145,-50)
pen.goto(-85,-100)
pen.goto(-160,-100)
pen.end_fill()
#tang cay 3
pen.penup()
pen.goto(-160,-50)
pen.down()
pen.fillcolor("#339900")
pen.begin_fill()
pen.goto(-205,-50)
pen.goto(-145,0)
pen.goto(-85,-50)
pen.goto(-160,-50)
pen.end_fill()


turtle.done()





