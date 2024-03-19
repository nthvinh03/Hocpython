from tkinter import*
from tkinter import ttk


root=Tk()
root.geometry('400x280')
root.title("Caculator")
root.configure(background="#99FF66")


#Tao giao dien may tinh 

nhap_so=Entry(root,width=50)
nhap_so.grid(row=0,column=0,columnspan=4,padx=50,pady=10)

#tao cac phim an 
Button(root,width=4,height=2,text="1").grid(row=1,column=0)
Button(root,width=4,height=2,text="2").grid(row=1,column=1)
Button(root,width=4,height=2,text="3").grid(row=1,column=2)
Button(root,width=4,height=2,text="+").grid(row=1,column=3)


Button(root,width=4,height=2,text="4").grid(row=2,column=0)
Button(root,width=4,height=2,text="5").grid(row=2,column=1)
Button(root,width=4,height=2,text="6").grid(row=2,column=2)
Button(root,width=4,height=2,text="-").grid(row=2,column=3)


Button(root,width=4,height=2,text="7").grid(row=3,column=0)
Button(root,width=4,height=2,text="8").grid(row=3,column=1)
Button(root,width=4,height=2,text="9").grid(row=3,column=2)
Button(root,width=4,height=2,text="x").grid(row=3,column=3)


Button(root,width=4,height=2,text="0").grid(row=4,column=0)
Button(root,width=4,height=2,text="Clear").grid(row=4,column=1)
Button(root,width=4,height=2,text="=").grid(row=4,column=2)
Button(root,width=4,height=2,text=":").grid(row=4,column=3)

Button(root,width=4,height=2,text=".").grid(row=5,column=0)

#ham xu ly khi nhan phim 
def onPress(number):
    print(number)

#ham xu ly khi nhan phim = 
def onEqual():
    print("Xu ly")

#ham xu ly khi nhan clear
def onClear():
    print("Xu ly")


#cap nhat lai su kien cho cac phim an 
    
Button(root,width=4,height=2,text="1",command=lambda:onPress("1")).grid(row=1,column=0,pady=2)
Button(root,width=4,height=2,text="2",command=lambda:onPress("2")).grid(row=1,column=1,pady=2)
Button(root,width=4,height=2,text="3",command=lambda:onPress("3")).grid(row=1,column=2,pady=2)
Button(root,width=4,height=2,text="+",command=lambda:onPress("+")).grid(row=1,column=3,pady=2)

Button(root,width=4,height=2,text="4",command=lambda:onPress("4")).grid(row=2,column=0,pady=2)
Button(root,width=4,height=2,text="5",command=lambda:onPress("5")).grid(row=2,column=1,pady=2)
Button(root,width=4,height=2,text="6",command=lambda:onPress("6")).grid(row=2,column=2,pady=2)
Button(root,width=4,height=2,text="-",command=lambda:onPress("-")).grid(row=2,column=3,pady=2)

Button(root,width=4,height=2,text="7",command=lambda:onPress("7")).grid(row=3,column=0,pady=2)
Button(root,width=4,height=2,text="8",command=lambda:onPress("8")).grid(row=3,column=1,pady=2)
Button(root,width=4,height=2,text="9",command=lambda:onPress("9")).grid(row=3,column=2,pady=2)
Button(root,width=4,height=2,text="x",command=lambda:onPress("x")).grid(row=3,column=3,pady=2)

Button(root,width=4,height=2,text="0",command=lambda:onPress("0")).grid(row=4,column=0,pady=2)
Button(root,width=4,height=2,text="Clear",command=onEqual).grid(row=4,column=1,pady=2)
Button(root,width=4,height=2,text="=",command=onClear).grid(row=4,column=2,pady=2)
Button(root,width=4,height=2,text=":",command=lambda:onPress(":")).grid(row=4,column=3,pady=2)

def onEqual():
    value=nhap_so.get()

    result=eval(value)

    nhap_so.delete(0,'end')

    nhap_so.insert('end',result)

def onClear():
    nhap_so.delete(0,'end')

def onPress(number):
    nhap_so.insert('end',number)



root.mainloop()