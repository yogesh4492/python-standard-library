from tkinter import *

root=Tk()
root.title("Yogesh Patel File")
root.geometry("500x500")
root.resizable(False,False)

var1=IntVar()
Radiobutton(root,text="Male",variable=var1,value=1).place(x=50,y=10)
Radiobutton(root,text="Female",variable=var1,value=2).place(x=150,y=10)

mainloop()