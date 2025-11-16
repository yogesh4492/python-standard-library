from tkinter import *

root=Tk()

root.geometry("500x200")
def add():
    num1=E1.get()
    num2=E2.get()
    label2.config(text=f"Addition :{int(num1)+int(num2)}")


lable=Label(root,text="Enter Number1= ")
lable.pack()
lable1=Label(root,text="Enter Number2= ")
lable1.pack()

E1=Entry(root)
E2=Entry(root)
E1.pack()
E2.pack()
# E1.grid(row=0,column=1)
# E2.grid(row=0,column=2)
bu=Button(root,width=10,text="ADDition",command=add)
bu.pack()
label2=Label(root,text="")
label2.pack()

# label2.pack()
mainloop()