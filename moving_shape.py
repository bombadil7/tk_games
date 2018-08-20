import tkinter as tk


class myWindow():

    def __init__(self):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=300, height=300)
        self.canvas.pack()
        self.canvas.create_rectangle(130, 100, 170, 120, fill="purple")
        self.canvas.create_text(150, 20, text="Use A, W, S, D to move")
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
