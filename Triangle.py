
import turtle

d=float(input("Nhap vao chieu dai : "))
r=float(input("Nhap vao chieu rong : "))

S=d*r
print ("Dien tich hinh chu nhat = ",S)

pen=turtle.Turtle()
pen.hideturtle()
pen.fillcolor("green")
pen.begin_fill()
for i in range (4):
    pen.fd(d)
    pen.right(135)
    pen.fd(r)
    pen.right(45)

pen.end_fill()
turtle.done()