#
from tkinter import *
def cercle(x, y, r, coul='black'):
            ''' تابع رسم الدائرة'''
            can.create_oval(x-r, y-r, x+r, y+r, outline=coul)

def figure():
            "Dessiner une cible"
            """تابع رسم الدوائر متحدة المركز"""
            can.delete(ALL) #حذف أي رسمة
            #ارسم الخطين المتعامدين 
            can.create_line(100, 0, 100, 200, fill='blue')
            can.create_line(0, 100, 200, 100, fill='blue')
            rayon=15
            while rayon < 100:
                        cercle(100, 100, rayon)
                        rayon +=15

def Figure():
    '''رسم المهرج'''
    can.delete(ALL) #حذف أي رسمة
    #احداثيات الدوائر
    cc=[[100, 100, 80, 'red'],
        [70, 70, 15, 'blue'],
        [130, 70, 15, 'blue'],
        [70, 70, 5, 'black'],
        [130, 70, 5, 'black'],
        [44, 115, 20, 'red'],
        [156, 115, 20, 'red'],
        [100, 95, 15, 'purple'],
        [100, 145, 30, 'purple']]
    #رسم الدوائر
    i=0
    while i< len(cc):
        el= cc[i]
        cercle(el[0], el[1], el[2], el[3])
        i +=1


f=Tk()
can= Canvas(f, width=200, height=200, bg='ivory')
can.pack(side= TOP, padx=5, pady=5)
b1= Button(f, text='رسم دوائر ', command=figure)
b1.pack(side= LEFT, padx=3, pady=3)
b2= Button(f, text='رسم مهرج', command=Figure)
b2.pack(side= RIGHT, padx=3, pady=3)
f.mainloop()

    
