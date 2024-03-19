import turtle 
import random as r

#khởi tạo đối tượng turtle và đặt đối tượng về điểm 0,-200 để vẽ đường tròn nhốt rùa 
show=turtle.Screen()
show.bgcolor("#99CCFF")
pen=turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(0,-200)

pen.pensize(5)
pen.color("black")
pen.speed(20)
pen.pendown()
pen.circle(200)

#đặt con rùa về chính giữa đồi màu con rùa thành màu xanh hiển thị
pen.penup()
pen.shape("turtle")
pen.color("green")
pen.goto(0,0)

#tạo hướng đi ngẫu nhiên cho con rùa khi ở giữa đường bao 

huong=r.randint(0,360)
pen.right(huong)
pen.showturtle()

#bắt đầu cho rùa di chuyển khỏi đường bao, khi rùa di chuyển ra ngoài đường bao bắt rùa về vị trí ban đầu
count=0

while True:
    pen.speed(1)
    #cho rùa di chuyển một khoảng nhỏ hơn đường bao tránh để rùa đè lên vạch

    pen.forward(190)

    pen.hideturtle()
    pen.speed(10)
    pen.goto (0,0)
    hương=r.randint(0,360)
    pen.right(huong)
    pen.showturtle()
    count+=1
    if count >10:
        break

turtle.done()