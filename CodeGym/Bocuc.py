from tkinter import * 
from tkinter import ttk


root=Tk()

root.geometry('400x250')

root.title("Bố cục với pack")

Button(root,text="red" , fg="red").pack(side=LEFT)
Button(root,text="green", fg="green").pack(side=RIGHT)
Button(root,text="blue", fg="blue").pack(side=TOP)
Button(root,text="black", fg="black").pack(side=BOTTOM)


root.mainloop()