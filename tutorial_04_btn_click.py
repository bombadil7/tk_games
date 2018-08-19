import tkinter as tk

root = tk.Tk()


def printName():
    print("Hello there Andrei!")


button1 = tk.Button(root, text="Click Me", command=printName)
button1.pack()

root.mainloop()
