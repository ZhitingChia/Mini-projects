# BMI Calculator v1.0
# Created on 6/6/2019
# Created by: Zhiting

import tkinter as tk
from tkinter import *


def click():
   showBMI()    

def calculateBMI(height,weight):
    bmi = float(weight)/float(height)
    return "{0:.2f}".format(round(bmi,2))

def showBMI():
    height = heightEntry.get()
    weight = weightEntry.get()
    bmi = calculateBMI(height,weight)
    bmiString = str(bmi)
    tk.Label(window,text = "").grid(row = 3)
    tk.Label(window,text = "Height:"+height).grid(row = 4)
    tk.Label(window,text = "Weight:"+weight).grid(row = 5)
    tk.Label(window,text = "BMI:"+bmi).grid(row =6)
    heightEntry.delete(0,tk.END)
    weightEntry.delete(0,tk.END)

window = tk.Tk()
window.resizable(False,False)
window.title("Simple BMI Calculator")
tk.Label(window,text = "Height(m)").grid(row=0)
tk.Label(window,text = "Weight(kg)").grid(row=1)

heightEntry = tk.Entry(window)
weightEntry = tk.Entry(window)

heightEntry.grid(row=0,column =1)
weightEntry.grid(row=1, column = 1)

btn=Button()
btn.grid(row = 2, column =0, columnspan =3, sticky = tk.W+tk.E)

btn["text"]="Compute BMI!"
btn["command"]=click

tk.mainloop()
