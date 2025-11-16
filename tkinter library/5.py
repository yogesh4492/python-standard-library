import tkinter as tk

def greet():
    name = entry.get()
    label2.config(text=f"Hello {name}!")

root = tk.Tk()
root.title("Greeting App")

label = tk.Label(root, text="Enter your name:")
label.pack()

entry = tk.Entry(root)
entry.pack()

btn = tk.Button(root, text="Greet", command=greet)
btn.pack()

label2 = tk.Label(root, text="")
label2.pack()

root.mainloop()
