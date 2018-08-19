import tkinter as tk

root = tk.Tk()


def printName(event):
    print("Hello there Andrei!")


def leftClick(event):
    print("Left")


def rightClick(event):
    print("Right")


def leftKey(event):
    print("Left key pressed")


def rightKey(event):
    print("Right key pressed")


def scroll(event):
    print("Scroll")


def press_a(event):
    print("a pressed")


button1 = tk.Button(root, text="Click Me")
button1.bind("<Button-1>", printName)
button1.pack()

root.geometry("500x500")

root.bind("<Button-1>", leftClick)
root.bind("<Button-2>", scroll)
root.bind("<Button-3>", rightClick)
root.bind("<Left>", leftKey)
root.bind("<Right>", rightKey)
root.bind("a", press_a)

root.mainloop()
