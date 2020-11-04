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

#background
trianglephoto = PhotoImage(file = "triangle.png")
backpicture = Label(win, image = trianglephoto)

def triangleSolve ():
    h = hinput.get()
    if h == "":
        a = ainput.get()
        b = binput.get()
        c = cinput.get()

        if a == "" or (a =="" and b == "") or (a == "" and c == ""):
            line = "There is not enough information to calculate the area!"
        elif b == "" or (b=="" and c == ""):
            line = "There is not enough information to calculate the area!"
        elif c == "":
            line = "There is not enough information to calculate the area!"
        else:
            a = int(a)
            b = int(b)
            c = int(c)
            s = (a+b+c)/2
            answer = math.sqrt(s*(s-a)*(s-b)*(s-c))
            answer = round(answer, 5)
            answer = str(answer)
            line = "The area of the triangle is " + answer

    else:
        h = int(h)
        b = binput.get()
        if b == "":
            line = "There is not enough information to calculate the area!"
        else:
            b = int(b)
            answer = (b*h)/2
            answer = str(answer)
            line = "The area of the triangle is " + answer
    a_entry.delete(0,END)
    a_entry.insert(0, line)

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
eoutput.set("The area is...")

#widgets code top
leftside = Entry (win, textvariable = ainput, width = 6)
base = Entry (win, textvariable = binput, width = 6)
rightside = Entry (win, textvariable = cinput, width = 6)
height = Entry (win, textvariable = hinput, width = 6)

#widgets code bottom
instruc = Label (win, text = "Enter in as much information about the \n triangle shown and I will calculate the area")
calculate = Button(win, text = "Calculate!", command = triangleSolve)
a_entry = Entry(win, width = 40, textvariable=eoutput)

#place widgets
backpicture.place(x=0, y=0)
leftside.place(x=120, y = 145)
base.place (x=210, y = 220)
rightside.place( x=400, y = 165)
height.place (x=300, y= 150)

instruc.place(x = 0, y = 250)
calculate.place(x=300, y = 255)
a_entry.place (x = 10, y = 310)

win.mainloop()
