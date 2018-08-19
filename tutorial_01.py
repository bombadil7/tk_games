import tkinter as tk

root = tk.Tk()

topFrame = tk.Frame(root)
topFrame.pack()

botFrame = tk.Frame(root)
botFrame.pack(side=tk.BOTTOM)

theLabel1 = tk.Label(root, text="This is a Tkinter window")
theLabel1.pack()
theLabel2 = tk.Label(root, text="This is a second sentence")
theLabel2.pack()

button1 = tk.Button(topFrame, text="Click Me!", fg="Blue")
button1.pack(side=tk.LEFT)

button2 = tk.Button(topFrame, text="Hello!", fg="Red")
button2.pack(side=tk.RIGHT)

button3 = tk.Button(botFrame, text="Hello!", fg="Purple")
button3.pack(side=tk.LEFT)

button4 = tk.Button(botFrame, text="Hello!", fg="Yellow")
button4.pack(side=tk.RIGHT)

root.mainloop()
