import turtle

pen=turtle.Turtle()
pen.pensize(2)
pen.color("#FFFFFF")
pen.speed(5)
pen.hideturtle()


#ve hinh chu nhat
def Hinh_chu_nhat(dai : float,rong : float ,mau : str):
    pen.fillcolor(mau)
    pen.begin_fill()
    
    for i in range (2):
        pen.fd(rong)
        pen.right(90)
        pen.fd(dai)
        pen.right(90)
    pen.end_fill()



Hinh_chu_nhat(100,60,"#CC6699")
pen.penup()
pen.goto(0,100)
pen.pendown()
Hinh_chu_nhat(100,60,"#CC6666")
pen.penup()
pen.goto(60,0)
pen.pendown()
Hinh_chu_nhat(100,60,"#CC6699")
pen.penup()
pen.goto(60,100)
pen.pendown()
Hinh_chu_nhat(100,60,"#CC6666")
pen.penup()
pen.goto(120,0)
pen.pendown()
Hinh_chu_nhat(100,120,"#FF9999")
pen.penup()
pen.goto(5,-50)
pen.pendown()
Hinh_chu_nhat(30,20,"#FF9999")
pen.penup()
pen.goto(5,50)
pen.pendown()
Hinh_chu_nhat(30,20,"#FF9999")
pen.penup()
pen.goto(65,-50)
pen.pendown()
Hinh_chu_nhat(30,20,"#FF9999")
pen.penup()
pen.goto(65,50)
pen.pendown()
Hinh_chu_nhat(30,20,"#FF9999")
pen.penup()
pen.goto(150,-40)
pen.pendown()
Hinh_chu_nhat(60,60,"#FF9999")


turtle.done()
