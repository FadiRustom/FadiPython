from tkinter import *
from math import *
#P121
def eva(ev):
    ch.configure(text="Result= "+ str(eval(en.get())))

#Main
f= Tk()
en= Entry(f)
en.bind("<Return>", eva)
ch= Label(f)
en.pack()
ch.pack()
f.mainloop

