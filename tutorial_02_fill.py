import tkinter as tk

root = tk.Tk()

button1 = tk.Button(None, text="Click Me!", fg="Blue")
button1.pack()

button2 = tk.Button(None, text="Hello!", fg="Red", bg="grey")
button2.pack(fill=tk.X)

button3 = tk.Button(None, text="Hello!", fg="Purple", bg="Yellow")
button3.pack(side=tk.RIGHT, fill=tk.Y)

button4 = tk.Button(None, text="Hello!", fg="Yellow")
button4.pack()

root.mainloop()
