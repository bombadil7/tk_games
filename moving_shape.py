import tkinter as tk


class myWindow():

    def __init__(self):
        self.root = tk.Tk()
        self.winWidth = 300
        self.winHeight = 300
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
        self.canvas.move(1, 10, 0)
        self.root.update()

    def moveLeft(self, event):
        self.canvas.move(1, -10, 0)
        self.root.update()

    def moveUp(self, event):
        self.canvas.move(1, 0, -10)
        self.root.update()

    def moveDown(self, event):
        self.canvas.move(1, 0, 10)
        self.root.update()


window = myWindow()
window.root.mainloop()
