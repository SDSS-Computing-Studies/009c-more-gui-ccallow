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
win.geometry("400x220")

triangle_photo = win.PhotoImage(file = triangle.png)
backpicture = Label(win, image = triangle_photo)



backpicture.place(x=0, y=0, relwidth=1, relheight=1)

win.mainloop()
