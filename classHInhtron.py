import turtle
import math


#xay dung ten lop 

class Cicle:
    def __init__(self,x,y,r):
        self.r=r
        self.x=x
        self.y=y

    def draw(self):
        pen=turtle.Turtle()
        pen.penup()
        pen.goto(self.x,self.y)
        pen.pendown()
        pen.circle(self.r)
        turtle.done
    def area(self):
        return self.r**2 *math.pi
    
    def perimeter(self):
        return 2*math.pi*self.r
    

c=Cicle(100,100,50)
c.draw()
print(c.area())
print(c.perimeter())