from tkinter import * 
from tkinter import ttk

def select(event):
    selected_item=ch.get()
    label.config(text="Selected item : "+selected_item)

    
root=Tk()
root.geometry("500x500")
root.resizable(True,False)
def select():
    pass
label=Label(root,text="Selected Item : ").place(x=50,y=20)

ch=ttk.Combobox(root,values=["Option1","Option2"],state="readonly")
ch.pack()
# ch.place(x=100,y=100)
ch.set("Select")
# print(ch.get())
mainloop()