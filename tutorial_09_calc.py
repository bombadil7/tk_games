import tkinter as tk

root = tk.Tk()

equa = ""

equation = tk.StringVar()
equation.set("Enter your equation:")
calculation = tk.Label(root, textvariable=equation)
calculation.grid(columnspan=4)


def btnPress(num):
    global equa
    equa = equa + str(num)
    equation.set(equa)


def clear():
    global equa
    equa = ""
    equation.set(equa)


def evaluate():
    global equa
    equa = str(eval(equation.get()))
    equation.set(equa)
    equa = ""


Button1 = tk.Button(root, text="1", command=lambda: btnPress(1))
Button1.grid(row=1, column=0)
Button2 = tk.Button(root, text="2", command=lambda: btnPress(2))
Button2.grid(row=1, column=1)
Button3 = tk.Button(root, text="3", command=lambda: btnPress(3))
Button3.grid(row=1, column=2)
ButtonPlus = tk.Button(root, text="+", command=lambda: btnPress("+"))
ButtonPlus.grid(row=1, column=3)

Button4 = tk.Button(root, text="4", command=lambda: btnPress(4))
Button4.grid(row=2, column=0)
Button5 = tk.Button(root, text="5", command=lambda: btnPress(5))
Button5.grid(row=2, column=1)
Button6 = tk.Button(root, text="6", command=lambda: btnPress(6))
Button6.grid(row=2, column=2)
ButtonMinus = tk.Button(root, text="-", command=lambda: btnPress("-"))
ButtonMinus.grid(row=2, column=3)

Button7 = tk.Button(root, text="7", command=lambda: btnPress(7))
Button7.grid(row=3, column=0)
Button8 = tk.Button(root, text="8", command=lambda: btnPress(8))
Button8.grid(row=3, column=1)
Button9 = tk.Button(root, text="9", command=lambda: btnPress(9))
Button9.grid(row=3, column=2)
ButtonMult = tk.Button(root, text="*", command=lambda: btnPress("*"))
ButtonMult.grid(row=3, column=3)

ButtonCE = tk.Button(root, text="CE", command=clear)
ButtonCE.grid(row=4, column=0)
Button0 = tk.Button(root, text="0", command=lambda: btnPress(0))
Button0.grid(row=4, column=1)
ButtonEQ = tk.Button(root, text="=", command=evaluate)
ButtonEQ.grid(row=4, column=2)
ButtonDiv = tk.Button(root, text="/", command=lambda: btnPress("/"))
ButtonDiv.grid(row=4, column=3)

root.mainloop()
