from tkinter import * 
root=Tk()
root.geometry("500x500")
var1=Listbox(root)
var1.insert(1,"Choose Language")
var1.insert(2,"Python")
var1.insert(3,"Java")
var1.place(x=50,y=20)
mainloop()

