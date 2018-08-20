import tkinter as tk


class myWindow():

    def __init__(self):
        self.root = tk.Tk()
        self.winWidth = 300
        self.winHeight = 300
        self.step = 10
        self.canvas = tk.Canvas(self.root,
                                width=self.winWidth,
                                height=self.winHeight)
        self.canvas.pack()

        self.x = self.winWidth / 2
        self.y = self.winHeight / 2
        self.w = self.winWidth / 10
        self.h = self.winHeight / 20

        self.canvas.create_rectangle(self.x - self.w/2,
                                     self.y - self.h/2,
                                     self.x + self.w/2,
                                     self.y + self.h/2,
                                     fill="purple")
        self.canvas.create_text(self.winWidth/2, self.winHeight/15,
                                text="Use A, W, S, D to move")

        self.root.bind("a", self.moveLeft)
        self.root.bind("d", self.moveRight)
        self.root.bind("w", self.moveUp)
        self.root.bind("s", self.moveDown)

    def moveRight(self, event):
        if self.x + self.w/2 < self.winWidth:
            self.canvas.move(1, self.step, 0)
            self.root.update()
            self.x += self.step

    def moveLeft(self, event):
        if self.x - self.w/2 > 0:
            self.canvas.move(1, -self.step, 0)
            self.root.update()
            self.x -= self.step

    def moveUp(self, event):
        if self.y - self.h > 0:
            self.canvas.move(1, 0, -self.step)
            self.root.update()
            self.y -= self.step

    def moveDown(self, event):
        if self.y + self.h < self.winHeight:
            self.canvas.move(1, 0, self.step)
            self.root.update()
            self.y += self.step


window = myWindow()
window.root.mainloop()
