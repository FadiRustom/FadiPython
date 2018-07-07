from tkinter import *
frm=Tk()
text1= Label(frm, text='صباح الخير يا حلو',fg='red')
text1.pack()
but=Button(frm, text='خروج', command= frm.destroy)
but.pack()
frm.mainloop()
