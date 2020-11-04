  #! python3

# Have the user enter in the known information of a triangle
# if there is enogh to calculate area then caluclate
#If not use Heron's formula to find the height and then calculate

# Inputs:
# triangle information

# Outputs:
# "There is not enough information"
# "The area is _____ (from calculating Heron's formula)"
# The area is _____ (normal formula)"


import tkinter as tk
from tkinter import *
import math

win=tk.Tk()
win.geometry("500x350")

trianglephoto = PhotoImage(file = "triangle.png")
backpicture = Label(win, image = trianglephoto)

#text variables
ainput = StringVar()
ainput.set("")
binput = StringVar()
binput.set("")
cinput = StringVar()
cinput.set("")
hinput = StringVar()
hinput.set("")
eoutput = StringVar()
eoutput.set("Answers go here!")

backpicture.place(x=0, y=0, relwidth=1, relheight=1)
leftside = Entry (win, textvariable = ainput )
base = Entry (win, textvariable = binput)
rightside = Entry (win, textvariable = cinput)

win.mainloop()
