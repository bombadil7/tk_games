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


class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        start = [-3, -2, -1, 0, 1, 2, 3]
        random.shuffle(start)
        self.x = start[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)   # [x1, y1, x2, y2]
        if pos[1] <= 0 or pos[3] >= self.canvas_height:
            self.y *= -1
        if pos[0] <= 0 or pos[2] >= self.canvas_width:
            self.x *= -1


class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.move_left)
        self.canvas.bind_all('<KeyPress-Right>', self.move_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)   # [x1, y1, x2, y2]
        if pos[0] <= 0 or pos[2] >= self.canvas_width:
            self.x = 0

    def move_left(self, evt):
        self.x = -2

    def move_right(self, evt):
        self.x = 2


ball = Ball(canvas, 'red')
paddle = Paddle(canvas, 'blue')

while 1:
    try:
        ball.draw()
        paddle.draw()
    except:
        break
    root.update_idletasks()
    root.update()
    time.sleep(0.01)
