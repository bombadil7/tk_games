import tkinter as tk
import time


class myWindow():

    def __init__(self):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=300, height=300)
        self.canvas.pack()
        self.canvas.create_rectangle(130, 100, 170, 120, fill="purple")
        self.canvas.create_text(150, 20, text="Use A, W, S, D to move")


window = myWindow()
window.root.mainloop()
