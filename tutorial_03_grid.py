import tkinter as tk

root = tk.Tk()

label1 = tk.Label(root, text='Name: ')
entry1 = tk.Entry(root)
label2 = tk.Label(root, text="Password: ")
entry2 = tk.Entry(root)

label1.grid(row=0, column=0, sticky="E")
entry1.grid(row=0, column=1)
label2.grid(row=1, column=0, sticky="E")
entry2.grid(row=1, column=1)

check = tk.Checkbutton(root, text="Remember password")
check.grid(columnspan=2)

root.mainloop()
