from tkinter import *
''' يرنامج تحريك الكرة بالأسهم '''
# الإجراء العام للحركة تححد إحداثيات الكرة
def avance(x, y):
    global x1, y1
    x1, y1= x1+x, y1+y
    can1.coords(oval1, x1, y1, x1+30, y1+30)


# معالجة الأحداث
def gauche(): #يسار
    avance(-10, 0)

def droite(): #يمين
    avance(10, 0)

def haut(): #فوق
    avance(0, -10)

def bas(): #تحت
    avance(0, 10)

#-----------Main-----------
#Variable
x1=y1=10
#Visual
f=Tk()
f.title('Move the Ball')
can1= Canvas(f, bg='dark grey', height=400, width=400)
oval1= can1.create_oval(x1, y1, x1+30, y1+30, width=2, fill='red')
can1.pack(side=LEFT)
Button(f, text='خروج', command=f.quit).pack(side=BOTTOM)
Button(f, text='فوق', command=haut).pack()
Button(f, text='يسار', command=gauche).pack()
Button(f, text='يمين', command=droite).pack()
Button(f, text='تحت', command=bas).pack()
#-----View 
f.mainloop()
#------Exit
f.destroy()







