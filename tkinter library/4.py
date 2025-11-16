from tkinter import *

root=Tk()
root.title("Chat Application")
Label(root,text="First Name : ").grid(row=0)
Label(root,text="Last Name : ").grid(row=1)

entry1=Entry(root)
entry2=Entry(root)
entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)
mainloop()