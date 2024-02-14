import turtle
import math

width=float(input("Enter the Width : "))
length=float(input("Enter the Length : "))

chuvi=(width+length)*2
dientich=width*length

print("Chu vi hinh chu nhat : ",chuvi)
print("Dien tich hinh chu nhat : ",dientich)

pen=turtle.Turtle()

pen.fillcolor("green")
pen.begin_fill()
for i in range(2):
    pen.forward(length)
    pen.right(90)
    pen.forward(width)
    pen.right(90)

pen.end_fill()

turtle.done()