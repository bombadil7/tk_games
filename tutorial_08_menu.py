import tkinter as tk

root = tk.Tk()


def random():
    print("This is a statement")


mainMenu = tk.Menu(root)
root.configure(menu=mainMenu)
subMenu = tk.Menu(mainMenu)
mainMenu.add_cascade(label="File", menu=subMenu)

subMenu.add_command(label="Random Func", command=random)
subMenu.add_separator()
subMenu.add_command(label="New File", command=random)


root.mainloop()
