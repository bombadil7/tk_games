import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()
canvas.create_rectangle(20, 20, 80, 280)

canvas.create_line(0, 0, 300, 300)

canvas.create_polygon(10, 15, 20, 30, 50, 25, 25, 10)

root.mainloop()
