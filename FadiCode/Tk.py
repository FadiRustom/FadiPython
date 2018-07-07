from tkinter import *
f=Tk()
txt=Label(f, text=' Welcome to user ', fg='red')
txt.pack()
cmd=Button(f, text='Exit', command= f.destroy)
cmd.pack()






f.mainloop()
