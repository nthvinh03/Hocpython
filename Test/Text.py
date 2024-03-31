import turtle
import random

# Tạo màn hình đua rùa
window = turtle.Screen()
window.title("Đua rùa vui nhộn")
window.bgcolor("white")

# Vẽ đường đua
pen = turtle.Turtle()
pen.speed(0)
pen.color("gray")
pen.penup()
pen.setpos(-250, 200)
pen.pendown()
pen.pensize(3)
pen.right(90)
pen.forward(400)

# Tạo các rùa
colors = ["red", "blue", "green", "orange"]
turtles = []
for i in range(4):
    turtle = turtle.Turtle()
    turtle.shape("turtle")
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(-250, 160 - i * 80)  # Vị trí xuất phát của rùa
    turtles.append(turtle)

# Người chơi đặt cược
player_bet = window.textinput("Đua rùa vui nhộn", "Hãy đặt cược vào rùa bạn nghĩ sẽ chiến thắng (1-4):")
player_bet = int(player_bet)

# Bắt đầu đua rùa
while True:
    for turtle in turtles:
        distance = random.randint(0, 10)
        turtle.forward(distance)

        # Kiểm tra rùa đạt đích chưa
        if turtle.xcor() > 230:
            winner = turtles.index(turtle) + 1
            if winner == player_bet:
                window.textinput("Kết quả", "Bạn đã chiến thắng! Rùa số {} là người thắng cuộc.".format(winner))
            else:
                window.textinput("Kết quả", "Bạn đã thua cuộc. Rùa số {} là người thắng cuộc.".format(winner))
            window.bye()
            exit()

# Đóng chương trình khi người dùng đóng cửa sổ
turtle.done()