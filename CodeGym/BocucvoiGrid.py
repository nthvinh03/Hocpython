from tkinter import *
from tkinter import ttk


root=Tk()

root.geometry('400x250')

root.configure(bg="#FFFAFA")

root.title("Bố cục với Grid")

Label(root,text="Tên đăng nhập :").grid(row=0,column=0)
Entry(root).grid(row=0,column=1)
Label(root,text="Mật khẩu").grid(row=1,column=0)
Entry(root).grid(row=1,column=1)
Label(root,text="====================").grid(row=2,column=1)
Button(root,text="Đăng nhập").grid(row=3,column=0)
Button(root,text="Quên mật khẩu").grid(row=3,column=1)
Button(root,text="Đăng kí").grid(row=3,column=3)

root.mainloop()
