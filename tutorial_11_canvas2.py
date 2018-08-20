import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()


def createRect(x1, y1, x2, y2):
    canvas.create_rectangle(x1, y1, x2, y2, fill="blue")


createRect(5, 50, 200, 70)
createRect(5, 5, 20, 200)

root.mainloop()
