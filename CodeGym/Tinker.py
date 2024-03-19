from tkinter import *
from tkinter import ttk


#Tạo cửa sổ chính cho giao diện
root= Tk()

#Thiết lập độ rộng cho giao diện 
root.geometry('600x350')
#Đặt tiêu đề cho cửa số chính

root.title("First Program")

# Bắt đầu chương trình
root.configure(bg='#FFCCFF')
# Tạo text Hello world 
Label(root,text="Hello World !").pack()

#tạo lable
ttk.Label(root,text="Hello World !").pack()

#tạo nút ấn
ttk.Button(root,text="Cộng").pack()

#tạo combobox 
ttk.Combobox(root,values=["Mùa xuân","Mùa Hạ","Mùa Thu","Mùa Đông"]).pack()

#tạo checkbox
ttk.Checkbutton(root,text="Chọn").pack()

#tạo ô nhập dữ liệu
ttk.Entry(root).pack()

#tạo thanh kéo
ttk.Scale(root,from_=0,to=100,orient=HORIZONTAL).pack()

#ô nhập số 
ttk.Spinbox(root,from_=0,to=100).pack()

#ô nhập nhiều text
Text(root).pack()

#Kết thúc chương trình 

#Sử dụng dụng giao diện
root.mainloop()




