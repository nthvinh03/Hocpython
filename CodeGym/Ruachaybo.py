import turtle as t
import random



#Cài đặt màn hình
screen=t.Screen()
screen.setup(width=600,height=500)
screen.bgcolor("#FFFF99")

#Hiển thị cửa sổ dự đoán con rùa nào thắng
#Con rùa nào thắng cuộc 
screen_1=screen.textinput(prompt="Mời dự đoán con rùa nào chiến thắng : ",
                          title="Nhập vào màu sắc con rùa (đỏ, xanh, vàng, nâu, cam, hồng ",)

#Lưu lại list màu của các con rùa
color_=["red","blue","yellow","brown","orange","pink"]

#Vị trí ban đầu theo trục y của các con rùa 
#Theo trục x=-250,cách vị trí 0,0 250 về bên trái 

y_position=[0,-30,30,-60,60,90]

#Lưu lại vận tốc của các con rùa 
#Các giá trị này được chọn một cách ngẫu nhiên 
#cho các con rùa khi chạy

speed_=[10,5,15,20,25,30]

#Tạo một list để lưu các con rùa 

lst_rua=[]
run=True

#Xây dựng hàm đê thiết lâp vị trí ban đầu , màu  cho các con rùa và lưu vào list

for turtle in range (0,6):
    turtles=t.Turtle(shape="turtle")
    turtles.shapesize(2)
    turtles.penup()
    #Di chuyển rùa về bên trái cùng của đường đua
    turtles.goto(-250,y=y_position[turtle])
    #Màu của rùa
    turtles.color(color_[turtle])
    #Lưu vào list
    lst_rua.append(turtles)


#Xây dựng hàm di chuyển cho các con rùa 
#Mỗi con rùa khoảng cách di chuyển, tốc độ được chọn ngẫu nhiên trong các giá trị được lưu phía trên 

def random_walk(turtles):
    global run
    for turtle in turtles:
        turtle.forward(random.choice(speed_))
        #Kiểm tra điều kiện cán đích 
        #Khi 1 con rùa cán đích thì dừng lại
        if turtle.xcor() >250:
            run =False

while run:
    random_walk(lst_rua)

screen.exitonclick()

