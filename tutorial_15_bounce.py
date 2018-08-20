import tkinter as tk
import random
import time

root = tk.Tk()
root.title("Bounce!")
root.resizable(0, 0)
root.wm_attributes("-topmost", 1)

canvas = tk.Canvas(root, width=500, height=500, bd=0,
                   highlightthickness=0)
canvas.pack()

root.update()
#    time.sleep(0.1)

root.mainloop()
