import tkinter as tk
from tkinter import messagebox as mb

root = tk.Tk()

mb.showinfo("Window Title", "The past isn't gone, it's not even passed!")
answer = mb.askquestion("Question 1", "Are you human?")

if answer == "yes":
    mb.showinfo("Congrats",
                "Thank god!  It's good to know another human is out there.")
else:
    mb.showinfo("Alien", "You are a 100% confirmed Alien")

root.mainloop()
