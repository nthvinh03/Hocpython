import turtle

pen=turtle.Turtle()

pen.pensize(3)
pen.speed(5)

pen.hideturtle()

pen.circle(90)
pen.penup()
pen.goto(50,100)
pen.pendown()
pen.circle(20)
pen.penup()
pen.goto(-50,100)
pen.pendown()
pen.circle(20)
pen.penup()
pen.goto(-10,80)
pen.pendown()

for i in range (3):
    pen.forward(20)
    pen.right(120)


pen.penup()
pen.goto(-40,30)
pen.pendown()
pen.right(60)
pen.circle(50,120)
turtle.mainloop()


turtle.done()

