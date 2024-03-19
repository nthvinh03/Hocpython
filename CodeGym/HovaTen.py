from tkinter import*   
from tkinter import ttk 


root=Tk()
root.geometry('400x200')
root.title("Họ và Tên")

Label(root, text = "Họ").grid(row = 0, column = 0)
Entry(root).grid(row = 0, column = 1)

Label(root, text = "Tên").grid(row = 1, column = 0)
Entry(root).grid(row = 1, column = 1)

Button(root, text = "Hiển thị").grid(row = 2, column = 0)
Label(root,text="Xin chào : ").grid(row = 2, column = 1)





def Ho_Ten():
    Ho_=Ho.get()
    Ten_=Ten.get()
    char_=Ho_+" "+Ten_
    Hien_thi.config(text="Xin chào : "+char_)


Label(root, text = "Họ ").grid(row = 0, column = 0)
Ho=Entry(root)
Ho.grid(row=0,column=1)

Label(root, text = "Tên").grid(row = 1, column = 0)
Ten=Entry(root)
Ten.grid(row=1,column=(1))

Button(root ,text="Hiển thị",command=Ho_Ten).grid(row=2,column=0)

Hien_thi=Label(root,text="Xin chào ")
Hien_thi.grid(row=2,column=1)

root.mainloop()

