# برنامج رسم خطوط على شاشة رسومية
# يستند على مكتبة الرسوميات في بايثون
from tkinter import *
from random import randrange
# تعريف دالات لمعالجة الأحداث
# إجراء رسم خط
def drawline():
    " DrawLine Function: Draw the Line with canevas can1"
    global x1, y1, x2, y2, coul
    can1.create_line(x1,y1,x2,y2, width=2, fill=coul)
    y2,y1= y2+10, y1-10 #تعديل الإحداثيات للسطر القادم
# إجراء تغيير لون الخط بشكل عشوائي
def changecolor():
    " Chngement line color create random of color list: pal"
    global coul # عام: ليتمكن من تغيير قيمته
    pal=['purple','cyan','maroon','green','red','blue','orange','yellow']
    c= randrange(8)
    # توليد رقم عشوائي بين 0 و7
    coul= pal[c]
    print(pal[c])
#--------البرنامج الرئيسي --------

# اسناد قيم للمتقيرات: يمكن التطوير!
# إحداثيات الخط
x1, y1, x2, y2 = 10, 190, 190, 10
#لون الخط
coul= 'dark green'
# إنشاء الواجهة الرئيسية"السيد"
fen1=Tk()
# إنشاء الأدوات على النافذة "الواجهة" التابع
can1= Canvas(fen1,bg='dark grey',height=200,width=200)
can1.pack(side=LEFT)
bou1= Button(fen1,text='Quit',command=fen1.quit)
bou1.pack(side=BOTTOM)
bou2= Button(fen1,text='Tracer Line',command=drawline)
bou2.pack()
bou3= Button(fen1,text='Autre Color',command=changecolor)
bou3.pack()
# بدء استقبال الأحداث
fen1.mainloop()
# إغلاق النافذة
fen1.destroy()
