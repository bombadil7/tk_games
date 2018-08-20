import tkinter as tk
import time
root = tk.Tk()

canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()
canvas.create_rectangle(130, 100, 170, 120, fill="purple")
canvas.create_text(150, 20, text="Use A, W, S, D to move")

root.mainloop()
