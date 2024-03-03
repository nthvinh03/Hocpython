import turtle 

pen=turtle.Turtle()
pen.pensize(3)
pen.hideturtle()
pen.color("red")

def hinhvuong(a:int):
    for i in range (4):
        pen.forward(a)
        pen.right(90)

hinhvuong(100)

turtle.done()