from tkinter import * 


root=Tk()
root.geometry("900x900")
root.title("Yogesh Desktop File")
root.resizable(False,False)
var1=IntVar()
Checkbutton(root,text="Male",variable=var1).place(x=50,y=10)
var2=IntVar()
Checkbutton(root,text="Female",variable=var2).place(x=150,y=10)
mainloop()