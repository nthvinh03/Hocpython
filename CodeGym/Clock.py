import turtle
import datetime
import math

#xây dựng lớp clock
class Clock:

    def __init__(self):

        #cài đặt cửa sổ 
        self.window = turtle.Screen()
        self.window.title("Đồng hồ")
        self.window.bgcolor("white")
        self.window.setup(width=600, height=600)
        self.window.tracer(0)

        #vẽ đường tròn tô màu
        self.clock_face = turtle.Turtle()
        self.clock_face.speed(0)
        self.clock_face.hideturtle()
        self.clock_face.color("black")
        self.clock_face.penup()
        self.clock_face.goto(0, -200)
        self.clock_face.pendown()
        self.clock_face.fillcolor("#66CCCC")
        self.clock_face.begin_fill()
        self.clock_face.circle(200)
        self.clock_face.end_fill()

        #vẽ kim giờ
        self.hour_hand = turtle.Turtle()
        self.hour_hand.speed(0)
        self.hour_hand.shape("arrow")
        self.hour_hand.color("black")
        self.hour_hand.shapesize(stretch_wid=0.4, stretch_len=9)
        self.hour_hand.penup()
        self.hour_hand.goto(0, 0)

        #vẽ kim phút
        self.minute_hand = turtle.Turtle()
        self.minute_hand.speed(0)
        self.minute_hand.shape("arrow")
        self.minute_hand.color("black")
        self.minute_hand.shapesize(stretch_wid=0.4, stretch_len=12)
        self.minute_hand.penup()
        self.minute_hand.goto(0, 0)

        #vẽ kim giây
        self.second_hand = turtle.Turtle()
        self.second_hand.speed(0)
        self.second_hand.shape("arrow")
        self.second_hand.color("red")
        self.second_hand.shapesize(stretch_wid=0.2, stretch_len=13)
        self.second_hand.penup()
        self.second_hand.goto(0, 0)

    #vẽ chi tiết mặt đồng hồ
    def draw_clock_face(self):
        font = ("Arial", 12, "normal")
        hour_font = ("Arial", 8, "normal")

        for i in range(1, 13):
            angle = math.pi / 2 - 2 * math.pi * (i / 12)
            x = 160 * math.cos(angle)
            y = 160 * math.sin(angle)
            self.clock_face.penup()
            self.clock_face.goto(x, y)
            self.clock_face.pendown()
            self.clock_face.write(str(i), align="center", font=font)
            self.clock_face.penup()
            self.clock_face.goto(0, 0)

        for i in range(12):
            angle = math.pi / 2 - 2 * math.pi * (i / 12)
            x1 = 180 * math.cos(angle)
            y1 = 180 * math.sin(angle)
            x2 = 200 * math.cos(angle)
            y2 = 200 * math.sin(angle)
            self.clock_face.penup()
            self.clock_face.goto(x1, y1)
            self.clock_face.pendown()
            self.clock_face.goto(x2, y2)

    #cập nhật kim giờ phút giây theo giờ hiện tại 
    def update_clock(self):
        while True:
            current_time = datetime.datetime.now().time()
            hour = current_time.hour % 12
            minute = current_time.minute
            second = current_time.second

            hour_angle = -2 * math.pi * (hour / 12) + math.pi / 2
            minute_angle = -2 * math.pi * (minute / 60) + math.pi / 2
            second_angle = -2 * math.pi * (second / 60) + math.pi / 2

            self.hour_hand.setheading(math.degrees(hour_angle))
            self.minute_hand.setheading(math.degrees(minute_angle))
            self.second_hand.setheading(math.degrees(second_angle))

            self.window.update()

clock = Clock()
clock.draw_clock_face()
clock.update_clock()
turtle.done()