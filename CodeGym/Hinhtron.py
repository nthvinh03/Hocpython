import turtle
import math
pen=turtle.Turtle()

r=float(input("Enter the radius : "))
chuvi=2*math.pi*r

dientich=2*math.pi*r*r

print("Chu vi cua hinh tron ban kinh {0} la {1}".format(r,chuvi))
print("Dien tich cua hinh tron ban kinh {0} la {1}".format(r,dientich))


pen.fillcolor("red")
pen.begin_fill()
pen.circle(r)
pen.end_fill()

turtle.done()