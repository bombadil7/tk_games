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
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        start = [-3, -2, -1, 0, 1, 2, 3]
        random.shuffle(start)
        self.x = start[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)   # [x1, y1, x2, y2]
        if pos[1] <= 0 or self.hit_paddle(pos) == True:
            self.y *= -1
        elif pos[3] >= self.canvas_height:
            self.hit_bottom = True
            canvas.create_text(245, 100, text="Game Over")
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


paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'red')

while 1:
    #    try:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
#    except:
#        break
    root.update_idletasks()
    root.update()
    time.sleep(0.01)
