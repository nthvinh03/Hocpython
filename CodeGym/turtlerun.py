import turtle
import random
import time

# Khởi tạo màn hình và rùa
screen = turtle.Screen()
screen.title("Turtle Race Game")
screen.bgcolor("white")

# Vẽ đường đua
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.goto(-200, 200)
for _ in range(11):
    pen.write("|", align="center", font=("Courier", 12, "normal"))
    pen.right(90)
    pen.forward(20)
    pen.pendown()
    pen.forward(400)
    pen.penup()
    pen.backward(420)
    pen.left(90)
    pen.forward(40)

# Tạo các rùa
colors = ["red", "blue", "green", "orange", "purple"]
turtles = []
for i in range(5):
    turtle_obj = turtle.Turtle()
    turtle_obj.shape("turtle")
    turtle_obj.color(colors[i])
    turtle_obj.penup()
    turtle_obj.goto(-220, 170 - i * 40)
    turtles.append(turtle_obj)

# Hàm tính thời gian đến đích và hiển thị thông báo
def finish_line(turtle_obj):
    start_time = time.time()
    turtle_obj.forward(400)
    end_time = time.time()
    elapsed_time = round(end_time - start_time, 2)
    turtle_obj.goto(-220, turtle_obj.ycor())
    turtle_obj.write(f"Winner! Time: {elapsed_time}s", align="right", font=("Courier", 12, "bold"))

# Di chuyển các rùa ngẫu nhiên
while True:
    for turtle_obj in turtles:
        distance = random.randint(1, 10)
        turtle_obj.forward(distance)
        if turtle_obj.xcor() >= 200:
            finish_line(turtle_obj)
            break

# Đóng cửa sổ khi nhấn Esc
screen.listen()
screen.onkeypress(screen.bye, "Escape")
turtle.done()