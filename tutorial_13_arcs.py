import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()
canvas.create_arc(10, 10, 200, 80, extent=45, style=tk.ARC)
canvas.create_arc(10, 80, 200, 160, extent=90, style=tk.ARC)

canvas.create_text(150, 150, text="This is my first GUI text,"
                   " and it is awesome!",   font=("Times", 30))

root.mainloop()
