import tkinter as tk

root = tk.Tk()

label1 = tk.Label(root, text="Enter your expression:")
label1.pack()


def evaluate(event):
    data = e.get()
    ans.configure(text="Answer: " + str(eval(data)))


e = tk.Entry(root)
e.bind("<Return>", evaluate)
e.pack()
ans = tk.Label(root)
ans.pack()

root.mainloop()
