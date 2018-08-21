import tkinter as tk
import random
import time

root = tk.Tk()
root.title("Pong!")
root.resizable(0, 0)
root.wm_attributes("-topmost", 1)

canvas = tk.Canvas(root, width=500, height=400, bd=0,
                   highlightthickness=0)
canvas.config(bg='black')
canvas.pack()
root.update()

canvas.create_line(250, 0, 250, 400, fill="#a0a0a0")

root.mainloop()
