import turtle

pen=turtle.Turtle()
pen.speed(1)



def Xoanoc(radius,angle):
    for i in range(20):
        pen.circle(radius,angle)
        radius+=5
   
Xoanoc(5,50)


turtle.done()
    